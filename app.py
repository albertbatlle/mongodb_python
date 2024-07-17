import database, bcrypt

def app(): 

    db = database.connect()

    while True:
        # Menu
        print("----------------------")
        print("1: Añadir un usuario")
        print("2: Ver usuarios")
        print("3: Buscar usuario por mail")
        print("-----------------------")
        print("4: Añadir una compra (embedded)")
        print("5: Añadir una compra (referenced)")
        print("Escribre 'exit' para salir")

        opcion = input("Seleccione una opción: ")

        

        if opcion == "1":
            nombre = input("Nombre: ")
            email = input("email: ")

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

        if opcion == "exit":
            print("Bye")
            exit()

app()