import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

def swap(index1, val1, index2, val2):
    a[index2] = val1
    a[index1] = val2
    
numSwaps = 0
firstElement = 0
lastElement = 0

for i in range(n):
    # Track number of elements swapped during a single array traversal
    numberSwaps = 0
    for j in range((n - 1)):
        # Swap adjacent elements if they are in decreasing order
        if a[j] > a[(j + 1)]:
            swap(j, a[j], (j + 1), a[(j + 1)])
            numberSwaps += 1
            numSwaps += 1

    # If no elements were swapped during a traversal, array is sorted
    if numberSwaps == 0:
        break

print("Array is sorted in {0} swaps.".format(numSwaps))
print("First Element: " + str(a[0]))
print("Last Element: " + str(a[len(a) - 1]))