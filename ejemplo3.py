# Programa que puede causar un error de división por cero
numerador = float(input("Dame el numerador: "))
divisor = float(input("Dame el divisor: "))

try:
    resultado = numerador / divisor
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
print("El programa continúa su ejecución.") 