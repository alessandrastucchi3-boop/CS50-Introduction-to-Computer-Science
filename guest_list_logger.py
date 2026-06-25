#Vamos a crear un script que simule el control de acceso para un evento. 
# El programa debe pedir nombres de invitados y escribirlos automáticamente en 
# un archivo de texto (.txt), guardando el historial para siempre.

invitado = input("Nombre del invitado: ")

with open("lista_invitados.txt", "a") as archivo:
    archivo.write(invitado + "\n")
    print(f"{invitado} ha sido registrado con éxito\n")
    
print("--- Lista Actual de Invitados ---")
    
with open("lista_invitados.txt", "r") as archivo:
    print(archivo.read())
