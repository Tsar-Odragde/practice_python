from bs4 import BeautifulSoup
import requests


def run():
    soup = BeautifulSoup((requests.get("https://www.nytimes.com/")).text, "html.parser")
    a = 0
    b = 0 
    c = 0
    for n in soup.find_all(class_="styln-hp-briefing-subhead css-pcs5ck"):
        a = n.get_text()
    for n in soup.find_all(class_="e1lsht870"):
        b = n.get_text()
    for n in soup.find_all(class_="e1voiwgp0"):
        c = n.get_text()
    with open('nyt.txt', 'r+') as nyt_file:
        nyt_file.write(f"{a} {b} {c}")


if __name__=="__main__":
    run