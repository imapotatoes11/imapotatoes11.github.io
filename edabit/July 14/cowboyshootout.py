#https://edabit.com/challenge/TbhTAgZbNvBW2ecyt
def roger_shots(lst):
    count=len([e for e in lst if e in ['Bang!','BangBang!']])/2
    return count
print(roger_shots(["Bang!","Bang!","sseofih"]))