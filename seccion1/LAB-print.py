print("Hola, mundo") # Imprime "Hola, mundo" en la terminal
print("Sebastian")
# print(Sebastian)   Si se intenta poner un texto sin commillas, automaticamente Python arroja error en la terminal
# print "Sebastian"  Si se intenta poner texto sin parentesis, arroja error en la terminal

# -------------------

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

# -------------------



print("    *")
print("   * *")
print("  *   *")
print(" *     *")
print("***   ***")
print("  *   *")
print("  *   *")
print("  *****")

# La salida de la terminal es una flecha que apunta hacia arriba, hecha por asteriscos