from tkinter import Tk, Label, Button, Entry, StringVar, Frame, Text
from tkinter import ttk


class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Run")
        self.root.wm_minsize(1000, 500)
        self.root.grid_anchor(anchor="c")

        self.first_row = 0
        self.first_column = 0
        self.max_plot = 10

        self.message = Label(root, text="Enter Text: ")
        self.message.grid(row = self.first_row, column = self.first_column, \
             sticky = "w", padx = 4, pady = 4)

        self.entry_box = Entry(root, width=50)
        self.entry_box.grid(row = self.first_row , column = self.first_column + 1)

        self.button = Button(text="Show Text", command=self.get_text)
        self.button.grid(row=self.first_row, column=self.first_row + 2, sticky="w")

        self.lines = 50
        self.text = Text(root, height=self.lines, width=50)
        self.text.grid(row = self.first_row + 10, column = self.first_column + 1)

    
    def get_text(self):
        entered_text = self.entry_box.get()
        display = Label(root, text=entered_text)
        display.grid(row=self.first_row + 1, column=self.first_column + 1)



if __name__ == "__main__":
    try:
        root = Tk()
        window = Window(root)
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()