import numpy as np
from sympy import *
from tabulate import tabulate

#Pedir la funcion
def pedir_valores():
    f = input("Ingrese su funcion ")
    x = symbols('x')
    f_sympy = sympify(f)  # Convierte la cadena en una expresión de SymPy
    f_lambdified = lambdify(x, f_sympy, 'numpy')

    print("Ingrese los extremos de integracion")
    e1,e2 = int(input("Extremo 1 ")), int(input("Extremo 2 "))
    n = int(input("En cuantos subintervalos quiere dividir el intervalo principal? "))

    h = (e2-e1)/n
#Calcular valores de los subintervalos para la funcion
def subintervalos(e1,e2,h):
    print("Vamos a calcular la funcion para cada parte de los subintervalos, nos queda: ")
    listaf = [e1,]
    a = e1
    while a < e2:
        a = a + h
        listaf.append(a)
    print(listaf)
    return listaf

#Calcular valores de la funcion en los puntos
def valor_funcion(listaf,f_lambdified):
    print("Calculamos los valores de la funcion en los puntos y nos queda una tabla: ")
    listay = []
    for x_val in listaf:
        fx = f_lambdified(x_val)  # Evaluar la función en el punto x_val
        fx_rounded = round(fx, 8)  # Redondear al octavo decimal
        listay.append(fx_rounded)

    f0 = listay[0]
    fn = listay[-1]

    # print(listay)
    return listay

#Calcular error
def error(f_sympy,x,e1,e2,h):
    #Calcular la segunda derivada
    segunda_derivada = diff(f_sympy, x, x)
    segunda_derivada_funcion = lambdify(x, segunda_derivada, 'numpy')

    #Calcular el valor maximo de la segunda derivada
    x_eval = np.linspace(e1, e2, 100)
    valores_segunda_derivada = segunda_derivada_funcion(x_eval)
    max_segunda_derivada = np.max(np.abs(valores_segunda_derivada))

    error = ((e2 - e1) * h**2 * max_segunda_derivada) / 12

    print("El error del metodo es: ", error)

#Calcular suma para el metodo
def suma(listay):
    suma = 0
    for e in listay[1:-1]:
        suma += e
    return suma

# Mostrar tabla de subintervalos y valores de la función
def mostrar_tabla(listaf, listay):
    table = [["Subintervalo", "Valor de la función"]]
    for i in range(len(listaf)):
        table.append([listaf[i], listay[i]])
    print(tabulate(table, headers="firstrow", tablefmt="grid", colalign=("center", "center")))

#Calcular valor real por calculadora
def calcu(f_sympy,e1,e2):
    print("--------------- LA RESPUESTA DE LA INTEGRAL POR CALCULADORA ES: -----------------")
    x=symbols("x")
    res = integrate(f_sympy, (x,e1, e2))
    res_decimal = res.evalf()
    print(f"El resultado es {res} o aproximadamente {res_decimal}")

#Calcular por metodo del trapecio
def trapecio():
    print("--------------- VAMOS A IGRESAR LOS PARAMETROS ---------------")
    f = input("Ingrese su funcion ")
    x = symbols('x')
    f_sympy = sympify(f)  # Convierte la cadena en una expresión de SymPy
    f_lambdified = lambdify(x, f_sympy, 'numpy')

    print("Ingrese los extremos de integracion")
    e1,e2 = int(input("Extremo 1 ")), int(input("Extremo 2 "))
    n = int(input("En cuantos subintervalos quiere dividir el intervalo principal? "))

    h = (e2-e1)/n

    print("----------- VAMOS A RESOLVER POR METODO DE TRAPECIOS -----------------")

    # Obtener los subintervalos y los valores de la función
    listaf = subintervalos(e1, e2, h)
    listay = valor_funcion(listaf, f_lambdified)

    f0 = listay[0]
    fn = listay[-1]

    mostrar_tabla(listaf, listay)

    suma_intermedia = suma(listay)

    ft = h/2*(f0 + 2*suma_intermedia + fn)
    print("El resultado con el metodo del trapecio es: ", ft)

    error(f_sympy,x,e1,e2,h)

    calcu(f_sympy,e1,e2)

def main():
    print("Quiere resolver algun ejercicio de los ya cargados(Ingrese A) o Ingresar su propia funcion(Ingrese B?")
    el = input("Ingrese su respueta: ")



if __name__ == "__main__":
    trapecio()
