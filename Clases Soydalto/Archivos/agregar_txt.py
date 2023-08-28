
with open('Archivos\\texto_de_antonio.txt','a') as archivo:
    
    #sobreescribiendo el archivo
    #archivo.write("jajajajajaj te lo vas a mamar sapo")
    
    #agregando 2 lineas con writelines
    archivo.writelines(["hola maestro como andas\n","misericordia\n\n"])
    
    #agregando otras 2 lineas
    archivo.writelines(["eres un estupido lo sabias\n?","misericordia"])
    