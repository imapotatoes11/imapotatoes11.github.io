import random as r
def is_prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def list_prime(n,output):
    r=[]
    with open(output,'w') as file:
        file.write('')
    for i in range(2,n):
        if i%10000==0:
            print(f'big thinking {i/10000}')
        if is_prime(i):
            r.append(i)
            print(f'found {i}')
            with open(output,'a') as file:
                file.write(f'{str(i)}\n')
    return tuple(r)
print(list_prime(int(input("Prime number range: ")),'prime_numbers.txt'))