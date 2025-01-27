import tkinter as tk

class GUI:
    def __init__(self, board):
        # Create a new window
        window = tk.Tk()

        # Set the window title
        window.title("Quoridor DX")

        # Set the window size
        self.canvas_width = 800
        self.canvas_height = 800
        self.cell_size = self.canvas_height/10

        # Create a canvas widget
        self.canvas = tk.Canvas(window, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        board.be_cool()

        # Draw the game board on the canvas++
        self.draw_board(self.canvas, board)
        
        window.mainloop()

    def draw_board(self, canvas, board):
        self.canvas.delete("all")  # Clear the canvas

    # Draw the board lines
        for i in range(1, board.width):
            canvas.create_line(0, i * self.cell_size, self.canvas_width, i * self.cell_size)
            canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_height)

        # Draw the board cells
        for i in range(board.width):
            for j in range(len(board.cells[i])):
                x = j * self.cell_size
                y = i * self.cell_size
                canvas.create_text(x + self.cell_size // 2, y + self.cell_size // 2, text=board.cells[i][j])
        self.canvas.pack()
        board.be_cool()

    def update_gui(self, game_state):
        pass
