#------------------ESTO SIRVE TANTO PARA LISTAS, TUPLAS Y CONJUNTOS------------------

animales = ["gato","perro","loro","cocodrilo"]
numeros = [52,19,24,90]

#recorriendo la lista animales
for animal in animales:
    print(f'Ahora la variable animal es a : {animal}')
    
#recorriendo la lista numeros y multiplicando cada valor por 10
for numero in numeros:
    resultado = numero * 10
    print(resultado)

#iterando dos listas del mismo tamaño al mismo tiempo
for numero,animal in zip(animales,numeros):
    print(f'recorriendo la lista 1: {numero}')
    print(f'recorriendo la lista 2 :{animal}')
    
#forma no optima de recorrer una lista con su indice (no funciona para conjuntos)
for num in range(len(numeros)):
    print(numeros[num])
    
#forma correcta de recorrer una lista con su indice
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(num)
    print(f'el indice es : {indice} y el valor es: {valor}')
    print(type(num))
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')