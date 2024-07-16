from pymongo import MongoClient


def connect(database):
    try:
        client = MongoClient("mongodb+srv://root:Sagrera2017@cluster0.vxax9o3.mongodb.net/")
        db = client[database]
        print("Conexión a MongoDB Correcta!")
        return db

    except Exception as e:
        print("Error de conexión a MongoDB: " + e)

def insertUser(collection, data):
    db = connect("test")
    db[collection].insert_one(data)
    print("Usuario registrado con éxito")