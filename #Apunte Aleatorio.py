#Apunte Aleatorio
#Diego Espinosa
import random

valor = random.random()
print("(0 y 1) valor generado: ", valor)

valor = random.randrange(10)
print("(0 y 9) valor generado: ", valor)

valor = random.randrange(1,11)
print("(1 y 10) valor generado: ", valor)

#Uniform (a,b)
valor = random.uniform(5, 8)
print("(5 y 8) valores decimales generado: ", valor)

#Elegir de forma aleatoria de una lista

valor = random.choice([10, 20, 30, 40, 50])
print("Valor elegido de la lista: ", valor)

dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]
valor = random.choice(dias)
print("Dia elegido de la lista: ", valor)