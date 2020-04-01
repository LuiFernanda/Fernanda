"""COLAS: FIFO"""
#cola de cientes en un banco
print("clientes en el banco")
cola = ["Juan","María"]
#Llega nuevo cliente
cola.append("Luis")
#imprimir turnos
print("Turnos")
print(cola.index("Juan"),cola.index("María"),cola.index("Luis"))
print(cola)
#Se atiende cliente
print("Turno número:",cola.index("Juan") )
print(cola [0],"fue atendido")
cola.pop(0)
print(cola)