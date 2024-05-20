from cs50 import get_int
height = 0
while height < 1 or height > 8:
    height = get_int("Height: ")

for w in range(height):
    if w < height:
        print(' ' * ((height-1)-w) + '#' * (w+1) + ' ' * 2 + '#' * (w+1))
