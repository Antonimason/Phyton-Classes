#funciones integradas en python

numeros = [4,7,1,42,15]

#encontrando el numero mayor de una lista
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero emnor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales (numero, decimales)
numero = round(12.34356,3)

#retorna False -> 0, vacio, False,ninguno / True -> distinto a 0, True, cadena, datos no vacios
resultado_bool = bool(0)

#retorna True, si todos los valores son verdaderos (deben ser iterables)
resultado_all = all([234,"true",[344,33]])

#suma todos los valores de un iterable
suma_total = sum(numeros)

print(suma_total)