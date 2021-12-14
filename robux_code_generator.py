import random
many=int(input("how many to generate"))
def gen():
    result=[]
    for i in range(4):
        res=[]
        for i in range(4):
            tf=random.choice([True,False])
            if tf:
                rs=random.randint(65,89)
            else:
                #rs=random.randint(97,122)
                rs=random.randint(65,89)
            res.append(chr(rs))
        result.append(''.join(res))
        result.append('-')
    return ''.join(result).removesuffix('-')
for i in range(many):
    print(gen())