# frase completa
print("Nunca pares de aprender")
# la coma separa los argtumentos con un espacio
print("Nunca", "pares", "de", "aprender")
# con la concatenación no se separan
print("Nunca" + "pares" + "de" + "aprender")
# concateno y agrego espacios
print("Nunca" + " " + "pares" + " " + "de" + " " + "aprender")
# uso de sep para agregar espacios
print("Nunca", "pares", "de", "aprender", sep=" ")
# uso de end
print("Nunca", end=" ")
print("pares de aprender")
# variables
frase = "Nunca pares de aprender"
author = "Platzi"
print("Frase:", frase, "Autor:", author)
# formato con f-strings
print(f"Frase: {frase}, Autor: {author}")
# formato con format()
print("Frase: {}, Autor: {}".format(frase, author))
# impresión de números con decimales
valor = 3.14159
print("Valor: {:.2f}".format(valor))
# saltos de linea
print("Hola\nmundo")
# con comillas
print("Hola soy 'Carli'")
# rutas de archivos
print("La ruta de archivo es: C:\\Users\\Usuario\\Desktop\\archivo.txt")
