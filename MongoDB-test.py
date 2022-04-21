import pymongo
import datetime
import pprint
from bson.objectid import ObjectId

#connct to mongo atlas (client --> cluster)
client = pymongo.MongoClient('mongodb+srv://abanoub_137:iot123@iotproject.tjqwr.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# client = pymongo.MongoClient('mongodb+srv://mina25:iot123@mongodbcluster.njzak.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
# print(client.list_database_names())

#git specific database
db = client['ITI_IoT_DB']  #or -->client.ITI_IoT_DB
# print(db.list_collection_names())

#insert document
# studentDocument = {
#     "fname": "mina",
#     "lname": "kameel",
#     "age": 25,
#     "courses": ["mongodb", "python", "pymongo"]
#     }
# id = db.students.insert_one(studentDocument).inserted_id
# print(id)
# studentDocuments = [
#     {
#     "fname": "ahmed",
#     "lname": "khouly",
#     "age": 25,
#     "courses": ["mongodb", "python", "pymongo"]
#     },
#     {
#     "fname": "mohamed",
#     "lname": "adel",
#     "age": 25,
#     "courses": ["mongodb", "python", "pymongo"]
#     }
# ]
# ids = db.students.insert_many(studentDocuments).inserted_ids
# print(ids)

#Query for one document (find -- mapping)
# pprint.pprint(db.students.find_one())
# pprint.pprint(db.students.find_one({'fname': "abanoub"}))
# pprint.pprint(db.students.find_one({'_id': ObjectId('62601d17eef5c4c2465fbdec')}))

#Query for many documents
# for student in db.students.find():
#     pprint.pprint(student)

#counting
print(db.students.count_documents({}))