import json
from typing import List

import certifi as certifi
import motor as motor
#import pymongo as pymongo
from fastapi import FastAPI
import motor.motor_asyncio

from models import ProducerResponse

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



@app.get("/producer-performance/{name}", response_model=List[ProducerResponse])
async def say_hello(name: str):
    if name == "Atomic":
        f = open('sample.json')

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        response = []

        for item in data:

            print("Item: ", item)
            producer_data_object = ProducerResponse(**item)
            print("Instatioation worked")
            response.append(producer_data_object)

        return response
    return {"message": "Producer not found"}


