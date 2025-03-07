from pymongo import MongoClient
from Credentials import *
from urllib.parse import quote_plus

encoded_username = quote_plus(mongo_user_id)
encoded_password = quote_plus(mongo_password)

print(encoded_username)
print(encoded_password)

uri = f"mongodb+srv://{encoded_username}:{encoded_password}@cluster0.5ps3l.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
     




