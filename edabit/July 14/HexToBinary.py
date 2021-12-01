#https://edabit.com/challenge/BuCaGYh8keiWJGmcC
def to_binary(n):
    #return bin(n).removeprefix('0b')
    return bin(n).replace('0b','')
print(to_binary(0xFF))
print(to_binary(0xAA))
print(to_binary(0xFA))