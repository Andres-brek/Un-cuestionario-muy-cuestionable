def Video_games(Nombre):
    print("Escogiste el examen de video juegos ")
    print("ok",Nombre,"vamos con la primera pregunta")
    Respuestas = 0

    #pregunta 1
    prgunta = print("""Vamos con algo facíl, cómo se llama el protagonista de la saga The legend of zelda?
    1)Zelda
    2)Link
    3)shinji
    4)Kratos""")
    Respuesta = input()
    pregunta = "2"
    if pregunta == Respuesta:
        print("Correcto")
        Respuestas += 1
    else:
        print("incorrecto")


    #pregunta 2
    prgunta = print("""El personaje de Luigi aparece en el juego super mario 64?
    1)Sí
    2)No""")
    Respuesta = input()
    pregunta = "2"
    if pregunta == Respuesta:
        print("Correcto")
        Respuestas += 1
    else:
        print("incorrecto")


    #pregunta 3
    prgunta = print("""En qué juego Kratos asesina a Zeus?
    1)God of war 1
    2)God of war 2
    3)God of war 3
    4)God of war ascension""")
    Respuesta = input()
    pregunta = "3"
    if pregunta == Respuesta:
        print("Correcto")
        Respuestas += 1
    else:
        print("incorrecto")
    

    #preguntas 4
    prgunta = print("""Cual fue el juego mas famoso en el genero Battle royal?
    1)Free fire
    2)Call of duty war zone
    3)Apex legends
    4)Fortnite""")
    Respuesta = input()
    pregunta = "4"
    if pregunta == Respuesta:
        print("Correcto")
        Respuestas += 1
    else:
        print("incorrecto")
    

     #preguntas 5
    prgunta = print("""En que año salio a la venta el atari 2600?
    1)1980
    2)1960
    3)1977
    4)1976""")
    Respuesta = input()
    pregunta = "3"
    if pregunta == Respuesta:
        print("Correcto")
        Respuestas += 1
    else:
        print("incorrecto")
    return Respuestas

    
    