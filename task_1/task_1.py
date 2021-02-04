#!/bin/python3

'''Given two arrays of a size n. You need to create an array of 2n length where numbers from both arrays are intercharged
(1st - 2nd - 1st - 2nd...). The initial order of the numbers should be saved.'''

def Concatenate(n, arr_1, arr_2):

    total_arr = []
    i = 0

    while i < n:
        total_arr.append(arr_1[i])
        total_arr.append(arr_2[i])
        i += 1

    return ' '.join([str(num) for num in total_arr]) 

    # return True if len(total_arr) == 2 * n else False

if __name__ == '__main__':

    n = int(input())

    arr_1 = input().split()

    arr_2 = input().split()

    result = Concatenate(n, arr_1, arr_2)

    print(result)