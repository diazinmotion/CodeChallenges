import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())
    n_binary = format(n, "b")

    max_number = 0
    cons_one = 0

    for i in n_binary:
        i = int(i)
        if i == 1:
            cons_one += 1

            if cons_one > max_number:
                max_number = cons_one
        else:
            cons_one = 0
        
    print(max_number)