import time as t
f=open("ramtest.txt","r+")
for i in range (555555555555):
    print(i)
    lines=f.readlines()
    f.close()
    del lines[:]
    f=open("ramtest.txt","w+")
    f.write(str(i))
f.write(str(i))
f.close()