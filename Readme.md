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