# Prime number Determiner
# replace input() with raw_input() in Python version 2.7 input() works with version 3 
import math as Math

POSITIVE_MESSAGE = " is a prime number"
NEGATIVE_MESSAGE = " is not a prime number"


def is_number_prime(number):
    """
    Function which checks whether the number is a prime number or not
    :param number: integer - to be checked for prime-ness
    :return: boolean - true if prime, else false
    """

    """
    This is the main logic behind reducing the numbers to check for as factors
        if N = a * b; where a<=b and a,b C (1, N)
        then, a * b >= a*a;
        which leads to => a*a <= N
                       => a <= sqrt(N)
    Hence checking only till the square root of N 
    """
    upper_lim = Math.floor(Math.sqrt(number)) + 1
    is_prime = True if number != 1 else False

    for i in range(2, upper_lim):
        if number % i == 0:
            is_prime = False
            break
            # The moment there is a divisor of 'number', break the iteration, as the number is not prime

    return is_prime


while True:
    startOrEnd = str(input('Start or End : '))
    if startOrEnd == 'Start':
        number = int(input('Number to Check : '))
        result = str(number)
        prime_status = is_number_prime(number)

        if prime_status:
            result += POSITIVE_MESSAGE
        else:
            result += NEGATIVE_MESSAGE
        print(result)
    else:
        print('Program Ended...')
        break
