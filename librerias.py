import math
l=int(input("Ingrese la tasa media: "))
x=int(input("Ingrese el valor de k: "))
ex=math.exp(-l)
lan=l**x
pk=(ex*lan)/math.factorial(x)
print("El resultado es de: ",pk)
print("El valor en porcentaje es de: ",pk*100 "%")