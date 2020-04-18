from math import sqrt
#Orlando Rubio RNX And Jeisson Tadeo Diaz

print("a(x^2)+bx+c=0\n")
print("La a es el coeficiente de la ecuacion cuadratica, la b es el coeficiente de la variable lineal y la c es el termino independiente... !TENGA CUIDADO!\n")

A = int(input("Ingrese el coeficiente de la variable cuadratican\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el termino independiente\n"))

if((B**2)-4*A*C) < 0:
    print("La raiz cuadrada de un numero negativo no existe")
else:
    r1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
    r2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
    print("La solucion es: \n")
    print(r1)
    print(r2)