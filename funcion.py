def sumar_numeros():
    try:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))
        suma = numero1 + numero2
        print(f"La suma de {numero1} y {numero2} es: {suma}")
    except ValueError:
        print("Por favor, ingresa solo números.")

# Llamamos a la función
sumar_numeros()
