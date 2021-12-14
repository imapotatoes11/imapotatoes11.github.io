res=[]
a=int(input("amount:"))
for i in range(a):
    res.append(i**2)
    print(i)
    print(res)
m=[i for i in range(a)]
print('done')
print(res)

from matplotlib import pyplot as plt
plt.scatter(m,res)
plt.show()