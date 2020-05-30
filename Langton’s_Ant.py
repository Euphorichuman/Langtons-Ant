import turtle
import sys
import time
import math
from win32api import GetSystemMetrics
from easygui import multenterbox, msgbox

def langtonAnt():
    
    #Configuración el multenterbox para pedir datos al usuario
    msg = "Por favor, introduzca los datos" + "\nNota 1: Tenga en cuenta que la posición x, y = (0, 0) es el centro de la ventana, pero su <<n>> será tomado de forma global." + "\nNota 2: Tenga en cuenta que La hormiga sigue un camino aparentemente azaroso hasta los 10.000 pasos."
    title = "La hormiga de Langton"
    fieldNames = ["Número de movimientos:", "Posición inicial x:", "Posición inicial y:", "Tamaño <<n>> de la grilla:"]
    fieldValues = multenterbox(msg, title, fieldNames)
    if fieldValues is None:
        sys.exit(0)
    
    #Se comprueba que el usuario ha llenado todos los campos
    while 1:
        errorMsg = ""
        for i, name in enumerate(fieldNames):
            if fieldValues[i].strip() == "":
                errorMsg += "{} Es un campo requerido para iniciar.\n\n".format(name)
        if errorMsg == "":
            break #Todos los campos llenos
        fieldValues = multenterbox(errorMsg, title, fieldNames, fieldValues)
        if fieldValues is None:
            break
    
    #Configuración la ventana
    widht = GetSystemMetrics(0)
    height = GetSystemMetrics(1)
    wn = turtle.Screen()
    wn.title("La Hormiga de Langton")
    wn.bgcolor("white")
    wn.screensize(widht, height)

    #Se llama la función para dibujar el borde de la grilla
    border((int(fieldValues[3])+10))

    #Configuración del texto contador de movimientos
    text = turtle.Turtle()
    text.speed(0)
    text.color("red")
    text.penup()
    text.hideturtle()
    text.goto(0, 300)

    #Dicionario con las cordenadas y su respectivo color 
    maps = {}

    #Configuración de la hormiga
    ant =  turtle.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.penup()
    ant.goto(int(fieldValues[1]), int(fieldValues[2]))
    ant.speed(0)
    pos = coordinate(ant)

    #Variable para contar los movimientos
    cont = 0

    #Variable para verificar que la hormiga no se salga de los limites
    hit = False
    
    #Movimiento de la hormiga
    while cont <= int(fieldValues[0])-1 and hit == False:
        step = 10
        if pos not in maps or maps[pos] == "white":
            ant.fillcolor("black")
            ant.stamp()
            invert(maps, ant, "black")
            ant.right(90)
            ant.forward(step)
            pos = coordinate(ant)
            cont += 1
        elif maps[pos] == "black":
            ant.fillcolor("white")
            ant.stamp()
            invert(maps, ant, "white")
            ant.left(90)
            ant.forward(step)
            pos = coordinate(ant)
            cont += 1
        
        #Comprueba que la hormiga esta dentro de la grilla
        if round(math.fabs(ant.xcor())) > (int(fieldValues[3]) / 2) - 1:
            hit = True
            msgbox(msg="La hormiga no puede segir avanzando porque chocó con los bordes de la grilla que usted introdujo."
            "\nSi desea que la hormiga complete todos los movimientos, se recomienda introducir una grilla mas grande.", title="Fuera de límites", ok_button="Aceptar")
        if round(math.fabs(ant.ycor())) > (int(fieldValues[3]) / 2) - 1:
            hit = True
            msgbox(msg="La hormiga no puede segir avanzando porque chocó con los bordes de la grilla que usted introdujo."
            "\nSi desea que la hormiga complete todos los movimientos, se recomienda introducir una grilla mas grande.", title="Fuera de límites", ok_button="Aceptar")

        text.clear()
        text.write("Movimientos: {}".format(cont), align="center", font=("Courier", 24, "normal")) 

    while True:
        wn.update()        

#Devuelve la cordenada de la hormiga en una tupla
def coordinate(ant):
    return (round(ant.xcor()), round(ant.ycor()))

#Invierte el color de la celda de la grilla en que está la hormiga
def invert(graph, ant, color):
    graph[coordinate(ant)] = color

#Dibuja el borde de la grilla
def border(n):
    border = turtle.Turtle()
    border.hideturtle()
    border.penup()
    border.goto(n/2, 0)
    border.pendown()
    border.left(90)
    border.forward(n/2)
    border.left(90)
    border.forward(n)
    border.left(90)
    border.forward(n)
    border.left(90)
    border.forward(n)
    border.left(90)
    border.forward(n/2)

#Se ejecuta el código
langtonAnt()