grid = [['.', '.', '0', '0', '.', '0', '0', '.', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0', '0', '0', '.'],
        ['.', '.', '0', '0', '0', '0', '0', '.', '.'],
        ['.', '.', '.', '0', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.']]

y = 0
for x in range(len(grid)):
    for y in range(len(grid[x])):
        print(grid[x][y], end="")
    print()