print("HEY !! All the best, Happy programming")
import requests
import time
import tkinter as tk
from plyer import notification
import bs4
import threading
import datetime


def getData(url):
    r = requests.get(url)
    return r.text

def get_corona_detail_of_india():
    url = getData('https://www.covid19india.org/')
    bs = bs4.BeautifulSoup(url, 'html.parser')
    x = bs.find("div", class_="Level")
    print(x)

get_corona_detail_of_india()
