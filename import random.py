import random
#Diego Espinosa

# Genera 9 calificaciones aleatorias entre 5 y 10 (incluyendo el 10)
lista = [random.randint(5, 10) for _ in range(9)]

# Calcula el promedio
promedio = sum(lista) / len(lista)

print("Calificaciones:", lista)
print("Promedio:", promedio)