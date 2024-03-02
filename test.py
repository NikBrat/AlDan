import time
f = open('1494.txt', 'r')
e = open('1494_2.txt', 'w')
st = f.readline().split("'\n'")
f.close()
for num in st:
    e.write(f'{num}\n')
e.close()


"""start = time.thread_time()

for i in range(250):
    n = int(input())

end = time.thread_time()"""
