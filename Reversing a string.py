s = "hello world from cpp"
reversed_s = ' '.join(s.split()[::-1])
print(reversed_s)

# Alternate Method

s = "hello world from cpp"
reversed_s = ' '.join(reversed(s.split()))
print(reversed_s)

