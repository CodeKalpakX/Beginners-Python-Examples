"""
ansi-colors.py
Print 256 ANSI(8bit) color chart
Reference : https://en.wikipedia.org/wiki/ANSI_escape_code

*** Warning!
In some terminal/OS environments,
this code may display different colors or color may not be displayed properly
"""

START_ESCAPE_8BIT = "\033[38;5;"
END_ESCAPE = "\033[0;0m"
SQUARE_CHAR = '\u25A0'


def print_square_8bit(color):
    print(START_ESCAPE_8BIT + str(color) + 'm' + SQUARE_CHAR + END_ESCAPE, end="")


print("System standard colors:       ", end="")
for i in range(8):
    print_square_8bit(i)
print()

print("System high intensity colors: ", end="")
for i in range(8, 16):
    print_square_8bit(i)
print()

step = 0
print("216 Colors: ")
for i in range(16, 232):
    print_square_8bit(i)
    step += 1
    if step % 24 == 0:  # Make newline every 24 colors
        print()
print()

print("Grayscale colors: ", end="")
for i in range(232, 256):
    print_square_8bit(i)
print()
