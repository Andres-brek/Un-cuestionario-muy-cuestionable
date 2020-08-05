def run():
    #menu principal
    print("""Hola este es un examen hecho en python, primero elige un tema para el examen:
    1) Video juegos
    2) Historia 
    3) Ingles 
    4) Anime :3""")
    #opcion tomada por el usuario, recuerda que la varible esta tomada como un string por esto mismo la comparacion tiene comillas
    Opcion = input("Qué opción deseas: ")
    if Opcion == "1":
        Video_games()
    elif Opcion == "2":
        Historia()
    elif Opcion == "3":
        ingles()
    elif Opcion == "4":
        anime()
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