### Ejercicio 1: `TypeError` al concatenar

Problema:

El siguiente código intenta calcular el área de un rectángulo y mostrar el resultado en una oración. Sin embargo, genera un error. Identifica el error y corrígelo.

``` Python
largo = 10
ancho = 5
area = largo * ancho
mensaje = "El área del rectángulo es: " + area
print(mensaje)
```

***

### Ejercicio 2: `SyntaxError` por falta de paréntesis

Problema:

El siguiente código tiene un error de sintaxis. ¿Puedes encontrarlo y arreglarlo?

``` Python
nombre = "Carlos"
print("Hola, " + nombre + " bienvenido al curso de Python!"
```

***

### Ejercicio 3: Error de lógica al calcular un promedio

Problema:

El siguiente programa intenta calcular el promedio de tres números. El código se ejecuta, pero el resultado es incorrecto. Usa el método del print() para depurar el código y corregir el error de lógica.

``` Python
nota1 = 70
nota2 = 85
nota3 = 90
promedio = nota1 + nota2 + nota3 / 3
print("El promedio es:", promedio)
```

***

### Ejercicio 4: Manejando un `ValueError` con `try...except`

Problema:

Escribe un programa que pida al usuario su año de nacimiento y calcule su edad. Usa try...except para manejar el caso en que el usuario no ingrese un número. Tip: usa `except ValueError` o bien `except Excepcion as e` para capturar el error

***

### Ejercicio 5: Usando `assert` para validar una condición

Problema:

Escribe un fragmento de código que calcule el precio final de un artículo con un descuento del 15%. Luego, usa la sentencia assert para verificar que el precio final sea menor que el precio original. Simula una situación en la que el cálculo del descuento sea erróneo.

Solución:

Debes usar assert para validar la condición de que el precio final es menor que el original. El AssertionError se activará si el cálculo del descuento es incorrecto, lo cual demuestra la utilidad de esta técnica para encontrar errores de lógica.
