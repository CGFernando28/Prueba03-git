def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: No debe divirse en cero"
    return a / b

def calculadora():
    print("Selecciona una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("-----------------------------------------")

    while True:
        eleccion = input("Ingresa el número de la operación (1/2/3/4): ")

        if eleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if eleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif eleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif eleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif eleccion == '4':
                print(f"{num1} / {num2} = {dividir(num1, num2)}")
            elif eleccion == '5':
                print("Saliendo...")
                break
        else:
            print("Operación no válida.")

        otra_vez = input("¿Quieres hacer otra operación? (si/no): ")
        if otra_vez.lower() != 'si':
            break

if __name__ == "__main__":
    calculadora()
    print("La señal de salida es esta")
    print("Adios Goku")

