#https://edabit.com/challenge/LgvppFDZoMpBKf8JW
def digital_clock(seconds):
    hours=(seconds//60)//60
    minutes=(seconds//60)%60
    secs=seconds%60
    return str(hours)+':'+str(minutes)+':'+str(secs)
print(digital_clock(5025))