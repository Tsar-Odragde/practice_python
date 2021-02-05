from bs4 import BeautifulSoup
import requests


def run():
    soup = BeautifulSoup((requests.get("https://www.nytimes.com/")).text, "html.parser")
    for n in soup.find_all(class_="styln-hp-briefing-subhead css-pcs5ck"):
        print(n.string)
    for n in soup.find_all(class_="e1lsht870"):
        print(n.string)
    for n in soup.find_all(class_="e1voiwgp0")[2:22]:
        print(n.string)
    

if __name__=="__main__":
    run()