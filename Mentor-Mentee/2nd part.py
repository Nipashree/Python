from flask import Flask, render_template, request, jsonify, session, redirect, url_for
import mysql.connector
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mentor_mentee.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    user_type = db.Column(db.String(20), nullable=False)  # 'teacher' or 'student'
    roll_number = db.Column(db.String(20), nullable=True)  # Only for students
    name = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Problem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    problem_text = db.Column(db.Text, nullable=False)
    solved = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship
    student = db.relationship('User', backref=db.backref('problems', lazy=True))

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user_type = data.get('userType')
    roll_number = data.get('rollNumber', '')
    
    user = User.query.filter_by(username=username, user_type=user_type).first()
    
    if user and user.check_password(password):
        # For students, also check roll number
        if user_type == 'student' and user.roll_number != roll_number:
            return jsonify({'success': False, 'message': 'Invalid roll number'})
        
        session['user_id'] = user.id
        session['user_type'] = user.user_type
        session['username'] = user.username
        
        return jsonify({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'name': user.name,
                'user_type': user.user_type,
                'roll_number': user.roll_number
            }
        })
    
    return jsonify({'success': False, 'message': 'Invalid credentials'})

@app.route('/api/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'success': True})

@app.route('/api/submit_problem', methods=['POST'])
def submit_problem():
    if 'user_id' not in session or session['user_type'] != 'student':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    data = request.get_json()
    problem_text = data.get('problem')
    
    if not problem_text:
        return jsonify({'success': False, 'message': 'Problem text is required'}), 400
    
    problem = Problem(
        student_id=session['user_id'],
        problem_text=problem_text
    )
    
    db.session.add(problem)
    db.session.commit()
    
    return jsonify({'success': True, 'message': 'Problem submitted successfully'})

@app.route('/api/get_student_problems', methods=['GET'])
def get_student_problems():
    if 'user_id' not in session or session['user_type'] != 'student':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    problems = Problem.query.filter_by(student_id=session['user_id']).order_by(Problem.created_at.desc()).all()
    
    problems_data = []
    for problem in problems:
        problems_data.append({
            'id': problem.id,
            'problem': problem.problem_text,
            'solved': problem.solved,
            'timestamp': problem.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify({'success': True, 'problems': problems_data})

@app.route('/api/get_all_problems', methods=['GET'])
def get_all_problems():
    if 'user_id' not in session or session['user_type'] != 'teacher':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    problems = db.session.query(Problem, User).join(User, Problem.student_id == User.id).order_by(Problem.created_at.desc()).all()
    
    problems_data = []
    for problem, student in problems:
        problems_data.append({
            'id': problem.id,
            'studentName': student.name,
            'rollNumber': student.roll_number,
            'problem': problem.problem_text,
            'solved': problem.solved,
            'timestamp': problem.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify({'success': True, 'problems': problems_data})

@app.route('/api/search_problems/<roll_number>', methods=['GET'])
def search_problems(roll_number):
    if 'user_id' not in session or session['user_type'] != 'teacher':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    student = User.query.filter_by(roll_number=roll_number.upper(), user_type='student').first()
    
    if not student:
        return jsonify({'success': True, 'problems': []})
    
    problems = Problem.query.filter_by(student_id=student.id).order_by(Problem.created_at.desc()).all()
    
    problems_data = []
    for problem in problems:
        problems_data.append({
            'id': problem.id,
            'studentName': student.name,
            'rollNumber': student.roll_number,
            'problem': problem.problem_text,
            'solved': problem.solved,
            'timestamp': problem.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    
    return jsonify({'success': True, 'problems': problems_data})

@app.route('/api/toggle_problem_status/<int:problem_id>', methods=['POST'])
def toggle_problem_status(problem_id):
    if 'user_id' not in session or session['user_type'] != 'teacher':
        return jsonify({'success': False, 'message': 'Unauthorized'}), 401
    
    problem = Problem.query.get_or_404(problem_id)
    problem.solved = not problem.solved
    db.session.commit()
    
    return jsonify({'success': True, 'solved': problem.solved})

# Initialize database and create sample data
def init_db():
    db.create_all()
    
    # Check if sample data already exists
    if User.query.first():
        return
    
    # Create sample teacher
    teacher = User(
        username='teacher',
        name='Professor Smith',
        user_type='teacher'
    )
    teacher.set_password('teacher123')
    db.session.add(teacher)
    
    # Create sample students
    student1 = User(
        username='student1',
        name='John Doe',
        user_type='student',
        roll_number='CS001'
    )
    student1.set_password('student123')
    db.session.add(student1)
    
    student2 = User(
        username='student2',
        name='Jane Smith',
        user_type='student',
        roll_number='CS002'
    )
    student2.set_password('student123')
    db.session.add(student2)
    
    db.session.commit()
    
    # Create sample problems
    problem1 = Problem(
        student_id=student1.id,
        problem_text='I am having trouble understanding recursion in programming. The concept seems confusing and I cannot solve recursive problems effectively.'
    )
    
    problem2 = Problem(
        student_id=student2.id,
        problem_text='I find it difficult to manage time during exams. I often run out of time before completing all questions.',
        solved=True
    )
    
    db.session.add(problem1)
    db.session.add(problem2)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        init_db()
    app.run(debug=True)
