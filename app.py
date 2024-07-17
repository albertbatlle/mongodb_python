import database, utils, bcrypt, datetime, logging

def app(): 

    db = database.connect()

    while True:
        # Menu
        print("---------Users---------")
        print("1: Añadir un usuario")
        print("2: Ver usuarios")
        print("3: Buscar usuario por mail")
        print("4: TODO: Eliminar usuario por mail")
        print("5: TODO: Login")
        print("--------Purchases------")
        print("6: Añadir una compra (embedded)")
        print("7: TODO: Añadir una compra (referenced)")
        print("Escribre 'exit' para salir")

        opcion = input("Seleccione una opción: ")

        

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("email: ")
            while utils.validar_email(email) == False:
                email = input("Introduce email correcto: ")
           # if not utils.validar_email(email):
            #    print("Email con formato incorrecto")
             #   return
            password = input("Contraseña: ")
            passHashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            # Validar si el mail ya está registrado
            if database.testFindOne(db, "users", email):
                print("Email ya registrado en la app")
            else:
                #Creamos una variable tipo dict(diccionario) igual que un JSON
                data = {
                    "nombre": nombre,
                    "email": email,
                    "password": passHashed
                }

                database.insertUser(db, "users", data)
                
        if opcion == "2":
            userObj = database.findUsers(db, "users")
            for user in userObj:
                print(user)

        if opcion == "3":
            email = input("Escribre un mail: ")
            user = database.testFindOne(db, "users", email)
            if user:
                print(user)
            else:
                print("Usuario no encontrado")

        if opcion == "4":
            email = input("Escribe el mail del usuario a suprimir: ")
            suprimido = database.deleteUser(db, "users", email)
            suprimido = dict(suprimido.raw_result)
            if suprimido['n'] == 1:
                print(f"Usuario {email} suprimdo ")
            else:
                print(f"Usuario {email} no encontrado")
        
        if opcion == "5":
            logging.getLogger('pymongo.<componentName>').setLevel(logging.DEBUG)
            # https://pymongo.readthedocs.io/en/stable/examples/logging.html
        
        if opcion == "6":
            email = input("Email del usuario: ")
            producto = input("Producto: ")
            cantidad = input("Cantidad: ")
            precio = input("Precio: ")
            data = {
                "producto": producto,
                "cantidad": cantidad,
                "precio": precio,
                "fecha": datetime.datetime.now()
            }
            database.insertPurchase(db, "users", email, data)

        if opcion == "exit":
            print("Bye")
            exit()

app()