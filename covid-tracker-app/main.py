print("HEY !! All the best, Happy programming")
import requests
import time
import tkinter as tk
import plyer
import bs4
import threading
import datetime


def getData(url):
    r = requests.get(url)
    return r.text


def get_corona_detail_worldwide():
    url = getData('https://www.worldometers.info/coronavirus/?#countries')
    bs = bs4.BeautifulSoup(url, 'html.parser')
    x = bs.find("div", class_="content-inner").find_all('div', id="maincounter-wrap")
    world_details = ""
    for b in x:
        name = b.find("h1").get_text()
        no = b.find("div", class_="maincounter-number").find("span").get_text()
        # print(name + "  " + no)
        world_details = world_details + name + "  " + no + "\n"

    return world_details


def refresh():
    newData = get_corona_detail_worldwide()
    print("Refreshing...")
    label_b['text'] = newData

def notify_me():
    while True:
        plyer.notification.notify(
            title="COVID 19 Cases",
            message=get_corona_detail_worldwide(),
            timeout=10,
            app_icon="covid.ico",
        )
        time.sleep(30)


window = tk.Tk()
window.geometry("500x300+10+10")
window.title('COVID-19 Update')
window.iconbitmap("covid.ico")
frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text="Lets Fight COVID-19", font=("Helvetica", 25))
label_a.pack()
frame_b = tk.Frame()
label_b = tk.Label(master=frame_a, text=get_corona_detail_worldwide(), font=("poppins", 25))
label_b.pack()
frame_a.pack()
frame_b.pack()

reBtn = tk.Button(window, text="REFRESH", font=("poppins", 15), relief='solid', command=refresh)
reBtn.pack()

#create a new thread
th1= threading.Thread(target=notify_me)
th1.setDaemon(True)
th1.start()

window.mainloop()
