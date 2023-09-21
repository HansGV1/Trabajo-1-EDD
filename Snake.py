# Trabajo 1 Estructura de Datos
#
# Snake Game
#
# Integrantes:
# + Hans Guillermo García Vargas - hggarciag@unal.edu.co
# + Jose Manuel Molina Vásquez  - josemoloinav@unal.edu.co
# + Juan Jose Alzate Rojas - jalzatero@unal.edu.co
# + Ingrese aquí su nombre - ingrese aquí su correo
#
# Universidad Nacional de Colombia
#
#


# Ambiente (Interfaz)
# Ingrese su código aquí



# Serpiente
# Ingrese su código aquí
from tkinter import Tk, Frame, Canvas, Button, Label



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

#interfaz
interfaz = Tk()
interfaz.title('Snake')
interfaz.geometry('630x650')
interfaz.config(bg='white')
interfaz.resizable(width=False, height=False)

# se crea el frame para los botones, y la info del juego
f1 = Frame(interfaz, width=630, height=14, bg='grey')
f1.grid(column=0, row=0)

# se crea el frame para el juego
f2 = Frame(interfaz, width=630, height=633, bg='black')
f2.grid(column=0, row=1)

# se crea el Canvas (superficie de dibujo) y se pone en el frame 2
cv = Canvas(f2, bg='white', width=624, height=624)
cv.pack()

# se crean los rectangulos en el canvas
for i in range(0,624,48):
    for j in range(0,624,48):
        cv.create_rectangle(i,j,i+48, j+48, fill='grey')

#canvas.create_text(75,75, text='🍎', fill='red2', font = ('Arial',18), tag = 'food')

# se crea el boton de salir, y se pone en el frame f1
button1 = Button(f1, text='Salir', bg='blue') #, command = salir)
button1.grid(row=0, column=0, padx=20)

# se crea el boton de iniciar, y se pone en el frame f1
button2 = Button(f1, text='Iniciar', bg='orange') #, command = movimiento)
button2.grid(row=0, column=1, padx=20)

# se crea el boton de pausa, y se pone en el frame f1 (opcional)
button3 = Button(f1, text='Pausa', bg='green') #, command = pausa)
button3.grid(row=0, column=2, padx=20)

# los siguientes 3 Labels, son para indicar la cantidad de manzanas comidas
# se crea el Label al lado del contador de manzanas comidas, y se pone en el frame f1
cantidad1 =Label(f1, text='Cantidad', bg='grey', fg = 'black', font=('Arial',12, 'bold'))
cantidad1.grid(row=0, column=3, padx=0)

# se crea el Label con la manzana, y se pone en el frame f1
cantidad2 =Label(f1, text='🍎', bg='grey', fg = 'red', font=('Arial',12, 'bold'))
cantidad2.grid(row=0, column=4, padx=0)

# se crea el Label con la manzana, y se pone en el frame f1
cantidad3 =Label(f1, text=':', bg='grey', fg = 'black', font=('Arial',12, 'bold'))
cantidad3.grid(row=0, column=5, padx=0)

interfaz.mainloop()