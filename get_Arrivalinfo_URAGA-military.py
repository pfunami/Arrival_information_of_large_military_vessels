import requests, os, time, datetime
from bs4 import BeautifulSoup

all_vessels = []


def search(elems):
    latest_vessels = []
    hit = False
    for elem in elems:
        if elem.getText() == "官船":
            if not hit:
                print("HIT!", datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'), "\n")
                hit = True
            print("data:\t\t\t", elem.find_previous().find_previous().getText())
            name = elem.find_previous().getText()
            print("name:\t\t\t", name)
            latest_vessels.append(str(elem.find_previous().getText()))
            print("type:\t\t\t", elem.getText())
            elem = elem.find_next().find_next().find_next().find_next()
            print("country:\t\t", elem.getText())
            elem = elem.find_next()
            print("destination:\t", elem.getText(), "\n")
    if not hit:
        print("Not Found.", datetime.datetime.now().strftime('%Y年%m月%d日 %H:%M:%S'), "\n")

    return latest_vessels


def note(vessels):
    if len(vessels) >= 1:
        ves_str = ""
        for vessel in vessels:
            ves_str += vessel + ", "
        ves_str = ves_str[:-2]
        os.system(
            "osascript -e 'display notification \"{}\" with title \"新規入港予定情報取得\"'".format(ves_str))


def main(all):
    target_url = 'https://www6.kaiho.mlit.go.jp/tokyowan/schedule/URAGA/schedule_3.html'
    try:
        r = requests.get(target_url)
        soup = BeautifulSoup(r.content, 'lxml')
        elems = soup.select('td')
        latest = search(elems)
        if latest != all:
            all = latest
            note(all)
    except Exception as e:
        print("ConnectionError, ", e)
    finally:
        return all


while True:
    all_vessels = main(all_vessels)
    print("-------------------------")
    time.sleep(60)
