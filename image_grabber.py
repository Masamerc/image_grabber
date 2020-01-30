from tkinter import *
from tkinter import messagebox, PhotoImage, filedialog
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor


class Window:

    def __init__(self, root):
        self.root = root
        self.root.title("ImageGrabber v0.101262020")
        self.root.iconphoto(True, PhotoImage(file="./assets/logo.png"))

        self.image_urls = []
        self.folder = ""
        self.target_URL = ""

        self.first_row = 0
        self.first_column = 0

        self.message = Label(root, text="Enter Target URL:")
        self.message.grid(row = self.first_row, column = self.first_column,
                            sticky = "e")

        # Text box for the target url
        self.entry_box = Entry(root, width=100)
        self.entry_box.grid(row=self.first_row,
                            column=self.first_column + 1, pady=10)
        # Button to scrape image urls from the url
        self.get_url_button = Button(text="Get Images", command=self.scrape_urls, width=12)
        self.get_url_button.grid(
                            row=self.first_row, column=self.first_column + 2, sticky="w")
        
        # Button to select a folder in which images will be saved
        self.file_button = Button(
            text="Open Folder", command=self.get_folder, width=12)
        self.file_button.grid(
                            row=self.first_row, column=self.first_column + 3, sticky="w")

        # Button to start downloading images
        self.scrape_button = Button(text="Download Images", command=self.save_images, width=24)
        self.scrape_button.grid(
            row=self.first_row + 1, column=self.first_column + 2, columnspan=2, sticky="s")

        # Text box that shows the web-scraping results
        self.lines = 30
        self.text = Text(root, height=self.lines, width=80)
        self.text.grid(row = self.first_row + 2, column = self.first_column + 1,
                        pady=10)

        # Scrollbar for the text box
        self.scroll_bar = Scrollbar(root)
        self.scroll_bar.grid(row = self.first_row + 2, column = self.first_column + 2, sticky="w") 
        self.text.configure(yscrollcommand=self.scroll_bar.set)
        self.scroll_bar.configure(command=self.text.yview)

    def get_folder(self):
        """
        Lets users choose destination folder 
        """
        self.folder = filedialog.askdirectory(initialdir="/")
        if self.folder:
            displayed_text = "Selected Destination: " + "\n" + self.folder
        else:
            displayed_text = "Please Select a Folder"
        label = Label(root, text=displayed_text, bg='#7EDC84')
        label.grid(row=self.first_row + 1, column=self.first_column + 1)

    def scrape_urls(self):
        """
        Makes request to the target url and gets all the links to images
        """
        target_url = self.entry_box.get()
        prefix_target_url = target_url.split("/")[:3]
        prefix_target_url = "/".join(prefix_target_url)
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(target_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        images = soup.find_all("img")

        for image in images:
            if image.get("src", 0) != 0:
                source = image["src"]
            else:
                source = image["data-src"]
            self.image_urls.append(source)
        
        self.text.insert(END, f"Scraping {target_url}...")

        self.image_urls = [image for image in self.image_urls  if image.endswith("jpg") or image.endswith("png") or image.endswith("gif")]
        self.image_urls = [prefix_target_url + image if "http" not in image else image for image in self.image_urls ]
        self.image_urls = list(set(self.image_urls))
        self.text.delete(1.0, END)
        self.text.insert(END, f"Successfully scraped {len(self.image_urls)} images.")
        self.text.insert(END, "\n" + "|")

        for image in self.image_urls:
            self.text.insert(END, "\n")
            self.text.insert(END, f"|--{image}")
            self.text.insert(END, "\n" + "|")

    def download_image(self, image_url):
        """
        Makes request to the target url and gets all the links to images
        """
        response = requests.get(image_url)
        filename = image_url.split("/")[-1]
        if "." not in filename:
            filename = filename + ".jpeg"
        with open(f"{self.folder}/{filename}", "wb") as f:
            f.write(response.content)

    def save_images(self):
        """
        saving images taking advantage of multi-thread pool
        """
        self.text.insert(END, "--Started Saving Files.....")
        with ThreadPoolExecutor() as executor:
            executor.map(self.download_image, self.image_urls)
        messagebox.showinfo(title="Operation Completed",
                            message=f"Successfully saved {len(self.image_urls)} images")

if __name__ == "__main__":
    try:
        root = Tk()
        # root.tk.call('tk', 'scaling', 1.5)
        window = Window(root)
        root.mainloop()

    except KeyboardInterrupt:
        root.destroy()
