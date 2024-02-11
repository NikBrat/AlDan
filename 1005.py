diff = 200000

def recurs(heap1, heap2, stones, crnt, amnt):
    global diff
    if crnt == amnt:
        if diff > abs(heap1 - heap2):
            diff = abs(heap1 - heap2)
        return
        
    recurs(heap1 + stones[crnt], heap2, stones, crnt+1, amnt)
    recurs(heap1, heap2 + stones[crnt], stones, crnt+1, amnt)

counter = int(input())
stones = sorted([int(s) for s in input().split()], reverse=True)

recurs(heap1=0, heap2=0, stones=stones, crnt=0, amnt=counter)
print(diff)
