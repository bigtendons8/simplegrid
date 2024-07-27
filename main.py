def create_grid(x, y, item):
    grid = []
    for i in range(y):
        row = []
        for cell in range(x):
            row.append(item)
        grid.append(row)

    return grid
    

def print_grid(grid):
    for row in grid:
        row_str = ""
        for cell in row:
            row_str += str(cell)
        print(row_str)


grid = create_grid(3, 4, 0)
print_grid(grid)

