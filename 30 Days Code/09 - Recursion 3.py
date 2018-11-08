import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n > 1:
        res = n * factorial(n - 1)
    elif n == 1:
        res = 1
    
    return res
    
if __name__ == '__main__':
    n = int(input())

    result = factorial(n)
    print(result)
