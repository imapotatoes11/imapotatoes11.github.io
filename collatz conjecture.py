#https://codehs.com/student/2490383/section/269821/assignment/60085198/#
import random
def collatz(n):
    steps = 0
    highestno = 1
    while True:
        if n == 1:
            break
        if n % 2 == 0:
            n = n / 2
            steps += 1
            if n > highestno:
                highestno = n
        else:
            n = 3*n + 1
            steps += 1
            if n > highestno:
                highestno = n
    return (steps, highestno)

import threading as t
total_steps=[]
heighest_number=[]
for i in range(10000):
    rr=random.randint(1,1000)
    #print(collatz(random.randint(1,1000)))
    coll=collatz(rr)
    total_steps.append(coll[0])
    heighest_number.append(coll[1])
    print([coll,rr])
print("(steps, highestNumber),originalNumber")
print(f'max {max(total_steps)} steps')
print(f'{max(heighest_number)} highest number')