import certifi as certifi
import motor as motor
#import pymongo as pymongo
from fastapi import FastAPI
import motor.motor_asyncio




app = FastAPI()

username = "outdoor_insights" #"mongo"
password = "P6mItv39dblb4WF9" #"mongo"
"""mongo_db_connection_string = "mongodb+srv://" \
                             "{username}:{password}@cluster0.gvyd35q.mongodb.net/?retryWrites=true" \
                             "&w=majority".format(username=username, password=password)"""
mongo_db_connection_string = "mongodb+srv://" \
                             "{username}:{password}@cluster0.olpftqz.mongodb.net/?retryWrites=true" \
                             "&w=majority".format(username=username, password=password)


#mongodb+srv://outdoor_insights:P6mItv39dblb4WF9@cluster0.olpftqz.mongodb.net/?retryWrites=true&w=majority
#client = pymongo.MongoClient(mongo_db_connection_string)

#client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])

#trying somehting new
#tlsCAFile=certifi.where()
#client = motor.motor_asyncio.AsyncIOMotorClient(mongo_db_connection_string)
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_db_connection_string, tlsCAFile=certifi.where())
db = client.sample_training

@app.get("/")
async def root():

    #db = client.sample_training
    #collection = await db.companies
    #entry = await collection.find_one()
    #entry = await db["students"].find_one().to_list(1000)
    #entry = await db["companies"].find_one()
    #entry = await db["companies"].find().to_list(1000)
    entry = await db["test"].find().to_list(1000)
    print(entry)

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
