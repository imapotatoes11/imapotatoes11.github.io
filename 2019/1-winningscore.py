apples3=int(input())
apples2=int(input())
apples1=int(input())
banana3=int(input())
banana2=int(input())
banana1=int(input())
totalapple=apples3=apples2+apples1
totalbanana=banana3+banana2+banana1
if totalapple>totalbanana:
    print("A")
elif totalbanana>totalapple:
    print("B")
else:
    print("T")