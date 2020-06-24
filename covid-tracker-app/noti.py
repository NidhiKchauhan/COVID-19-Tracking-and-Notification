print("HEY !! All the best, Happy programming")
import requests
import time
from plyer import notification
from bs4 import BeautifulSoup


def notifyMe(title, message):
    notification.notify(
        title=title,
        message=message,
        app_icon="E:\covid.ico",
        timeout=15
    )


def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        myHtmlData = getData('https://www.mohfw.gov.in/')
        soup = BeautifulSoup(myHtmlData, 'html.parser')
        # print(soup.prettify())

        myData = ""
        for x in soup.find('tbody').find_all('tr'):
            myData += x.get_text()
        myData = myData[1:]
        itemList = myData.split("\n\n")

        states = ['Delhi', 'Uttar Pradesh', 'Punjab', 'Rajasthan']
        for item in itemList[0:35]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = f'Cases of COVID 19 for State {dataList[1]}'
                nText = f"Active Cases: {dataList[2]}\nCured: {dataList[3]}\nDeaths: {dataList[4]}\nTotal Confirmed Cases: {dataList[5]} "
                notifyMe(nTitle, nText)
                time.sleep(2)
        time.sleep(3600)
