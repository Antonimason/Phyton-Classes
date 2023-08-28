#creando diccionarios con dict()
diccionario = dict(nombre="Antonio", apellido="Giambra");

#las listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario = {frozenset(["Antonio","Giambra"]) : "jajaja"}

#creando diccionario con fromkeys()
diccionario = dict.fromkeys(["nombre","appellido"])

print((diccionario))