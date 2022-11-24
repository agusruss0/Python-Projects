import matplotlib.pyplot as plot
import numpy as np

x = np.linspace((-np.pi),np.pi,10000)
y = np.sin(x)

figura = plot.figure  ('Graficando con Python')
axis = figura.subplots()

axis.plot(x, y , '--')

axis.set_title ('Graficando con Python')
axis.set_xlabel('X')
axis.set_ylabel('Y')
axis.legend('f(x)')
axis.grid()

plot.draw()
plot.show()

