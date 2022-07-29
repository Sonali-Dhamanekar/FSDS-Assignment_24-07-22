import pymongo
client = pymongo.MongoClient("mongodb+srv://Sonali_D:Amita7688@cluster0.susuaej.mongodb.net/?retryWrites=true&w=majority")
db = client.test

import json

#read attribute.json file
attribute1=open('C:\\Users\\sonal\\anaconda3\\Attribute DataSet.json','r')
jsondata1=attribute1.read()

print(jsondata1)

database1=client['attribute_table1']
collection1 = database1['user_data1']

collection1.insert_many(jsondata1)

for i in collection1.find():
    print(i)