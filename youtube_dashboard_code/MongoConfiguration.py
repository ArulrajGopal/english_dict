from pymongo import MongoClient
from Credentials import *


uri = f"mongodb+srv://{mongo_user_id}:{mongo_password}@cluster0.olep9qs.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
     

