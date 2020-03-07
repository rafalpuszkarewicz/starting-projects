import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Google Chrome Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
}
url = "https://www.amazon.de/Automate-Boring-Stuff-Python-Programming/dp/1593275994"
res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.content, "lxml")

price = soup.select(
    "#buyNewSection > div > div > div > div.a-fixed-left-grid-col.dualLineHeader.a-col-right > a > div > div:nth-child(2) > span > span"
)
print(price[0].get_text())
# prices = soup.find_all(class_="a-price", attrs={"data-a-size": "l"})

# for price in prices:
#     print(price.find(class_="a-offscreen").string)

