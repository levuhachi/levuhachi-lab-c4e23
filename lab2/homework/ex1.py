from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel
from youtube_dl import YoutubeDL

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)

raw_data = conn.read()

soup = BeautifulSoup(raw_data,"html.parser")
section = soup.find("section","chart-grid")

li_list = section.find_all("li")

top_song = []

for li in li_list:    
    a1 = li.h3.a
    a2 = li.h4.a
    title = a1.string
    artist = a2.string
    link = url + a1["href"]
    top = OrderedDict({
        "Title":title,
        "Artist":artist,
        "Link":link,
    })
    top_song.append(top)

    options = {
        'default_search': 'ytsearch', 
        'max_downloads': 1 
    }
    dl = YoutubeDL(options)
    dl.download([title])

pyexcel.save_as(records=top_song,dest_file_name="ex1.xlsx")