#!/bin/python3

'''In order to save his personal data, Vasya decided to unwrap the numbers in his messages 
(which means writing them vise versa). The negative sign should remain at the beginning in case of a negative number.
No need to print out leading zeroes at the beginning of the output. Help Vasya write a program for doing that.'''

def viceVersa(n):

    output = '' # initialize variables
    l = []

    for i in n[::-1]: # iterate through string in reversed order with step '-1' 
        l.append(i) # append all the symbols to the list

    output = output.join(l).lstrip('0') # remove leading zeroes and turn list 'l' into a string 'output'

    if output[-1] == '-': # if the n input is a negative number (last char == '-')
        output = '-' + output[:-1]  # pop it from the end and prepend it 

    return output if n != '0' else '0' # return 0 in case n = 0 is given

if __name__ == '__main__':

    n = input()

    result = viceVersa(n)

    print(result)