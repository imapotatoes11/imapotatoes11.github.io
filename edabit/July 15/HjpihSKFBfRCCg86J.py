#https://edabit.com/challenge/HjpihSKFBfRCCg86J
def compound_interest(principal, time, interest, periods):
    return round(principal*(1+(interest/periods))**(periods*time),2)
print(compound_interest(10000,10,0.06,12))