#2 listas, una con nombres otra con apellidos

nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robertix","Tarado"]

#Registrar esta informacion en un TXT de forma optima

with open("nombres_y_apellidos.txt","w") as arch:
    arch.writelines("Los datos son:\n\n")
    [arch.writelines(f"Nombres: {n}\nApellido: {a}\n-----------\n") for n,a in zip(nombres,apellidos)]