print("PROPAGACION DE MENSAJES ENTRE INDIVIDUOS.")
print("  r. ROJO     a. AZUL")
primera = input("  Elija un una variable (r o a): ")
if primera == "r":
    x = int(input("ingrese su patch"))
    print("Su mensaje se difundio", x, "veces") 
else:
    print("Su color de agente no puede difundir los mensajes, No ha llegado a la meta")
