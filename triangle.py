'''
Debra, G8, Computer Science
This program willprint a triangle that is 
8 lines in height and 8 characters in width.
'''
import sys

if len(sys.argv) != 2:
    print("usage: triangle.py <dimensions>", file=sys.stderr)
    sys.exit(1)

dimensions = int(sys.argv[1])

# outer loop
for i in range(1, dimensions+1):
    for _ in range(i):
        # print characters on same line
        print("#", end="")
    # go to next line
    print()


