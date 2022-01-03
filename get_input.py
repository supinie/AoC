import requests
from bs4 import BeautifulSoup

def get_input(url):
    res = requests.get(url, cookies = {"session": "53616c7465645f5ffc3c43ee685d67e13c78fc273f4dadeda9fb094669d1df3a45abdd0471d1839b195c0ac568340829"})
    html_page = res.content

    soup = BeautifulSoup(html_page, "html.parser")
    text = soup.find_all(text=True)

    return text