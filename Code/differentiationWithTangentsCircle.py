import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

plt.ion()
style.use('ggplot')

radius = 2
iteration = 10
jump = 0.001
accuracy = 1
colourCircle = 'blue'
colourTangent = 'red'
xPoint = 0
yPoint = 2

function1 = '('+str(radius**2)+' - x1**2)**(1/2)'
function2 = '-('+str(radius**2)+' - x2**2)**(1/2)'

x1 = np.arange(-2, (2+jump), jump)
x2 = np.arange((2-jump), (-2-jump), -jump)

y1 = eval(function1)
y2 = eval(function2)

x = np.append(x1, x2)
y = np.append(y1, y2)

for i in range(iteration):
    plt.clf()

    plt.plot(x, y, color=colourCircle)

    xEndPoint = radius/accuracy
    yEndPoint = eval(function1.replace('x1', 'xEndPoint'))

    slope = (yEndPoint-yPoint)/(xEndPoint-xPoint)

    plt.plot([xPoint, xEndPoint+5], [yPoint, yEndPoint+(5*slope)], color=colourTangent)
    plt.plot([xPoint, -(xEndPoint+5)], [yPoint, yEndPoint+(5*slope)], color=colourTangent)

    accuracy *= 2

    plt.text(-radius, radius, 'i='+str(i+1))

    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.axis('equal')
    plt.show()
    plt.pause(1)


