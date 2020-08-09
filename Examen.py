import Preguntas
def run():
    Nombre = input("Antes de empezar el examen me gustaria saber tu nombre: ")
    #menu principal
    print("""Hola""",Nombre, """este es un examen hecho en python, primero elige un tema para el examen:
    1) Video juegos
    2) Historia 
    3) Ingles 
    4) Anime :3""")
    #opcion tomada por el usuario, recuerda que la varible esta tomada como un string por esto mismo la comparacion tiene comillas
    Opcion = input("Qué opción deseas: ")
    if Opcion == "1":
        Respuestas = Preguntas.Video_games(Nombre)
        if Respuestas >= 3:
            print("Pasaste putita")
        else:
            print("vales monda")
    elif Opcion == "2":
        Respuestas = Preguntas.Historia(Nombre)
        if Respuestas >= 3:
            print("Pasaste putita")
        else:
            print("vales monda")
    elif Opcion == "3":
        Preguntas.ingles()
    elif Opcion == "4":
        Preguntas.anime()
    else:
        print("""Escogiste una opcion incorrecta quieres intentarlo de nuevo
        1)si
        2)no""")
        repetir = input("Qué opción deseas: ")
        if repetir == "1":
            run()
        else:
            print("Ok, hasta luego")




if __name__ == "__main__":
    run()