from tkinter import *
from tkinter import filedialog

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Run")
        self.root.wm_minsize(1000, 500)
        self.root.grid_anchor(anchor="c")

        self.image_urls = []
        self.folder = ""
        self.target_URL = ""

        self.first_row = 0
        self.first_column = 0
        self.max_plot = 10

        self.message = Label(root, text="Enter Target URL:")
        self.message.grid(row = self.first_row, column = self.first_column, \
             sticky = "w", padx = 4, pady = 4)

        self.entry_box = Entry(root, width=50)
        self.entry_box.grid(row = self.first_row , column = self.first_column + 1)

        self.enter_url_button = Button(text="Show Text", command=self.download_images)
        self.enter_url_button.grid(row=self.first_row, column=self.first_row + 2, sticky="w")
        self.file_button = Button(text="Open Folder", command=self.get_folder)
        self.file_button.grid(row=self.first_row, column=self.first_row + 3, sticky="w")

        self.lines = 50
        self.text = Text(root, height=self.lines, width=50)
        self.text.grid(row = self.first_row + 10, column = self.first_column + 1)

    
    def download_images(self):
        target_url = self.entry_box.get()
        """
        get all the image urls thats out there
        """
        print(self.folder, target_url)
        


    def get_folder(self):
        self.folder = filedialog.askdirectory(initialdir="/")
        displayed_text = "Selected Destination: "+ "\n" + self.folder 
        label = Label(root, text=displayed_text)
        label.grid(row=self.first_row + 1, column=self.first_column + 1)
        

if __name__ == "__main__":
    try:
        root = Tk()
        window = Window(root)
        root.mainloop()
    except KeyboardInterrupt:
        root.destroy()
