class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [['E' for _ in range(width)] for _ in range(height)]
    def be_cool(self):
        print('cool')
board = Board(width=9, height=9)
print(board.cells)
