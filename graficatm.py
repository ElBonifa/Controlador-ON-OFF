import json

import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib import pyplot
from matplotlib.animation import FuncAnimation
from random import randrange
d = 0

plt.style.use('ggplot')
x_data = []
y_data = []


figure = pyplot.figure()
line, = pyplot.plot_date(x_data, y_data, '-')
line2, = pyplot.plot_date(x_data, y_data, '*')
line3, = pyplot.plot_date(x_data, y_data, '*')
line4, = pyplot.plot_date(x_data, y_data, '*')
filelist = []
filelist5 = []
filelist6 = []
filelist7 = []
#line3, = pyplot.plot_date(x_data, y_data, '*')
def graficamedida(frame):
    x_data.append(datetime.now())
    #y_data.append(randrange(0, 100))
    data = [1]
    data1 = [1]
    data2 = [1]
    data3 = [1]
    with open('Medida.json') as file:

        data.pop(0)
        data = json.load(file)
    filelist2 = data[0]
    filelist0 = float(filelist2[-1])
    filelist.append(filelist0)
    print("DATA:")
    largox = len (x_data)
    print(largox)
    print(filelist)

    #line.set_data(x_data, y_data)
    line.set_data(x_data,filelist)
    figure.gca().relim()
    figure.gca().autoscale_view()
    y_data.append(randrange(10, 20))
    with open('Setpoint2.json') as file1:
        data1.pop(0)
        data1 = json.load(file1)
    filelist3 = data1[0]
    filelist4 = float(filelist3[-1])
    filelist5.append(filelist4)

    largox = len(x_data)
    print("Datos analizados",filelist,filelist5,"Dimencion:", largox)
    line2.set_data(x_data, filelist5)
  ##--------------Rango de Actuador------------------------------
    with open('valormaximo.json') as file2:
        data2.pop(0)
        data2 = json.load(file2)
    filelist3M = data2[0]
    filelist4M = float(filelist3M[-1])
    filelist6.append(filelist4M)
    line3.set_data(x_data, filelist6)
    with open('valorminimo.json') as file3:
        data3.pop(0)
        data3 = json.load(file3)
    filelist3m = data3[0]
    filelist4m = float(filelist3m[-1])
    filelist7.append(filelist4m)
    line4.set_data(x_data, filelist7)

    figure.gca().relim()
    figure.gca().autoscale_view()

    return line,


animacion3 = FuncAnimation(figure, graficamedida,  interval=300)
pyplot.show()