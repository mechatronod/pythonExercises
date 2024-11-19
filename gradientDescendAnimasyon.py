#gradient descent algoritması ile fonksiyon minimumu bulma
#gradient descent algoritması animasyonu oluşturma

from matplotlib.animation import FuncAnimation
from matplotlib import pyplot as plt
import numpy as np

def yFonksiyon(x):
    return x **2

def yTurevi(x):
    return 2*x

x = np.arange(-100,100,0.1)
y = yFonksiyon(x)

mevcutDurum = (80,yFonksiyon(80))

learning_rate = 0.01

for _ in range(1000):
    yeni_X = mevcutDurum[0] - learning_rate*yTurevi(mevcutDurum[0])
    yeni_Y = yFonksiyon(yeni_X)
    mevcutDurum = (yeni_X,yeni_Y)
    print(mevcutDurum)
    if (abs(mevcutDurum[0] - mevcutDurum[1])<0.01):
        break

    plt.plot(x,y)
    plt.scatter(mevcutDurum[0], mevcutDurum[1],color="red")
    plt.pause(0.01)
    
    plt.clf()

# plt.show()