from pymongo import MongoClient
from collections import Counter
from matplotlib import pyplot
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

customers = db ["customers"]

customers_list = customers.find()

refs = {}

for c in customers_list:
    refs[c['ref']] = refs.get(c['ref'],0) + 1
for k,v in refs.items():
    print(k,v,sep=":")

refs_data = list(refs.values())
refs_name = list(refs.keys())

pyplot.pie(refs_data,labels=refs_name,autopct="%.1f%%",shadow = True)
pyplot.title("The percentage of Each Reference")
pyplot.axis("equal")
pyplot.show()
