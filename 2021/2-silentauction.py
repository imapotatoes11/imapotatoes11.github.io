number=int(input())
bids={
    "s":0
}
for i in range(number):
    name=input("")
    bid=int(input(""))
    bids[name]=bid

#for i in range(number):
inverse = [(value, key) for key, value in bids.items()]
print(max(inverse)[1])