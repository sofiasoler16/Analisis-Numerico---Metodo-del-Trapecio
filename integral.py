from sympy import *
f = input("Ingrese su funcion ")
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

listay = []

for x in listaf:
    fx = eval(f, {'x': x})  # Evaluar la función en el punto x
    listay.append(fx)

print(listay)

f0 = listay[0]
fn = listay[n-1]

suma = 0
for e in listay[1:-1]:
    suma += e
print("El resultado de la suma es ",suma)

ft = h/2*(f0 + 2*suma + fn)
print("El resultado con el metodo del trapecio es ", ft)


print("LA RESPUESTA DE LA INTEGRAL POR CALCULADORA ES:")
x=symbols("x")
res = integrate(f,(x,e1, e2))
res_decimal = res.evalf()
print(f"El resultado es {res} o aproximadamente {res_decimal}")


e = res_decimal-ft
print("El error del metodo es ", e)
