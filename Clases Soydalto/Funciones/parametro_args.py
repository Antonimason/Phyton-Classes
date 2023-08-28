#forma no optima de sumar valores
#def suma (lista):
#    numeros_sumados = 0
#    for numero in lista:
#        numeros_sumados= numeros_sumados + numero
#    return numeros_sumados

#resultado = suma([5,4,9,10,34])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resulta = suma_total([3,52,2533,23523,12])
print(resulta)

#utilizando el operador * como argumento (*args)(siempre va al final de todos los parametros)
def suma(nombre, *numeros):
    return f"{nombre}, la suma de tus numeros es: {sum(numeros)}"

resultado = suma("antonio",4,5,6,7,9)
print(resultado)

