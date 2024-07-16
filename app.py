import database, bcrypt


while True:
    # Menu
    print("1: Añadir un usuario")
    print("2: Ver usuarios")
    print("3: Buscar usuario por mail")
    print("4: Escribre 'exit' para salir")

    opcion = input("Seleccione una opción: ")

    

    if opcion == "1":
        nombre = input("Nombre: ")
        email = input("email: ")

        password = input("Contraseña: ")
        passHashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
        # Validar si el mail ya está registrado
        if database.testFindOne("users", email):
            print("Email ya registrado en la app")
        else:
            #Creamos una variable tipo dict(diccionario) igual que un JSON
            data = {
                "nombre": nombre,
                "email": email,
                "password": passHashed
            }

            database.insertUser("users", data)
            
    if opcion == "2":
        userObj = database.findUsers("users")
        for user in userObj:
            print(user)


    if opcion == "exit":
        print("Bye")
        exit()