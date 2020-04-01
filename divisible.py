try:
    n=int(input("numero: "))
    print("El numero es divisible entre", [i for i in [2,3,5,7] if n%i==0])
except:
    print("no es un numero")
