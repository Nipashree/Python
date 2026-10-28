def countBalls(balls):
    stack = []

    for ball in balls:
        while stack and stack[-1] > 0 and ball < 0:
            if stack[-1] < abs(ball):
                stack.pop()
                continue
            elif stack[-1] == abs(ball):
                stack.pop()
            break
        else:
            stack.append(ball)

    return len(stack)
