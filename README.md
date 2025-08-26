## ¿Qué son la depuración y las pruebas?

La **depuración** es el proceso de encontrar y corregir errores (bugs) en un programa. La **prueba** de un programa consiste en ejecutarlo para verificar que funciona correctamente y produce los resultados esperados. Ambas son tareas esenciales para cualquier programador.

## Tipos de errores en programación

Existen tres tipos principales de errores que puedes encontrar en tus programas de Python:

### 1. Errores de sintaxis (Syntax Errors)

Estos errores ocurren cuando no sigues las reglas del lenguaje Python. El intérprete no puede entender tu código y detiene la ejecución.

Ejemplo: Olvidar un paréntesis, una comilla o usar una palabra clave incorrectamente.

``` Python
# Ejemplo de SyntaxError
print("Hola, mundo!"
```

### 2. Errores en tiempo de ejecución (Runtime Errors)

Estos errores ocurren mientras el programa se está ejecutando, aunque la sintaxis sea correcta. Son a menudo causados por operaciones imposibles de realizar, como dividir entre cero.

Ejemplo: Intentar una operación matemática no válida o acceder a un índice de una lista que no existe.

``` Python
# Ejemplo de ZeroDivisionError
print(10 / 0)
```

### 3. Errores de lógica (Logic Errors)

Son los más difíciles de encontrar, ya que el programa se ejecuta sin problemas, pero produce un resultado incorrecto. La causa es un fallo en la lógica del código, es decir, el programa hace lo que le dices, no lo que quieres que haga.

Ejemplo: Calcular el área de un cuadrado, pero usas la fórmula del perímetro.

``` Python
# Ejemplo de Logic Error
# El programa calcula el perímetro en lugar del área
lado = 5
area = 4 * lado
print("El área del cuadrado es:", area)
```

***

## Estrategias básicas para depurar y probar 🕵️

### 1. El método del `print()`

Esta es la técnica más simple y común. Consiste en insertar sentencias `print()` en tu código para mostrar el valor de las variables en puntos clave de la ejecución. Esto te ayuda a rastrear el flujo del programa y a ver dónde el valor de una variable se desvía de lo que esperas.

Ejemplo 1: Depurando un error de lógica

En este ejemplo, queremos calcular el doble de la suma de dos números, pero obtenemos un resultado incorrecto porque la suma no está entre paréntesis, lo que hace que la multiplicación se realice primero.

``` Python
# Queremos sumar dos números y multiplicar el resultado por 2

# Versión con error
print("Versión CON error")
num1 = float(input("Dame el número 1: "))
num2 = float(input("Dame el número 2: "))
resultado = num1 + num2 * 2
print("El resultado sin depurar es:", resultado) # Esperamos 30, pero obtenemos 25

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
```

***

### 2. Comentarios y código temporal 📝

Si sospechas que una parte de tu código está causando un error, puedes comentarla (usando `#`) para ver si el programa funciona sin ella. También puedes agregar líneas de código temporales para aislar el problema.

Ejemplo 2: Aislando un error de tipo

En este caso, se intenta sumar una cadena de texto (str) con un número (int), lo que provoca un TypeError. Comentar la línea problemática nos ayuda a identificar el origen del fallo.

``` Python
# Versión con error
edad = float(input("Dame tu edad: "))
nombre = input("Dame tu nombre: ")
# print("Hola, " + nombre + " y tienes " + edad + " años.") # Descomenta para ver el TypeError
print("Este print no tiene errores")

# Versión corregida
edad_str = str(edad)
print("Hola, " + nombre + " y tienes " + edad_str + " años.")
```

***

### 3. Uso de `try...except` para manejar errores 🛡️

En Python, puedes usar los bloques `try` y `except` para "atrapar" errores que pueden ocurrir en tiempo de ejecución. Esto evita que tu programa se detenga abruptamente y te permite manejar el error de una manera controlada.

Ejemplo 3: Manejando un ZeroDivisionError

Aquí, el programa intenta dividir por cero. El bloque except captura este error y ejecuta un mensaje, en lugar de detener la ejecución.

``` Python
# Programa que puede causar un error de división por cero
numerador = float(input("Dame el numerador: "))
divisor = float(input("Dame el divisor: "))

try:
    resultado = numerador / divisor
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("¡Error! No se puede dividir entre cero.")
print("El programa continúa su ejecución.")
```

***

### 4. Afirmaciones (`assert`) para verificar la lógica 🧐

La sentencia `assert` te permite verificar si una condición es verdadera. Si la condición es falsa, el programa se detiene con un AssertionError. Esto es útil para comprobar supuestos y encontrar errores de lógica.

Ejemplo 4: Verificando la entrada del usuario

Imagina que quieres asegurarte de que una edad ingresada sea positiva.

``` Python
# El programa solicita una edad y usa assert para verificarla
edad = -5  # Simulación de una entrada incorrecta
# assert edad > 0, "La edad debe ser un número positivo."
print("La edad ingresada es:", edad)

# Simulación con entrada correcta
edad_correcta = 25
assert edad_correcta > 0, "La edad debe ser un número positivo."
print("La edad ingresada es:", edad_correcta)
```

***

### 5. Pruebas de caja negra y caja blanca 📦

Estas son dos filosofías de prueba de software.

* **Prueba de caja negra:** Pruebas el programa sin conocer su funcionamiento interno. Solo te enfocas en las entradas y las salidas, verificando que para una entrada específica, obtienes la salida esperada.

* **Prueba de caja blanca:** Pruebas el programa conociendo su código interno. Te aseguras de que cada línea de código, cada camino de ejecución, sea probado y funcione como se espera. Este tema lo veremos más adelante, ya que revisemos funciones definidas por el usuario.

#### Ejemplo de prueba de caja negra para `math.sqrt()` 📦

El propósito de esta prueba es confirmar que la función `math.sqrt()` devuelve la raíz cuadrada correcta para diferentes valores de entrada, sin considerar su funcionamiento interno.

**Descripción de la prueba:**

* **Función a probar:** `math.sqrt()`

* **Librería necesaria:** `math`

* **Entradas:** Se probarán valores de entrada positivos y un caso de borde (un valor que puede causar un error si no se maneja correctamente).

* **Salidas esperadas:** Un valor numérico que sea la raíz cuadrada del valor de entrada.

**Código de la prueba:**

``` Python
import math

# Prueba 1: con un número entero positivo
numero1 = 9
# Entrada: 9
# Salida esperada: 3.0
resultado1 = math.sqrt(numero1)
print("Prueba de caja negra para 'math.sqrt()':")
print(f"La raíz cuadrada de {numero1} es: {resultado1}")
# Usamos 'assert' para verificar el resultado
assert resultado1 == 3.0, "Error: La raíz cuadrada de 9 no es la esperada."
print("¡Prueba 1 superada!")

print("---")

# Prueba 2: con un número de punto flotante
numero2 = 16.0
# Entrada: 16.0
# Salida esperada: 4.0
resultado2 = math.sqrt(numero2)
print(f"La raíz cuadrada de {numero2} es: {resultado2}")
assert resultado2 == 4.0, "Error: La raíz cuadrada de 16.0 no es la esperada."
print("¡Prueba 2 superada!")

print("---")

# Prueba 3: con un valor de borde (cero)
numero3 = 0
# Entrada: 0
# Salida esperada: 0.0
resultado3 = math.sqrt(numero3)
print(f"La raíz cuadrada de {numero3} es: {resultado3}")
assert resultado3 == 0.0, "Error: La raíz cuadrada de 0 no es la esperada."
print("¡Prueba 3 superada!")
```

**Resultado de la prueba:**

Si el programa se ejecuta sin arrojar un `AssertionError`, significa que la función `math.sqrt()` se comporta de manera esperada para todas las entradas de prueba. Esta es la esencia de la **prueba de caja negra**: validar la funcionalidad de una parte del código sin necesidad de ver su implementación interna.


