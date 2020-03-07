import requests
from bs4 import BeautifulSoup
import os


headers = {
    "User-Agent": "Mozilla Firefox Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0"
}
url = "https://xkcd.com"

os.makedirs("xkcd", exist_ok=True)

while not url.endswith("#"):

    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "lxml")
    comic = soup.find(id="comic")
    prev_page = soup.find("a", attrs={"rel": "prev"})["href"]
    # checking for correct image url
    try:
        image = comic.find("img")["src"]
        link = "https:" + image
        response = requests.get(link)
    except:
        url = "https://xkcd.com" + prev_page
        continue

    # creating file path with xkcd folder path and name of the file from the url
    path = os.path.join("xkcd", os.path.basename(link))

    # if file doesn't exist, save it
    if not os.path.isfile(path):

        with open(path, "wb") as f:

            print("Downloading image: " + link)
            for chunk in response.iter_content(10000):
                f.write(chunk)
    else:
        print("File already exists!")

    url = "https://xkcd.com" + prev_page
