import requests
from bs4 import BeautifulSoup
import os
import time


def search(elems):
    hit = False
    for elem in elems:
        if elem.getText() == "官船":
            if not hit:
                print("!HIT!\n")
                hit = True
            print("data:\t\t", elem.find_previous().find_previous().getText())
            print("name:\t\t", elem.find_previous().getText())
            vesels.append(str(elem.find_previous().getText()))
            print("type:\t\t", elem.getText())
            elem = elem.find_next().find_next().find_next().find_next()
            print("country:\t", elem.getText())
            elem = elem.find_next()
            print("destination\t", elem.getText(), "\n")

    if not hit:
        print("Not Found.")


def note():
    if len(vesels) >= 1:
        ves_str = ""
        for vessel in vesels:
            ves_str += vessel + ", "
        ves_str = ves_str[:-2]
        os.system(
            "osascript -e 'display notification \"{}\" with title \"新規入港予定情報取得\"'".format(ves_str))


def main():
    search(Elems)
    note()


while True:
    target_url = 'https://www6.kaiho.mlit.go.jp/tokyowan/schedule/URAGA/schedule_3.html'
    r = requests.get(target_url)  # requestsを使って、webから取得

    soup = BeautifulSoup(r.content, 'lxml')

    Elems = soup.select('td')
    vesels = []

    main()
    time.sleep(10)
