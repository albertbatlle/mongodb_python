# MongoDB
- MongoDB es un sist de BBDD NoSQL (Not only SQL) que se caracteriza por estar orientado a "documentos". Esto significa que en lugar de guardar los datos en tablas (BBDD relacionales) se estructuran en datos similares a JSON (JavaScript Object Notation) con un esquema dinámico. Esto hace que la integración de los datos en ciertas aplicaciones  sea más fácil y rápida. 

# Características principales:
1- Esquema flexible: Los documentos en MongoDB no requieren de una estructura definida préviamente, lo que permite almacenar datos de manera más flexible y evolucionar el esquema de datos con el tiempo.

2- Escalabilidad: MongoDB esta diseñado para ser escalable horizontalmente, distribuyendo los datos a través de múltiples servidores para manejar grandes vólumenes de información y cargas de trabajo.

3- Consultas poderosas: Soporta consultas complejas, índices y agregaciones permitiendo realizar operaciones complejas sobre los datos.

4- Alta disponibilidad: MongoDB puede configurarse para mantener los datos disponibles incluso en situaciones de fallo de hardware o red.

5- Rendimiento: Debido a su arquitectura de almacenamiento de documentos y su capacidad de indexación, MongoDB puede proporcionar un rendimiento rápido sobretodo a aplicaciones que trabajan con grandes vólumenes de datos.

# Trabajar con MongoDB
## Servidor
- [MongoDB Atlas (nube)](https://www.mongodb.com/try/download/community)
- [MongoDB Community (local)](https://www.mongodb.com/products/platform/atlas-database)

## Cliente
- [MongoDB Compass](https://www.mongodb.com/try/download/compass)

# Estructura MongoDB
- Database
    - Collections (tablas)
        - Documents (Campos)
            - Datos (JSON)

## JSON
- JavaScript Object Notation: Es una estructura de datos (objeto JS solamente con props)

{
    "nombre_prop": valor, 
    "nombre_prop2": valor,
    "nombre_prop3": {
        "nombre_prop3-1": valor,
        "nombre_prop3-2": valor
    }
}

# Como relacionar documentos
- En este ejemplo estamos en primer lugar, gesionando usuarios en MongoDB. Queremos relacionar compras a estos usuarios. ¿Cómo lo hacemos en MongoDB?

## 1- Relación embebido (embedded)
- En este enfoque, las compras de un uusario se almacenan como un subdocumento dentro del documento de usuario. Ésta estructura es útil si las compras de todos los usuarios no son muy elevadas y no van a crecer de forma descontrolada, dado que MongoDB tiene un límite de 16MB por documento

{
    '_id': ObjectId('6697d45cf8cc178843fae2e6'), 
    'nombre': 'a', 
    'email': 'a@a.a', 
    'password': b'$2b$12$LgVhJOz15n/2zs9B6N10xO2Gp.AuV7Fx8kj12tEMfI0TWqYHhAsRq'
    'compras': [
        {
            'id': ObjectId('323456782003539),
            'producto': "Lavadora",
            'cantidad': 2,
            'precio': 1300,
            'fecha': "2024-07-09"
        },
        {
            'id': ObjectId('323456782872319),
            'producto': "Tostadora",
            'cantidad': 1,
            'precio': 35,
            'fecha': "2024-07-15"
        }
    ]
}

## 2- Relación referenciada (referenced)
- En este enfoque, las compras se almacenan en una colección separada y cad compra tiene una referencia al usuario que la compró mediante un id único. Este método es más flexible y escalable, especialmente si esperas que las compras sean elevadas.

```json users:

{
    '_id': ObjectId('6697d45cf8cc178843fae2e6'), 
    'nombre': 'a', 
    'email': 'a@a.a', 
    'password': b'$2b$12$LgVhJOz15n/2zs9B6N10xO2Gp.AuV7Fx8kj12tEMfI0TWqYHhAsRq'
}

```json purchaces:
{
    'id': ObjectId('323456782003539),
    'user_id': 1,
    'producto': "Lavadora",
    'cantidad': 2,
    'precio': 1300,
    'fecha': "2024-07-09"
}

{
    'id': ObjectId('323456782872319),
    'user_id': 1,
    'producto': "Tostadora",
    'cantidad': 1,
    'precio': 35,
    'fecha': "2024-07-15"
}
