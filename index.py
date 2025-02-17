from coche import Coche

def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Acelerar")
    print("2. Frenar")
    print("3. Mostrar información del coche")
    print("4. Salir\n")

def ejecutar_menu(coche: Coche):
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            try:
                velocidad = int(input("\n¿Cuánto deseas acelerar? "))
                coche.acelerar(velocidad)
            except ValueError:
                print("\nPor favor, ingresa un valor numérico válido.")
        elif opcion == "2":
            try:
                velocidad = int(input("\nCuánto deseas frenar? "))
                coche.frenar(velocidad)
            except ValueError:
                print("\nPor favor, ingresa un valor numérico válido.")
        elif opcion == "3":
            coche.mostrar_info()
        elif opcion == "4":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intenta nuevamente.")

def obtener_datos_coche():
    marca = input("\nIngresa la marca del coche: ")
    modelo = input("\nIngresa el modelo del coche: ")
    color = input("\nIngresa el color del coche: ")
    return Coche(marca, modelo, color)
1
# Ejemplo de uso
coche = obtener_datos_coche()
ejecutar_menu(coche)
