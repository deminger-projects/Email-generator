from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

key = os.getenv("MONGO_DB_CONNECTION_STRING")

print(key)

cluster = MongoClient(key)

db = cluster["generator"]
collection = db["emails"]

res = collection.find()
print(res)

for dokument in res:
    print(dokument)

