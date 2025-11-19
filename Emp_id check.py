# List of employee IDs
employee_ids = [101, 203, 305, 412, 589, 678]

# Take input from user
eid = int(input("Enter employee ID to search: "))

# Check if the ID exists
if eid in employee_ids:
    print("Found")
else:
    print("Not Found")
