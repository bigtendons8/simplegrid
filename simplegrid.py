class Grid:
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item

        self.grid = []
        for i in range(y):
            row = []
            for cell in range(x):
                row.append(item)
            self.grid.append(row)


    def __str__(self):
        grid_str = ""
        for row in self.grid:
            row_str = ""
            for cell in row:
                row_str += str(cell)
            grid_str += row_str + "\n"
        return grid_str



grid = Grid(3, 4, 0)
print(grid)
