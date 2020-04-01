from collections import deque

#Colas en un CarWash
cola=deque (["Tesla","Honda","Toyota"])
print("carros en espera en Carwash")
print("Turno 1: ",cola[0])
print("Turno 2: ",cola[1])
print("Turno 3: ",cola[2])
cola.append("ford")
print("nuevo turno 4:",cola[3])
cola.popleft()
print("carros en espera en Carwash")
print("Turno 2: ",cola[0])
print("Turno 3: ",cola[1])
print("Turno 4: ",cola[2])
 

