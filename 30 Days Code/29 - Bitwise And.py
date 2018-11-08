import math
import os
import random
import re
import sys

# Bila banyak inputan akan menghasilkan Timeout Error
# def processBitwise(k, n):
#     max_number = 0
#     arrS = range(1, (n + 1))

#     for i in arrS:
#         for j in range(i + 1, (n + 1)):
#             bitwiseAnd = (i & j)
#             if bitwiseAnd < k and bitwiseAnd > max_number:
#                 max_number = bitwiseAnd
                

#     return max_number


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])
        k = int(nk[1])

        # cara tercepat dari bitwiseAnd
        print(k-1 if ((k-1) | k) <= n else k-2)