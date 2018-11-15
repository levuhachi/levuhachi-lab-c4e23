from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import pyexcel

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)

raw_data = conn.read()
page_content = raw_data.decode("utf8")

soup = BeautifulSoup(page_content, "html.parser")
table = soup.find('table',id="tableContent")

tr_list = table.find_all("tr")

data_list = []

for t in tr_list:
    td_list = t.find_all("td")
    data = OrderedDict({})

    if td_list and td_list[0] is not None and td_list[0].string is not None:
        
        data['Title'] = (td_list[0].string.strip())
        
        data['Term 4 - 2016'] = (td_list[1].string)
        data['Term 3 - 2016'] = (td_list[2].string)
        data['Term 2 - 2016'] = (td_list[3].string)
        data['Term 1 - 2016'] = (td_list[4].string)
    
    
    if data:
        print(data)
        data_list.append(data)

# print(datas)

pyexcel.save_as(records=data_list,dest_file_name="Financial_Report.xlsx")


