import math
import os
import random
import re
import sys

if __name__ == '__main__':
    result = []
    # str_pattern = r"^([a-z]{1,20}) ([a-z]{1,50}@gmail\.com)$"
    pattern_name = r"^[a-z]{1,20}"
    pattern_gmail = r"[a-z]+@gmail\.com{1,50}"

    N = int(input())

    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]

        name_match = re.search(pattern_name, firstName)
        email_match = re.search(pattern_gmail, emailID)
        
        if email_match:
            result.append(name_match.group())

    print("\n".join(sorted(result)))