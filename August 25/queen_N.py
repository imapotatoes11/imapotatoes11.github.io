N = 4
choice = [2 ** e for e in range(N)]

import functools
from functools import *


def nq_solution_recursion(pcs, RQ, NQ):
    if RQ == 0:
        return pcs
    else:
        npcs = []
        for pc in pcs:
            next_options = [2 ** i for i in range(NQ)]
            for j, e in enumerate(pc):
                next_options = [i for i in next_options if (i << (NQ - RQ - j) | i | i >> (NQ - RQ - j)) & e == 0]
            for next_option in next_options:
                npcs.append([*pc, *[next_option]])
        return nq_solution_recursion(npcs, RQ - 1, NQ)

def nq_solution(N):
    return nq_solution_recursion([[]], N, N)

# print(NQ_SOLUTION([[2 ** e] for e in range(8)],7,8))
# print(NQ_SOLUTION([[2 ** e] for e in range(6)],5,6))
# print(NQ_SOLUTION([[2 ** e] for e in range(5)],4,5))
# print(NQ_SOLUTION([[2 ** e] for e in range(4)],3,4))
# print(NQ_SOLUTION([[2 ** e] for e in range(3)],2,3))


for i in range(12):
    answer = nq_solution(i)
    print(len(answer),answer)
