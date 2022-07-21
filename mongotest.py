import pymongo

# client = pymongo.MongoClient("mongodb+srv://Nivedhita:<nivi1995>@cluster0.59gvbhi.mongodb.net/?retryWrites=true&w=majority")
client = pymongo.MongoClient("mongodb+srv://Nivedhita:nivi1995@cluster0.59gvbhi.mongodb.net/?retryWrites=true&w=majority")
db = client.test




d = {
    "name":"sudhanshu",
    "email" : "sudhanshu@ineuron.ai",
    "surname" : "kumar"
}

db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)

