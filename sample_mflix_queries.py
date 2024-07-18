from pymongo import MongoClient

client = MongoClient("mongodb+srv://root:Sagrera2017@cluster0.vxax9o3.mongodb.net/")
db = client["sample_mflix"]

# Ejercicios Consulta
# 1- Obtener todas las películas
# movies = db["movies"].find()
# print(movies)

# for movie in movies:
#     print(movie["title"])


# 2- Obtener todos los títulos de las películas de género Acción
# movies = db["movies"].find({"genres": "Action"})

# for movie in movies:
#     print(movie["title"])

# 3- Obtener todos los títulos de las películas de acción que hayan sido rodadas en 2014:
# movies = db["movies"].find({"genres": "Action", "year": 2014})

# for movie in movies:
#      print(movie["title"])


# 4- Películas de acción ordenadas por título:
# movies = db["movies"].find({"genres": "Action"}).sort("title")

# for movie in movies:
#     print(movie["title"])

# 5- Obtener los 5 primeros títulos de las películas del gérenro acción ordenads por título
# movies = db["movies"].find({"genres": "Action"}).sort("title").limit(5)

# for movie in movies:
#     print(movie["title"])


# 6- Obtener todos los títulos de las películas de género "Action" que tengan un rating de más de 8 y que se estrenaron en el mes de enero.

movies = db["movies"].find({"genres": "Action", "imdb.rating":{"$gt": 8}})

for movie in movies:
    print(movie["title"])

#, "released": {"$regexp": "^1914-01"}