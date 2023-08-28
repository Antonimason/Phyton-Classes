#usando open para abrir un archivo
archivo = open("Archivos\\texto_de_antonio.txt")

#leer archivo completo
#archivo = archivo.read()

#leer linea por linea
#lineas = archivo.readlines()

#leer una sola linea
linea = archivo.readline()

#cerrar el archivo
archivo.close()

print(linea)