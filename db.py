from pymongo import MongoClient

conn = MongoClient(host="127.0.0.1", port=27017)

def dbConect():
    conn = MongoClient(host="127.0.0.1", port=27017)

def insertDB(document, dbName, collection_name):
    db = conn.get_database(dbName)
    coll = db.get_collection(collection_name)

    coll.insert_one(document)