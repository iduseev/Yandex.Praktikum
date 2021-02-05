#!/bin/python3

'''There are n students registered for the Yandex.Praktikum Algo&DS Course. This course's web-page was visited by every 
student except two during last several days. Find ID's of those students
Constrains: n-> int, 2 <= n <= 10^3.
First line contains n, second line contains n-2 integers not greater than n - these are IDs.
Output: print out IDs in ascending order.'''

def findID(n, arr):

    ID = [] # initialize empty list

    for i in range(1, n + 1): # iterate from 1 to n+1 because ID is a positive integer 
        if i not in arr: # if number i is not presented in arr 
            ID.append(i) # append it to the empty list

    ID_sorted = sorted(ID) # sort ID list for number so be in ascending order

    return ' '.join(str(num) for num in ID_sorted) # return numbers converted into a line separated by space

if __name__ == '__main__':

    n = int(input())

    arr = [int(num) for num in input().split()]

    result = findID(n, arr)

    print(result)