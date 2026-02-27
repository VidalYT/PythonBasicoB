# Práctica 4 - Función Calculadora
# ======================================================
# Instrucciones Función Calculadora:
# Cree un función en python llamada calculadora, la cual debe tomar los parámetros (num_1, num_2, operacion) y debe ser capaz de realizar toda la lógica de un calculadora simple como: sumar, restar, multiplicar y dividir.
# Nota: Las entradas serán proporcionadas por el usuario.
# ======================================================

print("[ ============ Calculadora ============ ]")
num_1 = float(input("Escriba el valor del primer número: "))
num_2 = float(input("Escriba el valor del segundo número: "))
operacion = input("¿Cuál operacion deseas hacer? +, -, *, / -> ")

# Funciones de los operadores.
def sumar(num_1, num_2):
    return num_1 + num_2
    
def restar(num_1, num_2):
    return num_1 - num_2

def multiplicar(num_1, num_2):
    return num_1 * num_2

def dividir(num_1, num_2):
    return num_1 / num_2

# Llama a la función y lo muestra en pantalla.
if operacion == "+":
    resultado = sumar(num_1, num_2)
    print("El resultado de la suma es: ", resultado)

if operacion == "-":
    resultado = restar(num_1, num_2)
    print("El resultado de la resta es: ", resultado)

if operacion == "*":
    resultado = multiplicar(num_1, num_2)
    print("El resultado de la multiplicación es: ", resultado)

if operacion == "/":
    resultado = dividir(num_1, num_2)
    print("El resultado de la división es: ", resultado)
