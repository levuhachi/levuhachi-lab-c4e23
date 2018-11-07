# Anh có thể vui lòng chuyển sang file ex4(complete) giúp em ạ ^_^ 
# Công trình này vẫn đang trong giai đoạn xây dựng ạ 
from pymongo import MongoClient
from collections import Counter
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_database()

customers = db ["customers"]

customers_list = customers.find()

# refs = [k['ref'] for k in customers_list if k.get('ref')]
refs = []
for k in customers_list:
    if k.get(['ref']):
        refs.append(k['ref'])

counter = Counter(refs)

# counter = Counter(k['ref'] for k in customers_list if k.get('ref'))

# refs.append(Counter(k['ref'] for k in customers_list if k.get('ref')))

data = counter.values()
names = counter.keys()

# data = list(refs.values())
# names = list(refs.keys())

pyplot.pie(data, labels=names, autopct = "%.1f%%", shadow = True)
pyplot.axis("equal")  
pyplot.title("Percentage of each Reference")
pyplot.show()

client.close()