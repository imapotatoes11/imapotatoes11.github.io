
import random
def gen(n):
    r = []
    for i in range(n):
       r.append(random.randint(-15,20))
    return r



def checkMax1(array):
    rtc = 0
    best = 0
    n = len(array)
    for a in range(0,n):
        for b in range(a,n):
            sum = 0
            for k in range(a,b+1):
                sum += array[k]
                rtc +=1
            best = max(best,sum)
    return best,rtc


def checkMax2(array):
    rtc = 0
    best = 0
    n = len(array)
    for a in range(0,n):
        sum = 0
        for b in range(a,n):
            sum += array[b]
            best = max(best,sum)
            rtc += 1
    return best,rtc


def checkMax3(array):
    rtc = 0
    best = 0
    sum = 0
    n=len(array)
    for k in range(n):
        sum=max(array[k],sum+array[k])
        best=max(best,sum)
        rtc+=1
    return best,rtc


def checkPerformance(array):
    return checkMax1(array)[1],checkMax2(array)[1],checkMax3(array)[1]

performance = []
for i in range(1,10):
    array = gen(i)
    performance.append(checkPerformance(array))
one=[]
two=[]
three=[]
del i
for i in range(len(performance)):
    one.append(performance[i][0])
    two.append(performance[i][1])
    three.append(performance[i][2])

print(performance)
print('First algorithm: '+str(one))
print('Second algorithm: '+str(two))
print('Third algorithm: '+str(three))


#1. implement def checkMax3(array): and then call in the end




