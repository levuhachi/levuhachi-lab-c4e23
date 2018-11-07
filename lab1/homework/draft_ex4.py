from pymongo import MongoClient
from collections import Counter

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)

db = client.get_default_database()

customers = db ["customers"]

customers_list = customers.find()
# ["events", "wom", "wom", "ads"]
refs = []
for k in customers_list:
    if k.get('ref'):
        refs.append(k["ref"])
print(refs)
