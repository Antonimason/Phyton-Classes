cadena1 = "Hola soy Antonio"
cadena2 = "Bienvenido maquinola"

#convierte a mayusculas
mayusc = cadena1.upper()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula
primer_letra_mayusc = cadena1.capitalize()

#buscamos una cadena en otra cadena
busqueda_find = cadena1.find("Hola") #Devuelve la posicion del dato, cuando no encuentra un valor devuelve -1 ()

#buscamos una cadena en otra cadena
busqueda_index = cadena1.index("a") #Devuelve la posicion del dato, cuando no encuentra un valor devuelve un error (exception error)

#si es numerico, devolvemos True, sino devolvemos false
es_numerico = cadena1.isnumeric() #output false, porque el string no tiene numero

#si es alfanumerico devolvemos true, sino devolvemos false. (los espacios no son caracteres alfanumericos)
es_alfanumerico = cadena1.isalpha()

#buscamos una cadena en otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("Ho")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("io")

#remplaza un pedazo de la cadena dada, por otra dada. si el valor 1 se encuentra en la cadena original, reemplaza el valor 1 de la misma por le valor 2
cadena_nueva = cadena1.replace("Ho","holu maquina")

#separar cadenas con la cadena que le pasemos. quiere decir que puedes transformar un string en un array
caddena_separada = cadena1.split(" ")

print(caddena_separada)