import numpy as np
from sympy import *

# x = symbols('x')
f = input("Ingrese su funcion ")
# funcion_simbolica = sympify(f)
# funcion = lambdify(x, funcion_simbolica, 'numpy')

print("Ingrese los extremos de integracion")
e1,e2 = int(input("Extremo 1 ")), int(input("Extremo 2 "))

print("Lo vamos a resolver por Metodo del Trapecio")
n = int(input("En cuantos subintervalos quiere dividir el intervalo principal? "))
h = (e2-e1)/n

print("Vamos a calcular la funcion para cada parte de los subintervalos")
listaf = [e1,]
a = e1
while a < e2:
    a = a + h
    listaf.append(a)
print(listaf)

# Evaluación de la función en cada punto
listay = []

x = symbols('x')
f_sympy = sympify(f)  # Convierte la cadena en una expresión de SymPy
f_lambdified = lambdify(x, f_sympy, 'numpy')

# for x in listaf:
#     fx = eval(f, {'x': x})  # Evaluar la función en el punto x
#     listay.append(fx)

for x_val in listaf:
    fx = f_lambdified(x_val)  # Evaluar la función en el punto x_val
    fx_rounded = round(fx, 8)  # Redondear al octavo decimal
    listay.append(fx_rounded)

print(listay)

f0 = listay[0]
fn = listay[-1]

suma = 0
for e in listay[1:-1]:
    suma += e
print("El resultado de la suma es ",suma)

ft = h/2*(f0 + 2*suma + fn)
print("El resultado con el metodo del trapecio es ", ft)


print("LA RESPUESTA DE LA INTEGRAL POR CALCULADORA ES:")
x=symbols("x")
res = integrate(f_sympy, (x,e1, e2))
res_decimal = res.evalf()
print(f"El resultado es {res} o aproximadamente {res_decimal}")

#ERROR DEL METODO

#Calcular la segunda derivada
segunda_derivada = diff(f_sympy, x, x)
segunda_derivada_funcion = lambdify(x, segunda_derivada, 'numpy')

#Calcular el valor maximo de la segunda derivada
x_eval = np.linspace(e1, e2, 100)
valores_segunda_derivada = segunda_derivada_funcion(x_eval)
max_segunda_derivada = np.max(np.abs(valores_segunda_derivada))

error = ((e2 - e1) * h**2 * max_segunda_derivada) / 12

e = res_decimal-ft
print("El error del metodo es ", error)
