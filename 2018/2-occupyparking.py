n=int(input())
first=input()
second=input()
cars=0
for i in range(n):
    if first[i]=="C" and second[i]=="C":
        cars+=1
print(cars)