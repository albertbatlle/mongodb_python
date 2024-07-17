from pymongo import MongoClient

def connect():
        client = MongoClient("mongodb+srv://root:Sagrera2017@cluster0.vxax9o3.mongodb.net/")
        db = client["test"]
        print("Conexión a MongoDB Correcta!")
        return db

def insertUser(db, collection, data):
     #db = connect("test")
    db[collection].insert_one(data)
    print("Usuario registrado con éxito")
    

def findUsers(db, collection):
        return db[collection].find()

def testFindOne (db, collection, email):
    return db[collection].find_one({"email":email})

def insertPurchase(db, collection, email, data):
      result = db[collection].update_one(
            {"email":email},
            {"$push": {"compras": data}}
        )
      
      result = dict(result.raw_result)
      if result["updatedExisting"]:
            print("Compra realizada.")
      else:
            print("Usuario no registrado en nuestra BBDD.")

    #   if dict(result.raw_result.updatedExisting):
    #       print("Compra realizada")
    #   else:
    #         print("Usuario no registrado en nuestra app")

def deleteUser(db, collection, email):
      return db[collection].delete_one({'email': email})
      
def loggingUser(db, collection, email, password):
      