#Lista
lista = ["Antonio Giambra", "Antonimason", True, 1.72] #se pueden modifiar

#Tupla
tupla = ("Antonio Giambra", "Antonimason", True, 1.72) #la tupla no se puede modificar

lista[3] = "Maquinola" #esto es valido

#tupla[3] = "Maquinola" #esto no es valido

#Creando un conjunto (set)

conjunto = {"Antonio Giambra", "Antonimason", True, 1.72} #es una colección desordenada de elementos que no se repiten. Esto significa que todos los elementos de un conjunto deben ser distinto. Puede agregar y eliminar elementos de un conjunto; por lo tanto, el conjunto es un colección mutable. Puede contener elementos de diferentes tipos de datos.

#print(conjunto[3]) -> no se peude acceder el elemento

#Creando un diccionario (dict) = la estructura es key : value y separamos con comas

diccionario = {
    'nombre' : "Antonio Giambra",
    'instagram' : "Antonimason",
    'esta emocionado' : True,
    'altura' : 1.72,
    'dato_duplicado' : "Antonimason"
}
tipo_de_dato = type(diccionario) #type(dato) nos devuelveque tipo de dato es
print(diccionario['altura'])
print(tipo_de_dato)