import Preguntas
#aqui preguntamos el nombre del usuario para poder utilizarlo mas adelante
def Nombre():
    Nombre = input("Antes de empezar el examen me gustaria saber tu nombre: ")
    run(Nombre)


def run(Nombre):
    #menu principal
    print("""Hola""",Nombre, """este es un examen hecho en python, primero elige un tema para el examen:
    1) Video juegos
    2) Historia 
    3) Anime :3""")
    #opcion tomada por el usuario, recuerda que la varible esta tomada como un string por esto mismo la comparacion tiene comillas
    Opcion = input("Qué opción deseas: ")
    if Opcion == "1":
        Respuestas = Preguntas.Video_games(Nombre)
        if Respuestas >= 3:
            print("Pasaste putita")
        else:
            print("vales monda")
        Repeticion(Nombre)
    elif Opcion == "2":
        Respuestas = Preguntas.Historia(Nombre)
        if Respuestas >= 3:
            print("Pasaste putita")
        else:
            print("vales monda")
        Repeticion(Nombre)
    elif Opcion == "3":
        Respuestas = Preguntas.Anime(Nombre)
        if Respuestas >= 3:
            print("pasaste putita")
        else:
            print("no pasaste")
        Repeticion(Nombre)   
    else:
        print("""Escogiste una opcion incorrecta""")
        Repeticion(Nombre)


def Repeticion(Nombre):
    print("""Quieres intentarlo de nuevo?
    1)si
    2)no""")
    repetir = input("Qué opción deseas: ")
    if repetir == "1":
        run(Nombre)
    else:
        print("Ok, hasta luego")




if __name__ == "__main__":
    Nombre()
