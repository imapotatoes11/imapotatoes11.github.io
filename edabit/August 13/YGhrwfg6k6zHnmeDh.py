#https://edabit.com/challenge/YGhrwfg6k6zHnmeDh
def get_discounts(prices,discountP):
    discount=int(discountP.removesuffix('%'))/100
    return [e*discount for e in prices]
print(get_discounts([1,2,3,4,5],"98%"))