#https://edabit.com/challenge/mz7mpEnMByAvBzMrc
def power_of_two(n):
    import math
    return True if math.log(n,2).is_integer() else False
print(power_of_two(32))
print(power_of_two(1))
print(power_of_two(18))