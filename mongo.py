import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://octaviodevtech:octavio112020@clusteroctavio.n8a1lsl.mongodb.net/dsmdb?retryWrites=true&w=majority")

db = client["dsmdb"]

coleccion = db["dsmdb.students"]

documentos = coleccion.find()

for documento in documentos:
    print(json.dumps(documento, indent=4))