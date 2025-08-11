# Calcular el tiempo total de juego en horas y minutos: Escribe un algoritmo que solicite el tiempo total 
# jugado en minutos y lo convierta a horas y minutos.

tiempo_total = 150
horas = tiempo_total // 60
minutos = tiempo_total % 60

print("El tiempo total de juego es", tiempo_total)
print("El tiempo convertido es de",horas,"h",minutos,"m")