frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "Hola Antonio"
numeros = [2,5,8,19]

#evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me voya comer una {fruta}')
    
#evitar que el bucle siga ejecutandose
for fruta in frutas:
    if fruta == 'pera':
        break
    print(f'Me voya comer una {fruta}')

#recorrer una cadena de texto
for letra in cadena:
    print(letra)
    
#for en una sola linea de codigo (duplicamos los numeros)
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)