def exp(base,power,number):
    with open("exponents.txt",'w') as file:
        file.write(str(base**power))
    try:
        for i in range(number-1):
            with open("exponents.txt",'r') as file:
                ye=int(file.read())
            with open("exponents.txt",'w') as file:
                file.write(str(ye**power))
            if i%5==0:
                print("thinking... ")
    except:
        pass
    with open("exponents.txt",'a') as file:
        file.write('\n')
        file.write(f'first number: {str(base)}\n')
        file.write(f'exponent used: {str(power)}\n')
        file.write(f'amount: {str(number)}\n')
exp(int(input("base: ")),int(input("exponent: ")),int(input("multiplier (1-1000): ")))
import webbrowser as wb
wb.open('exponents.txt')