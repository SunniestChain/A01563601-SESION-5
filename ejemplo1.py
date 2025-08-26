# Versión depurada con print()
print("")
print("Versión depurada con print")
num1 = float(input("Dame el número 1: "))
num2 = float(input("Dame el número 2: "))
print("El valor de num1 es:", num1)
print("El valor de num2 es:", num2)
resultado = num1 + num2 * 2
print("El resultado intermedio (num2 * 2) es:", num2 * 2)
print("El resultado final es:", resultado)

# Versión corregida
print("")
print("Versión CORREGIDA")
resultado_corregido = (num1 + num2) * 2
print("El resultado corregido es:", resultado_corregido)