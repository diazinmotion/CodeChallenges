import math
import os
import random
import re
import sys

def get_hourglass(arr_data, hg_len = 3):
    result = []

    # max sum of the listed array
    max_sum = 0

    # set the max len of x axis and y axis
    max_data_x = len(arr_data[0])
    max_data_y = len(arr_data)

    # initiate index for y axis
    y_index = 0

    for y_max in range(hg_len, (max_data_y + 1)):
        x_index = 0
        for x_max in range(hg_len, (max_data_x + 1)):
            # clear array for temp data
            arr_hg = []

            # decide mid point for the hourglass
            mid_pt_x = x_max - 2
            mid_pt_y = y_max - 2
            for y in range(y_index, y_max):
                for x in range(x_index, x_max):
                    # this is for mid section of the hourglass
                    if y == mid_pt_y:
                        if x == mid_pt_x:
                            # insert the data to result array
                            arr_hg.append(arr_data[y][x])
                            continue
                        else:
                            continue

                    arr_hg.append(arr_data[y][x])

            # get the maximum sum of the listed data
            result.append(sum(arr_hg))
            
            x_index += 1
        y_index += 1

    return max(result)

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(get_hourglass(arr))