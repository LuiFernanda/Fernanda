
def poblacion(num):
    return {
        "n1": 10,
        "n2": 9,
        "n3": 12,
        "n4": 1,
    }[num]

num = ["n1", "n2", "n3", "n4"]
print("el numero maximo es:", max(num, key=poblacion)) 
print("el numero minimo es:", min(num, key=poblacion))  