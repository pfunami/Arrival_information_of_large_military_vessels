import requests
from bs4 import BeautifulSoup

target_url = 'https://www6.kaiho.mlit.go.jp/tokyowan/schedule/URAGA/schedule_3.html'
r = requests.get(target_url)  # requestsを使って、webから取得

soup = BeautifulSoup(r.content, 'lxml')

elems = soup.select('td')
before = elems
hit = False
for elem in elems:

    if elem.getText() == "官船":
        if not hit:
            print("!HIT!\n")
        hit = 1
        print("data:\t\t", elem.find_previous().find_previous().getText())
        print("name:\t\t", elem.find_previous().getText())
        print("type:\t\t", elem.getText())
        elem = elem.find_next().find_next().find_next().find_next()
        print("country:\t", elem.getText())
        elem = elem.find_next()
        print("destination\t", elem.getText(), "\n")

if hit == 0:
    print("Not Found.")
