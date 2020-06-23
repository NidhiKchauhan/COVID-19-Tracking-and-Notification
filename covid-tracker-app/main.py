print("HEY !! All the best, Happy programming")
import requests
import bs4
import tkinter as tk
import plyer
import time
import datetime

#to get the data from html webpage
def get_html_data(url):
    data = requests.get(url)
    return data

def get_corona_detail_of_india():
    url = "https://www.mohfw.gov.in/"
    html_data = get_html_data(url)
    bs= bs4.BeautifulSoup(html_data.text,'html.parser')
    #print(bs.prettify())
    '''active = bs.find_all("li",class_="bg-blue")
    print(active)
    for block in active:
        active_no = block.find("li").get_text()
        active_name= block.find("span").get_text()
        print()
        print()
        print(active_name+"   :   "+active_no )'''

    info = bs.find("div", class_="site-stats-count").find("ul").find_all("li")
    print(info)
    print()
    print(len(info))
    print()
    for block in info:
            count = block.find("strong").get_text()
            text = block.find("span").get_text()
            print(text + "   :   " + count)

def main():
    get_corona_detail_of_india()

if __name__ == '__main__':
    main()

