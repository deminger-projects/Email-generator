#import sys
#print(sys.path) // pro zjisteni cesty pro knihovny
#python -m pip install pymongo --target=C:\Users\domin\AppData\Local\Programs\Python\Python313\Lib\site-packages
import os
import pymongo
from pymongo import MongoClient

from dotenv import load_dotenv
from generator_demo import demo

# Load environment variables from the .env file
load_dotenv()

key = os.getenv("MONGO_DB_CONNECTION_STRING")

vygenerovane_emaily = demo()



cluster = MongoClient(key)

db = cluster["generator"]
collection = db["emails"]

posty = []

for email in vygenerovane_emaily:
    posty.append({"email": email, "delka": 2, "iterace": 64567, "poskytovatel": "gmail"})

res = collection.insert_many(posty)

print(res)
