import math
l=int(input("Ingrese la tasa media: "))
x=int(input("Ingrese el valor de k: "))
ex=math.exp(-l)
lan=l**x
pk=(ex*lan)/math.factorial(x)
print("El Resultado es: ",pk)
print("Porcentaje: ",pk*100)