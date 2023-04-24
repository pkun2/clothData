from pymongo import MongoClient

conn = MongoClient(host="127.0.0.1", port=27017)

dbName = "bigdata"
collection_name = "mushinsa"

def dbConect():
    conn = MongoClient(host="127.0.0.1", port=27017)

    dbName = "bigdata"
    collection_name = "mushinsa"

def insertDB(name):
    db = conn.get_database(dbName)
    coll = db.get_collection(collection_name)

    document = {"name": name}
    coll.insert_one(document)