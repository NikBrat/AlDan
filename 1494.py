N = int(input())
stack = [[0, 0]]
h = 0

for i in range(N):
    ball = int(input())
    if ball == stack[-1][1]:
        stack[-1][1] -= 1
        if stack[-1][1] < stack[-1][0]:
            del stack[-1]
    elif ball > stack[-1][1]:
        if ball > h+1:
            stack.append([h+1, ball - 1])
        h = ball
    else:
        print('Cheater')
        exit()

print('Not a proof')





