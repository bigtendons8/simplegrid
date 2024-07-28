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
        
        self.selected_x = 0
        self.selected_y = 0

    def __str__(self):
        grid_str = ""
        for row in self.grid:
            row_str = ""
            for cell in row:
                row_str += str(cell)
            grid_str += row_str + "\n"
        return grid_str


    def __iter__(self):
        for row in self.grid:
            for cell in row:
                yield cell


    def select(self, x, y):
        self.selected_x = x
        self.selected_y = y
    

    def move(self, x, y):
        self.selected_x += x
        self.selected_y += y

    def change(self, x, y, item):
        self.grid[y][x] = item

    
    def change_here(self, item):
        self.grid[self.selected_y][self.selected_x] = item

    
    def read(self, x, y):
        return self.grid[y][x]


    def read_here(self):
        return self.grid[self.selected_y][self.selected_x]


    def find(self, item):
        result = []
        y = 0
        x = 0
        for row in self.grid:
            y += 1
            for cell in row:
                x += 1
                if cell == item:
                    result.append((x, y))

        return result

    
    def in_bounds(self, x, y):
        return x <= self.x and y <= self.y


