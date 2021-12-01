#https://edabit.com/challenge/2vvfEodtq4RYsbcrh
def is_safe_bridge(string):
    if " " in string:
        return False
    else:
        return True
print(is_safe_bridge("#####"))