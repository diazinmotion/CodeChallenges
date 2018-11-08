import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    # nilai tip
    tip_val = float(tip_percent / 100) * meal_cost
    tax_val = float(tax_percent / 100) * meal_cost
    
    print(round(meal_cost + tip_val + tax_val))
    
if __name__ == '__main__':
    meal_cost = float(input())
    
    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)
