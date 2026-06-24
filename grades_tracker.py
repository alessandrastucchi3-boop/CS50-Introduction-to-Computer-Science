#Imagina que eres el profesor del curso y quieres un sistema rápido para 
# consultar las notas de tus estudiantes sin tener que buscar uno por uno en una lista.

calificaciones = {
    "Ron": 8.5,
    "Hermione": 10.0,
    "Harry": 7.5
}

estudiante = input("Dame el nombre de un estudiante: ")

if estudiante in calificaciones:
    print("La calificacion de {} es {}".format(estudiante, calificaciones[estudiante]))
else:
    calific = float(input("Dame su calificacion: "))
    calificaciones[estudiante] = calific