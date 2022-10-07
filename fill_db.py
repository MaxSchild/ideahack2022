import certifi as certifi
from pymongo import MongoClient

# Connecting to MongoDB server
# client = MongoClient('host_name', 'port_number')
username = "outdoor_insights" #"mongo"
password = "P6mItv39dblb4WF9" #"mongo"
address = "cluster0.olpftqz.mongodb.net/?retryWrites=true" #os.environ["MONGODB_ADDRESS"]
#username = "mongo"
#password = "mongo"

mongo_db_connection_string = "mongodb+srv://" \
                             "{username}:{password}@{address}"\
    .format(username=username, password=password, address=address)

"""mongo_db_connection_string = "mongodb+srv://" \
                             "{username}:{password}@cluster0.569a2ry.mongodb.net/?retryWrites=true&w=majority"\
    .format(username=username, password=password)"""
client = MongoClient(mongo_db_connection_string, tlsCAFile=certifi.where())
print("Created Client")

# Connecting to the database named
# GeeksForGeeks
db = client.ideahack2022
databases = client.list_databases()
print("Databases:", databases)
#ädb = client.test

print("DB:", db)
#list all collections and drop them
collections = db.list_collection_names()
print("collections:", collections)

#iterate through all collections and drop them
for collection in collections:
    print("Deleting Collection:", collection)
    my_collection = db[collection]

    my_collection.drop()


