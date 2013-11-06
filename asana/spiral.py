######################################################
# Yuechen Zhao <yuechenzhao@college.harvard.edu>
# Nov 6, 2013
# Asana Coding Challenge
#
# Note: there was a 30-minute time limit, after which
# this code was not modified, so no polishing was done
# after completing the challenge.
#######################################################

"""
spiral(matrix)

Prints the items in the matrix supplied in spiral order.
Assumes that the matrix has an obvious spiral order. If the matrix
does not have an obvious spiral order, the function may only print
a portion of the matrix.

Arguments
=========
matrix (list of lists):
	A 2-D matrix of values to print. Each value must give a valid
	result for the str() function.

Returns
=======
This function does not return anything.
"""
def spiral(matrix):
	# calculate the lower bound and upper bound of matrix dimensions
	y_a = 0
	y_z = len(matrix)
	x_a = 0
	x_z = len(matrix[0]) if y_z > 0 else 0

	result = ""
	while x_a < x_z and y_a < y_z:
		# print top row
		for c in range(x_a, x_z):
			result += str(matrix[y_a][c]) + " "

		# print right column (without topmost element)
		if (x_z - x_a > 1):
			for r in range(y_a + 1, y_z):
				result += str(matrix[r][x_z - 1]) + " "

		# print bottom row (without rightmost element)
		if (y_z - y_a > 1):
			# But if just one element, better include it!
			if (x_z - x_a == 1):
				result += str(matrix[y_z - 1][x_a]) + " "

			else:
				for c in reversed(range(x_a, x_z - 1)):
					result += str(matrix[y_z - 1][c]) + " "

		# print left column (without bottommost and topmost element)
		if (x_z - x_a > 1):
			for r in reversed(range(y_a + 1, y_z - 1)):
				result += str(matrix[r][x_a]) + " "
		# bound the matrix we print
		x_a += 1
		x_z -= 1
		y_a += 1
		y_z -= 1

	print result

# Example
matrix = \
[[11, 12, 13, 14, 15],
[21, 22, 23, 24, 25],
[31, 32, 33, 34, 35],
[41, 42, 43, 44, 45]]

# Print matrix in spiral form
spiral(matrix)