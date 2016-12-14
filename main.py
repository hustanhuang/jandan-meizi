from urllib.request import urlopen
from bs4 import BeautifulSoup as Soup

from threading import Thread
from queue import Queue, Empty

from os import mkdir
from sys import argv

base_url = "http://jandan.net/ooxx/page-"

page_raws = Queue()
img_urls = []

def download(idx_start, idx_end):
    for idx in range(idx_start, idx_end+1):
        print("finished page", idx)
        with urlopen(base_url + str(idx)) as page:
            raw = page.read()
        page_raws.put(raw)

def process():
    idx = 0
    while True:
        if not downloader.is_alive() and page_raws.empty():
            break
        raw = page_raws.get()

        print("process page", idx)
        idx += 1

        posts = Soup(raw, 'lxml').ol
        for post in posts.find_all("li"):
            post = post.find("div", attrs={"class":"text"}).p
            for img in post.find_all("a"):
                img_urls.append(img["href"])

downloader = Thread(target=download, args=(int(argv[1]), int(argv[2])))
downloader.start()

process()

downloader.join()

mkdir(argv[1] + '-' + argv[2])
with open(argv[1] + '-' + argv[2] + "/urls", "w") as f:
    for url in img_urls:
        f.write(url + '\n')
