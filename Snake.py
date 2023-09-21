# Trabajpo 1 Estructura de Datos
#
# Snake Game
#
# Integrantes:
# + Hans Guillermo García Vargas - hggarciag@unal.edu.co
# + Jose Manuel Molina Vásquez  - josemoloinav@unal.edu.co
# + Ingrese aquí su nombre - ingrese aquí su correo
# + Ingrese aquí su nombre - ingrese aquí su correo
#
# Universidad Nacional de Colombia
#
#


# Ambiente (Interfaz)
# Ingrese su código aquí



# Serpiente
# Ingrese su código aquí



# Manzana
import random
poscuadros =  [15, 45, 75,105,135,165, 195, 225, 255, 
    285, 315, 345, 375] 
manzana = "⬛"
def posmanzana():
    cordxmanzana = random.choice(poscuadros)
    cordymanzana = random.choice(poscuadros)
    cords = (cordxmanzana, cordymanzana)
    #definir posicion serpiente

