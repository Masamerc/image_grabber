import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

img_urls = [
    "https://images.unsplash.com/photo-1576092609932-2b3abade2479", 
    "https://images.unsplash.com/photo-1576100246753-1c1b4fa73481",
    "https://images.unsplash.com/photo-1576097099022-b013b35f2d21"
]

def download_image(img_url):
        print(f"Downloading image from {img_url}...")
        response = requests.get(img_url)
        filename = img_url.split("/")[-1]
        if "." not in filename:
            filename = filename + ".jpeg"
        with open(f"./photos/{filename}", "wb") as f:
            f.write(response.content)

with ThreadPoolExecutor() as executor:
    results = executor.map(download_image, img_urls)

