class Canvas:
    def __init__(self, width, height,img):
        self.width = width
        self.height = height
        self.img=img

    def draw_point(self, x, y, char):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = char

    def render(self):
        for row in self.grid:
            print(''.join(row))