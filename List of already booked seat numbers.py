# List of already booked seat numbers
booked_seats = [5, 12, 18, 25, 30, 42]

# Take seat number input from user
seat = int(input("Enter seat number to check: "))

# Check if seat is booked
if seat in booked_seats:
    print("Seat", seat, "is already BOOKED.")
else:
    print("Seat", seat, "is AVAILABLE.")

# Algorithm:

# Start
# Store booked seat numbers in an array
# Input the seat number to check
# Search the array for the input value
# If found → display “Booked”
# Else → display “Available”
# Stop
