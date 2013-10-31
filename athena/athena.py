# PROTOYPE ONLY. See athena.c for functional program. #
# Yuechen Zhao <yuechenzhao@college.harvard.edu> #
# Written for Athena Health Coding Challenge 2013. #
# Counts tours on a grid. #

from sys import argv

# The width and height of board
width = int(argv[1])
height = int(argv[2])

# The final destination
dest_square = (1, height)

# The visited set
visited = set()

# Traverse the board
def traverse(pos, steps, paths):
    # Visiting this square
    visited.add(pos)

    # The four possible directions
    x = pos[0]
    y = pos[1]
    squares_to_try = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]

    # Check to see if finished this traversal
    if (steps == (height * width) - 2 and dest_square in squares_to_try):
        visited.remove(pos)
        return paths + 1

    # Try possible paths
    for square in squares_to_try:
        if (square[0] >= 1 and square[0] <= width and
            square[1] >= 1 and square[1] <= height and
            (square not in visited) and square != (1, height)):
            # Count the number of paths
            paths = traverse(square, steps + 1, paths)

    visited.remove(pos)
    return paths

print traverse((1,1), 0, 0)
