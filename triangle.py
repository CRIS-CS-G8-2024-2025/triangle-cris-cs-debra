'''
Debra, G8, Computer Science
This program willprint a triangle that is 
8 lines in height and 8 characters in width.
'''
import sys

USAGE='''
usage: triangle.py [dimensions] [character]
  Arguments:
    - no arguments, draws a triangle of dimensions of 8 and character '#'
    - with dimensions argument, draws a triangle of given dimensions and character '#'
    - with dimensions and character arguments, draws a triangle
      of given dimensions and given character
'''

# height and base of right triangle
dimensions = 8

# character that makes up triangle
character = '#'

if len(sys.argv) == 2:
    # dimension given, but no character
    dimensions = int(sys.argv[1])
elif len(sys.argv) == 3:
    # dimension given, and character
    dimensions = int(sys.argv[1])
    character = sys.argv[2]
elif len(sys.argv) != 1:  # default
    print(USAGE, file=sys.stderr)
    sys.exit(1)


# outer loop
for i in range(1, dimensions+1):
    for _ in range(i):
        # print characters on same line
        print(character, end="")
    # go to next line
    print()


