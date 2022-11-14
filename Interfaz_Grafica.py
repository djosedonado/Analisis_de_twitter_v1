import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import busqueda_Usuario
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading


x_data = []#array eje x
y_data = []#array eje y



def Panel_Banner(panelPrincipal):#panel del encabezado
    panelBanner = Frame(panelPrincipal)#creacion del panel
    panelBanner.pack(fill="x")
    panelBanner.config(bg="white")#color
    panelBanner.config(height=90)#altura del banner
    tituloBanner = Label(panelBanner , text="Analisis de tweets",fg="blue",font=("Comic Sans MS",18),bg="white")
    tituloBanner.place(x=450,y=20)#ubicacion del texto del banner
    Caja_Texto(panelPrincipal)#llamado de la caja de texto y el boton

    
def Caja_Texto(panelPrincipal):#caja de text
    def funciones():#funcion del proceso a ejecutar
        hilo1 = threading.Thread(target=PanelGrafico(panelPrincipal,cajaTexto.get()))#hilos de la Grafica
        hilo1.start()#Inicializacion de proceso en el hilo 1
    cajaTexto = Entry(panelPrincipal,bd=4)
    cajaTexto.config(width=25)#tamaño
    cajaTexto.place(x=60,y=90)#ubicacion
    botonCaja = Button(panelPrincipal,command=funciones)#accion del boton
    botonCaja.place(x=100,y=50)#ubicacion
    botonCaja.config(text="Buscar")#texto del boton
    botonCaja.config(width=10)#tamaño


def Panel_Seguidores(panelPrincipal,datos):
    panelSeguidores = Frame(panelPrincipal)
    panelSeguidores.pack()
    panelSeguidores.place(x=200,y=90)
    panelSeguidores.config(bg="white",width=200,height=100)
    seguidoresBanner = Label(panelSeguidores,text="Seguidores")
    seguidoresBanner.place(x=37,y=10)
    seguidoresBanner.config(bg="white",font=("Areal",18))
    text_Seguidores = Label(panelSeguidores,text=datos[0],font=("Areal",18),bg="white")
    text_Seguidores.place(x=75,y=45)

def Panel_Seguidos(panelPrincipal,datos):
    panelSeguidos = Frame(panelPrincipal)
    panelSeguidos.pack()
    panelSeguidos.place(x=400,y=90)
    panelSeguidos.config(bg="white",width=200,height=100)
    seguidoresBanner = Label(panelSeguidos,text="Seguidos")
    seguidoresBanner.place(x=37,y=10)
    seguidoresBanner.config(bg="white",font=("Areal",18))
    text_Seguidores = Label(panelSeguidos,text=datos[1],font=("Areal",18),bg="white")
    text_Seguidores.place(x=75,y=45)

def Panel_tweets(panelPrincipal,datos):
    paneltweets = Frame(panelPrincipal)
    paneltweets.pack()
    paneltweets.place(x=600,y=90)
    paneltweets.config(bg="white",width=200,height=100)
    seguidoresBanner = Label(paneltweets,text="Tweets")
    seguidoresBanner.place(x=37,y=10)
    seguidoresBanner.config(bg="white",font=("Areal",18))
    text_Seguidores = Label(paneltweets,text=datos[2],font=("Areal",18),bg="white")
    text_Seguidores.place(x=75,y=45)

def Panel_listas(panelPrincipal,datos):
    panellistas = Frame(panelPrincipal)
    panellistas.pack()
    panellistas.place(x=800,y=90)
    panellistas.config(bg="white",width=200,height=100)
    seguidoresBanner = Label(panellistas,text="Listas")
    seguidoresBanner.place(x=37,y=10)
    seguidoresBanner.config(bg="white",font=("Areal",18))
    text_Seguidores = Label(panellistas,text=datos[3],font=("Areal",18),bg="white")
    text_Seguidores.place(x=75,y=45)


def PanelGrafico(panelPrincipal,buscarUser):#panel DE GRAFICA SEGUIDORES
    print(buscarUser)
    PanelGrafico = Frame(panelPrincipal)
    PanelGrafico.pack()
    PanelGrafico.config(bg="white",width=820,height=520)
    PanelGrafico.place(x=250,y=190)
    figure = pyplot.figure()
    line, = pyplot.plot_date(x_data, y_data, '-')
    def grafica(frame):
        while True: 
            datos = busqueda_Usuario.tweets(buscarUser)
            x_data.append(datetime.now())
            y_data.append(datos[0])
            line.set_data(x_data, y_data)
            figure.gca().relim()
            figure.gca().autoscale_view()
            Panel_Seguidores(panelPrincipal,datos)
            Panel_Seguidos(panelPrincipal,datos)
            Panel_tweets(panelPrincipal,datos)
            Panel_listas(panelPrincipal,datos)
            return line,
    animacion3 = FuncAnimation(figure, grafica, interval=3000)
    canvas = FigureCanvasTkAgg(figure,master=PanelGrafico)
    canvas.get_tk_widget().place(x=140,y=50)
    canvas.draw()
    



def Panel_Principal(raiz):
    panelPrincipal = Frame(raiz)#panel principal llamado con su variable el frame
    panelPrincipal.pack(fill="both",expand="True")#damos el paquete de ajustes a toda la pantalla
    panelPrincipal.config(bg="white")#color del data frame
    panelPrincipal.config(width=1080,height=720)#tamaño del frame
    Panel_Banner(panelPrincipal)
    



def Interfaz_Grafica():
    raiz = Tk()#ventana
    raiz.title("Interfaz Grafica")
    raiz.resizable(0,0)
    raiz.geometry("1080x720")
    Panel_Principal(raiz)
    raiz.mainloop()


if __name__ == "__main__":
    Interfaz_Grafica()


