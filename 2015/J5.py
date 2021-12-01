#import lib.recursion_helper
#from lib.recursion_helper import *
test = 1
if test==1:
    n = 6
    k = 2
elif test==2:
    n = 8
    k = 4
else:
    n = input() #pie
    k = input() #person

#@recursion_analyer_on
#@recursion_performance_guarded
def count(n, k, m):
    if k < 1:
        return 0
    elif k == 1:
        if n<=0:
            return 0
        else:
            return 1
    elif k > 1:
        if 0<n < k:
            return 0
        elif k == n:
            return 1
        elif n > k:
            m0 = n // k if n % k == 0 else n // k + 1
            s0 = 0
            for i in range(m0, m + 1):
                s0 += count(n - i, k - 1, i)
            return s0
        else:
            return 0
print((count(n, k, n)))


#
# def enumerate_possibilities(n, k, m):
#     if k < 1:
#         return []
#     elif k == 1:
#         if n<=0:
#             return []
#         else:
#             return [[n]]
#     elif k > 1:
#         if 0<n < k:
#             return []
#         elif k == n:
#             return [[1]*k]
#         elif n > k:
#             m0 = n // k if n % k == 0 else n // k + 1
#             s0 = 0
#             answers = []
#             for i in range(m0, m + 1):
#                 # if k - i >= 0:
#                 l =  enumerate_possibilities(n - i, k - 1, i)
#                 for e in l:
#                     e.append(i)
#                     answers.append(e)
#             return answers
#
#
#
#
# print((count(4, 2, 4)))
# print((count(9, 3, 9)))
# print((count(9, 4, 9)))
# print((count(20, 1, 20)))
# print((count(70, 70, 70)))
# print((count(25,8,25)))
# print((count(70,15,70)))
# print((count(99,42,99)))
# print((count(120,20,120)))
# print((count(250,130,250)))
