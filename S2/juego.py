import random

secreto = 0

# Límite superior del número aleatorio
maximo = 50
intentos = 10

# Contadores de las partidas
jugadas = 0
ganadas = 0
perdidas = 0

# Se va a actualizar al juego con menos intentos
mejor_puntuacion = 11

# Lleva la cuenta de cuántas veces he jugado cada dificultad
facil = 0
medio = 0
dificil = 0

historial = ""

# Bucle principal
while True:
    print("""
1. Jugar una nueva partida
2. Ver estadisticas (partidas jugadas, ganadas, perdidas)
3. Ver instrucciones del juego
4. Salir del programa
""")
    
    opcion = input("Escriba la opción que quiera: ")

    match opcion:
        case "1":
            print(f"""
--- SELECCIONA DIFICULTAD
1. FACIL - Numero entre 1 y 50 (10 intentos )
2. MEDIO - Numero entre 1 y 100 (7 intentos )
3. DIFICIL - Numero entre 1 y 200 (5 intentos )
---
""")        

            # Esto ejecuta el código mientras el usuario
            # se equivoque. Si el usuario pone una opción
            # válida, entonces va a ternminar el bucle.
            dificultad = ""
            while True:
                opcion = input("Escriba la dificultad: ")
                match opcion:
                    case "1":
                        maximo = 50
                        intentos = 10
                        dificultad = "facil"
                        facil += 1
                        break
                    case "2":
                        maximo = 100
                        intentos = 7
                        dificultad = "medio"
                        medio += 1
                        break
                    case "3":
                        maximo = 200
                        intentos = 5
                        dificultad = "dificil"
                        dificil += 1
                        break
                    case _:
                        print(f"La opción es inválida")
            secreto = random.randint(1, maximo)

            repeticiones = 0
            jugadas += 1
            for i in range(intentos):
                print(f"INTENTOS RESTANTES: {intentos - repeticiones}")
                print(f"{historial=}")
                while True:
                    numero = input(f"Escriba un número entre 1 y {maximo}: ")

                    if numero.isdigit():
                        if not (1 <= int(numero) <= maximo):
                            print("Número inválido")
                            continue
                        break 
                    else:
                        print("No es un número!")

                numero = int(numero)

                diferencia = abs(secreto - numero)
                
                historial += f"{numero}, "

                repeticiones += 1
                
                # Cuando se gana la partida!
                if numero == secreto:
                    if repeticiones < mejor_puntuacion:
                        mejor_puntuacion = repeticiones
                    print(f"""
--- RESUMEN DE LA PARTIDA ---
Numero secreto : {secreto}
Intentos usados : {repeticiones} de {intentos}
Tus intentos : {historial}
Nivel : {dificultad}
Resultado : GANASTE
""")
                    
                    ganadas += 1
                    break 
                
                # Solo para facil
                if dificultad == "facil":
                    # “¡Hirviendo!” (diferencia ≤ 5), “Tibio” (6-10),
                    # “Frı́o” (11-20), “Congelado” (21+)
                    if diferencia <= 5:
                        print("Hirviendo!")
                    elif 6 <= diferencia <= 10:
                        print("Tibio!")
                    elif 11 <= diferencia <= 20:
                        print("Frío!")
                    elif diferencia >= 21:
                        print("Congelado!") 

                # Solo para facil y medio
                if dificultad == "facil" or dificultad == "medio":
                    if diferencia <= 10:
                        print("Estas cerca!")
                    else:
                        print("Estas lejos!")

                # Todos los niveles
                if numero > secreto:
                    print("El número es muy alto!")
                else:
                    print("El número es muy bajo!")
            else:
                print(f"""
--- RESUMEN DE LA PARTIDA ---
Numero secreto : {secreto}
Intentos usados : {repeticiones} de {intentos}
Tus intentos : {historial}
Nivel : {dificultad}
Resultado : PERDISTE
                """)
                perdidas += 1
            historial = ""

        case "2":
            print(f"""
--- ESTADISTICAS ---
Partidas jugadas : {jugadas}
Partidas ganadas : {ganadas} | {(ganadas / jugadas) * 100}%
Partidas perdidas : {perdidas} | {(perdidas / jugadas) * 100}%
Mejor puntuacion : {mejor_puntuacion}
Niveles por partidas:
Fácil: {facil} partidas jugadas
Medio: {medio} partidas jugadas
Difícil: {dificil} partidas jugadas
""")
        case "3":
            print("""
Este juego trata de adivinar el número generado
aleatoriamente utilizando la menor cantidad de intentos.
""")
        case "4":
            print("Adios!")
            break