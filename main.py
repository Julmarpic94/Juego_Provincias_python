import turtle
import pandas


screen = turtle.Screen()
screen.title("Paises de Europa")
image = "spainMap.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("provincias.csv")
all_provincias = data.provincia.to_list()
provincias_nombradas = []



while len(provincias_nombradas) < 50:
    pregunta = screen.textinput(f"Provincias Restantes: {len(provincias_nombradas)}/50", prompt="Adivina una provincia").title()
    print(pregunta)
    if pregunta == "Exit":
        provincias_aprender = []
        for provincia in all_provincias:
            if provincia not in provincias_nombradas:
                provincias_aprender.append(provincia)
        #Almacenar las provincias por aprender en el un csv
        new_data = pandas.DataFrame(provincias_aprender)
        new_data.to_csv("ProvinciasApender.csv")
        break

    if  pregunta in all_provincias:
        #si está la provincia creamo suan toruga para escribir el nombre
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        dato_provincia = data[data.provincia == pregunta]
        t.goto(dato_provincia.x.item(), dato_provincia.y.item())
        t.write(dato_provincia.provincia.item())
        provincias_nombradas.append(dato_provincia.provincia.item())





# Detecta los clics del mouse y llama a la función para mostrar las coordenadas



