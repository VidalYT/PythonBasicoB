# Tuplas
mi_tupla = (2, 4)
print("Mi tupla: ", mi_tupla)

# Lista
mi_lista = [1, 3.1416, "Christian", mi_tupla]
print("El primer elemento de mi lista: ", mi_lista[0])
print("El primer elemento de mi lista: ", mi_lista[3])
print("El primer elemento de mi lista: ", mi_lista[2])

# Diccionarios
mi_diccionario = {
    "mi_lista": mi_lista,
    "nombre": "christian",
    "Pi": 3.1416,
    "Tel": "664-2334455"
}
print("Llave para accesar a mi_lista", mi_diccionario["mi_lista"])
print("Llave para accesar a Pi", mi_diccionario["Pi"])
print("Llave para accesar a tel", mi_diccionario["Tel"])