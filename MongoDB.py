import pymongo

clusterUrl = "mongodb+srv://abanoub_137:iot123@iotproject.tjqwr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

def connectToMongoClient(copyUrl):
    return  pymongo.MongoClient(copyUrl)

def writeOnDatabase(client, databaseName, document):
    db = client[databaseName]
    id = db.students.insert_one(document).inserted_id
    return id
