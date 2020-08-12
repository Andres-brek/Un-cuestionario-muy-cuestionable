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
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    

    #pregunta 2
    prgunta = print("""El personaje de Luigi aparece en el juego super mario 64?
    1)Sí
    2)No""")
    Respuesta = input()
    pregunta = "2"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #pregunta 3
    prgunta = print("""En qué juego Kratos asesina a Zeus?
    1)God of war 1
    2)God of war 2
    3)God of war 3
    4)God of war ascension""")
    Respuesta = input()
    pregunta = "3"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #preguntas 4
    prgunta = print("""Cual fue el juego mas famoso en el genero Battle royal?
    1)Free fire
    2)Call of duty war zone
    3)Apex legends
    4)Fortnite""")
    Respuesta = input()
    pregunta = "4"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

     #preguntas 5
    prgunta = print("""En que año salio a la venta el atari 2600?
    1)1980
    2)1960
    3)1977
    4)1976""")
    Respuesta = input()
    pregunta = "3"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    return Respuestas


def Historia(Nombre):
    print("Escogiste el examen de historia ")
    print("ok",Nombre,"vamos con la primera pregunta")
    Respuestas = 0


    #pregunta 1
    prgunta = print("""fecha de inicio de la primera guerra mundial
    1)1915
    2)1920
    3)1918
    4)1914""")
    Respuesta = input()
    pregunta = "4"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    

    #pregunta 2
    prgunta = print("""quien recorrio los alpes para llegar a roma?
    1)Anibal
    2)simon bolivar
    3)aleddin pasha""")
    Respuesta = input()
    pregunta = "1"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #pregunta 3
    prgunta = print("""quien fue espartaco?
    1)Fue un esclavo y protagonizo una rebelion 
    2)Fue un lider del imperio romano
    3)Fue comandante del ejercito romano
    4)Fue un filoso""")
    Respuesta = input()
    pregunta = "1"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #preguntas 4
    prgunta = print("""que pais fue el ultimo en rendirse, en la segunda guerra mundial?
    1)Japon
    2)Estados Unidos
    3)Alemania
    4)Rusia""")
    Respuesta = input()
    pregunta = "1"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    
    
    #preguntas 5
    prgunta = print("""Cuando fue creada la Organizacion de naciones unidas?
    1)En la primera guerra mundial
    2)En la segunda guerra mundial
    3)En la guerra fria""")
    Respuesta = input()
    pregunta = "2"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

def Anime(Nombre):
    print("Escogiste el examen de anime ")
    print("ok",Nombre,"vamos con la primera pregunta")
    Respuestas = 0


    #pregunta 1
    prgunta = print("""como se llama el protagonista de evangelion?
    1)mami
    2)sasuke
    3)shinji
    4)rei""")
    Respuesta = input()
    pregunta = "3"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    

    #pregunta 2
    prgunta = print("""quien es el cantante del primer opening de SAO
    1)Lisa
    2)Flow
    3)Sambomaster""")
    Respuesta = input()
    pregunta = "1"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #pregunta 3
    prgunta = print("""cuando se estreno el primer tomo de naruto?
    1)24 de agosto de 1998 
    2)21 de septiembre de 1999
    3)10 de noviembre de 1998
    4)9  de enero de 2000""")
    Respuesta = input()
    pregunta = "2"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
   

    #preguntas 4
    prgunta = print("""A que anime pertenece el opening "Daddy Daddy do!"?
    1)Bakemonogatari
    2)Darling in the franxx
    3)Kaguya sama: love is war
    4)Rent a girlfriend""")
    Respuesta = input()
    pregunta = "3"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    
    
    #preguntas 5
    prgunta = print("""A que anime pertenece el opening "Ren´ai circulation"?
    1)Bakemonogatari
    2)Darling in the franxx
    3)Kaguya sama: love is war
    4)Rent a girlfriend""")
    Respuesta = input()
    pregunta = "1"
    Respuestas = Probador_de_respuestas(Respuesta,pregunta,Respuestas)
    return Respuestas




# aqui se reciben las respuestas otorgadas por el usuario y de devuelve un "+1" si la respuesta es correcta, por el contrario se devuelve el mismo valor 
def Probador_de_respuestas(Respuesta,pregunta,Respuestas):
    calificacion = Respuestas
    if pregunta == Respuesta:
        print("Correcto")
        calificacion += 1
        return calificacion
    else:
        calificacion = calificacion
        print("incorrecto")
        return calificacion

    
    