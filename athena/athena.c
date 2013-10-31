/*************************************************
 * Yuechen Zhao <yuechenzhao@college.harvard.edu>
 * Written for Athena Health Coding Callenge 2013 
 *
 * Counts tours on a grid.
 *
 * Compile with gcc -O2 flag.
 ************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// width and height of board
int width;
int height;

// grid representation, to keep track of visited squares
bool **visited;

// the traverse function, for recursive grid traversal
int traverse(int x, int y, int steps, int paths) {
  // visiting this square
  visited[x][y] = true;

  // the four possible directions
  int squares[8];
  squares[0] = x - 1; squares[1] = y;
  squares[2] = x + 1; squares[3] = y;
  squares[4] = x;     squares[5] = y - 1;
  squares[6] = x;     squares[7] = y + 1;

  /* check to see if finished this traversal
   * traversal is finished if visited all the squares, and last square
   * is the lower left.
   */ 
  if (steps == (height * width) - 2) {
    for (int i = 0; i < 8; i += 2) {
      if (squares[i] == 0 && squares[i + 1] == height - 1) {
	// count this path, "unvisit" this square for backtrack
	visited[x][y] = false;
	return paths + 1;
      }
    }
  }

  // traverse all possible paths, count paths
  for (int i = 0; i < 8; i += 2) {
    if (squares[i] >= 0 && squares[i] < width &&
        squares[i + 1] >= 0 && squares[i + 1] < height && 
        !(visited[squares[i]][squares[i + 1]]) && 
        !(squares[i] == 0 && squares[i + 1] == height - 1)) {
      paths = traverse(squares[i], squares[i + 1], steps + 1, paths);
    }
  }

  visited[x][y] = false;
  return paths;
}

// main function
int main (int argc, char **argv) {
  if (argc != 3) {
    printf("Usage: ./athena <width> <height>\n");
    return -1;
  }

  // the width and height of board
  width = atoi(argv[1]);
  height = atoi(argv[2]);
  if (width <= 0 || height <= 0) {
    printf("Both the width and height must be positive integers.\n");
    return -1;
  }

  /* create grid, zeroed so that everything is false
   * visited is a 2d representation of grid with true value if it's 
   * already been visited as a part of the path, false otherwise.
   */
  visited = calloc(width, sizeof(bool *));
  for (int i = 0; i < width; i++)
    visited[i] = calloc(height, sizeof(bool));

  // traverse from upper left to lower right
  printf("%d\n", traverse(0, 0, 0, 0));

  // free memory
  for (int i = 0; i < width; i++)
    free(visited[i]);
  free(visited);
}
