from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

#1. Connect to the page
url = "https://dantri.com.vn"
conn = urlopen(url)

#2. Download the page content
raw_data = conn.read()
page_content = raw_data.decode("utf8")

with open ("dantri.html","w") as f:
    f.write(page_content)

#3. Find ROI region (Region of Interest)
soup = BeautifulSoup(page_content, "html.parser")
# print(soup.prettify())
ul = soup.find("ul", "ul1 ulnew") # href = "", id = ""
# print(ul.prettify())

#4. Extract data
li_list = ul.find_all("li")
# li = li_list[0]
news_list = []
for li in li_list:
    a = li.h4.a  # dấu chắm nghĩa là "của" -- a là của h4 là của li
    title = a.string
    link = url + a["href"]
    # print(title,link, sep = ": ")
    news = OrderedDict({
        "title":title,
        "link":link,
    })
    news_list.append(news)
    # print(news)
    # print ("*****")
print(news_list)
# print(a.string) #muốn lấy phần bên giữa hai cái thẻ
# print(a["href"])

#5. Save data
pyexcel.save_as(records=news_list,dest_file_name="test2.xlsx")
