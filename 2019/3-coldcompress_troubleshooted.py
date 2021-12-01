l = int(input())
list = []
count = 0
lst = []


def encode(input):
    lc = None
    count = 0
    for i, c in enumerate(input):
        if lc == None:
            lc = c
            count = 1
        elif lc == c:
            count += 1
        elif lc != c:
            lst.append(f'{count} {lc}')
            lc = c
            count = 1
    lst.append(f'{count} {lc}\n')


for i in range(l):
    intput = input()
    encode(intput)
print((' '.join(lst)).strip())

for j in range(l):
    if intput[i] in intput[0]:
        count += 1
