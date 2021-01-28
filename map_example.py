#This is to demonstrate the use of map function in python
#Problem Statement: Using the function Map, count the number of words that start with ‘S’ in input_list.
#Sample Input: ['Santa Cruz','Santa fe','Mumbai','Delhi']
#Sample Output: 2

#Solution:
input_list = ['Santa Cruz','Santa fe','Mumbai','Delhi']

count = sum(map(lambda x: x[0] == 'S', input_list))

print(count)        # Output: 2
