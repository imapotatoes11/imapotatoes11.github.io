"""
people=int(input())
infectedAtStart=int(input())
infectedPerDay=int(input())
day=0
infected=infectedAtStart
while True:
    day+=1
    infected=infected*infectedPerDay
    if infected>=people:
        print(day)
        break
    if infectedPerDay<2:
        print(day)
        break
"""
p=int(input())
n=int(input())
r=int(input())

infected=n
totalinfected=n
day=0

while totalinfected<p:
    infected=infected*r
    totalinfected+=infected
    day+=1

print(day)