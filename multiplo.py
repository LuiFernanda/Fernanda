def multiplos_hasta_limite(numero, limite):
    
    multiplos = []
    i = 1
    multiplo = numero

    while multiplo <= limite:
        multiplos.append(multiplo)
        i += 1
        multiplo = numero * 1

        return multiplos

 m = multiplos_hasta_limite(12, 100)
  print(m)       