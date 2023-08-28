#si es un modulo con un codigo corto
#import modulo_saludar as m_saludar
#saludo = m_saludar.saludar("Antonio")
#print(saludo)



#si es un modulo con un codigo super largo
#desde ese modulo, importamos dos funciones
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_cosco

saludo = saludar_normal("Antonio")
saludo_raro = saludar_como_cosco("Antonio")

#msotrando los resultados
print(saludo)
print(saludo_raro)

#para ver las propiedades y metodos de el namespace
#print(dir(m_saludar))

#accedemos al nombre de este modulo
print(__name__)

#accedemos al nombre del modulo llamado
#print(m_saludar.__name__)