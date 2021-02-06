from bs4 import BeautifulSoup
import requests


def run():
    soup = BeautifulSoup(requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture").text, "html.parser")
    for n in soup.find_all(name="div", class_="body"):
        for i in n.find_all(name="p"):
            print(i.get_text())


if __name__=="__main__":
    run()