# STRING

"string"
'string'
"""string mas
    largo
    en cuanto a lineas """
'''string mas
    largo
    en cuanto a lineas'''
    
nombre = "Antonio";

# NUMEROS Y FLOAT

40

42.5

numero = 36;

# BOOLEANOS

False
True

# CONCATENACION

bienvenida = "Hola " + nombre + " como estas?";
print(bienvenida);

# CONCATENACION CON F-STRING = funciona para convertir cualquier dato en texto
nombre = 5;
bienvenido = f"Hola {nombre} commo estas?"
# ELIMINAR UNA VARIABLE DECLARADA
#del bienvenido
print(bienvenido);

# OPERADORES DE PERTENENCIA (in / not in) = se utilizan para comprobar si un valor o variable se encuentran en una secuencia

print("ola" in bienvenida); # True
print("Lucas" not in bienvenida) # False