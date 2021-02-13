from fastapi import FastAPI
import pymongo
from Usermodel import Users

app = FastAPI()
fackdb = []

client = pymongo.MongoClient()
db = client["testingdb"]
collection = db['users']


@app.get("/")
def read_root():
    return {"greetings":"some greetings"}


@app.get("/users")
async def get_users():
    usersList = []
    users = collection.find(
        {}, #no filter added, obtaining all users
        { "_id": 0, "user_id":1, "name": 1, "age": 1 }
    ) #omiting _id to return
    for user in users:
        usersList.append(user)
    return usersList


@app.get("/users/{user_id}")
def get_a_user(user_id:int):
    usersList = []
    users = collection.find(
        {"user_id":user_id},
        { "_id": 0, "user_id":1, "name": 1, "age": 1 }
    ) #omiting _id to return
    for user in users:
        usersList.append(user)
    return usersList


@app.post("/users/")
def create_user(user:Users):
    user = collection.insert_one(dict(user))
    return {"last_insert_id":str(user.inserted_id)}


@app.put("/users_update_entire/{user_id}")
def update_usere(user_id:int,user: Users):
    collection.update_many({"user_id":user_id},{"$set":dict(user)}) #to update more than one user
    #collection.update_one({"user_id":user_id},{"$set":dict(user)}) #to update only one user
    return {"task":"update success"}


@app.put("/users_update_name_alone/{user_id}")
def update_usere(user_id:int,usernamename):
    collection.update_many({"user_id":user_id},{"$set":{"name":usernamename}}) #to update more than one user
    #collection.update_one({"user_id":user_id},{"$set":{"name":usernamename}}) #to update only one user
    return {"task":"update success"}


@app.delete("/users/{user_id}")
def delete_usere(user_id:int):
    collection.delete_many({"user_id":user_id}) #to delete more than one user
    #collection.delete_one(dict(user)) #to delete only one users
    return {"task":"deletion success"}
