
# Accept User Input, consider (4)
n = int(raw_input("How big? "))

# Building block of our mountain of money
s = '$'

# Process for constructing mountain
# Since n = 4,
# range (1, n+1) would be all the integers from 1 to 4 including 1 and 4
# Mountain formed would be:
#    $    i = 1,   ' ' * n-i = 4-1 = 3  is empty space taken 3 times,    s*i is '$' taken once(i times)
#   $$    i = 2,   ' ' * n-i = 4-2 = 2  ,  s*i is '$' taken twice(i times)
#  $$$    and so on
# $$$$
# Again, notice how i and n change for each iteration
for i in range( 1 , n+1):
    print (' ' *(n-i) + s*i)


print("\n")  


# Other variant
s = '$$'
for i in range( 1 , n+1):
    print (' ' *(n-i) + s*i)
