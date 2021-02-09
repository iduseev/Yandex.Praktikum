#!/bin/python3

# This solution implies naive approach and exceeds time limit for the 27th test on Yandex.Algorithms

'''Rita and Gosha are playing a game. Each of them has n dibs with score points indicated on them.
First, Gosha gives a number k and Rita has to choose two dibs with the sum of scores equal to k. 
Then it is Rita's turn, and Gosha looks for the dibs. Rita is off of this game and decides to write a program
which selects the dibs automatcally. Help Rita write a correct algorithm.

Input:
1-st line contains No of dibs n, 2 <= n <= 10^4
2-nd line contains n integers - scores written on Rita's dibs ranging from -10^5 to 10^5
3-d line contains a number hidden by Gosha ranging from -10^5 <= k <= 10^5.

Output:
Return two numbers in non-descending order - scores on dibs which sum up k. 
If there are several pairs satisfying the condition, return any of them.
If none of pairs found, return None'''

def chooseDibs(n, k, dibs):
    pairs = []
    i = 0
    
    while i < n:
        for j in range(n):
            if dibs[i] != dibs[j] and dibs[i] + dibs[j] == k:
                # pairs[dibs[i]] = dibs[j]
                pairs.extend((dibs[i], dibs[j]))
                pairs.sort()
                return ' '.join([str(num) for num in pairs])
                
        i += 1
    
    return None 


if __name__ == '__main__':

    n = int(input())

    dibs = [int(num) for num in input().split()]

    k = int(input())

    result = chooseDibs(n, k, dibs)

    print(result)