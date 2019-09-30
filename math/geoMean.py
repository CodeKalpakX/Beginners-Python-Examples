#!/usr/bin

# Geometric Mean: https://en.wikipedia.org/wiki/Geometric_mean

def geoMean(*args):
    '''Calculates and returns geometric mean of list of integers'''
    n = len(args)

    prod = 1
    for i in range(n):
        prod = prod*args[i]

    gmean = prod**(1/n)
    return gmean


if __name__ == "__main__":

    flag = 1
    while(flag):

        # Take input from user
        numbers = list(map(int, input('Enter integers separated by space: ').split()))

        # call function
        g = geoMean(*numbers)  #list unpacking

        # display output
        print('The geometric mean of {} is {:.4}\n'.format(numbers, g))

        flag = int(input('Enter 1 to repeat, 0 to quit: '))
        print()
