from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import os

CUR_PATH = os.getcwd()
ASSET_PATH = CUR_PATH + "\\assets\\" if os.name == "nt" else CUR_PATH + "/assets/"

class Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Test Run")
        self.root.iconbitmap(ASSET_PATH + "logo.ico")

        # self.root.wm_minsize(600, 400)
        # self.root.grid_anchor(anchor="c")

        self.image_urls = []
        self.folder = ""
        self.target_URL = ""

        self.first_row = 0
        self.first_column = 0
        self.max_plot = 10

        self.message = Label(root, text="Enter Target URL:")
        self.message.grid(row = self.first_row, column = self.first_column,
                            sticky = "e", pady=10, padx=10)

        self.entry_box = Entry(root, width=80)
        self.entry_box.grid(row=self.first_row,
                            column=self.first_column + 1, pady=10)

        self.enter_url_button = Button(text="Scrape'em", command=self.download_images)
        self.enter_url_button.grid(
                            row=self.first_row, column=self.first_column + 2, sticky="w", pady=10)
        self.file_button = Button(text="Open Folder", command=self.get_folder)
        self.file_button.grid(
                            row=self.first_row, column=self.first_column + 3, sticky="w", pady=10)

        self.test_button = Button(text="Test Functionality", command=self.download_images)
        self.test_button.grid(row=self.first_row + 1,
                            column=self.first_column + 1, padx=10)

        self.lines = 45
        self.text = Text(root, height=self.lines, width=60)
        self.text.grid(row = self.first_row + 2, column = self.first_column + 1,
                        padx=10, pady=10)

    def download_images(self):
        """
        get all the image urls thats out there
        """
        target_url = self.entry_box.get()

        self.text.insert(END, self.folder)
        self.text.insert(END, "\n")
        self.text.insert(END, target_url)

        messagebox.showinfo(title="Job Completely Successfully",\
                            message=f"Finished downloading {len(self.image_urls)} images")
        

    def get_folder(self):
        self.folder = filedialog.askdirectory(initialdir="/")
        if self.folder:
            displayed_text = "Selected Destination: "+ "\n" + self.folder 
        else:
            displayed_text = "Please Select a Folder"
        label = Label(root, text=displayed_text)
        label.grid(row=self.first_row + 1, column=self.first_column + 1)
        

if __name__ == "__main__":
    try:
        root = Tk()
        root.tk.call('tk', 'scaling', 1.5)
        window = Window(root)
        root.mainloop()

    except KeyboardInterrupt:
        pass
