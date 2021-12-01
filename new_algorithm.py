from itertools import permutations
#get length of password in "password.txt"
with open("password.txt",'r') as file:
    fi=file.read()


#colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


with open('new_algorithm_out.txt','w') as file:
    file.write('\n')

with open('password.txt','r') as file:
    pw=file.read()#DEBUG
for num in range(len(fi)+1):#int(input("max length (4): "))+1):#MAX LENGTH OF PASSWORD IN 'range()' !!!max 4!!!
    perms = [''.join(p) for p in permutations('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`~-_=+\|]}[{'";:/?.>,<",num)]
    with open('new_algorithm_out.txt','a') as file:
        for i in perms:
            file.write(i)
            file.write('\n')
            if i==pw:
                #print("THE PASSWORD IS: ")
                #print(i)
                #print(pw)#DEBUG
                exit(Exception(bcolors.OKBLUE+bcolors.BOLD+f"The password is {bcolors.ENDC}\""+pw+f"\"{bcolors.OKBLUE}"))
                break