import database


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
        #Creamos una variable tipo dict(diccionario) igual que un JSON
        data = {
            "nombre": nombre,
            "email": email,
            "password": password
        }

        database.insertUser("users", data)

        
     #   database.connect("test")


    if opcion == "exit":
        print("Bye")
        exit()