# Program to calculate Fibonacci bonus for level N

# Take user input
n = int(input("Enter level number: "))

# First two Fibonacci bonuses
a, b = 0, 1

if n == 1:
    print("Bonus points:", a)
elif n == 2:
    print("Bonus points:", b)
else:
    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c
    print("Bonus points:", b)


# Algorithm:

# Start
# Input N
# Set a = 0, b = 1
# If N = 1 → output a
# Else if N = 2 → output b
# Else repeat from i = 3 to N:
# c = a + b
# a = b
# b = c
# Output b as bonus
# Stop
