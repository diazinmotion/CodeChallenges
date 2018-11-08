import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    is_weird = False
    
    if N < 0 and N > 100:
        raise ValueError("Greater than the Constraints")
    
    # menentukan ganjil atau genap
    is_even = False
    if N % 2 == 0:
        is_even = True
        
    # case 1
    if not is_even:
        is_weird = True
    elif is_even and (N >= 6 and N <= 20):
        is_weird = True
        
    # print result
    if is_weird:
        print("Weird")
    else:
        print("Not Weird")
