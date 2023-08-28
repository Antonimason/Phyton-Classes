#creando una lista con list()
lista = list(["Hola","Antonio",34,45,10,True])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a la lista
lista.append("JAJAJAJA")

#agregando un elemento a la lista en un indice especifico. inser(indice,dato)
lista.insert(2, "Toma MAMA")

#agregrando varios elementos a la lista
lista.extend([False,2030])

#eliminando un elemento de la lista (por su indice). con -1 eliminas el ultimo, con -2 eliminas el penultimo
lista.pop(0) #-1 eliminas el ultimo, con -2 eliminas el penultimo y asi sucesivamente

#removiendo un elemento de la lista por su valor
lista.remove("Antonio") #si no consigue el valor, devuelve un error

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando la lista de forma ascendente (solo con numeros y booleanos)(si usamos el parametro reverse=True lo ordena en reverse)
#lista.sort()

#invirtiendo los elementos de una lista 
#lista.reverse()

#verificando si un elemento se encuentra en la lista
elemento_encontrado = lista.index(34)

print(elemento_encontrado)