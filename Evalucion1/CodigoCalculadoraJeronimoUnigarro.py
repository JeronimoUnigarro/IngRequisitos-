
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

while True:
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Elige una opción: ")
    
    if opcion == "5":
        break
    
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    
    if opcion == "1":
        print("Resultado:", suma(num1, num2))
    elif opcion == "2":
        print("Resultado:", resta(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicacion(num1, num2))
    elif opcion == "4":
        print("Resultado:", division(num1, num2))
    else:
        print("Opción no válida")

print("Hasta luego!")
