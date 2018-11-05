#database
from pymongo import MongoClient

uri = "mongodb://admin:admin123@ds011462.mlab.com:11462/c4e23-blog"

#Step1: Connect
client = MongoClient(uri)

#Step2: Get default database
db = client.get_default_database()

#Step3: Get collection
posts = db["posts"]   #lazy loading
movies = db["movies"]

#Step4: Create data
new_post = {
    "title":"Today is a sunny day",
    "content":"I still code at home",
}
new_movie = {
    "title":"Home Alone",
    "imdb":8.0
}

#Step5: Insert data
# posts.insert_one(new_post)
# movies.insert_one(new_movie)

# Step 5: Read data
post_list = posts.find()
# p = post_list[1]
for p in post_list:
    print(p["title"])
    print(p["content"])
    print("------")


#Step6: Close connection
client.close()