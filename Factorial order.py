n = 5

def cal(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        print(fact)

cal(6)
