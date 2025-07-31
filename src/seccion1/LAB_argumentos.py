print("La Witsi Witsi Araña subió a su telaraña.")
print() # Imprime una línea en blanco en la terminal
print("Vino la lluvia \ny se la llevó.") # \n es un salto de línea, se puede usar para separar líneas en un mismo print

print("La Witsi Witsi Araña" , "subió" , "a su telaraña.") # Se pueden separar los textos con comas, Python los separa automáticamente con un espacio

# -------------------

print("Mi nombre es", "Python.")
print("Monty Python.")

print("Mi nombre es", "Python.", end=" ") # end=" " evita el salto de línea al final del print
print("Monty Python.")

print("Mi", "nombre", "es", "Monty", "Python.", sep="-") # sep="-" separa los textos con un guion en lugar de un espacio

print("Mi", "nombre", "es", sep="_", end="*")
print("Monty", "Python.", sep="*", end="*\n")