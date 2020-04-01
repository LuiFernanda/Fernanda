

a = int(input("ingrese el preciofrutas"))
b = int(input("ingrese el precioverduras"))
c = int(input("ingrese el preciogranos")) 
p = int(input("ingrese presupuesto para ecuacion")) 

resultadoe = a + b + c
 
if resultadoe <= p:

    print   ("tu gasto es:",resultadoe)
    print ("Eres buen comprador ")
else:
    print ("que mal comprador eres")



