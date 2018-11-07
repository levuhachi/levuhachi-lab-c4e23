from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")
table = soup.find(id="tableContent")

tr_list = table.find_all("tr")

kqhdkd = []

for tr in tr_list:
    # for td in tr.stripped_strings:
    #     title = td
    #     print(title)
    title = tr.contents
    print(title)









