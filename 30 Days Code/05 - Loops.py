import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    # constraint
    if n >= 2 and n <= 20:
        for i in range(1, 11):
            result = n * i;
            print("{0} x {1} = {2}".format(n, i, result))