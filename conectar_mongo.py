
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://eledelaf:Ly5BX57aSXIzJVde@articlesprotestdb.bk5rtxs.mongodb.net/?retryWrites=true&w=majority&appName=ArticlesProtestDB"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # Data base
    db = client["URLS"]
    # Colección
    collection = db["Primer Querys"]
    

except Exception as e:
    print(e)

