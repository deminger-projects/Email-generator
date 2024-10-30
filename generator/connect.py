import os

from pymongo import MongoClient
from dotenv import load_dotenv

def connect(): #pripoji se do DB a vrati pripojeni k potrebnym kolekcim

    load_dotenv() # Load environment variables from the .env file

    key = os.getenv("MONGO_DB_CONNECTION_STRING")

    cluster = MongoClient(key)
    
    db = cluster[os.getenv("DB")]

    collection_email = db[os.getenv("COLLECTION_EMAILS")]
    collection_check = db[os.getenv("COLLECTION_CHECKS")]
    
    return [collection_email, collection_check]

 