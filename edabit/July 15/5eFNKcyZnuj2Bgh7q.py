#https://edabit.com/challenge/5eFNKcyZnuj2Bgh7q
def is_automorphic(n):
    return str(n**2).endswith(str(n))
print(is_automorphic(5))