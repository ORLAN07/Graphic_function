from py_expression_eval import Parser
from numpy import array
import matplotlib.pyplot as plt
#Orlando Rubio RNX And Jeisson Tadeo Diaz

def hanging_line(point1, point2):

    a = (point2[1] - point1[1])/(np.cosh(point2[0]) - np.cosh(point1[0]))
    b = point1[1] - a*np.cosh(point1[0])
    x = np.linspace(point1[0], point2[0], 100)
    y = a*np.cosh(x) + b

    return (x,y)

parser = Parser()
print("Actualmente puede usar 3 variables X\n")
function = input("Ingresa la funcion\n")
NUM = int(input("Ingresa la cantidad de valores para X \n"))
a = []

for i in range(NUM):
    print("Ingrese el valor de X en el campo, ", i+1)
    VAL = int(input())
    a.append([VAL, parser.parse(function).evaluate({'x': VAL})])
    print(a)

for j in a:
    point = j
    x,y = hanging_line(point, point)
    plt.plot(point[0], point[1], 'o')

plt.plot(x,y)
plt.show()