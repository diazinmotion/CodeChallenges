import sys


S = input().strip()
try:
    str_num = int(S)
    print(str_num)
except ValueError:
    print("Bad String")