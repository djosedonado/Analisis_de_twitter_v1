import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
import busqueda_Usuario
from tkinter import Tk, Frame, Button
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ventana = Tk()
#ventana.geometry("1080x720")

def main():
    ventana.title("Analisis de Datos")
    ventana.resizable(0, 0)
    ventana.config(bg="white")
    frame = Frame(ventana)
    frame.pack()
    frame.config(bg="blue")
    frame.config(width=1080,height=720)
    

    #plt.style.use('ggplot')
    x_data = []
    y_data = []
    figure = pyplot.figure()
    line, = pyplot.plot_date(x_data, y_data, '-')

    def grafica3(frame):
        while True: 
            datos = busqueda_Usuario.tweets("auronplay")
            x_data.append(datetime.now())
            y_data.append(datos[0])
            line.set_data(x_data, y_data)
            figure.gca().relim()
            figure.gca().autoscale_view()
            return line,
    
    animacion3 = FuncAnimation(figure, grafica3, interval=3000)
    canvas = FigureCanvasTkAgg(figure,master=frame)
    canvas.get_tk_widget().pack(padx=5,pady=5,expand=1,fill="both")
    canvas.draw()
    ventana.mainloop()


if __name__ == "__main__":
    main()







#animacion3 = FuncAnimation(figure, grafico, interval=5000)
