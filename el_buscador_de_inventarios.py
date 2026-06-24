#Imagina que estás desarrollando el sistema para una tienda o un juego donde 
# tienes una lista con los artículos disponibles en el inventario. 
# El usuario quiere saber si un artículo específico está en stock 
# y, si es así, en qué posición de la lista se encuentra.

art = ["laptop", "mouse", "teclado", "monitor", "auriculares"]
index = 0
searched_art = input("Cual articulo estas buscando`? ")

for i in range(len(art)):
    if searched_art == art[i]:
        index = i + 1
        print(f"Found in position {index}")
        break
    
else:
    print("Not found")    
    
