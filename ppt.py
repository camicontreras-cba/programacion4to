import random  # Trae una herramienta para elegir al azar (la usa la PC)

# Lista con las opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Diccionario: para cada opción, qué le gana
# "piedra" le gana a "tijera", "papel" le gana a "piedra", "tijera" le gana a "papel"
gana_a = {
    "piedra": "tijera",
    "papel": "piedra",
    "tijera": "papel",
}

# Contadores de puntos
puntos_usuario = 0
puntos_pc = 0

print("=== PIEDRA, PAPEL O TIJERA ===")
print("Escribí 'salir' para terminar.")

# Bucle infinito: el juego sigue hasta que el usuario escriba 'salir'
while True:
    # Pide la elección y la pasa a minúsculas y sin espacios de sobra
    eleccion_usuario = input("\nElegí piedra, papel o tijera: ").lower().strip()

    # Si escribió 'salir', corta el bucle
    if eleccion_usuario == "salir":
        break

    # Si escribió algo que no es una opción válida, vuelve a preguntar
    if eleccion_usuario not in opciones:
        print("Opción no válida, probá de nuevo.")
        continue  # 'continue' salta al inicio del bucle

    # La PC elige una opción al azar
    eleccion_pc = random.choice(opciones)
    print(f"La PC eligió: {eleccion_pc}")

    # Comparamos las dos elecciones
    if eleccion_usuario == eleccion_pc:
        print("¡Empate!")
    elif gana_a[eleccion_usuario] == eleccion_pc:
        print("¡Ganaste esta ronda!")
        puntos_usuario += 1  # Suma 1 punto al usuario
    else:
        print("Perdiste esta ronda.")
        puntos_pc += 1  # Suma 1 punto a la PC

    # Muestra el marcador
    print(f"Marcador -> Vos: {puntos_usuario} | PC: {puntos_pc}")

# Al salir del bucle, muestra el resultado final
print("\n=== FIN DEL JUEGO ===")
print(f"Resultado final -> Vos: {puntos_usuario} | PC: {puntos_pc}")
if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego!")
elif puntos_pc > puntos_usuario:
    print("La PC ganó el juego.")
else:
    print("Quedaron empatados.")

