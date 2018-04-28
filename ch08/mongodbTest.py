# -*- coding: utf-8 -*-

import pymongo
import datetime
client = pymongo.MongoClient()
db = client.papers
collection = db.books
# book = {"author": "Mike",
#         "text": "My first book",
#         "tags": ["爬虫", "python", "网络"],
#         "date": datetime.datetime.utcnow()
#         }
# book_id = collection.insert(book)
for i in collection.find({"author": "Mike"}):
    print i

collection.update({"author":"Mike"}, {"$set": {"text":"python BooK"}}, multi=True)
for i in collection.find({"author": "Mike"}):
    print i

print "process remove"
collection.remove({"author": "Mike"})
for i in collection.find({"author": "Mike"}):
    print i

print "process end"