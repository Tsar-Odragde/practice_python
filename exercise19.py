from bs4 import BeautifulSoup
import requests


def run():
    url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
    r_url = requests.get(url).text
    soup = BeautifulSoup(r_url, "html.parser")
    for n in soup.find_all(name="p"):
        print(n.get_text())


if __name__=="__main__":
    run()