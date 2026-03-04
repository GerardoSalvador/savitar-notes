# Python Ofensivo

## Secciones del curso

### Temas del curso (Videos)

#### Subtemas de cada uno de los videos

## Introduccion al curso de python ofensivo

Nos detalla la ruta correcta para llegar a ser pentester, llevando primero el curso de linux, luego el de personalizacion de linux, luego este de python y por ultimo el de introduccion a la ciberseguridad.

## Historia y filosofía de Python

* Python fue creado por Guido Van Rossum, programador Holandes en 1989.
* El propósito principal del desarrollo de python, era la productividad del programador y la legibilidad del código.
* La filosofia de python se resume en el Zen Of Python, la cual es una colección de 19 aforismos que sirven como guia para escribir programas en Python.
* Python es un lenguaje de programación de **alto nivel e interpretado**.

## Características y ventajas de Python

### Características

* **Sintaxis simple y fácil de aprender:** Python es famoso por su legibilidad, lo que facilita el aprendizaje para los principiantes y permite a los desarrolladores expresar conceptos complejos en menos líneas de código que serían necesarias en otros lenguajes.
* **Interpretado:** Python es procesado en tiempo de ejecución por el intérprete. Puedes ejecutar el programa tan pronto como termines de escribir los comandos, sin necesidad de compilar.
* **Tipado dinámico:** Python sigue las variables en tiempo de ejecución, lo que significa que puedes cambiar el tipo de datos de una variable en tus programas.
* **Multiplataforma:** Python se puede ejecutar en una variedad de sistemas operativos como Windows, Linux y MacOs.
* **Bibliotecas extensas:** Python cuenta con una gran biblioteca estándar que está disponible sin cargo alguno para todos los usuarios.
* **Soporte multiparadigma:** Python soporta varios estilos de programación, incluyendo programación orientada a objetos, imperativa y funcional.

### Ventajas de usar Python

* **Productividad mejorada:** La simplicidad de Python aumenta la productividad de los desarrolladores ya que les permite enfocarse en resolver el problema en lugar de la complejidad del lenguaje.
* **Amplia comunidad:** Una comunidad grande y activa significa que es fácil encontrar ayuda, colaboración y contribuciones de terceros.
* **Aplicabilidad en múltiples dominios:** Python se utiliza en una variedad de aplicaciones, desde desarrollo web hasta inteligencia artificial, ciencia de datos y automatización.
* **Compatibilidad y colaboración:** Python se integra fácilmente con otros lenguajes y herramientas, y es una excelente opción para equipos de desarrollo colaborativos.

## Diferencias entre Python2, Python3, PIP2 y PIP3

Python 2 y 3 son dos versiones del lenguaje de programacion Python, cada una con sus propias características y diferencias clave. PIP2 y PIP3 son las herramientas de gestión de paquetes correspondientes a cada versión, utilizadas para instalar y administrar bibliotecas y dependencias.

Python2 vs Python3:

* **Sintaxis de print:** En python 2, 'print' es una declaración, mientras que en Python3, 'print()' es una función, lo que requiere el uso de paréntesis.
* **División de enteros:** Python 2 realiza una división entera por defecto, mientras que Python 3 realiza una división real (flotante) por defecto.
* **Unicode:** Python 3 usa Unicode (texto) como tipo de datos por defecto para representar cadenas, mientras que Python 2 utiliza ASCII.
* **Librerías:** Muchas librerías populares de Python 2 han sido actualizadas o reescritas para Python 3, con mejoras y nuevas funcionalidades.
* **Soporte:** Python 2 llegó al final de su vida útil en 2020, lo que significa que ya no recibe actualizaciones, ni siquiera para correciones de seguridad.

PIP2 vs PIP3:

* **Gestión de paquetes:** PIP2 y PIP3 son herramientas que permiten instalar paquetes para Python 2 y Python 3, respectivamente. Es importante usar la versión correcta para garantizar la compatibilidad con la versión de Python que estés utilizando.
* **Comandos de instalación:** El uso de PIP o PIP3 antes de un comando determina si el paquete se instalará en Python2 o Python3. Algunos sistemas operativos pueden requerir especificar PIP 2 o PIP3 explícitamente para evitar ambigüedades.
* **Ambientes virtuales:** Es una buena práctica usar ambientes virtuales para mantener separadas las dependencias de proyectos específicos y evitar conflictos entre versiones de paquetes para Python2 y Python3.

## El interprete de Python

El intérprete de Python es el motor que ejecuta el código. Cuando nos referimos al intérprete de Python nos referimos al programa que lee y ejecuta el código en tiempo real.

Funciones clave del intérprete de Python:

* **Ejecución de código:** El intérprete ejecuta el código línea por línea, lo que facilita la depuración y permite a los desarrolladores probar fragmentos de códigos de forma interactiva.
* **Modo interactivo:** El intérprete puede usarse en un modo interactivo que permite a los usuarios ejecutar comando de Python uno a uno y ver los resultados de inmediate.
* **Modo script:** Además puede ejecutar programas completos o scripts que se escriben en archivos con la extensión *'.py'*
* **Compilación a Bytecode:** Internamente, el intérprete compila el código a bytecode antes de ejecutarlo, lo que mejora el rendimiento.
* **Máquina Virtual de Python:** El bytecode compilado se ejecuta en la Máquina Virtual de Python (Python Virtual Machine - PVM), que es una abstracción que hace que el código sea portable y se pueda ejecutar en cualquier S.O. donde el intérprete esté disponible.

Ventajas del intérprete:

* **Facilidad de uso:** La capacidad de ejecutar código inmediatamente y de manera interactiva hace de Python una herramienta excelente para principiantes y para el desarrollo rápido de aplicaciones.
* **Portabilidad:** Está disponible en múltiples plataformas.
* **Extensibilidad:** Permite la extensión con módulos escritos en otros lenguajes como C o C++, lo que puede ser utilizado para optimizar el rendimiento.

## Shebang y convenios de Python

* **Shebang:** Sirve para decir con que debe ser interpretado el script

Si deseamos correr el script como un ejecutable podemos dejar la shebang, agregar permisos de ejecución al script python y ejecutarlo como ejecutable como:

```Python
#!/usr/bin/python3
#!/usr/bin/env python3
print("Hola")
```

> #/home/gersal > **chmod +x test.py** \
> #/home/gersal > **./test.py** \
> hola

* **Uso de  main:** Python define todos sus scripts como modulos principales, el uso de main me permite validar al importarla a otro script que el módulo es el principal o secundario, segun cual este ejecutando.

Código de test.py

```Python
#!/usr/bin/python3
if __name__ == '__main__':
    print("Soy el módulo principal")
else:
    print("No soy el módulo principal")
```

> #/home/gersal > **./test.py** \
> Soy el módulo principal

Código de prueba.py

```Python
#!/usr/bin/python3
import test
```

> #/home/gersal > **./prueba.py** \
> No soy el módulo principal

### Convenios de Python

```Python
#!/usr/bin/python3
def comprobacionEstadoApi(): # Convenio loweCamelCase, usado para crear nombres de funciones, el primer caracter de la primera palabra que conforma el nombre de la funcion debe ir en minúscula, y el primer caracter de las palabras siguientes debe estar en mayúsculas.

class TwitterApi: # Convenio UpperCamelCase, usado para crear nombres de clases y excepciones, el primer caracter de todas las palabras que conforman el nombre de la clase inician con mayúscula

    VERSION_API = 1 # Convenio SCREAMING_SNAKE_CASE, usado para crear nombres de constantes en python
    URL_API = "https://gerardosalvador.com.mx"

# La guía de estilo para la programación en Python (PEP 8), nos dice que los nombres de funciones en Python deberían seguir el convenio snake_case
def comprobar_estado_api(): # Convenio snake_case usado para establecer el nombre de las funciones o variables en python
```

## Variables y tipos de datos

```Python
#!/usr/bin/python3

ip_address = "192.168.1.1" # variable de tipo cadena
port = 80 # variable de tipo entero
number = 4.5 # variable de tipo float
print(type(ip_address)))
print(type(port)))
print(type(number)))
```

> #/home/gersal > **./variables.py** \
> <class 'str' > \
> <class 'int' > \
> <class 'float' >

### Type casting

El type casting sirve para convertir de un tipo de dato a otro.

```Python
#!/usr/bin/python3

number = 4
print(number)
print(type(number))

number = float(4)
print(number)
print(type(number))

number = str(4)
print(number)
print(type(number))
```

> #/home/gersal > **./variables.py** \
> 4 \
> <class 'int' > \
> 4.0 \
> <class 'float' > \
> 4 \
> <class 'str' >

### Listas

```python
#!/usr/bin/env python3

my_ports = [22, 10, 34] # Estructura de creación de una lista
my_ports.append (80) # Con append solo podemos pasarle un argumento
my_ports.extend([84, 85]) # Extend si nos permite agregar mas de un argumento a una lista en python
my_ports += [86, 87]

for port in my_ports:
    print(f"Puerto: {port}")
print(f"\n[+] La lsita tiene un total de {len(my_ports)} elementos")

my_ports = sorted(my_ports) # Para ordenar una lista de menor a mayor
del my_ports[0] # El 0 indica la posicion que se desea eliminar de una lista

for port in my_ports:
    print(f"Puerto: {port}")
print(f"\n[+] La lsita tiene un total de {len(my_ports)} elementos")
```

> #/home/gersal > **./listas.py** \
> Puerto: 22 \
> Puerto: 10 \
> Puerto: 34 \
> Puerto: 80 \
> Puerto: 84 \
> Puerto: 85 \
> Puerto: 86 \
> Puerto: 87 \
> [+] La lista tiene un total de 10 elementos \
> #/home/gersal > **./listas.py** \
> Puerto: 10 \
> Puerto: 22 \
> Puerto: 34 \
> Puerto: 80 \
> Puerto: 84 \
> Puerto: 85 \
> Puerto: 86 \
> Puerto: 87 \
> [+] La lista tiene un total de 10 elementos

### Uso de listas

```python
#!/usr/bin/env python3
my_list[5, 6, 7, 8, 9, 10]
print(my_list[:2]) # Imprime los primeros 2 elementos de la lista my_list
print(my_list[:3]) # Imprime los primeros 3 elementos de la lista my_list
print(my_list[:4]) # Imprime los primeros 4 elementos de la lista my_list
print(my_list[4]) # Imprime el elemento de la posicion 4, pos 0, pos 1, pos 2, etc
print(my_list[0]) # Imprime el elemento de la posicion 0, pos 0, pos 1, pos 2, etc
print(my_list[0:3]) # Imprime un rango de una lista definiendo el rango con pos:pos, el último no lo contempla [5, 6, 7]
print(my_list[2:]) # Omite los 2 primeros elementos de la lista
print(my_list[3:]) # Omite los 3 primeros elementos de la lista
print(my_list[-1]) # Imprime en reversa, siendo -1 el último elemento de la lista
```

> [5, 6] \
> [5, 6, 7] \
> [5, 6, 7, 8] \
> 9 \
> 5 \
> [5, 6, 7] \
> [7, 8, 9, 10] \
> [8, 9, 10] \
> [10]

```python
#!/usr/bin/env python3
my_list = [1, 2, 3, 4]
my_list.insert(2, 9) # Insertamos en la posicion 2 el valor 9
print(my_list)
my_list.insert(2, 5)
print(my_list)
my_list.pop() # Elimina el ultimo elemento de una lista
my_list.index(4) # Para saber el indice del valor 4

print(max(my_list)) # Nos devuelve el valor mas alto
print(min(my_list)) # Nos devuelve el valor mas bajo
print(sum(my_list)) # suma los valores de la lista
print(len(my_list)) # nos dice el tamaño de la lista
print(sum(my_list) / len(my_list)) # nos da el promedio de los numeros dentro de la lista
print(round(sum(my_list) / len(my_list), 2)) # redondea a 2 decimales
```

> [1, 2, 9, 3, 4] \
> [1, 2, 5, 9, 3, 4] \
> [1, 2, 5, 9, 3] \
> 5 \
> 9 \
> 1 \
> 14

## Operadores básicos en Python

```python
#!/usr/bin/env python3
first_number = 12
second_number = 7
result = first_number ** second_number # Elevar a una potencia.
print("{:,}".format(result)) # Nos da el formato de separacion por comas en miles
print("{:,}".format(result).replace(",", ".")) # Las comas las cambia por puntos
```

> 35,831,808 \
> 35.831.808

## String Formatting

Python proporciona varias maneras de formatear cadenas, permitiendo insertar variables en ellas, así como controlar el espaciado, alineación y precisión de los datos mostrados

### Operador % (Porcentaje)

También conocido como 'interpolación de cadenas', este método clásico utiliza marcadores de posición como '%s' para enteros, o '%f' para números de puntos flotante.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print(name)
print("Hola mi nombre es " + name)
print("Hola, mi nombre es %s" % name)
print("Hola, mi nombre es %s y soy un %s" % (name, rol))
print("Hola, mi nombre es %s,  soy un %s y tengo %d años" % (name, rol, edad)) #la %d infiere a decimal
```

> gerardo \
> Hola mi nombre es gerardo \
> Hola, mi nombre es gerardo \
> Hola, mi nombre es gerardo y soy un pentester \
> Hola, mi nombre es gerardo, soy un pentester y tengo 26 años

### Método format()

Introducción en Python 2.6, permite una mayor flexibiliad y claridad. Utiliza llaves '{}' como marcadores de posición dentro de la cadena y puede incluir detalles sobre el formato de la salida.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print("Hola, soy {}!".format(name))
print("Hola, soy {}! y tengo {} años".format(name, edad))
print("Hola, soy {0}! y tengo {1} años. No es broma, mi nombre real es {0}".format(name, edad))# Jugando con los indices
```

> Hola, soy gerardo! \
> Hola, soy gerardo! y tengo 26 años \
> Hola, soy gerardo! y tengo 26 años. No es broma, mi nombre real es gerardo

### F-Strings (Literal String Interpolation)

Disponible desde Python 3.6, los F-Strings ofrecen una forma concisa y legible de incrustar expresiones dentro de literales de cadena usando la letra 'f' antes de las comillas de apertura y llaves para indicar dónde se insertarán las variables o expresiones.

```python
#!/usr/bin/env python3
name = "gerardo"
rol = "pentester"
edad = 26

print(f"Hola, soy {name}!")
print(f"Hola, soy {name}! y tengo {edad}")
print(f"Hola, soy {name}! y tengo {edad}. No es broma, mi nombre real es {name}")
```

> Hola, soy gerardo! \
> Hola, soy gerardo! y tengo 26 años \
> Hola, soy gerardo! y tengo 26 años. No es broma, mi nombre real es gerardo

## Control de flujos (Condicionales y Bucles)

### Condicionales

Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código dependiendo de si una o más condiciones son verdaderas o falsas. En Python, las declaraciones condicionales más comunes son 'if', 'elif' y 'else'

* if: Evalúa si una condición es verdadera y, de ser así, ejecuta un bloque de código.

```python
#!/usr/bin/env python3
edad = 20
mensaje  = "Eres mayor de edad" if edad >= 18 else "Eres menor de edad" # Operadores ternarios
```

* * and: Condición lógica que me ayuda a determinar que se cumpla una accion y otra
* * or: Condición lógica que me ayuda a determinar que se cumpla una accion u otra

* elif: Abreviatura de "else if", se utiliza para verificar múltiples expresiones sólo si las anteriores no son verdaderas.
* else: Captura cuaquier caso que no haya sido capturado por las declaraciones 'if' y 'elif' anteriores.

### Bucles

Los bucles permiten ejecutar un bloque de código repetidamente mientras una condición sea verdadera o para cada elemento en una secuencia. Los dos tipos principales de bucles que utilizamos en Python son 'for' y 'while'.

* **for:** Se usa para iterar sobre una secuencia (como una lista, un diccionario, una tupla o un conjunto) y ejecutar un bloque de código para cada elemento de la secuencia.

```python
#!/usr/bin/env python3
for i in range(5):
    print(i)

names = ["Gerardo", "Marcelo", "Lobotec", "Hackermate", "TheGoodHacker"]
for name in names:
    print(name)
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> Gerardo \
> Marcelo \
> Lobotec \
> Hackermate \
> TheGoodHacker

Tanto bucles for como while pueden usar la sentencia else:

```python
#!/usr/bin/env python3
for i in range(6):
    if i == 10:
        break
else:
    print("Bucle concluido exitosamente")
print("Continuamos con la ejecución del bucle")
```

> Bucle concluido exitosamente \
> Continuamos con la ejecución del bucle

* **while:** Ejecuta un bloque de código repetidamente mientras una condición específica se mantiene verdadera.

```python
#!/usr/bin/env python3
i = 0

while i < 5:
    print(i)
    i += 1
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \

* **enumerate:** Siempre devuelve el indice y el elemento

```python
#!/usr/bin/env python3
nombres = ["Gerardo", "Marcelo", "TheGoodHacker", "Lobotec"]
for i, nombre in enumerate(nombres):
    print(f"Nombre [{i+1}]: {nombre}")


odd_list = [1, 3, 5, 7, 9]
cuadrado = [i ** 2 for i in odd_list]
print(cuadrado)
```

> Nombre [1]: Gerardo \
> Nombre [2]: Marcelo \
> Nombre [3]: TheGoodHacker \
> Nombre [4]: Lobotec \
> [1, 9, 24, 49, 81]

### Control de flujo en bucles

Existen declaraciones de control de flujo que pueden modificar el comportamiento de los bucles, como 'break', 'continue' y 'pass'.

* break: Termina el bucle y pasa el control a la siguiente declaración fuera del bucle.

```python
for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(10):
    print(i)
    if i == 5:
        break
```

> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 5

* continue: Omite el resto del código dentro del bucle y continúa con la siguiente iteración.

```python
#!/usr/bin/env python3
for i in range(10):
    if i == 5:
        continue
    print(i)
```

En la salida vemos como se omite el valor 5
> 0 \
> 1 \
> 2 \
> 3 \
> 4 \
> 6 \
> 7 \
> 8 \
> 9

* pass: No hace nada, se utiliza como una declaración de relleno donde el código eventualmente irá, pero no ha sido escrito todavía.

## Funciones  y ámbitos de las variables

### Funciones

Las funciones son bloques de código reutilizables diseñados para realizar una tarea específica. Se definen usando la palabra reservada 'def' seguido de un nombre descriptivo, paréntesis que pueden contener parámetros y dos puntos. Los parámetros son 'variables de entrada' que pueden cambiar cada vez que se llama a la función. Esto permite a las funciones operar con diferentes datos y producir resultados correspondientes.

Las funciones pueden devolver valores al programa principal o a otras funciones mediante la palabra clave "return". Esto las hace increíblemente versátiles, ya que pueden procesar datos y luego pasar esos datos modificados a otras partes del programa.

```python
#!/usr/bin/env python3
def saludo():
    print("\nHola mundo")

saludo()
```

> Hola mundo

Pasando un argumento a la función para imprimir el nombre pasado quedaría:

```python
#!/usr/bin/env python3
def saludo(nombre):
    print(f"\nHola {nombre}")

saludo("Gerardo")
```

> Hola Gerardo

Realizando una suma con una función pasando dos argumentos para ser sumados:

```python
#!/usr/bin/env python3
def suma(numero_uno, numero_dos):
    print("[+] La suma es igual a: ",numero_uno + numero_dos)

suma(2,3)
```

> [+] La suma es igual a: 5

```python
#!/usr/bin/env python3
def suma(number_one, number_two):
    return x + y
resultado = suma(2, 8) #Es conveniente guardar el resultado de una función en una variable

print(f"\n[+] El resultado es {suma(1,5)}")
```

> [+] El resultado es 6

### Ámbito de las variables (Scope)

El ámbito de las variables se refiere a la región de un porgrama donde esa variable es accesible, hay dos tipos de principales ámbitos:

* Local: Las variables definidas dentro de una función tienen un ámbito local, lo que significa que solo pueden ser accesadas y modificadas dentro de la función donde fueron creadas.

```python
#!/usr/bin/env python3
def mi_funcion():
    variable_local = "Soy local"
    print(variable_local)

mi_funcion()
print(variable_local) # Nos da error porque es una variable local de la funcion por lo cual no esta accesible desde fuera de la funcion
```

> Soy local \
> Error, Error, Error

* Global: Las variables definidas fuera de todas las funciones tiene un ámbito global, lo que significa que pueden ser accesadas desde cualquier parte del programa. Sin embargo, para modificar una variable global dentro de una función, se debe declarar como global.

```python
#!/usr/bin/env python3
variable = "Soy global"

def mi_funcion():
    variable = "Soy local"
    print(variable)

mi_funcion()
print(variable)
```

> Soy local \
> Soy global

```python
#!/usr/bin/env python3
variable = "Soy global"
def my_function():
    global variable
    variable = "Soy global y he sido modificado"
    print(variable)

my_function()
print(variable)
```

> Soy global y he sido modificado \
> Soy global y he sido modificado

## Funciones lambda anónimas

Esta clase se centra en una característica poderosa y expresiva de Python que permite la creación de funciones en una sola línea: las funciones Lambda.

### Funciones Lambda

Las funciones lambda son también conocidas como funciones anónimas debido a que no se les asigna un nombre explícito al definirlas. Se utilizan para crear pequeñas funciones en el lugar donde se necesitan, generalmente para una operación específica y breve. En python, una función lambda se define con la palabra clave 'lambda', seguida de una lista de argumentos, dos puntos y la expresión que desea evaluar y devolver.

Una de las ventajas de las funciones lambda es su simplicidad sintáctica, lo que las hace ideal para su uso en operaciones que requieren una función por un breve momento y para casos donde la definición de una función tradicional completa sería excesivamente verbosa.

```python
#!/usr/bin/env python3
my_function = lambda: "Hola mundo"
print(my_function)
```

> Hola mundo

Pasando un argumento a funcion anónima

```python
#!/usr/bin/env python3
cuadrado = lambda x: x**2 #recibe el parametro "x"
print(cuadrado(6))
```

> 36

pasando dos argumentos a función anónima

```python
#!/usr/bin/env python3
suma = lambda x, y: x + y
print(suma(2,10))
```

> 12

### Usos comunes de las funciones lambda

* Con funciones de órden superior: Como aquellas que requieren otra función como argumento, por ejemplo, 'map()', 'filter()' y 'sorted()'.

* * map()

```python
#!/usr/bin/env python3
#map recibe una funcion y un iterable
numeros = [1,2,3,4,5]
cuadrados = map(lambda x: x**2, numeros) #funcion e iterable

for numero in cuadrados:
    print(numero)
```

> 1 \
> 4 \
> 9 \
> 16 \
> 25

Simplificando la operacion anterior:

```python
#!/usr/bin/env python3
numeros = [1,2,3,4,5]
cuadrados = list(map(lambda x: x**2, numeros))

print(cuadrados)
```

> [1, 4, 9, 16, 25]

* * filter()

Ocupamos este caso para filtrar por numeros pares

```python
#!/usr/bin/env python3
#filter en base a la condicion si devuelve un true o un false te devuelve un numero
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
pares = list(filter(lambda x: x % 2 == 0, numeros))#lo metemos dentro de una lista para poder printearlo 

print(pares)
```

> [ 2, 4, 6, 8, 10, 12]

Para este caso filtramos por numeros impares

```python
#!/usr/bin/env python3
numeros = [1,2,3,4,5,6,7,8,9,10,11,12]
impares = list(filter(lambda x: x % 2 != 0, numeros))
print(impares)
```

> [1, 3, 5, 7, 9, 11]

* Operaciones simples: Para realizar cálculos o acciones rápidas donde una función completa sería inncesariamente larga.
* Funcionalidad en línea: Cuando se necesita una funcionalidad simple sin la necesidad de reutilizarla en otro lugar del código.

## Manejo de errores y excepciones

Los errores pueden ocurrir por muchas razones: errores de código, datos de entraa incorrectos, problemas de conectividad, entre otros. En lugar de permitir que un programa falle con un error, Python nos proporciona herramientas para 'atrapar' estos errores y manejarlos de manera controlada, evitando así que el programa se detenga inesperadamente y permitiendo reaccionar de manera adecuada.

### Excepciones

Una excepción en Python es un evento que ocurre durante la ejecución de un programa que interrumple el flujo normal de las instrucciones del programa. Cuando el intérprete se encuentra con una situación que no puede manejar, 'levanta' o 'arroja' una excepción.

### Bloques try y except

Para manejar las excepciones, utilizamos los bloques 'try' y 'except'. Un bloque 'try' contiene el código que puede producir una excepción, mientras que un bloque 'except'captura la excepción y contiene el código que se ejecuta cuando se produce una.

Division da error por división entre cero

```python
#!/usr/bin/env python3
try:
    num = 5/0
except ZeroDivisionError: # Se define el tipo de error para ser específico
    print("No se puede dividir un número entre cero")
```

> No se puede dividir un número entre cero

Division con otro tipo de dato para este ejemplo una cadena contra un entero

```python
#!/usr/bin/env python3
try:
    num = "Hola" / 4
except ZeroDivisionError: # Se define el tipo de error para ser específico
    print("No se puede dividir un número entre cero")
except TypeError: # Se define otro tipo de error
    print("No se puede dividir entre diferentes tipos de datos")
except:
    ("Esta excepcion la estoy agregando para añadir el except sin un tipo de error")
```

> No se puede dividir entre diferentes tipos de datos

### Otras palabras clave de manejo de excepciones

* else: Se puede usar después de los bloques 'except' para ejecutar código si el bloque 'try' no generó una excepción.
* finally: Se utiliza para ejecutar código que debe correr independientemente de si se produjo una excepción o no, como cerrar un archivo o una conexión de red.

```python
#!/usr/bin/env python3
try:
    num = "hola" / 1
except ZeroDivisionError:
    print("No se puede dividir un número entre cero")
except TypeError:
    print("Las operatorias matemáticas sólo deben realizarse con números")
else:
    print(f"La división de ambos números da como resultado {num}")
finally:
    print("Esto siempre se va a ejecutar")
```

> Las operatorias matemáticas sólo deben realizarse con números \
> Esto siempre se va a ejecutar

### Levantar excepciones

También es posible 'levantar' excepciones intecionalmente con la palabra clave 'raise', lo que permite forzar que se produzca una excepción bajo condiciones específicas.

```python
#!/usr/bin/env python3
x = -5
if x<0:
    raise Exception("No se pueden utilizar números negativos")
```

> Traceback (most recent call last): \
> raise Exception("No se pueden utilizar números negativos") \
> Exception: No se pueden utilizar números negativos

## Listas en Python

La listas son estructuras de datos que nos permiten almacenar secuencias ordenadas de elementos. Son mutables, lo que significa que podemos modificarlas después de su creación, y son dinámicas, permitiéndonos añadir o quitar elementos de ellas.

### Características de las Listas

* Almacenar datos herogéneos, es decir, pueden contener elementos de diferentes tipos (enteros, cadenas, flotantes y más) dentro de una misma lista.
* Ser indexadas y cortadas, lo que permite acceder a elementos específicos de la lista directamente a través de su índice.
* Ser anidadas, es decir, una lista puede contener otras lsitas como elementos, lo que permite crear estructuras de datos complejas como matrices.

### Operaciones con listas

* Añadir elementos con métodos como 'append()' y 'extend()'.
* Eliminar elementos con métodos como 'remove()' y 'pop()'.
* Ordenar las listas con el método 'sort()' o la función incorporada 'sorted'.
* Invertir los elementos de una lista con el método 'reverse()' o la sintaxis de corte '[::-1]'.
* Comprender las compresiones de listas, una forma "pythonica" de crear y manipular listas de manera concisa y eficiente.

```python
#!/usr/bin/env python3
tcp_ports = [21,22,25,80,443,8880,445,69]
print(tcp_ports)
print(len(tcp_ports)) # Imprime el tamaño de la lista

tcp_ports.append(1337) # Añade un nuevo valor a la lista
print(tcp_ports)

tcp_ports.remove(22) # Remueve el valor 22 de la lista
print(tcp_ports)

tcp_ports.sort() # Ordena los valores de menor a mayor
print(tcp_ports)

tcp_ports.reverse() # Ordena los valores de manera inversa
print(tcp_ports)

other_ports = tcp_ports[2:4] # Nos muestra un rango de valores dentro de la lista por indice
print(other_ports)

attacks = ["Phising", "DDoS", "SQL Injection", "Man In The Middle", "Cross-Site Scripting"]
for i, attack in enumerate(attacks):
    print(f"\nAtaque #{i}: {attack}\n")

attacks = ["Phising", "DDoS", "SQL Injection", "Man In The Middle", "Cross-Site Scripting"]

attacks_uppercase = [attack.upper() for attack in attacks] # Convertimos los nombres a Mayúsculas
print(attacks_uppercase)

names = ["Gerardo", "Marcelo", "HackerMate", "Lobotec", "Hackavis", "Savitar"]
edades = [26, 27, 45, 13, 20, 27]

for name, edad in zip(names,edades): # Zip nos sirve para recorrer dos listas del mismo tamaño a la par
    print(f"{name} tiene {edad} años")

print(names)
deleted_user = names.pop(3) # Eliminamos un nombre de la lista por su indice a la vez que lo agregamos a una variable
print(f"El usuario eliminado ha sido {deleted_user}")
print(names)

names.insert(2, "Ivon") # Inserta un elemento en la posicion 2 y recorre la lista
print(names)
```

> [21, 22, 25, 80, 443, 8880, 445, 69] \
> 8 \
> [21, 22, 25, 80, 443, 8880, 445, 69, 1337] \
> [21, 25, 80, 443, 8880, 445, 69, 1337] \
> [21, 25, 69, 80, 443, 445, 1337, 8880] \
> [8880, 1337, 445, 443, 80, 69, 25, 21] \
> [445, 443] \
> Ataque #0: Phising \
> Ataque #1: DDoS \
> Ataque #2: SQL Injection \
> Ataque #3: Man In The Middle \
> Ataque #4: Cross-Site Scripting \
> ['PHISING', 'DDOS', 'SQL INJECTION', 'MAN IN THE MIDDLE', 'CROSS-SITE SCRIPTING'] \
> Gerardo tiene 26 años \
> Marcelo tiene 27 años \
> Hackermate tiene 45 años \
> Lobotec tiene 13 años \
> Hackavis tiene 20 años \
> ['Gerardo', 'Marcelo', 'HackerMate', 'Lobotec', 'Hackavis', 'Savitar'] \
> El usuario eliminado ha sido Lobotec \
> ['Gerardo', 'Marcelo', 'HackerMate', 'Hackavis', 'Savitar'] \
> ['Gerardo', 'Marcelo', 'Ivon', 'HackerMate', 'Hackavis', 'Savitar']

## Tuplas en Python

Las tuplas son colecciones ordenadas de elementos que no pueden modificarse una vez creadas (inmutables). Esta característica las hace ideales para asegurar que ciertos datos permanezcan constantes a lo largo del ciclo de vida de un programa.

```python
#!/usr/bin/env python3
numeros = (1,2,3,4,5) # Las tuplas se definen con paréntesis
my_first_tuple = (2,4,6,8)
my_second_tuple = (1,3,5,7)

my_third_tuple = my_first_tuple + my_second_tuple
print(my_third_tuple)

my_third_tuple = my_first_tuple * 3
print(my_third_tuple)

numeros_pares = tuple(i for i in numeros if i % 2 == 0)
print(numeros_pares)
```

> (1, 2, 3, 4, 5, 6, 7, 8) \
> (2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8) \
> (2, 4) \

### Características de las tuplas

* Inmutabilidad: Una vez que se crea la tupla, no puedes cambiar, añadir o eliminar elementos. Esta inmutabilidad garantiza la integridad de los datos que desea mantener constantes.
* Indexación y Slicing: Al igual que las listas, puedes acceder a los elementos de la tupla mediante índices y también puedes realizar operaciones de slicing para obtener subsecuencias de la tupla.
* Heterogeneidad: Las tuplas pueden contener elementos de diferentes tipos, incluyendo otras tuplas, lo que las hace muy versátiles.

### Operaciones con tuplas

Aunque no puedes modificar una tupla, hay varias funciones que puedes realizar:

* Empaquetado y desempaquetado de tuplas: Las tuplas permiten asignar y desasignar sus elementos a múltiples variables de forma simultánea.
* Concatenación y repetición: Similar a las listas, puedes combinar tuplas usando el operardo '+' y repetir los elementos de una tupla un número determinado de veces con el operador '*'.
* Métodos de búsqueda: Puedes usar métodos como 'index()' para encontrar la posición de un elemento y 'count()' para contar cuántas veces aparece un elemento en la tupla

### Uso de tupla en python

* Funciones y asignaciones múltiples: Las tuplas son muy útiles cuando una función necesita devolver múltiples valores o cuando se realizan asignaciones múltiples en una sola línea.
* Estructuras de datos fijas: Se usan para crear estructuras de datos que no deben cambiar, como los días de la semana o las coordenadas de un punto en el espacio.

## Conjuntos en Python

Los conjuntos son una colección de elementos sin órden y sin elementos repetidos, inspirados en la teoría de conjutnos de las matemáticas. Son ideales para la gestión de coleeciones de elementos únicos y operaciones que requieren eliminar duplicados o realizar comparaciones de conjuntos.

### Características de los conjuntos

* Unicidad: Los conjuntos automáticamente descartan elementos duplicados, lo que los hace perfectos para recolectar elementos únicos.
* Desordenados: A diferencia de las listas y las tuplas, los conjuntos no mantiene los elementos en ningún órden específico.
* Mutabilidad: Los elementos de un conjunto pueden ser agregados o eliminados, pero los elementos mismos deben ser inmutables (por ejemplo, no puedes tener un conjunto de listas, ya que las listas se pueden modificar).

### Operaciones con conjuntos

Exploraremos las operaciones básicas de conjutnos que Python facilita, como:

* Adición y eliminación: Añadir elemento con 'add()' y eliminar elementos con 'remove()' o 'discard()'.
* Operaciones de conjuntos: Realizar uniones, intersecciones, diferencias y diferencias simétricas utilizando métodos o operadores respectivos.
* Pruebas de pertenencia: Comprobar rápidamente si un elemento es miembro de un conjunto.
* Inmutabilidad opcional: Usar el tipo 'frozenset' para crear conjutnos que no se pueden modificar despues de su creación.

### Uso de conjuntos en Python

* Eliminacion de duplicados: Son útiles cuando necesitas asegurarte de que una colección no tenga elementos repetidos.
* Relaciones entre colecciones: Facilitan la comprensión y el manejo de relaciones matemáticas entre colecciones, como subconjuntos y superconjuntos.
* Rendimiento de búsqueda: Proporcionan una búsqueda de elementos más rápida que las listas o las tuplas, lo que es útil para grandes volúmenes de datos.

```python
#!/usr/bin/env python3

mi_conjunto = {1,2,3}

mi_conjunto.add(98)
print(mi_conjunto)

mi_conjunto.update({23,32,11})
print(mi_conjunto)

mi_conjunto.remove(3)
print(mi_conjunto)

#mi_conjunto.remove(1222) # Al no encontrar el elemento nos dará error, usar discard()cuando no estemos seguros que ese elemento esta dentro del set.
mi_conjunto.discard(1222) # Usamos discard para evitar errores al no encontrarlo
print(mi_conjunto)

# INTERSECCIONES
first_set = {1,2,3,4,5}
second_set = {1,2,3,4,5,6,7,8}

intersection_set = first_set.intersection(second_set)
print(f"Nos muestra los elementos en comun del primer set {first_set} y el segundo set {second_set}: {intersection_set}")

# UNIONES
union_set = first_set.union(second_set)
print(f"Nos muestra ambos set unidos sin repeticiones, primer set {first_set} y el segundo set {second_set}: {union_set}")

# SUBCONJUNTOS
print(first_set.issubset(second_set))

# BUSQUEDA
mi_set = set(range(1000))
print(34 in mi_set)
```

> {1, 2, 3, 98} \
> {32, 1, 2, 3, 98, 23, 11} \
> {32, 1, 2, 98, 23, 11} \
> {32, 1, 2, 98, 23, 11} \
> Nos muestra los elementos en comun del primer set {1, 2, 3, 4, 5} y el segundo set {1, 2, 3, 4, 5, 6, 7, 8}: {1, 2, 3, 4, 5} \
> Nos muestra ambos set unidos sin repeticiones, primer set {1, 2, 3, 4, 5} y el segundo set {1, 2, 3, 4, 5, 6, 7, 8}: {1, 2, 3, 4, 5, 6, 7, 8} \
> True \
> True

## Diccionarios en Python

Los diccionarios en Python son colecciones desordenadas de pares clave-valor. A diferencia de las secuencias, que se indexan mediante un rango numérico, los diccionarios se indexan con claves únicas, que pueden ser cualquier tipo inmutable, como cadenas o números.

### Característias de los diccionarios

* Desordenados: Los elementos en un diccionario no están ordenados y no se accede a ellos mediante un índice numérico, sino a través de claves únicas.
* Dinámicos: Se pueden agregar, modificar y eliminar pares clave-valor.
* Claves únicas: Cada clave en un diccionario es única, lo que previene de duplicaciones y sobreescrituras accidentales.
* Valores accesibles: Los valores no necesitan ser únicos y pueden ser de cualquier tipo de dato.

### Operaciones con diccionarios

* Agregar y modificar: Cómo agregar nuevos pares clave-valor y modificar valores existentes.
* Eliminar: Cómo eliminar pares clave-valor usando del o el metodo 'pop()'
* Métodos de diccionarios: Utilizar métodos como 'keys()', 'values()' y 'items()' para acceder a las claves, valores o ambos en forma de pares.
* Comprensión de diccionarios: Una forma elegante y concisa de construir diccionarios basados en secuencias o rangos.

### Uso de diccionarios en Python

* Almacenamiento de datos estructurados: Idelaes para almacenar y organizar datos que están relacionados de manera lógica, como una base de datos de memoria.
* Búsqueda eficiente: Los diccionarios son altamente optimizados para recuperar valores cuando se conoce la clave, proporcionando tiempos de búsqueda muy rápidos.
* Flexibilidad: Pueden ser anidad, lo que significa que los valores dentro de un diccionario pueden ser otros diccionarios, listas o cualquer otro tipo de dato.

```python
#!/usr/bin/env python3
mi_diccionario = {"nombre":"Gerardo", "edad":26, "estado":"Tabasco"} # Establecemos claves:valor para nuestro diccionario
print(mi_diccionario["nombre"]) # Vemos el valor para la clave nombre

mi_diccionario["nombre"] = "Salvador" # Actualizamos el valor para la clave nombre
print(mi_diccionario["nombre"])

mi_diccionario["Profesion"] = "Consultor cybersec" # Agregamos una nueva clave:valor al dict
print(mi_diccionario)

del mi_diccionario["estado"]
print(mi_diccionario)

for key, value in mi_diccionario.items():
    print(f"\nPara la clave\033[1;31m {key}\033[0;m tenemos el valor \033[1;31m {value}\033[0;m")

cuadrados = {x: x**2 for x in range(6)}
print(cuadrados)

print(cuadrados.keys())
print(cuadrados.values())

mi_diccionario2 = {"carrera":"sistemas", "mascotas":"perro"}
mi_diccionario.update(mi_diccionario2)
print(mi_diccionario)

my_dict = {
    "nombre": "Gerardo",
    "hobbies": {"Primero":"Música", "Segundo":"Futbol"},
    "edad": 26
}

print(my_dict["hobbies"]["Segundo"])

for key, value in my_dict.items():
    print(f"[{key}]: [{value}]")
```

> Gerardo \
> Salvador \
> {'nombre': 'Salvador', 'edad': 26, 'estado': 'Tabasco', 'Profesion': 'Consultor cybersec'} \
> {'nombre': 'Salvador', 'edad': 26, 'Profesion': 'Consultor cybersec'} \
> Para la clave nombre tenemos el valor  Salvador \
> Para la clave edad tenemos el valor  26 \
> Para la clave Profesion tenemos el valor  Consultor cybersec \
> {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25} \
> dict_keys([0, 1, 2, 3, 4, 5]) \
> dict_values([0, 1, 4, 9, 16, 25]) \
> {'nombre': 'Salvador', 'edad': 26, 'Profesion': 'Consultor cybersec', 'carrera': 'sistemas', 'mascotas': 'perro'} \
> Futbol \
> [nombre]: [Gerardo] \
> [hobbies]: [{'Primero': 'Música', 'Segundo': 'Futbol'}] \
> [edad]: [26]

## Proyecto de videojuegos

Este proyecto integrador nos servirá para consolidar nuestras habilidades de programación, ya que abordaremos la administración de ventas, la gestión de stock y la actualización de datos en un sistema de control central.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

tope = 700

juegos = ["Super Mario Bros", "Zelda", "CyberPunk", "Final Fantasy"]

# Géneros
generos = {
    "Super Mario Bros": "Aventura",
    "Zelda": "Aventura",
    "CyberPunk": "Rol",
    "Final Fantasy": "Rol"
}
# Ventas y Stock
ventas_y_stock = {
    "Super Mario Bros":(400, 200),
    "Zelda":(600, 20),
    "CyberPunk":(60, 120),
    "Final Fantasy":(924, 3),

}

# Clientes
clientes = {
    "Super Mario Bros": {"Marcelo", "Hackermate", "Hackavis", "Securiters", "Lobotec"},
    "Zelda": {"Marcelo", "Hackermate", "Hackavis"},
    "CyberPunk": {"Ivon", "Gerardo", "Mauricio"},
    "Final Fantasy": {"Indira", "Rogelio", "Gonzalo"}
}

mi_juego = "Zelda"

# Sumario
def sumario(juego):
    print(f"[i] Resumen del juego {juego}\n")
    print(f"\t[+] Género del juego: {generos[juego]}")
    print(f"\t[+] Total de ventas para este juego: {ventas_y_stock[juego][0]} unidades")
    print(f"\t[+] Total de stock para este juego: {ventas_y_stock[juego][1]} unidades")
    print(f"\t[+] Clientes que han adquirido el juego: {', '.join(clientes[juego])}\n")

for juego in juegos:
    if ventas_y_stock[juego][0] > tope:
        sumario(juego)

ventas_totales = lambda: sum(ventas for juego, (ventas, _) in ventas_y_stock.items() if ventas_y_stock[juego][0] > tope)
print(f"El total de ventas es {ventas_totales()}")
```

## PROGRAMACIÓN ORIENTA A OBJETOS EN PYTHON (POO) - 8

## Clases y objetos (1/2)

La programación orienta a objetos, es un paradigma de programación que utiliza objetos y clases en su enfoque central.
Es una manera de estructurar y organizar el código que refleja cómo los desarrolladores piensan sobre el mundo real y las entidades dentro de él.

### Clases

Las clases son los fundamentos de la POO. **Actúan como plantillas para la creación de objetos y definen atributos y comportamientos que los objetos creados a partir ella tendrán**.
En Python, una clase se define con la palabra clave 'class' y proporcionan la estructura inicial para todo objeto que se derive de ella

### Instancias de clases

**Un objeto es una instancia de una clase**. Cada vez que se crea un objeto, se está creando una isntancia que tiene su propio espacio de memoria y conjunto de valores para los atributos definidos por su clase.
Los objetos encapsulan datos y funciones juntos en una entidad discreta.

### Métodos de clase (1/2)

Los métodos de clase **son funciones que se definen dentro de una clase y solo pueden ser llamados por las instancias de esa clase**. Estos métodos son el mecanismo principal para interactuar con los objetos, permitiéndoles realizar operaciones o acciones, modificar su estado o incluso interactuar con otros objetos.

---
Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Persona:
    def __init__(self, nombre, edad, profesion): # Definimos el constructor con los parámetros que vamos a recibir
        self.nombre = nombre
        self.edad = edad
        self.profesion = profesion

    def saludo(self): # Persona.saludo(marcelo)
        return f"Hola soy {self.nombre} y tengo {self.edad} años"

# Objeto = Clase(Atributos de inicio pasados al constructor)
gerardo = Persona("Salvador", 26, "Consultor") # Estamos creando una instancia de la clase Persona, nombrando al objeto gerardo
juan = Persona("Gerardo", 21, "Pentester")

print(gerardo.saludo())
print(juan.saludo())
```

> Hola soy Salvador y tengo 26 años \
> Hola soy Gerardo y tengo 21 años

---
Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Animal:
    
    def __init__(self, nombre, animal): # Animal.__init__(gato, nombre, animal)
        self.nombre = nombre # Definimos los atributos
        self.animal = animal

    def descripcion(self): # # Animal.descripcion(objeto)
        return f"{self.nombre} es un {self.animal}"
    
gato = Animal("QWERTY", "Gato")
perro = Animal("Canela", "Perro")
print(gato.descripcion())
print(perro.descripcion())
```

> QWERTY es un Gato \
> Canela es un Perro

---
Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class CuentaBancaria:

    # Inicializando el atributo dinero en caso que si al instanciar la clase no pasan el valor, dinero sea 0 por defecto
    def __init__(self, cuenta, nombre, dinero = 0):
        self.cuenta = cuenta
        self.nombre = nombre
        self.dinero = dinero

    def depositar_dinero(self, deposito): # CuentaBancaria.depositar_dinero(Gerardo)
        self.dinero += deposito # self.dinero = dinero del objeto, self.deposito = self.dinero + deposito
        print(f"\n[+] Operación exitosa: Se han depositado {deposito}\n\tSALDO: ${self.dinero}\n")
    
    def retirar_dinero(self, retiro): #CuentaBancaria.retirar_dinero(Gerardo, retiro)
        
        if retiro > self.dinero:
            print(f"[!] Operación denegada: Fondos insuficientes\n")
        
        if retiro <= self.dinero:
            self.dinero -= retiro # self.dinero = self.dinero - retiro
            print(f"[+] Operación exitosa: Se han retirado ${retiro}\n\tSALDO ${self.dinero}\n")

# Se inicializa el objeto con valores, instancia del objeto
gerardo = CuentaBancaria("123454", "Gerardo Salvador", 1000)

# Se juega con los métodos de la clase CuentaBancaria
gerardo.depositar_dinero(500)
gerardo.retirar_dinero(10000)
gerardo.retirar_dinero(200)

```

> [+] Operación exitosa: Se han depositado 500 \
> &nbsp; SALDO: $1500 \
> [!] Operación denegada: Fondos insuficientes \
> [+] Operación exitosa: Se han retirado $200 \
> &nbsp; SALDO $1300

## Clases y objetos (2/2)

Dentro del paradigma de la Programación Orientada a Objetos en Python, existen conceptos avanzados como los decoradores, métodos de clase y  métodos estáticos que enriquecen y expanden las posibilidades de cómo interactuamos con las clases y sus instancias.

### Decoradores

Los decoradores son una herramienta poderosa en Python que permite modificar el comportamiento de una función o método.
Funcionan como 'envoltorios', que agregan funcionalidad antes y después del método o función decorada, sin cambiar su código fuente.
En POO, los decoradores son frecuentemente utilizados para agregar funcionalidades de manera dinámica a los métodos, como la sincronización de hilos, la memorización de resultados o la verificación de permisos.

### Métodos de clase (2/2)

Un método de clase es un método que está ligado a la clase y no a una instancia de la clase.
Esto significa que el método puede ser llamado sobre la clase misma, en lugar de sobre un objeto de la clase.
Se definen utilizando el decorador *'@classmethod'* y su primer argumento es siempre una referencia a la clase, convencionalmente llamada 'cls'.
Los métodos de clase son utilizados a menudo para definir métodos "factory" que pueden crear instancias de la clase de diferentes maneras.

### Métodos estáticos 1/2

Los métodos estáticos, definidos con el decorador *'@staticmethod'*, no reciben una referencia implícita ni a la instancia (self) ni a la clase (cls). Son básicamente como funciones regulares, pero pertenecen al espacio de nombre de la clase.
Son útiles cuando queremos realizar alguna funcionalidad que está relacionada con la clase, pero que no requiere acceder a la instancia o a los atributos de la clase.

Estos elementos de la POO en Python nos permiten crear abstracciones más claras y mantener el código organizado, modular y flexible, facilitando el mantenimiento y la extensibilidad del software.

---

Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Rectangulo:
    
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    # Con este decorador estoy convirtiendo el resultado de este método a una propiedad, de tal manera si quisiera verla directamente como una propiedad de las que se definen en el constructor sin emplear parentesis
    @property
    def area(self): # Rectangulo.area(rect1)
        return self.ancho * self.alto
    
    # Método especial que al estar definido nos muestra información del objeto al que estamos pasandole un print(objeto), sin definir este método especial, al hacer print nos reportaria que es un objeto
    def __str__(self):
        return f"[+] Propiedades del Rectangulo:\n\tAncho:\t{self.ancho}\n\tAlto:\t{self.alto}\n\tArea:\t{self.area}\n"
    
    # Método especial que nos devuelve un valor booleano para comparar ambos objetos
    def __eq__(self, otro):
        return self.alto == otro.alto and self.ancho == otro.ancho

rect1 = Rectangulo(20,89)
rect2 = Rectangulo(40,35)

print(f"[+] El área es {rect1.area}\n")
print(f"[+] El área es {rect2.area}\n")

# Al pedir la impresion para saber que son estos valores, nos buscará por el método especial __str__ y si esta definido nos mostrará lo que hayamos especificado, de otra manera, nos dirá que es un objeto
print(rect1) 
print(rect2)

# Al establecer esta igualdad al hacer print, nos buscará el método especial __eq__ para hacer la comparacion y nos devolverá un boolean
print(rect1==rect2)
```

> [+] Propiedades del Rectangulo: \
> &nbsp; Ancho:  20 \
> &nbsp; Alto:   89 \
> &nbsp; Area:   1780 \
> [+] Propiedades del Rectangulo: \
> &nbsp; Ancho:  40 \
> &nbsp; Alto:   35 \
> &nbsp; Area:   1400 \
> False

---

Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:

    # Variable de clase
    best_seller_value = 5000

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        return
    
    # El método estático no necesita que le pasen el objeto, puesto que no accedemos a ninguna de las propiedades del objeto para llevar a cabo nuestra operatoria.
    # Decorador, como argumento no necesitan que le pasen el objeto, o acceder a sus propiedades, no necesitamos acceder a ninguna de las propiedades del objeto para llevar a cabo nuestra operacion
    @staticmethod
    def es_best_seller(venta):
        print(venta > Libro.best_seller_value) # Para referenciar a las variables de clase, hay que llamar a la clase

mi_libro = Libro("Como ser un Lammer?", "Gerardo", 12)

# Como es un método estático de la clase, en vez de referenciar al objeto mi_libro.es_best_seller(7000) se referencia a la clase Libro.es_best_seller
Libro.es_best_seller(7000)
```

> True

---

Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:

    # Variable de clase
    best_seller_value = 5000
    IVA = 0.21

    def __init__(self, titulo, autor, precio):
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        return
    
    # El método estático no necesita que le pasen el objeto, puesto que no accedemos a ninguna de las propiedades del objeto para llevar a cabo nuestra operatoria.
    # Decorador, como argumento no necesitan que le pasen el objeto, o acceder a sus propiedades, no necesitamos acceder a ninguna de las propiedades del objeto para llevar a cabo nuestra operacion
    @staticmethod
    def es_best_seller(venta):
        print(venta > Libro.best_seller_value) # Para referenciar a las variables de clase, hay que llamar a la clase


    # El decorador recibe como argumento la clase y para este ejemplo la clase nos determina que iva aplicar, puesto que la clase la trae el objeto al ser instanciado
    @classmethod
    def precio_con_iva(cls, precio):
        print(precio + precio * cls.IVA)


class LibroDigital(Libro):
    IVA = 0.10

mi_libro = Libro("Como ser un Lammer?", "Gerardo", 17.5)
mi_libro_digital = LibroDigital("Ser o no ser", "Salvador", 17.5)

# Como es un método estático de la clase, en vez de referenciar al objeto mi_libro.es_best_seller(7000) se referencia a la clase Libro.es_best_seller
Libro.es_best_seller(7000)

# precio_con_iva(clase, precio_con_iva(objeto.precio))
Libro.precio_con_iva(mi_libro.precio)
LibroDigital.precio_con_iva(mi_libro_digital.precio)
```

> True \
> 21.175 \
> 19.25

## Métodos estáticos y métodos de clase

Los métodos estáticos y los métodos de clase son dos herramientas poderosas en la programación orientada a objetos en Python, que ofrecen flexibilidad en cómo se puede acceder y utilizar la funcionalidad asociada con una clase.

### Métodos de clase

Se definen con el decorador '@classmethod', lo que les permite tomar la clase como primer argumento, generalmente nombrada 'cls'. Este acceso a la clase permite que los métodos de clase interactúen con la estructura de la clase en sí, como modificar atributos de clase que afectarán a todas las instancias. Se utilizan para tareas que requieren conocimiento del estado global de la clase, como la construcción de instancias de maneras específicas, también conocidos como métodos factory.

### Métodos estáticos 2/2

Se definen con el decorador '@staticmethod' y no reciben un argumento implícito de referencia a la clase o instancia. Son similares a las funciones regulares definidas dentro del cuerpo de una clase.
Se utilizan para funciones que, aunque conceptualmente pertenecen a la clase debido a la relevancia temática, no necesitan acceder a ningún dato específico de la clase o instancia.
Proporcionan una manera de encapsular la funcionalidad dentro de una clase, manteniendo la cohesión y la organización del código.

Ambos métodos contribuyen a un diseño de software más limpio y modular, permitiendo una clara separación entre la funcionalidad que opera con respecto a la clase en su totalidad y la funcionalidad que es independiente de las instancias de clase y de la clase misma.
La elección entre utilizar un método de clase o un método estático a menudo depende del requisito específico de acceso o no a la clase o a sus instancias.

---

Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# MÉTODOS ESTÁTICOS
class Calculadora:

    @staticmethod
    def suma(num1, num2): # no se usa self porque no jugamos con objetos
        return num1 + num2
    
    @staticmethod
    def resta(num1, num2): # no se usa self porque no jugamos con objetos
        return num1 - num2
    
    @staticmethod
    def division(num1, num2):
        return num1 / num2 if num2 != 0 else "\n[!] Error no se puede dividir un numero entre 0"

print(Calculadora.suma(2,5))
print(Calculadora.resta(8,4))
print(Calculadora.division(8,0))

# MÉTODOS DE CLASE
class Automovil:
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @classmethod
    def deportivos(cls, marca):
        return cls(marca, "Deportivo")
    
    @classmethod
    def sean(cls, marca):
        return cls(marca, "Sean")

    def __str__(self):
        return f"La marca {self.marca} es un modelo {self.modelo}"

deportivo = print(Automovil.deportivos("Ferrari"))
sean = print(Automovil.sean("Toyota"))
```

> 7 \
> 4 \
> [!] Error no se puede dividir un numero entre 0 \
> La marca Ferrari es un modelo Deportivo \
> La marca Toyota es un modelo Sean

---

Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Estudiantes:

    estudiantes = []

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

        Estudiantes.estudiantes.append(self)

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18

    @classmethod
    def crear_estudiantes(cls, nombre, edad):
        if cls.es_mayor_de_edad(edad):
            return cls(nombre, edad)
        else:
            print(f"[!] Error: El estudiante {nombre} es menor de edad")

    @staticmethod
    def mostrar_estudiantes():
        for i, x in enumerate(Estudiantes.estudiantes):
            print(f"[+] Estudiante número [{i + 1}]: {x.nombre}")

Estudiantes.crear_estudiantes("HackerMate", 43)
Estudiantes.crear_estudiantes("Savitar", 28)
Estudiantes.crear_estudiantes("Xerosec", 12)
Estudiantes.crear_estudiantes("Hackavis", 8)

Estudiantes.mostrar_estudiantes()

```

> [!] Error: El estudiante Xerosec es menor de edad \
> [!] Error: El estudiante Hackavis es menor de edad \
> [+] Estudiante número [1]: HackerMate \
> [+] Estudiante número [2]: Savitar

---

Codigo: **Ejemplo 3 Externo**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Perro:
    especie = "Canino"  # Atributo de clase

    def __init__(self, nombre):
        self.nombre = nombre  # Atributo de instancia

    @classmethod
    def cambiar_especie(cls, nueva_especie):
        cls.especie = nueva_especie  # Modifica el atributo de clase

    def ladrar(self):
        print(f"{self.nombre} dice: ¡Guau!")

# Modificación del atributo de clase
Perro.cambiar_especie("Lobo")

# Instancias
perro1 = Perro("Rex")
perro2 = Perro("Firulais")

print(perro1.especie)  # Imprime "Lobo"
print(perro2.especie)  # Imprime "Lobo"
perro1.ladrar()        # Imprime "Rex dice: ¡Guau!"
```

> Lobo \
> Lobo \
> Rex dice: ¡Guau!

Se lee de manera más detallada en esta página web [Métodos de clase](https://oregoom.com/python/metodos-clase/)

## Comprendiendo mejor el uso de self

El uso de self es uno de los aspectos más fundamentales y a la vez confusos para quienes se adentran en la Programación Orientada a Objetos (POO) en Python. Este identificador es crucial para entender cómo Python maneja los métodos y atributos dentro de sus clases y objetos.

### Definición de 'self'

A nivel conceptual, 'self' es una referencia al objeto actual dentro de la clase. Es el primer parámetro que se pasa a cualquier método de una clase en Python. A través de self, un método puede acceder y manipular los atributos del objeto y llamar a otros métodos dentro del mismo objeto.

### Uso de 'self'

Cuando se crea una nueva instancia de una clase, Python pasa automáticamente la instancia recién creada como el primer argumento al método '\_\_init__' y a otros métodos definidos en las clases que tienen self como su primer parámetro. Esto es lo que permite que un método opere con datos específicos del objeto y no con datos de la clase en general o de otras instancias de la clase.

### Importancia de 'self'

El concepto de self es importante en la POO ya que asegura que los métodos y atributos se apliquen al objeto correcto. Sin self, no podríamos diferenciar entre las operaciones y datos de diferentes instancias de una clase.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Persona:

    def __init__(self, nombre, edad): # Persona.__init__(gerardo, nombre, edad)
        self.nombre = nombre # gerardo.nombre = nombre
        self.edad = edad # gerardo.edad = edad

    def presentacion(self): # Persona.presentacion(gerardo)
        return f"Hola soy {self.nombre} y tengo {self.edad} años" # gerardo.nombre gerardo.edad

gerardo = Persona("Gerardo", 26)
print(gerardo.presentacion())



class Calculador:

    def __init__(self, numero): # Calculador.__init__(calc, numero)
        self.numero = numero # calc.numero = 5

    def suma(self, otro_numero): # Calculador.suma(calc, otro_numero)
        return self.numero + otro_numero # calc.numero + 8 -> 5 + 8
    
    def doble_suma(self, num1, num2): # Calculador.doble_suma(calc, 2, 9)
        return self.suma(num1) + self.suma(num2) # calc.suma(2) + calc.suma(9) -> Calculador.suma(calc,2) + Calculador.suma(calc, 9)

calc = Calculador(5)
print(calc.suma(8))

print(calc.doble_suma(2,9))

```

> Hola soy Gerardo y tengo 26 años \
> 13 \
> 21

## Herencia y polimorfismo

La herencia y el polimorfismo son conceptos fundamentales en la programación orientada a objetos que permiten la creación de una estructura de clases flexible y reutilizable.

### Herencia

Es un principio de la POO que permite a una clase heredar atributos y métodos de otra clase, conocida como su clase base o superclase.
La herencia facilita la reutilización de código y la creación de una jerarquía de clases. Las subclases heredan las características de la superclase, lo que permite que se especialicen o modifiquen comportamientos existentes.

### Polimorfismo

Este concepto se refiere a la habilidad de objetos de diferentes clases de ser tratados como instancias de una clase común.
El polimorfismo permite que una función o método interactúe con objetos de diferentes clases y los trate como si fueran del mismo tipo, siempre y cuando compartan la misma interfaz o método.
Esto significa que el mismo método puede comportarse de manera diferente en distintas clases, un concepto conocido como sobrecarga de métodos.

Ambos, la herencia y el polimorfismo, son piedras angulares de la POO y son ampliamente utilizados para diseñar sistemas que son fácilmente extensibles y mantenibles.

---

Codigo: **Ejemplo 1** HERENCIA

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Animal:
    def __init__(self, nombre):
        self.nombre=nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")
    
class Perro(Animal):
    def hablar(self):
        return f"{self.nombre} dice Guauuu"

class Gato(Animal):
    def hablar(self):
        return f"{self.nombre} dice Miau"
    
bety=Gato("Bety")
canela=Perro("Canela")
loro=Animal("Lorenzo")

print(bety.hablar())
print(canela.hablar())
print(loro.hablar())

```

> Bety dice Miau \
> Canela dice Guauuu \
> Muestra error en consola con la especificacion

---

Codigo: **Ejemplo 2** POLIMORFISMO

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Animal:
    def __init__(self, nombre):
        self.nombre=nombre

    def hablar(self):
        raise NotImplementedError("Las subclases definidas deben implementar este método")
    
class Perro(Animal):
    def hablar(self):
        return f"Guauuu"

class Gato(Animal):
    def hablar(self):
        return f"Miau"
    
def hacer_hablar(objeto):
    print(f"{objeto.nombre} dice {objeto.hablar()}")
    
bety=Gato("Bety")
canela=Perro("Canela")
loro=Animal("Lorenzo")

hacer_hablar(bety)
hacer_hablar(canela)

```

> Bety dice Miau \
> Canela dice Guauuu

---

Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Automovil:
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo

    def describir(self):
        return f"Vehiculos: {self.marca} {self.modelo}"

class Coche(Automovil):
    def describir(self):
        return f"Coche: {self.marca} {self.modelo}"

class Moto(Automovil):
    def describir(self):
        return f"Moto: {self.marca} {self.modelo}"

# Polimorfismo    
def describir_vehiculo(vehiculo):
    print(vehiculo.describir())

coche = Coche("Toyoto", "Corolo")
moto = Moto("Honda", "CBR")

describir_vehiculo(coche)
describir_vehiculo(moto)

```

> Coche: Toyota Corola \
> Honda CBR

---

Codigo: **Ejemplo 4**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Dispositivo:
    def __init__(self, modelo):
        self.modelo=modelo

    def escanear_vulnerabilidades(self):
        raise NotImplementedError("Este metodo debe ser definido para el resto de subclases existentes")
    
class Ordenador(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Actualizacion de software necesaria, multiples desactualizaciones de software detectadas"
    
class Router(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] Análisis de vulnerabilidades concluido: Multiples puertos críticos detectados"
    
class TelefonoMovil(Dispositivo):
    def escanear_vulnerabilidades(self):
        return f"[+] Multiples aplicaciones detectadas con permisos excesivos"
    
def realizar_escaneo(dispositivo):
    print(dispositivo.escanear_vulnerabilidades())
    
pc = Ordenador("Dell")
cisco = Router("Cisco")
xiami = TelefonoMovil("Xiaomi")

realizar_escaneo(pc)
realizar_escaneo(cisco)
realizar_escaneo(xiami)

```

> [+] Análisis de vulnerabilidades concluido: Actualizacion de software necesaria, multiples desactualizaciones de software detectadas \
> [+] Análisis de vulnerabilidades concluido: Multiples puertos críticos detectados \
> [+] Multiples aplicaciones detectadas con permisos excesivos

---

Codigo: **Ejemplo 5**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# Para cuando das prioridad a un metodo sobre otro, o al padre en este caso
class A:
    def __init__(self):
        print("Inicializando A")

class B(A):
    def __init__(self):
        print("Inicializando B")
        super().__init__()

b = B()
```

> Inicializando A \
> Inicializando b

---

Codigo: **Ejemplo 6**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 
class A:
    def __init__(self, x):
        self.x = x
        print(f"Valor en x: {self.x}")

class B(A):
    def __init__(self, x, y):
        self.y = y
        super().__init__(x)
        print(f"Valor en y: {self.y}")

b = B(2,10)
```

> Valor en x: 2 \
> Valor en y: 10

---

Codigo: **Ejemplo 7**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 
class A:
    def saludo(self):
        return "Saludo desde A"

class B(A):
    def saludo(self):
        original = super().saludo()
        print(f"{original}, pero tambien saludo desde b")

saludo = B()
saludo.saludo()
```

> Saludo desde A, pero tambien saludo desde b

## Encapsulación y métodos especiales

El encapsulamiento en la programación orientada a objetos maneja principalmente tres niveles de visibilidad para los atributos y métodos de una clase: *públicos*, *protegidos* y *privados*. En python esta distinción se realiza mediante convenciones en la nomenclatura, más que a través de estrictas restricciones de acceso como en otros lenguajes.

### Atributos Públicos

Son accesibles desde cualquier parte del programa y, por convención, no tienen un prefijo especial. Se espera que estos atributos sean parte de la interfaz permanente de la clase.

### Atributos Protegidos

Se indica con un único guion bajo al principio del nombre (por ejemplo, ‘_atributo‘). Esto es solo una convención y no impide el acceso desde fuera de la clase, pero se entiende que estos atributos están protegidos y no deberían ser accesibles directamente, excepto dentro de la propia clase y en subclases.

### Atributos Privados

En Python, los atributos privados se indican con un doble guion bajo al principio del nombre (por ejemplo, ‘__atributo‘).
Esto activa un mecanismo de cambio de nombre conocido como ‘name mangling‘, donde el intérprete de Python altera internamente el nombre del atributo para hacer más difícil su acceso desde fuera de la clase.

### Métodos especiales

Los métodos especiales en Python son también conocidos como métodos mágicos y son identificados por doble guion bajo al inicio y al final (‘\_\_metodo__‘).
Permiten a las clases en Python emular el comportamiento de los tipos incorporados y responder a operadores específicos.
Por ejemplo, el método ‘\_\_init__‘ se utiliza para inicializar una nueva instancia de una clase, ‘\_\_str__‘ se invoca para una representación en forma de cadena legible del objeto y ‘\_\_len__‘ devuelve la longitud del objeto.

Algunos métodos especiales importantes en POO son:

* **\_\_init__(self, [...]):** Inicializa una nueva instancia de la clase.
* **\_\_str__(self):** Devuelve una representación en cadena de texto del objeto, invocado por la función ‘str(object)‘ y ‘print‘.
* **\_\_repr__(self):** Devuelve una representación del objeto que debería, en teoría, ser una expresión válida de Python, invocado por la función ‘repr(object)‘.
* **\_\_eq__(self, other):** Define el comportamiento del operador de igualdad ‘==‘.
* **\_\_lt__(self, other), \_\_le__(self, other), \_\_gt__(self, other), \_\_ge__(self, other):** Definen el comportamiento de los operadores de comparación (<, <=, > y >= respectivamente).
* **\_\_add__(self, other), \_\_sub__(self, other), \_\_mul__(self, other), etc.:** Definen el comportamiento de los operadores aritméticos (+, –, *, etc.).

El encapsulamiento y los métodos especiales son herramientas poderosas que, cuando se utilizan correctamente, pueden mejorar la seguridad, la flexibilidad y la claridad en la construcción de aplicaciones.

---

Codigo: **Ejemplo 1**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Ejemplo:
    
    def __init__(self):
        
        # Atributo protegido
        self._atributo_protegido = "Soy un atributo protegido y no deberías poder verme"

        # Atributo privado
        self.__atributo_privado = "Soy un atributo privado y no deberías poder verme" # name mangling 

ejemplo = Ejemplo()
print(ejemplo._atributo_protegido)
#print(ejemplo.__atributo_privado) # De esta manera no podemos ver el atributo privado
print(ejemplo._Ejemplo__atributo_privado) # De esta manera si podemos ver el resultado

```

> Soy un atributo protegido y no deberías poder verme \
> Soy un atributo privado y no deberías poder verme

---

Codigo: **Ejemplo 2**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal
class Coche:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.__kilometraje = 0 # Atributo privado

    def conducir(self, kilometros):

        if kilometros >= 0:
            self.__kilometraje += kilometros
        else:
            print(f"\n[!] Los kilometros deben ser mayores a 0\n")

    def mostrar_kilometros(self):
        return self.__kilometraje

coche = Coche("Toyto", "Corola")
coche.conducir(150)
print(coche.mostrar_kilometros()) # Esto si por convenio
print(coche._Coche__kilometraje) # Esto no por convenio 

```

> 150 \
> 150

---

Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"El libro '{self.titulo}' ha sido escrito por {self.autor}"
    
    def __eq__(self, otro):
        return self.autor == otro.autor and self.titulo == otro.titulo

libro = Libro("Gerardo lammer", "Gerardo")
print(libro)

libro_dos = Libro("Como ser un hacker", "Salvador")
print(libro_dos)

libro_tres = Libro("Gerardo lammer", "Gerardo")
print(f"Son iguales ambos libros -> {libro == libro_tres}")
```

> El libro 'Gerardo lammer' ha sido escrito por Gerardo \
> El libro 'Como ser un hacker' ha sido escrito por Salvador \
> Son iguales ambos libros -> True

---

Codigo: **Ejemplo 4**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class CuentaBancaria:

    def __init__(self, num_cuenta, titular, saldo_inicial = 0):
        self.num_cuenta = num_cuenta
        self.titular = titular
        self.__saldo = saldo_inicial # Atributo privado


    def depositar_dinero(self, cantidad):

        if cantidad > 0:
            self.__saldo += cantidad
            return f"\n[+] El saldo actual en la cuenta: {self.__saldo}"
        else:
            return f"El monto ha depositar es incorrecto"


    def retirar_dinero(self, cantidad):
        
        if cantidad > 0:
            if cantidad > self.__saldo:
                return f"\n[!] La cantidad a retirar supera el monto en la cuenta\n"
            else:
                self.__saldo -= cantidad
                return f"\n[+] Saldo actual en la cuenta: {self.__saldo}\n"
        else:
            return f"[!] El monto a retirar es incorrecto"

    def mostrar_dinero(self):
        
        return f"\n[+] El saldo actual en la cuenta es: {self.__saldo}\n"


manolo = CuentaBancaria("123", "Manolo vieira",1500)
print(manolo.depositar_dinero(500))
print(manolo.retirar_dinero(200))

print(manolo.mostrar_dinero())
```

> [+] El saldo actual en la cuenta: 2000 \
> [+] Saldo actual en la cuenta: 1800 \
> [+] El saldo actual en la cuenta es: 1800

---

Codigo: **Ejemplo 5**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Caja:

    def __init__(self, *items): # Se crea una tupla con la variable tupla
        self.items = items


    def mostrar_items(self):
        for item in self.items:
            print(item)
        print(type(self.items))

    def __len__(self): # Se define este metodo especial para poder usar len con el objeto, de otra manera nos daria error
        return len(self.items)

caja = Caja("Manzana", "Platano", "Kiwi", "Pera", "Sandia")
caja.mostrar_items()
print(len(caja))
```

> Manzana \
> Platano \
> Kiwi \
> Pera \
> Sandia \
> <class 'tuple'> \
> 5

---

Codigo: **Ejemplo 6**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Pizza:

    def __init__(self, size, *ingredientes):
        self.size = size
        self.ingredientes = ingredientes
        pass

    def descripcion(self):
        print(f"Esta pizza tiene {self.size} cm de longitud y los ingredientes son: {', '.join(self.ingredientes)}")


pizza = Pizza(12, "Chorizo", "Jamon", "Bacon", "Queso")
pizza.descripcion()
```

> Esta pizza tiene 12 cm de longitud y los ingredientes son: Chorizo, Jamon, Bacon, Queso

---

Codigo: **Ejemplo 7**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class MiLista:

    def __init__(self):
        self.data = [1,2,3,4,5]

    def __getitem__(self, index):
        return self.data[index]

lista = MiLista()
print(lista[2])


class Saludo:

    def __init__(self, saludo):
        self.saludo = saludo

    def __call__(self, nombre):
        return f"{self.saludo} {nombre}"

hola = Saludo("¡Hola")
print(hola("Luis!"))
print(hola("Alberto!"))


class Punto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, otro):
        return Punto(self.x + otro.x, self.y + otro.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    

p1 = Punto(2,8)
p2 = Punto(10,10)

print(p1 + p2) # (6,17)


class Contador:

    def __init__(self, limite):
        self.limite = limite
    
    def __iter__(self):
        self.contador = 0
        return self

    def __next__(self):
        if self.contador < self.limite:
            self.contador += 1
            return self.contador
        else:
            raise StopIteration

c = Contador(5)

for i in c:
    print(i)
```

> 3 \
> ¡Hola Luis! \
> ¡Hola Alberto! \
> (12, 18) \
> 1 \
> 2 \
> 3 \
> 4 \
> 5

## Decoradores y propiedades

### Decoradores 2/2

Los decoradores en Python son una forma elegante de modificar las funciones o métodos. Se utilizan para extener o alterar el comportamiento de la función sin cambiar su código fuente.
Un decorador es en sí mismo una función que toma otra función como argumento y devuelve una nueva función que, opcionalmente, puede agregar alguna funcionalidad antes y después de la función original.

### Propiedades

Las propiedades son un caso especial de decoradores que permiten a los desarrolladores añadir "getter", "setter" y "deleter" a los atributos de una clase de manera elegante, controlando así el acceso y la modificación de los datos.
En Python, esto se logra con el decorador '@property', que transforma un método para acceder a un atributo como si fuera un atributo público.

### Getters y setters

* El "getter" obtiene el valor de un atributo manteniendo el encapsulamiento y permitiendo que se ejecute una lógica adicional durante el acceso.
* El "setter" establece el valor de un atributo y puede incluir validación o procesamiento antes de que el cambio se refleje en el estado interno del objeto.
* El "deleter" puede ser utilizado para definir un comportamiento cuando un atributo es eliminado con del.

---

Codigo: **Ejemplo 1 DECORADORES**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def mi_decorador(funcion): # Funcion de orden superior
    def envoltura():
        print("Saludando en la envoltura del decorador antes de llamar a la función")
        funcion() # Llamada a la función principal saludo
        print("Saludando en la envoltura del decorador despues de llamar a la función")
    return envoltura

@mi_decorador
def saludo():
    print("Estoy saludando dentro de la funcion")

saludo()
```

> Saludando en la envoltura del decorador antes de llamar a la función \
> Estoy saludando dentro de la funcion \
> Saludando en la envoltura del decorador despues de llamar a la función

---

Codigo: **Ejemplo 2 PROPIEDADES**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad

    @property
    def edad(self): # Getter, definimos esta metodo como propiedad para mandar a llamar el atributo protegido de la clase sin expresarlo explicitamente como en el constructor sino como edad
        return self._edad
    
    @edad.setter # Setter, definimos este metodo para modificar el atributo protegido indirectamente, por convencion
    def edad(self, valor):
        if valor > 0:
            self._edad = valor        
        else:
            raise ValueError("[!] Operación denegada: Edad no puede ser cero o negativa")


gerardo = Persona("Gerardo",34)
gerardo.edad = 12 # Setter
gerardo.edad = -1
print(gerardo.edad) # Getter
```

---

Codigo: **Ejemplo 3**

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

import time

def cronometro(funcion):
    def envoltura(n):
        inicio = time.time()
        funcion(n)
        fin = time.time()
        print(f"Tiempo total transcurrido en la funcion {funcion.__name__}: {fin-inicio}")
    return envoltura


@cronometro
def pausa_corta(num):
    time.sleep(num)

@cronometro
def pausa_larga(num):
    time.sleep(num)

pausa_corta(2)
pausa_larga(3)
```

>

## Módulos y paquetes en Python

## Organización del código en módulos

La organización del código en módulos es una práctica esencial en Python para construir programas escalables y mantenibles. Los módulos son archivos de Python que contienen definiciones y declaraciones de variables, funciones, clases u otros objetos que se pueden reutilizar en diferentes partes del programa.

### Estructura de módulos

Cada módulo en Python es un archivo '.py' que encapsula tu código para un propósito específico.
Por ejemplo, puedes tener un módulo para operaciones matemáticas, otro para manejo de entradas/salidas y otro para la lógica de la interfaz de usuario.
Esta estructura ayuda a mantener el código organizado, facilita la lectura y hace posible la reutilización de código.

### Importación de módulos 1/2

Python utiliza la palabra clave 'import' para utilizar módulos. Puedes importar un módulo completo, como 'import math', o importar nombres específicos de un módulo utilizando 'from math import sqrt'. Python también permite la importación de módulos con un alias para facilitar su uso dentro del código, como 'import numpy as np'.

### Paquetes

Cuando los programas crecen y los módulos comienzan a acumularse, Python permite organizar módulos en paquetes. Un paquete es una carpeta que contiene módulos y un archivo especial llamado '\_\_init__.py', que indica a Python que esa carpeta contiene módulos que pueden ser importados.

### Ventajas de los módulos

* **Mantenimiento:** Los módulos permiten trabajar en partes del código de manera independiente sin afectar otras partes del sistema.
* **Espacio de nombres:** Los módulos definen su propio espacio de nombres, lo que significa que puedes tener funciones o clases con el mismo nombre en diferentes módulos sin conflicto.
* **Reutilización:** El código escrito en módulos puede ser reutilizado en diferentes programas simplemente importándolos donde se necesiten.

---

Codigo: **Ejemplo con funciones**

```python
def suma(x, y):
    return x + y
def resta(x, y):
    return x-y
def multiplicacion(x, y):
    return x*y
def division(x, y):
    if y == 0:
        raise ValueError("No es posible dividir entre cero")
    else:
        return x/y
```

---

Codigo: **Ejemplo de importacion de funciones**

```python
# Forma de importar 1
import test
# Llamado 1
print(test.suma(4,9))

# Forma de importar 2
from test import suma, resta, multiplicacion, division
# Llamado 2
print(resta(10,9))


print(multiplicacion(4,9))
print(division(4,2))
```

> 13 \
> 1 \
> 36 \
> 2

---

Codigo: **Ejemplo para ver que puedo usar de la libreria**

```python
import math
print(dir(math))


import modulo
print(modulo.__file__) # Nos servirá para ver donde está instalado el modulo
```

> ['\_\_doc__', '\_\_loader__', '\_\_name__', '\_\_package__', '\_\_spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

## Importación y uso de módulos

La importación y uso de módulos es una técnica fundamental en Python que permite la modularidad y la reutilización del código.
Los módulos son archivos de Python con extensión '.py' que contienen definiciones de funciones, clases y variables que se pueden utilizar en otros scripts de Python.

### Importación de módulos 2/2

La declaración 'import' es usada para incluir un módulo en el script actual. Cuando importas un módulo, Python busca ese archivo en una lista de directorios definida por 'sys.path', la cual incluye el directorio actual, los directorios listados en la variable de entorno 'PYTHONPATH', y los directorios de instalación por defecto.

### Uso de módulos

Una vez que un módulo es importado, puedes hacer uso de sus funciones, clases y variables, utilizando la sintaxis 'nombre_del_modulo.nombre_del_elemento'.
Esto es esencial para la organización del código, ya que permite acceder a código reutilizable sin necesidad de duplicarlo.

### Importación con alias

A veces, por conveniencia o para evitar conflictos de nombres, puedes querer darle a un módulo un alias al importarlo usando la palabra clave 'as': 'import modulo as alias'

Esto permite acceder a los componentes del módulo usando el alias en lugar del nombre completo del módulo.

### Importación específica

Si solo necesitas una o varias funciones específicas de un módulo, puedes importarlas directamente usando 'from modulo import funcion'.
Esto permite no tener que prefijar las funciones con el nombre del módulo cada vez que se llaman.
Además, puedes importar todas las definiciones de un módulo (aunque no es una práctica recomendada) usando 'from modulo import *'.

### Módulos de la biblioteca estándar

Python viene con la biblioteca estándar extensa que ofrece módulos para realizar una variedad de tareas, desde manipulación de texto, fecha y hora, hasta acceso a internet y desarrollo web.
Familiarizarse con la biblioteca estándar es crucial para ser un programador eficiente en Python.

### Módulos de terceros

Además de la biblioteca estándar, hay una amplia gama de módulos de terceros disponibles que puedes instalar y utilizar en tus programas.
Estos módulos a menudo se instalan utilizando herramientas de gestión de paquetes como ‘pip‘.

## Creación y distribución de paquetes

## Entrada y Salida de datos

### Entrada por teclado y salida por pantalla

La interacción del usuario a través de la consola es una habilidad esencial en Python, y en esta clase, exploraremos las funciones que permiten la entrada y salida de datos.
Utilizaremos ‘input()‘ para recoger la entrada del teclado y ‘print()‘ para mostrar mensajes en la pantalla.

En cuanto al formato de texto, veremos cómo manejar y presentar la información de manera amigable.
Esto incluye desde la manipulación básica de cadenas hasta técnicas más avanzadas de formateo de cadenas que permiten la inserción de variables y la alineación del texto.

La codificación de caracteres es un aspecto clave para garantizar que la entrada y salida manejen adecuadamente diferentes idiomas y conjuntos de caracteres, preservando la integridad de los datos y la claridad de la comunicación en la consola.

Dominar estas funciones es crucial para crear programas que requieran interacción con el usuario, y te brindarán las herramientas necesarias para construir aplicaciones interactivas robustas y fáciles de usar.

```python
while True:

    try:
        nombre = input("\n[+] dime tu nombre:")
        edad = int(input("\n[+] dame tu edad: "))

        print(f"tu nombre es {nombre}, el año que viene tendrás {edad + 1}")
        break
    except ValueError:
        print("El tipo esta mal")
```

```python
# Libreria getpass, no es una libreria built-in, es descargada con pip,
# sirve para ocultar las entradas por teclado, añadiendo seguridad
from getpass import getpass

password = getpass("\n[+] Introduce tu password: ")

print(f"\n[+] Tu contrasña es: {password}")
```

### Lectura y escritura de archivos

La lectura y escritura de archivos son operaciones fundamentales en la mayoría de los programas, y Python proporciona herramientas sencillas y poderosas para manejar archivos.
En esta clase, aprenderemos cómo abrir, leer, escribir y cerrar archivos de manera eficiente y segura.

### Manejo básico de archivos

Explicaremos cómo utilizar la función 'open()' para crear un objeto archivo y cómo los modos de apertura ('r' para lectura, 'w' para escritura, 'a' para añadir y 'b' para modo binario) afectan la manera en que trabajamos con esos archivos.

### Lectura de archivos

Detallaremos cómo leer el contenido de un archivo en memoria, ya sea de una sola vez con el método 'read()' o línea por línea con 'readline()' o iterando sobre el objeto archivo.

### Escritura de archivos

Examinaremos cómo escribir en un archivo usando métodos como 'write()' o 'writelines()', y cómo estos métodos difieren en cuanto a su manejo de strings y secuencias de strings.

### Manejadores de contexto

Unos de los aspectos más importantes de la lectura y escritura de archivos en Python es el uso de manejadores de contexto, proporcionados por la declaración 'with'.
Los manejadores de contexto garantizan que los recurso se manejen correctamente, abriendo el arcivo y asegurándose de que, sin importar cómo o dónde termine el bloque de código, el archivo siempre se cierre adecuadamente.
Esto ayuda a prevenir errores comunes como fugas de recursos o archivos que no se cierran si ocurre una excepción.

El uso de 'with open()' no solo mejora la legibilidad del código, sino que también simplifica el manejo de excepciones al trabajar con archivos, haciendo el código más seguro y robusto.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# example.txt ("Hola mundo")

# w -> para escribir, no guarda lo que tiene, borra y escribe
#f = open("example.txt", "w")

# r -> para leer, dando por hecho que ya exite
#f = open("example.txt", "r")

# a -> append, para añadir datos al final del todo de un archivo
f = open("example.txt", "a")

f.write("Hasta luego mundo")

f.close()

# Hacer de esta forma porque es más óptimo
# De esta forma no necesito cerrar el archivo python lo hace
with open("example.txt", "w") as f:
    f.write("Hola vicky como estas\n")
    f.write("Hola ivon como estas\n")
    f.write("Hola gerardo como estas\n")
    f.write("Hola salvador como estas\n")

with open("example.txt", "r") as f:
    file_content = f.read()

print(file_content)

with open("example.txt", "r") as f:
    for line in f:
        print(line.strip())


mi_lista = ["Primera linea\n", "Segunda linea\n", "tercera linea\n", "cuarta linea\n"]

with open ("example.txt", "w") as f:
    f.writelines(mi_lista)
```

### Formateo de cadenas y manipulación de datos

El formateo de cadenas y la manipulación de texto son habilidades esenciales en Python, especialmente en aplicaciones que involucran la presentación de datos al usuario o el procesamiento de información textual.
En esta clase, nos centraremos en las técnicas y herramientas que Python ofrece para trabajar con cadenas de texto.

#### Formateo de cadenas

Aprenderemos los distintos métodos de formateo de cadenas que Python proporciona, incluyendo:

* **Formateo clásico**: A través del operador %, similar al 'printf' en C.
* **Método format()**: Un enfoque versátil que ofrece numerosas posibilidades para formatear y alinear texto, rellenar caracteres, trabajar con números y más.
* **F-strings (Literal String Interpolation)**: Introducido en Python 3.6, este método permite incrustar expresiones dentro de cadenas de teto de una manera concisa y legible.

#### Manipulación de texto

Exploraremos las funciones y métodos incorporados para la manipulación de cadenas, que incluyen:

* **Métodos de búsqueda y reemplazo**: Como 'find()', 'index()', 'replace()' y métodos de expresiones regulares.
* **Métodos de prueba**: Para verificar el contenido de la cadena, como 'isdigit()', 'isalpha()', 'startwith()', y 'endswith()'.
* **Métodos de transformación**: Que permiten cambiar el caso de una cadena, dividirla en una lista de subcadenas o unirlas, como 'upper()', 'lower()', 'split()', y 'join()'.

También veremos cómo trabajar con cadenas Unicode en Python, lo que es esencial para aplicaciones modernas que necesitan soportar múltiples idiomas y caracteres especiales.

Al final de esta clase, tendrás una comprensión completa de cómo dar formato a las cadenas para la salida de datos y cómo realizar operaciones comunes de manipulación de texto.
Estas habilidades son fundamentales para la creación de aplicaciones que necesitan una interfaz de usuario sofisticada y para el procesamiento de datos en aplicaciones backend.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

nombre = "Gerardo"
edad = 26

print("Hola me llamo {} y tengo {}".format(nombre, edad))
print("Hola me llamo {1} y tnego {0}".format(edad, nombre))
print(f"Hola me llamo {nombre} y tengo {edad}") # Nos permiten realizar operatorias

cadena = "  Hola mundo!!    "
print(cadena.strip()) # quita espacios antes y despues del texto

cadena = "hola MUNDO"
print(cadena.lower())

cadena = "hola MUNDO"
print(cadena.upper())

cadena = "hola MUNDo"
print(cadena.replace('o', 'x')) # Donde esta 'o' cambialo por 'x'

cadena = "hola MUNDo"
nueva_cadena = cadena.split() # Crea una lista tomando en cuenta el delimitador, por default es "espacio"
print(nueva_cadena)

cadena = "Hola,mundo:test"
nueva_cadena = cadena.split(":")
print(nueva_cadena)

s = "Hola mundo!"
print(s.startswith('Hola'))

s = "Hola mundo!"
print(s.endswith('!'))

s = "gerardperezsanchez@gmail.com"
print(s.endswith('@gmail.com'))

s = "gerard@gmail.com"
print(s.find('@gmail.com'))

s = "gerard@gmail.com"
print(s.find('@gmail.com'))

#s = "gerard@gmail.com"
#print(s.index('salvador'))

s = "gerard@gmail.com"
print(f"Total de veces que sale el caracter e: {s.count('g')} ")

cadena = ["Hola", "mundo", "test"]
print(' '.join(cadena))

nombres = ["Gerardo", "Salvador", "Ivon"]
print(f"Los nombres en la lista son: {' '.join(nombres)}")

s = "hola como estas"
g = "Hola Como Estas"
print(s.capitalize()) # Mayuscula solo la primera
print(s.title()) # Mayuscula las primeras despues del espacio
print(g.swapcase()) # Invierte las mayusculas y minusculas

k = "Testing"
print(k.isalpha())

k = "Testing123"
print(k.isalpha())

k = "123"
print(k.isdigit())

k = " "
print(k.isspace())

k = "hola mundo"
print(k.islower())

k = "hola mundo"
print(k.isupper())

k = "Hola Mundo"
print(k.istitle())

k = "Hola, soy, Gerardo, y, no, me, gusta,"
print(k.replace(',','@'))

g = "Hola compañero de trabajo no me toques"
tabla = str.maketrans('aei','zpo') # transformamos aei hacia zpo respectivamente
nueva_cadena = s.translate(tabla)
print(nueva_cadena)
```

## Proyecto de POO para reforzar lo aprendido

### Proyecto de gestión de biblioteca de libros (1/2)

En este emocionante proyecto inicial, desarrollaremos un sistema de gestión para una biblioteca utilizando Python.

Este sistema nos permitirá agregar nuevos libros a la biblioteca y gestionar el préstamo de estos.
A través de la creación de este sistema, aplicaremos de manera práctica los fundamentos de la Programación Orientada a Objetos (POO), haciendo especial énfasis en conceptos clave como herencia y polimorfismo.
Diseñaremos clases para representar diferentes aspectos de una biblioteca, como libros, miembros y transacciones de préstamo.

Con este proyecto, no solo consolidaremos nuestra comprensión de POO, sino que también mejoraremos nuestras habilidades de programación en Python, creando un sistema funcional y útil.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:

    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):
        return f"Libro({self.id},{self.autor},{self.esta_prestado})"
    
    def __repr__(self):
        return self.__str__()
    
class Biblioteca:
    
    def __init__(self):
        self.libros = {} # {1 : Libro(1, "Gerardo Salvador", "El mundo de sofia")}
    
    def agregar_libro(self, libro):
        if libro.id not in self.libros:
            self.libros[libro.id] = libro
        else:
            print(f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

if __name__ == '__main__':

    biblioteca = Biblioteca()

    libro1 = Libro(1, "Gerardo Salvador", "El mundo de sofia")
    libro2 = Libro(2, "Gerardo Python", "Como ser un lammer")

    print(libro1)
    print(libro2)


    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    print(f"[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")
```

### Proyecto de gestión de biblioteca de libros (2/2)

En esta clase, continuamos avanzando en nuestro emocionante primer proyecto en Python, el desarrollo de un sistema de gestión de biblioteca.
Esta fase del proyecto nos permitirá profundizar en las funcionalidades que hemos comenzado a construir.
Nos enfocaremos en perfeccionar las características existentes y en añadir nuevas funcionalidades.

Al final de esta clase, nuestro objetivo es concluir el proyecto.
Nos aseguraremos de que todos los conceptos clave de la programación Orientada a Objetos, como la herencia, el polimorfismo y la utilización de clases, estén integrados de manera efectiva.
Esta clase no solo consolida lo aprendido hasta ahora, sino que también culmina en la finalización de un sistema funcional y bien estructurado.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Libro:

    def __init__(self, id, autor, titulo):
        self.id = id
        self.autor = autor
        self.titulo = titulo
        self.esta_prestado = False

    def __str__(self):
        return f"Libro({self.id},{self.autor}, {self.titulo}, {self.esta_prestado})"
    
    def __repr__(self):
        return self.__str__()
    
class Biblioteca:
    
    def __init__(self):
        self.libros = {} # {1 : Libro(1, "Gerardo Salvador", "El mundo de sofia")}
    
    def agregar_libro(self, libro):
        if libro.id not in self.libros:
            self.libros[libro.id] = libro
        else:
            print(f"\n[!] No es posible agregar el libro con ID {libro.id_libro}")

    def prestar_libro(self, id_libro):
        if id_libro in self.libros and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")

    @property
    def mostrar_libros(self):
        return [libro for libro in self.libros.values() if not libro.esta_prestado]

    @property
    def mostrar_libros_prestados(self):
        return [libro for libro in self.libros.values() if libro.esta_prestado]
    
class BibliotecaInfantil(Biblioteca):
    
    def __init__(self):
        super().__init__()
        self.libros_para_ninos = {} # -> {1:True, 2:False, 3:True}

    def agregar_libro(self, libro, es_para_ninos):
        super().agregar_libro(libro)
        self.libros_para_ninos[libro.id] = es_para_ninos

    def prestar_libro(self, id_libro, es_para_ninos):
        if id_libro in self.libros and self.libros_para_ninos[id_libro] == es_para_ninos and not self.libros[id_libro].esta_prestado:
            self.libros[id_libro].esta_prestado = True
        else:
            print(f"\n[!] No es posible prestar el libro con ID {id_libro}")
    
    @property
    def mostrar_estado_libros_para_ninos(self):
        return self.libros_para_ninos

if __name__ == '__main__':

    biblioteca = BibliotecaInfantil()

    libro1 = Libro(1, "Gerardo Salvador", "El mundo de sofia")
    libro2 = Libro(2, "Gerardo Python", "Como ser un lammer")
    libro3 = Libro(3, "Gerardo", "Aprende a colorear desde cero")

    biblioteca.agregar_libro(libro1, es_para_ninos=False)
    biblioteca.agregar_libro(libro2, es_para_ninos=False)
    biblioteca.agregar_libro(libro3, es_para_ninos=True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    biblioteca.prestar_libro(1, es_para_ninos = False)

    biblioteca.prestar_libro(1, es_para_ninos=True)

    print(f"\n[+] Libros en la biblioteca: {biblioteca.mostrar_libros}")

    print(f"\n[+] Libros prestados: {biblioteca.mostrar_libros_prestados}")

    print(f"\n[+] Libros para niños: {biblioteca.mostrar_estado_libros_para_ninos}")
```

### Proyecto de gestión de animales en tienda

En este proyecto, continuamos explorando la Programación Orientada a Objetos (POO), esta vez con un enfoque diferente.
Sin emplear herencia ni polimorfismo, nos centraremos en la creación de un sistema de gestión de animales en una tienda.

El proyecto involucrará el diseño y la implementación de dos clases principales que trabajarán de manera sinérgica.
Estas clases nos permitirán realizar una variedad de operaciones esenciales en la gestión de una tienda de animales.
Entre las funcionalidades que desarrollaremos, se incluyen métodos para agregar nuevos animales al inventario, mostrar los animales disponibles, alimentar a los animales y gestionar su venta.

A través de este proyecto, no solo afianzaremos nuestras habilidades en POO, sino que también demostraremos cómo diferentes clases pueden colaborar de forma efectiva para lograr objetivos comunes.
Este sistema nos dará una perspectiva práctica y realista sobre cómo la POO puede ser utilizada para resolver problemas y gestionar información en un contexto de negocios.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Animal:
    
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie
        self.alimentado = False

    def alimentar(self):
        self.alimentado = True

    def vender(self):
        self.alimentado = False

    def __str__(self):
        return f"{self.nombre} ({self.especie}) - {'Alimentado' if self.alimentado else 'Hambiento'}"

class TiendaAnimales:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def mostrar_animales(self):
        for animal in self.animales:
            print(animal)

    def alimentar_animales(self):
        for animal in self.animales:
            animal.alimentar()

    def vender_animal(self, nombre):
        for animal in self.animales:
            if animal.nombre == nombre:
                animal.vender()
                self.animales.remove(animal)
                return
        print(f"[!] No se ha encontrado ningun animal en la tienda con nombre {nombre}")



if __name__ == '__main__':

    tienda = TiendaAnimales("Vicky Zoo")

    gato = Animal("Kitty", "Gato")
    perro = Animal("Lobo", "Perro")

    tienda.agregar_animal(gato)
    tienda.agregar_animal(perro)

    tienda.mostrar_animales()
    tienda.alimentar_animales()

    print("[+] Alimentando animales")
    tienda.mostrar_animales()

    tienda.vender_animal("Lobo")
    print(f"\n[+] Mostrando los animales una ves Lobo ha sido vendido")

    tienda.mostrar_animales()

```

### Proyecto de administración de flota de vehiculos

En este proyecto de Python, nos embarcamos en el desafío de crear un sistema de administración para una flota de vehículos, aplicando nuevamente los principios de la Programación Orientada a Objetos.
Este proyecto se centrará en el diseño y la implementación de dos clases interactivas, que trabajarán en conjunto para gestionar eficientemente una flota de vehículos.

Dentro de las capacidades de nuestro sistema, incluiremos métodos para agregar nuevos vehículos a la flota, lo que nos permitirá expandir y diversificar nuestras opciones de alquiler.
Además, desarrollaremos funcionalidades para el alquiler de vehículos, brindando a los clientes la posibilidad de elegir entre diferentes tipos de vehículos según sus necesidades.

Otra característica clave será la gestión de la devolución de vehículos.
Este método facilitará el proceso de retorno de los vehículos alquilados, asegurando un control eficiente y organizado de la flota.

Este proyecto no solo fortalecerá nuestra comprensión y habilidad en POO, sino que también nos proporcionará valiosas lecciones sobre cómo las clases pueden interactuar para administrar operaciones complejas en un entorno empresarial real.

```python
#!/usr/bin/env python3
import os
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

class Vehiculo:
    def __init__(self, matricula, modelo):
        self.matricula = matricula
        self.modelo = modelo
        self.disponible = True

    def alquilar(self):
        if self.disponible:
            self.disponible = False
        else:
            print(f"[!] El vehiculo con mátricula {self.matricula} no se puede alquilar")

    def devolver(self):
        if not self.disponible:
            self.disponible = True
        else:
            print(f"[!] El vehiculo no se puede devolver porque no se ha alquilado")

    def __str__(self): 
        return f"Vehiculo(matricula={self.matricula}, modelo={self.modelo}, disponible={self.disponible})" # Vehiculo(matricula=X, modelo=Y, disponible=True/False)



class Flota:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def alquilar_vehiculos(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.alquilar()

    def devolver_vehiculo(self, matricula):
        for vehiculo in self.vehiculos:
            if vehiculo.matricula == matricula:
                vehiculo.devolver()

    def __str__(self):
        return "\n".join(str(vehiculo) for vehiculo in self.vehiculos)

if __name__ == '__main__':

    flota = Flota()

    flota.agregar_vehiculo(Vehiculo("CRM321","Hilux"))
    flota.agregar_vehiculo(Vehiculo("FFIXXX","Mazda Mx"))
    flota.agregar_vehiculo(Vehiculo("ADRRSQW","Xiaomi"))

    print("\n[+] Flota inicial:")
    print(flota)

    flota.alquilar_vehiculos("FFIXXX")

    print("\n[+] Flota:")
    print(flota)

    flota.devolver_vehiculo("FFIXXX")

    print("\n[+] Flota:")
    print(flota)

    flota.devolver_vehiculo("FFIXXX")

    print("\n[+] Flota:")
    print(flota)
```

### Proyecto de gestión de notas (1/2)

En este nuevo proyecto de Python, nos embarcamos en la construcción de un gestor de notas avanzado, aprovechando las técnicas de la Programación Orientada a Objetos (POO).
Nuestro objetivo es crear un sistema interactivo que nos permita manejar eficientemente una variedad de notas.

El corazón de nuestro proyecto será un menú interactivo desde el cual podremos realizar múltiples acciones.
Entre estas, incluiremos la capacidad de crear nuevas notas que serán almacenadas en disco, visualizar todas las notas existentes, buscar notas específicas por ciertos criterios y eliminar notas que ya no sean necesarias.

Para lograr esto, definiremos varias clases y métodos que colaborarán para manejar las diferentes operaciones relacionadas con las notas.
Una parte crucial de nuestro proyecto será la implementación de módulos múltiples, lo que nos permitirá organizar mejor nuestro código y hacerlo más mantenible.

Además, exploraremos los conceptos de serialización y deserialización de datos utilizando Pickle.
Esto nos permitirá guardar y recuperar eficientemente el estado de nuestras notas desde y hacia el disco, facilitando la persistencia de los datos a través de las sesiones de uso del gestor.

Este proyecto no solo fortalecerá nuestras habilidades en POO y manejo de datos, sino que también nos proporcionará experiencia práctica en la creación de aplicaciones Python que interactúan con el sistema de archivos y gestionan la información de manera eficiente.

---

Codigo: **main.py**

```python
#!/usr/bin/env python3
import os, pickle
from gestor_notas import GestorNotas

# Sistema de gestion de notas, craer nota en un archivo, leer nota con menu, 
# Serializacion y deserializacion pickle

def main():

    gestor = GestorNotas()

    while True:

        print(f"\n-------------\nMENU\n-------------")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar por una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opcion = input("\n[+] Escoge una opción: ")

        if opcion == "1":
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "5":
            break

        else:
            print("\n[!] La opción indicada es incorrecta\n")

        input(f"\n[+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
```

---

Codigo: **gestor_notas.py**

```python
#!/usr/bin/env python3
import pickle
from notas import Nota

class GestorNotas:
    def __init__(self, archivos_notas='notas.pkl'):
        self.archivos_notas = archivos_notas

        try:
            with open(self.archivos_notas, 'rb') as f:
                self.notas = pickle.load(f)

        except FileNotFoundError:
            self.notas = []

    def guardar_notas(self):
        with open(self.archivos_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()
```

---

Codigo: **notas.py**

```python
#!/usr/bin/env python3

class Nota:

    def __init__(self, contenido):
        self.contenido = contenido

```

### Proyecto de gestión de notas (2/2)

En esta clase, concluiremos nuestro proyecto de gestor de notas en Python utilizando Pickle.
Tras haber sentado las bases en nuestra sesión anterior, ahora es momento de integrar y finalizar todos los componentes de nuestro sistema.
Vamos a dedicar esta clase a revisar y perfeccionar las clases principales, asegurándonos de que todas las funcionalidades clave, como crear, visualizar, buscar y eliminar notas, funcionen de manera fluida.

Un enfoque importante será la implementación efectiva de la serialización y deserialización con Pickle.
Esta técnica es crucial para la persistencia de las notas en el disco, permitiendo que se guarden de forma segura y se recuperen en futuras sesiones del programa.

Al concluir esta clase, habremos completado un gestor de notas funcional y eficiente.
Este proyecto no solo refuerza nuestras habilidades en programación orientada a objetos y manejo de datos, sino que también nos proporciona experiencia práctica en la creación de aplicaciones Python interactivas y robustas.

---

Codigo: **main.py**

```python
#!/usr/bin/env python3
import os, pickle
from gestor_notas import GestorNotas

# Sistema de gestion de notas, craer nota en un archivo, leer nota con menu, 
# Serializacion y deserializacion pickle

def main():

    gestor = GestorNotas()

    while True:

        print(f"\n-------------\nMENU\n-------------")
        print("1. Agregar una nota")
        print("2. Leer todas las notas")
        print("3. Buscar por una nota")
        print("4. Eliminar una nota")
        print("5. Salir")

        opcion = input("\n[+] Escoge una opción: ")

        if opcion == "1":
            contenido = input("\n[+] Contenido de la nota: ")
            gestor.agregar_nota(contenido)

        elif opcion == "2":
            notas = gestor.leer_notas()

            print("\n[+] Mostrando todas las notas almacenadas: \n")

            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")

        elif opcion == "3":
            texto_busqueda = input("\n[+] Ingresa el texto a buscar como criterio en las notas: ")

            notas = gestor.buscar_nota(texto_busqueda)

            print(f"\n[+] Mostrando las notas que coinciden con el criterio de busqueda:\n")
            
            for i, nota in enumerate(notas):
                print(f"{i}: {nota}")
        elif opcion == "4":
            index = int(input("\n[+] Introduce el indice de la nota que quieres borrar:\n"))
            gestor.eliminar_nota(index)
        elif opcion == "5":
            break

        else:
            print("\n[!] La opción indicada es incorrecta\n")

        input(f"\n[+] Presiona <Enter> para continuar...")
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
    main()
```

---

Codigo: **gestor_notas.py**

```python
#!/usr/bin/env python3
import pickle
from notas import Nota

class GestorNotas:
    def __init__(self, archivos_notas='notas.pkl'):
        self.archivos_notas = archivos_notas

        try:
            with open(self.archivos_notas, 'rb') as f:
                self.notas = pickle.load(f)

        except FileNotFoundError:
            self.notas = []

    def guardar_notas(self):
        with open(self.archivos_notas, 'wb') as f:
            pickle.dump(self.notas, f)

    def agregar_nota(self, contenido):
        self.notas.append(Nota(contenido))
        self.guardar_notas()

    def leer_notas(self):
        return self.notas
    
    def buscar_nota(self, texto_busqueda):
        return [nota for nota in self.notas if nota.coincide(texto_busqueda)]
    
    def eliminar_nota(self, index):
        if index < len(self.notas):
            del self.notas[index]
            self.guardar_notas()
        else:
            print(f"\n[!] El índice proporcionado es incorrecto\n")
        
```

---

Codigo: **notas.py**

```python
#!/usr/bin/env python3

class Nota:

    def __init__(self, contenido):
        self.contenido = contenido

    def coincide(self, texto_busqueda):
        return texto_busqueda in self.contenido


    def __str__(self):
        return self.contenido
```

## Biblioteca estándar y herramientas adicionales

### Manejo de fechas y horas

La biblioteca 'datetime' en Python es una de las principales herramientas para trabajar con fechas y horas.
Aquí hay algunos aspectos clave sobre esta biblioteca:

* **Tipos de datos principales**: 'datetime' incluye varios tipos de datos, como 'date' (para fechas), 'time'(para horas), 'datetime'(para fechas y horas combinadas), y 'timedelta'(para representar diferencias de tiempo).
* **Manipulación de fechas y horas**: Permite realizar operaciones como sumar o restar días, semanas, o meses a una fecha, comparar fechas, o extraer componentes como el día, mes, o año de una fecha específica.
* **Zonas horarias**: A través del módulo 'pytz' que se integra con 'datetime', se pueden manejar fechas y horas en diferentes zonas horarias, lo que es crucial para aplicaciones que requieren precisión a nivel global.
* **Formateo y análisis**: 'datetime' permite convertir fechas y horas a strings y viceversa, utilizando códigos de formato específicos. Esto es útil para mostrar fechas y horas en formatos legibles o para parsear strings que representan fechas/horas.
* **Facilidad de uso**: A pesar de su potencia y flexibilidad, datetime es relativamente fácil de usar, lo que la hace accesible incluso para programadores principiantes.
* **Amplia aplicación**: Desde registros de eventos hasta cálculos de períodos de tiempo, datetime es indispensable en una variedad de aplicaciones, como sistemas de reservas, análisis de datos temporales, y más.

En resumen, datetime es una biblioteca integral y robusta para el manejo de fechas y horas en Python, ofreciendo una amplia gama de funcionalidades esenciales para el manejo de datos temporales en la programación.

```python
#!/usr/bin/env python3

import datetime

fecha = datetime.date(2023, 5, 13)
hora = datetime.time(14,15,15)
fecha_hora = datetime.datetime(2023, 5, 12, 14, 15, 16)

ahora = datetime.datetime.now()
año = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minuto = ahora.minute
segundo = ahora.second

print(fecha)
print(hora)
print(fecha_hora)

print(ahora)
print(año)
print(mes)
print(dia)
print(hora)
print(minuto)
print(segundo)
```

### Expresiones regulares

La librería 're' en Python proporciona un conjunto completo de herramientas para trabajar con expresiones regulares, que son patrones de cadenas diseñados para la búsqueda y manipulación de texto.

Aquí hay varios aspectos importantes de esta librería:

* **Funciones básicas**: 're' incluye funciones como 'search' (para buscar un patrón dentro de una cadena), 'match' (para verificar si una cadena comienza con un patrón específico), 'findall' (para encontrar todas las ocurrencias de un patrón), y 'sub' (para reemplazar partes de una cadena que coinciden con un patrón).
* **Compilación de patrones**: Permite compilar expresiones regulares en objetos de patrón, lo que puede mejorar el rendimiento cuando se usan repetidamente.
* **Grupos y captura**: Ofrece la capacidad de definir grupos dentro de patrones de expresiones regulares, lo que facilita extraer partes específicas de una cadena que coinciden con subpatrones.
* **flags**: Soporta modificadores que alteran la forma en que las expresiones regulares son interpretadas y coincididas, como ignorar y mayúsculas y minúsculas o permitir el modo multilínea.
* **Patrones complejos**: Permite la creación de patrones complejos utilizando una variedad de símbolos y secuencias especiales, como cuantificadores, aserciones y clases de caracteres.
* **Aplicaciones prácticas**: Las expresiones regulares son extremadamente útiles en tareas como la validación de formatos (por ejemplo, direcciones de correo electrónicos), el análisis de registros(logs), el procesamiento de lenguaje natural, y la limpieza y preparación de datos.
* **Curva de aprendizaje**: Aunque potentes, las expresiones regulares pueden ser complejas y requieren una curva de aprendizaje. Sin embargo, una vez dominadas, se convierten en una herramienta invaluable en el arsenal de cualquier programador.

En resumen, la librería 're' en Python es una herramienta esencial para cualquier tarea que implique procesamiento complejo de cadenas de texto, proporcionando una forma poderosa y flexible de buscar, analizar, y manipular datos basados en texto.

```python
#!/usr/bin/env python3
import os, re
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 


texto = "Mi gato está en el tejado y mi otro gato está en el jardin"
texto_1 = "Hoy estamos a fecha 10/10/2025, mañana estaremos a 11/10/2025"
texto_2 = "Los usuarios pueden contactarnos a soporte@hack.io o a sistemas@hack.io"
texto_3 = "Mi gato está en el tejado y mi perro está en el jardin"
texto_4 = "Campo1, Campo2, Campo3, Campo4, Campo5, Campo6"

texto = re.findall("gato", texto)
texto_1 = re.findall("\d{2}\/\d{2}\/\d{4}", texto_1)
texto_2 = re.findall("(\w+)@(\w+\.\w{2,})", texto_2)
texto_3 = re.sub("gato", "perro", texto_3)
texto_4 = re.split(",", texto_4)

print(texto)
print(texto_1)
print(texto_2)
print(texto_3)
print(texto_4)
print(texto_4[1])

# Validador de un correo electrónico

def validar_correo(correo):
    
    patron = "[A-Za-z0-9._+-]+@[A-Za-z0-9]+\.[A-Za-z]{2,}"

    if re.findall(patron, correo):
        return True
    else:
        return False

print(validar_correo("soporte@hack4u.io"))

################################################################

patrones = "car, carro, cart, masticar, magicarp"

print(re.findall("car", patrones))
print(re.findall(r"\bcar", patrones))
print(re.findall(r"car\b", patrones))
print(re.findall(r"\bcar\b", patrones))

################################################################

texto_5 = "Hoy estamos a dia 10/10/2023 mañana será 11/10/2023"
patron = r"\b(\d{2}\/\d{2}\/\d{4})\b"
print(re.findall(patron, texto_5))

for match in re.finditer(patron, texto_5):
    print(f"La fecha es: {match.group(0)}, la cual comienza en la posicion {match.start()} y termina en la posicion {match.end()}")
```

### Manejo de archivos y directorios

La librería ‘os‘ y el módulo ‘shutil‘ en Python son herramientas fundamentales para interactuar con el sistema de archivos, especialmente en lo que respecta a la creación y eliminación de archivos y directorios.

Aquí tienes una descripción detallada de ambas:

Librería os

* **Funcionalidades Básicas**: ‘os’ proporciona una interfaz rica y variada para interactuar con el sistema operativo subyacente. Permite realizar operaciones como la creación y eliminación de archivos y directorios, así como la manipulación de rutas y el manejo de la información del sistema de archivos.

Creación y Eliminación de Archivos y Directorios

* **Creación de Directorios**: Utilizando ‘os.mkdir()‘ u ‘os.makedirs()‘, se pueden crear directorios individuales o múltiples directorios (y subdirectorios) respectivamente.
* **Eliminación**: ‘os.remove()‘ se usa para eliminar archivos, mientras que ‘os.rmdir()‘ y ‘os.removedirs()‘ permiten eliminar directorios y directorios con subdirectorios, respectivamente.
* **Gestión de Rutas**: La sublibrería ‘os.path‘ es crucial para manipular rutas de archivos y directorios, como unir rutas, obtener nombres de archivos, verificar si un archivo o directorio existe, etc.

Módulo shutil

* **Operaciones de Alto Nivel**: Mientras que os se enfoca en operaciones básicas, ‘shutil‘ proporciona funciones de nivel superior, más orientadas a tareas complejas y operaciones en lotes.
* **Copiar y Mover Archivos y Directorios**: ‘shutil‘ es especialmente útil para copiar y mover archivos y directorios. Funciones como ‘shutil.copy()‘, ‘shutil.copytree()‘, y ‘shutil.move()‘ facilitan estas tareas.
* **Eliminación de Directorios**: Aunque ‘os‘ puede eliminar directorios, ‘shutil.rmtree()‘ es una herramienta más poderosa para eliminar un directorio completo y todo su contenido.
* **Manejo de Archivos Temporales**: ‘shutil‘ también ofrece funcionalidades para trabajar con archivos temporales, lo que es útil para operaciones que requieren almacenamiento temporal de datos.

En resumen, ‘os‘ y ‘shutil‘ en Python son bibliotecas complementarias para la gestión de archivos y directorios. Mientras ‘os‘ ofrece una gran flexibilidad para operaciones básicas y de bajo nivel, ‘shutil‘ brinda herramientas más potentes y de alto nivel, adecuadas para tareas complejas y operaciones en lotes. Juntas, forman un conjunto integral de herramientas para la manipulación eficaz del sistema de archivos en Python.

```python
#!/usr/bin/env python3
import os
import shutil # para borrar directorios con contenido

os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

if os.path.exists("mi_archivo.txt"):
    print(f"\n[+] El archivo existe")
else:
    print(f"\n[!] El archivo no existe")

#if not os.path.exists("mi_directorio"):
#    os.mkdir("mi_directorio")

if not os.path.exists("mi_directorio/mi_subdirectorio"):
    os.makedirs("mi_directorio/mi_subdirectorio")

print("[+] Listando todos los recursos del directorio actual de trabajo: \n")
recursos = os.listdir()
for recurso in recursos:
    print(recurso)

if os.path.exists("file1.txt"):
    os.remove("file1.txt")

#if os.path.exists("mi_directorio"): # No se pueden borrar directorios con archivos con la clase OS
#    os.removedirs("mi_directorio/mi_subdirectorio")

if os.path.exists("mi_directorio"):
    shutil.rmtree("mi_directorio")

#os.rename("file2.txt", "cambiado.txt") # Para cambiar el nombre de un archivo

#tamaño = os.path.getsize("/etc/passwd") # Obtiene el tamaño de un archivo

ruta = os.path.join("ProyectosPOO", "notas.py")
print(f"\n[+] Ruta: {ruta}")

archivo = os.path.basename(ruta)
directorio = os.path.dirname(ruta)
print(f"\n[+] Nombre del archivo: {archivo}")
print(f"\n[+] Nombre del archivo: {directorio}")

print(f"\n[+] Ruta: {ruta}")
directorio2, archivo2 = os.path.split(ruta)
print(f"[+] Archivo: {archivo2}, Directorio: {directorio2}")
```

### Conexiones de red  y protocolos (1/4)

Los protocolos TCP (Transmission Control Protocol) y UDP (User Datagram Protocol) son fundamentales en la comunicación de red, y la librería ‘socket‘ en Python proporciona las herramientas necesarias para interactuar con ellos.
Aquí tienes una descripción detallada de ambos protocolos y el uso de ‘socket‘:

#### Protocolo TCP

* **Orientado a la Conexión**: TCP es un protocolo orientado a la conexión, lo que significa que establece una conexión segura y confiable entre el emisor y el receptor antes de la transmisión de datos.
* **Fiabilidad y Control de Flujo**: Garantiza la entrega de datos sin errores y en el mismo orden en que se enviaron.También gestiona el control de flujo y la corrección de errores.
* **Uso en Aplicaciones**: Es ampliamente utilizado en aplicaciones que requieren una entrega fiable de datos, como navegadores web, correo electrónico, y transferencia de archivos.

#### Protocolo UDP

* **No Orientado a la Conexión**: A diferencia de TCP, UDP es un protocolo no orientado a la conexión. Envía datagramas (paquetes de datos) sin establecer una conexión previa.
* **Rápido y Ligero**: UDP es más rápido y tiene menos sobrecarga que TCP, ya que no verifica la llegada de paquetes ni mantiene el orden de los mismos.
* **Uso en Aplicaciones**: Ideal para aplicaciones donde la velocidad es crucial y se pueden tolerar algunas pérdidas de datos, como juegos en línea, streaming de video y voz sobre IP (VoIP).

#### Librería ‘socket’ en Python

La librería ‘socket‘ en Python es una herramienta esencial para la programación de comunicaciones en red. Permite a los desarrolladores crear aplicaciones que pueden enviar y recibir datos a través de la red, ya sea en una red local o a través de Internet.
Aquí tienes una visión general de la librería ‘socket‘:

* **Creación de sockets**: La librería ‘socket‘ proporciona clases y funciones para crear sockets, que son puntos finales de comunicación. Puedes crear sockets tanto para el protocolo TCP (Transmission Control Protocol) como para UDP (User Datagram Protocol).
* **Conexiones TCP**: Puedes utilizar ‘socket‘ para establecer conexiones TCP, que son conexiones confiables y orientadas a la conexión. Esto es útil para aplicaciones que requieren transferencia de datos confiable, como la transmisión de archivos o la comunicación cliente-servidor.
* **Comunicación UDP**: La librería ‘socket‘ también admite la comunicación mediante UDP, que es un protocolo de envío de mensajes sin conexión. Es adecuado para aplicaciones que necesitan una comunicación rápida y eficiente, como juegos en línea o aplicaciones de transmisión de video en tiempo real.
* **Funciones de envío y recepción**: Puedes utilizar métodos como ‘send()‘ y ‘recv()‘ para enviar y recibir datos a través de sockets. Esto te permite transferir información entre dispositivos de manera eficiente.
* **Gestión de conexiones**: La librería ‘socket‘ incluye métodos como ‘bind()‘ para asociar un socket a una dirección y puerto específicos, y ‘listen()‘ para poner un socket en modo de escucha, lo que le permite aceptar conexiones entrantes.
* **Conexiones cliente-servidor**: Con ‘socket‘, puedes crear aplicaciones cliente-servidor, donde un programa actúa como servidor esperando conexiones entrantes y otro actúa como cliente para conectarse al servidor.

En resumen, la librería ‘socket‘ en Python proporciona las herramientas necesarias para desarrollar aplicaciones de red, permitiendo la comunicación entre dispositivos a través de diferentes protocolos y ofreciendo control sobre la transferencia de datos.
Es una parte fundamental de la programación de redes en Python y se utiliza en una amplia variedad de aplicaciones, desde servidores web hasta aplicaciones de chat y juegos en línea.

---

Codigo: **server.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

# af inet = ipv4, sock stream = tcp
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
server_socket.bind(server_address)

# Limitar el límite de conexiones
server_socket.listen(1)

while True:

    client_socket, client_address =  server_socket.accept()
    data = client_socket.recv(1024)
    
    print(f"\n[+] Mensaje recibido del cliente: {data.decode()}")
    print(f"\n[+] Información del cliente que se ha comunicado con nosotros: {client_address}")

    client_socket.sendall(f"Un saludo crack\n".encode())
    client_socket.close()
```

---

Codigo: **client.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 1234)
client_socket.connect(server_address)

try:
    message = b"Este es un mensaje de prueba que estoy enviando al servidor"
    client_socket.sendall(message)
    data = client_socket.recv(1024)

    print(f"[+] El servidor nos  ha respondido con este mensaje: {data.decode()}")
finally:
    client_socket.close()
```

### Conexiones de red y protocolos (2/4)

#### Manejadores de contexto con conexiones

Los manejadores de contexto (‘with‘ en Python) se utilizan para garantizar que los recursos se gestionen de manera adecuada.
En el contexto de las conexiones de socket, un manejador de contexto se encarga de abrir y cerrar el socket de manera segura.
Esto evita que los recursos del sistema se queden en uso indefinidamente y asegura una gestión adecuada de las conexiones.

#### Diferencias entre send y sendall

* **send(data)**: El método ‘send()‘ se utiliza para enviar una cantidad específica de datos a través del socket. Puede no enviar todos los datos en una sola llamada y puede ser necesario llamarlo múltiples veces para enviar todos los datos.
* **sendall(data)**: El método ‘sendall()‘ se utiliza para enviar todos los datos especificados a través del socket. Realiza llamadas repetidas a ‘send()‘ internamente para garantizar que todos los datos se envíen por completo sin pérdidas.

La elección entre ‘send‘ y ‘sendall‘ depende de si se necesita garantizar la entrega completa de los datos o si se permite que los datos se envíen en fragmentos. send puede enviar datos en fragmentos, mientras que sendall garantiza que todos los datos se envíen sin pérdida.

---

Codigo: **server2.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def start_server():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        print(f"\n[+] Servidor en escucha en {host}:{port}")
        s.listen(1)
        conn, addr = s.accept()

        with conn:
            print(f"\n[+] Se ha conectado un nuevo cliente: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)

start_server()
```

---

Codigo: **client2.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def start_client():
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b"Hola, servidor!")
        data = s.recv(1024)

    print(f"[+] Mensaje recibido del servidor: {data.decode()}")


start_client()
```

---

Codigo: **server3.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def start_udp_server():
    
    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.bind((host, port))
        print(f"\n[+] Servidor UDP iniciado en {host}:{port}")

        while True:
            data, addr = s.recvfrom(1024)
            print(f"\n[+] Mensaje enviado por el cliente: {data.decode()}")
            print(f"\n[+] Información del cliente que nos ha enviado el mensaje: {addr}")

start_udp_server()
```

---

Codigo: **client3.py**

```python
#!/usr/bin/env python3
import os, socket
os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

def start_udp_client():
    host = 'localhost'
    port = 1234
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        message = "Hola, aquí estamos tensandola".encode("utf-8")
        s.sendto(message, (host, port))
start_udp_client()
```

### Conexiones de red y protocolos (3/4)

La función ‘setsockopt‘ en la programación de redes juega un papel crucial al permitir a los desarrolladores ajustar y controlar varios aspectos de los sockets.
Los sockets son fundamentales en la comunicación de red, proporcionando un punto final para el envío y recepción de datos en una red.

#### Niveles en setsockopt

Cuando utilizas ‘setsockopt’, puedes especificar diferentes niveles de configuración, que determinan el ámbito y la aplicación de las opciones que estableces:

* **Nivel de Socket (SOL_SOCKET)**: Este nivel afecta a las opciones aplicables a todos los tipos de sockets, independientemente del protocolo que estén utilizando. Las opciones en este nivel controlan aspectos generales del comportamiento del socket, como el tiempo de espera, el tamaño del buffer, y el reuso de direcciones y puertos.
* **Nivel de Protocolo**: Este nivel permite configurar opciones específicas para un protocolo de red en particular, como TCP o UDP. Por ejemplo, puedes ajustar opciones relacionadas con la calidad del servicio, la forma en que se manejan los paquetes de datos, o características específicas de un protocolo.

#### socket.SOL_SOCKET

‘socket.SOL_SOCKET‘ es una constante en muchos lenguajes de programación que se usa con ‘setsockopt’ para indicar que las opciones que se van a ajustar son a nivel de socket.
Esto significa que las opciones aplicadas en este nivel afectarán a todas las operaciones de red realizadas a través del socket, sin importar el protocolo de transporte específico (como TCP o UDP) que esté utilizando.

#### socket.SO_REUSEADDR

‘socket.SO_REUSEADDR‘ es otra opción comúnmente utilizada en setsockopt. Esta opción es muy útil en el desarrollo de aplicaciones de red. Lo que hace es permitir que un socket se enlace a un puerto que todavía está siendo utilizado por un socket que ya no está activo.
Esto es particularmente útil en situaciones donde un servidor se reinicia y sus sockets aún están en un estado de “espera de cierre” (TIME_WAIT), lo que podría impedir que el servidor se vuelva a enlazar al mismo puerto.

Al establecer ‘SO_REUSEADDR‘, el sistema operativo permite reutilizar el puerto inmediatamente, lo que facilita la reanudación rápida de los servicios del servidor.

En resumen, ‘setsockopt‘ con diferentes niveles y opciones, como ‘SOL_SOCKET‘ y ‘SO_REUSEADDR‘, proporciona una flexibilidad significativa en la configuración de sockets para una comunicación de red eficiente y efectiva.

### Conexiones de red y protocolos (4/4)

El uso de hilos con ‘threading‘ en Python es crucial para gestionar múltiples clientes en aplicaciones de red que utilizan sockets, especialmente en servidores.

Aquí te explico en detalle por qué es necesario:

* **Concurrencia y Manejo de Múltiples Conexiones**: Los servidores de red a menudo necesitan manejar múltiples conexiones de clientes simultáneamente. Sin hilos, un servidor tendría que atender a un cliente a la vez, lo cual es ineficiente y no escalable. Con ‘threading‘, cada cliente puede ser manejado en un hilo separado, permitiendo al servidor atender múltiples solicitudes al mismo tiempo.
* **Bloqueo de Operaciones de Red**: Las operaciones de red, como ‘recv‘ y ‘accept‘, suelen ser bloqueantes. Esto significa que el servidor se detendrá en estas operaciones hasta que se reciba algo de la red. Si un cliente se demora en enviar datos, esto puede bloquear todo el servidor, impidiendo que atienda a otros clientes. Con hilos, cada cliente tiene su propio hilo de ejecución, por lo que la lentitud o el bloqueo de uno no afecta a los demás.
* **Escalabilidad**: Los hilos permiten a los desarrolladores crear servidores que escalan bien con el número de clientes. Al asignar un hilo a cada cliente, el servidor puede manejar muchos clientes a la vez, ya que cada hilo ocupa relativamente pocos recursos del sistema.
* **Simplicidad en el Diseño de la Aplicación**: Aunque existen modelos alternativos para manejar la concurrencia (como la programación asíncrona), el uso de hilos puede simplificar el diseño y la lógica de la aplicación. Cada hilo puede ser diseñado como si estuviera manejando solo un cliente, lo que facilita la programación y el mantenimiento del código.
* **Uso Eficiente de Recursos de CPU en Sistemas Multi-Core**: Los hilos pueden ejecutarse en paralelo en diferentes núcleos de un procesador multi-core, lo que permite a un servidor aprovechar mejor el hardware moderno y manejar más eficientemente varias conexiones al mismo tiempo.
* **Independencia y Aislamiento de Clientes**: Cada hilo opera de manera independiente, lo que significa que un problema en un hilo (como un error o una excepción) no necesariamente afectará a los demás. Esto proporciona un aislamiento efectivo entre las conexiones de los clientes, mejorando la robustez del servidor.

En resumen, el uso de ‘threading‘ para manejar múltiples clientes en aplicaciones basadas en sockets es esencial para lograr una alta concurrencia, escalabilidad y un diseño eficiente que aproveche al máximo los recursos del sistema y proporcione un servicio fluido y estable a múltiples clientes simultáneamente.

---

* **sever4.py**

```python
#!/usr/bin/env python3

import socket, threading, pdb

class ClientThread(threading.Thread):

    def __init__(self, client_sock, client_addr):
        super().__init__()
        self.client_sock = client_sock
        self.client_addr = client_addr

        print(f"\n[+] Nuevo cliente conectado: {client_addr}")

    def run(self):

        message = ''

        while True:
            data = self.client_sock.recv(1024)
            message = data.decode()

            if message.strip() == 'bye':
                break

            print(f"\n[+] Mensaje enviado por el cliente: {message.strip()}")
            self.client_sock.send(data)

        print(f"[+] Cliente {client_addr} desconectado")

        self.client_sock.close()


HOST = 'localhost'
PORT = 1234

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT 
    server_socket.bind((HOST, PORT))

    print(f"\n[+] En espera de conexiones entrantes...")

    while True:

        server_socket.listen()
        client_sock, client_addr = server_socket.accept()

        new_thread = ClientThread(client_sock, client_addr)
        new_thread.start() # run()


```

---

* **clien4.py**

```python
#!/usr/bin/env python3

import socket

def start_client():

    host = 'localhost'
    port = 1234

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            message = input("\n[+] Introduce tu mensaje: ")
            s.sendall(message.encode())

            if message == 'bye':
                break
            data = s.recv(1024)
            print(f"\n[+] Mensaje de respuesta del servidor: {data.decode()}")

start_client()
```

---

Codigo: **server5.py**

```python
#!/usr/bin/env python3

import socket

def start_chat_server():
    host = 'localhost'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # TIME_WAIT
    server_socket.bind((host,port))
    server_socket.listen(1)

    print(f"\n[+] Listo para tensarla con una conexión...")
    connection, client_addr = server_socket.accept()
    print(f"\n[+] Se ha conectado el cliente {client_addr}")

    while True:
        client_message = connection.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del cliente: {client_message}")

        if client_message == 'bye':
            break

        server_message = input(f"\n[+] Mensaje para enviar al cliente: ")
        connection.send(server_message.encode())

    connection.close()

start_chat_server()
```

---

Codigo: **client5.py**

```python
#!/usr/bin/env python3

import socket

def start_chat_client():

    host = 'localhost'
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        client_message = input(f"\n[+] Mensaje para enviar al servidor: ")
        client_socket.send(client_message.encode())

        if client_message == 'bye':
            break

        server_message = client_socket.recv(1024).strip().decode()
        print(f"\n[+] Mensaje del servidor: {server_message}")
    
    client_socket.close()

start_chat_client()
```

## Manejo de líbrerias comunes

### Librerías os y sys

Las bibliotecas ‘os‘ y ‘sys‘ de Python son herramientas esenciales para cualquier desarrollador que busque interactuar eficazmente con el sistema operativo y gestionar el entorno de ejecución de sus programas.
Estas bibliotecas proporcionan una amplia gama de funcionalidades que permiten una mayor flexibilidad y control en el desarrollo de software.

#### Biblioteca os

La biblioteca ‘os‘ en Python es una herramienta poderosa para interactuar con el sistema operativo. Proporciona una interfaz portátil para usar funcionalidades dependientes del sistema operativo, lo que significa que los programas pueden funcionar en diferentes sistemas operativos sin cambios significativos en el código.
Algunas de sus capacidades incluyen:

* **Manipulación de Archivos y Directorios**: Permite realizar operaciones como crear, eliminar, mover archivos y directorios, y consultar sus propiedades.
* **Ejecución de Comandos del Sistema**: Facilita la ejecución de comandos del sistema operativo desde un programa Python.
* **Gestión de Variables de Entorno**: Ofrece funciones para leer y modificar las variables de entorno del sistema.
* **Obtención de Información del Sistema**: Proporciona métodos para obtener información relevante sobre el sistema operativo, como la estructura de directorios, detalles del usuario, procesos, etc.

#### Biblioteca sys

La biblioteca ‘sys‘ es fundamental para interactuar con el entorno de ejecución del programa Python. A diferencia de ‘os‘, que se centra en el sistema operativo, ‘sys‘ está más orientada a la interacción con el intérprete de Python.
Sus principales usos incluyen:

* **Argumentos de Línea de Comandos**: Permite acceder y manipular los argumentos que se pasan al programa Python desde la línea de comandos.
* **Gestión de la Salida del Programa**: Facilita el control sobre la salida estándar (stdout) y la salida de error (stderr), lo cual es esencial para la depuración y la presentación de resultados.
* **Información del Intérprete**: Ofrece acceso a configuraciones y funcionalidades relacionadas con el intérprete de Python, como la versión de Python en uso, la lista de módulos importados y la gestión de la ruta de búsqueda de módulos.

Ambas bibliotecas son cruciales para el desarrollo de aplicaciones Python que requieren interacción avanzada con el entorno de sistema y el intérprete. Su comprensión y uso adecuado permite a los desarrolladores escribir código más robusto, portable y eficiente.

---

Codigo: **OS & SYS**

```python
#!/usr/bin/env python3
import os, sys

os.system('cls' if os.name == 'nt' else 'clear') # Para limpiar terminal 

pwd = os.getcwd() # Nos da el directorio actual de trabajo
files = os.listdir(pwd) # Nos da los archivos del directorio que le estamos pasando
print(files)

for file in files:
    print(file)

# os.mkdir("mi_directorio") # Nos crea un directorio de trabajo en la ruta actual
# os.path.exists('mi_archivo.txt') # nos buscar si un archivo existe

# get_env = os.getenv('nombre_de_variable_entorno') # Nos buscar el valor de la variable de entorno

#____________________________________________sys
# Para controlar el numero de argumentos que se le pasa a un script

print(f"\n[+] Nombre del script: {sys.argv[0]}") # Recopila el nombre del script

print(f"[+] Total de argumentos que se estan pasando al programa: {len(sys.argv)}")
print(f"[+] Mostrando el primer argumento: {sys.argv[1]}")
print(f"[+] Mostrando el segundo argumento: {sys.argv[2]}")
print(f"[+] Mostrando todos los argumentos {sys.argv}")
print(f"[+] Mostrando todos los argumentos {', '.join(argument for argument in sys.argv)}")
print(f"Mostrando las rutas de python: {f',\n'.join(ruta for ruta in sys.path)}")


print(f"\n[+] Saliendo con un código de estado 1 (no exitoso)")
sys.exit(1)
```

### Librería request (1/2)

La biblioteca 'request' en python es una de las herramientas más populares y poderosas para realizar solicitudes HTTP. Su diseño es intuitivo y fácil de usar, lo que la hace una opción preferida para interactuar con APIs y servicios web.

#### Introducción a request

'requests' es una biblioteca de Python que simplifica enormemente el proceso de enviar solicitudes HTTP. Está diseñada para ser más fácil de usar que las opciones incorporadas en Python, como 'urllib', proporcionando una API más amigable.

#### Características Principales

* **Simplicidad y facilidad de uso**: Con requests, enviar solicitudes GET, POST, PUT, DELETE, entre otras, se puede realizar en pocas líneas de código. Su sintaxis es clara y concisa.
* **Gestión de parámetros URL**: Permite manejar parámetros de consulta y cuerpos de solicitud con facilidad, automatizando la codificación de URL.
* **Manejo de respuestas**: 'requests' facilita la interpretación de respuestas HTTP, proporcionando un objeto de respuesta que incluye el contenido, el estado, los encabezados, y más.
* **Soporte para autenticaciones**: Ofrece soporte integrado para diferentes formas de autenticación, incluyenod autenticación básica, digest, y OAuth.
* **Manejo de sesiones, y cookies:** Permite mantener sesiones gestionar cookies, lo cual es útil para interactuar con sitios web que requieren autenticación o mantienen estado.
* **Soporte para SSL**: 'request' manje SSL (Secure Sockets Layer) y TLS (Transport Layer Security), permitiendo realizar solicitudes seguras a sitios HTTPS.
* **Manejo de excepciones y errores**: Proporciona métodos para manejar y reportar errores de red y HTTP de manera efectiva.

#### Uso práctico

La biblioteca se utiliza ampliamente para interactuar con APIs RESTful, automatizar interacciones con sitios web, y en tareas de scrapping web, Sus capacidades para manejar solicitudes complejas y sus caracteríticas de seguridad la hacen ideal para una amplia gama de aplicaciones, desde scripts simples hasta sistemas empresariales complejos.

#### Conclusión

La comprensión y el uso efectivo de 'request' son habilidades esenciales para cualquier desarrollador Python que trabaje con HTTP y APIs web, Esta biblioteca no solo facilita la realización de tareas relacionadas con la red, sino que también ayuda a escribir código más limpio y mantenible.

---

Codigo: **get**

```python
#!/usr/bin/env python3

import os, requests

os.system('cls' if os.name == "nt" else "clear")

values = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

response = requests.get("https://httpbin.org/get", params=values)

print(f"\n[+] URL Final: {response.url}\n")
print(response.text)
```

---

Codigo: **post**

```python
#!/usr/bin/env python3

import os, requests

os.system('cls' if os.name == "nt" else "clear")

payload = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

response = requests.post("https://httpbin.org/post", data=payload)

print(f"\n[+] URL Final: {response.url}\n")
print(response.text)
```

---

Codigo: **tiempo de espera y manejo de excepciones**

```python
#!/usr/bin/env python3
import os, requests

os.system("cls" if os.name == "nt" else "clear")

try:
    response = requests.get("https://google.es", timeout=1)
    response.raise_for_status()

except requests.Timeout:
    print(f"\n[!] La petición ha excedido el límite de tiempo de espera")

except requests.HTTPError as http_err:
    print(f"\n[!] El tipo de error fue {http_err}")

except requests.RequestException as err:
    print(f"[!] Error: {err}")

else:
    print(f"[+] No ha habido ningun error en la solicitud")
```

---

Codigo: **recorriendo user-agent**

```python
#!/usr/bin/env python3

import os, requests

os.system("cls" if os.name == "nt" else "clear")

response = requests.get("https://httpbin.org/get")
data = response.json()

if 'headers' in data and 'User-Agent' in data['headers']:
    user_agent = data['headers']['User-Agent']
    print(f"\n[+]User-Agent: {user_agent}\n")
else:
    print(f"\n[!] No existe este campo en la respuesta\n")
```

### Librería requests (2/2)

#### Curiosidades y Aspectos Complementarios de requests

* **Orígenes y Popularidad**: requests fue creada por Kenneth Reitz en 2011. Su diseño enfocado en la simplicidad y la legibilidad rápidamente la convirtió en una de las bibliotecas más populares en Python. Su lema es “HTTP for Humans“, reflejando su objetivo de hacer las solicitudes HTTP accesibles y fáciles para los desarrolladores.
* **Comunidad y Contribuciones**: requests es un proyecto de código abierto y ha recibido contribuciones de numerosos desarrolladores. Esto asegura su constante actualización y adaptación a las nuevas necesidades y estándares de la web.
* **Inspiración en Otros Lenguajes**: El diseño de requests se inspira en otras bibliotecas HTTP de alto nivel de otros lenguajes de programación, buscando combinar lo mejor de cada uno para crear una experiencia de usuario óptima en Python.
* **Extensibilidad**: Aunque requests es poderosa por sí sola, su funcionalidad se puede ampliar con varios complementos. Esto incluye adaptadores para diferentes tipos de autenticación, soporte para servicios como AWS, o herramientas para aumentar su rendimiento.
* **Uso en la Educación y la Industria**: Debido a su simplicidad y potencia, requests se ha convertido en una herramienta de enseñanza estándar para la programación de red en Python. Además, es ampliamente utilizada en la industria para desarrollar aplicaciones que requieren comunicación con servicios web.
* **Casos de Uso Diversos**: Desde la automatización de tareas y el scraping web hasta el testing y la integración con APIs, requests tiene un rango de aplicaciones muy amplio. Su versatilidad la hace adecuada tanto para proyectos pequeños como para aplicaciones empresariales a gran escala.
* **Soporte para Proxies y Timeouts**: requests ofrece un control detallado sobre aspectos como proxies y timeouts, lo cual es crucial en entornos de producción donde la gestión del tráfico de red y la eficiencia son importantes.
* **Manejo Eficiente de Excepciones**: Proporciona una forma clara y consistente de manejar errores de red y HTTP, lo que ayuda a los desarrolladores a escribir aplicaciones más robustas y confiables.

En resumen, requests no solo es una biblioteca de alto nivel para solicitudes HTTP en Python, sino que también es un ejemplo brillante de diseño de software y colaboración comunitaria. Su facilidad de uso, junto con su potente funcionalidad, la convierte en una herramienta indispensable para cualquier desarrollador que trabaje con Python en el ámbito de la web.

---

Codigo: **Autenticacion libreria requests**

```python
#!/usr/bin/env python3

import os, requests

from requests.auth import HTTPBasicAuth

os.system("cls" if os.name == "nt" else "clear")

response_uno = requests.get("https://httpbin.org/basic-auth/foo/bar", auth=HTTPBasicAuth('foo', 'foo'))
response_dos = requests.get("https://httpbin.org/basic-auth/foo/bar", auth=('foo', 'bar'))

print(response_uno.text)
print(f"[!] Código de error: {response_uno.status_code} -> No autenticado\n")

print(response_dos.text)
print(response_dos.status_code)
```

---

Codigo: **cookies requests**

```python
#!/usr/bin/env python3

import os, requests
os.system("cls" if os.name == "nt" else "clear")

cookies = dict(cookies_are = "working")

response_uno = requests.get("https://httpbin.org/cookies", cookies=cookies)

print(cookies)
print(response_uno.text)
```

---

Codigo: **subir archivo mediante post con libreria requests**

```python
#!/usr/bin/env python3

import os, requests
os.system("cls" if os.name == "nt" else "clear")

url = "https://httpbin.org/post"
my_file = {'archivo': open('file.txt', 'r')}

response = requests.post(url, files=my_file)

print(response.text)
```

---

Codigo: **manteniendo sesion de cookies con requests**

```python
#!/usr/bin/env python3

import os, requests
os.system("cls" if os.name == "nt" else "clear")

url = "https://httpbin.org/cookies"
set_cookies_url = "https://httpbin.org/cookies/set/my_cookie/1234"

s =requests.session()

response = s.get(set_cookies_url)
response = s.get(url)
print(response.text)
```

```python
#!/usr/bin/env python3

import os
from requests import Request, Session
os.system("cls" if os.name == "nt" else "clear")

url = "https://httpbin.org/get"
s = Session()
headers = {"Custom-Header":"my_custom_header"}

req = Request('GET', url, headers=headers)

prepped = req.prepare()

prepped.headers['Custom-Header'] = 'my_header_changed'
prepped.headers['Another-Header'] = 'this_is_another_changed'
response = s.send(prepped)

print(response.text)
```

```python
#!/usr/bin/env python3

import os, requests

os.system("cls" if os.name == "nt" else "clear")

url = "http://github.com"

r = requests.get(url) # Para forzar a ir al sitio de arriba y no lo cambie por https

for request in r.history:
    print(f"{request.url}:{request.status_code}")

print(r.url)
print(r.history)
```

```python
#!/usr/bin/env python3

import os, requests

os.system("cls" if os.name == "nt" else "clear")

url = "http://github.com"

with requests.Session() as session:

    session.auth = ("foo", "bar")

    response1 = session.get("https://httpbin.org/basic-auth/foo/bar")
    print(response1.text)

    response2 = session.get("https://httpbin.org/get")
    print(response2.text)
```

### Librería Urllib3

‘urllib3‘ es una biblioteca de Python ampliamente utilizada para realizar solicitudes HTTP y HTTPS. Es conocida por su robustez y sus numerosas características, que la hacen una herramienta versátil para una variedad de aplicaciones de red. A continuación, se presenta una descripción detallada de ‘urllib3‘ y sus capacidades.

#### Descripción Detallada de la Biblioteca urllib3

#### **Funcionalidades Clave**

* **Gestión de Pool de Conexiones**: Una de las características más destacadas de ‘urllib3‘ es su manejo de pools de conexiones, lo que permite reutilizar y mantener conexiones abiertas. Esto es eficiente en términos de rendimiento, especialmente cuando se hacen múltiples solicitudes al mismo host.
* **Soporte para Solicitudes HTTP y HTTPS**: ‘urllib3‘ ofrece un soporte sólido para realizar solicitudes tanto HTTP como HTTPS, brindando la flexibilidad necesaria para trabajar con una variedad de servicios web.
* **Reintentos Automáticos y Redirecciones**: Viene con un sistema incorporado para manejar reintentos automáticos y redirecciones, lo cual es esencial para mantener la robustez de las aplicaciones en entornos de red inestables.
* **Manejo de Diferentes Tipos de Autenticación**: Proporciona soporte para varios esquemas de autenticación, incluyendo la autenticación básica y digest, lo que la hace apta para interactuar con una amplia gama de APIs y servicios web.
* **Soporte para Características Avanzadas del HTTP**: Incluye soporte para características como la compresión de contenido, el streaming de solicitudes y respuestas, y la manipulación de cookies, ofreciendo así un control detallado sobre las operaciones de red.
* **Gestión de SSL/TLS**: ‘urllib3‘ tiene capacidades avanzadas para manejar la seguridad SSL/TLS, incluyendo la posibilidad de trabajar con certificados personalizados y la verificación de la conexión segura.
* **Tratamiento de Excepciones y Errores**: La biblioteca maneja de manera eficiente las excepciones y errores, permitiendo a los desarrolladores gestionar situaciones como tiempos de espera, conexiones fallidas y errores de protocolo.

#### Aplicaciones y Uso

‘urllib3‘ se utiliza en una variedad de contextos, desde scraping web y automatización de tareas, hasta la construcción de clientes para interactuar con APIs complejas. Su capacidad para manejar conexiones de manera eficiente y segura la hace adecuada para aplicaciones que requieren un alto grado de interacción de red, así como para escenarios donde el rendimiento y la fiabilidad son cruciales.

#### Importancia en el Ecosistema de Python

Si bien existen otras bibliotecas como ‘requests‘ que son más amigables para principiantes, ‘urllib3‘ se destaca por su control detallado y su rendimiento en situaciones que requieren un manejo más profundo de las conexiones de red. Es una biblioteca fundamental para desarrolladores que buscan un control más granular sobre sus operaciones HTTP/HTTPS en Python.

* **Agregando al campo data con Urllib3**

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

http = urllib3.PoolManager() # Controlador de conexiones
# body = data
# field = form
data = "Esto es una prueba"
data = {"clave":"valor"}

#encoded_data = data.encode()# Se agrega al campo data
encoded_data = json.dumps(data).encode()
response = http.request('POST', 'https://httpbin.org/post', body=encoded_data)
print(response.data.decode())

```

---

Codigo: **Agregando un form con Urllib3**

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

http = urllib3.PoolManager() # Controlador de conexiones

response = http.request("POST", "https://httpbin.org/post", fields={"atributo":"valor"})
print(response.data.decode())
```

---

Codigo: **Estamos agregando body y header**

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

http = urllib3.PoolManager() # Controlador de conexiones

data =  {"atributo":"valor"}
encoded_data = json.dumps(data).encode()

response = http.request("POST", "https://httpbin.org/post", body=encoded_data, headers={"Content-Type":"application/jsssson"})
print(response.data.decode())
```

---

Codigo: **Creando nueva cabecera**

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

http = urllib3.PoolManager() # Controlador de conexiones

response = http.request("GET", "https://httpbin.org/get", headers={"NuevaCabecera":"Se tensa"})
print(response.data.decode())
```

---

Codigo: **Redireccionamiento con urllib3**

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

http = urllib3.PoolManager() # Controlador de conexiones

response = http.request("GET", "https://httpbin.org/redirect/1", redirect=False)
print(response.status)

print(f"Estamos siendo redirigidos a: {response.get_redirect_location()}")
```

---

Codigo: ****

```python
#!/usr/bin/env python3
import os, urllib3, json

os.system("cls" if os.name == "nt" else "clear")

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning) para evitar warnings ssl
http = urllib3.PoolManager() # Controlador de conexiones

response = http.request("GET", "https://httpbin.org/redirect/1", redirect=False)
print(response.status)

print(f"Estamos siendo redirigidos a: {response.get_redirect_location()}")
```

### Librería threading y multiprocesing

Las bibliotecas ‘threading‘ y ‘multiprocessing‘ en Python son herramientas esenciales para la programación concurrente y paralela. Proporcionan mecanismos para ejecutar múltiples tareas simultáneamente, aprovechando mejor los recursos del sistema. A continuación, se presenta una descripción detallada de ambas bibliotecas y sus diferencias.

#### Descripción Detallada de threading y multiprocessing

#### Biblioteca threading

‘threading‘ es una biblioteca para la programación concurrente que permite a los programas ejecutar múltiples ‘hilos‘ de ejecución al mismo tiempo. Los hilos son entidades más ligeras que los procesos, comparten el mismo espacio de memoria y son ideales para tareas que requieren poco procesamiento o que están limitadas por E/S.

* **Uso Principal**: Ideal para tareas que no son intensivas en CPU o que esperan recursos (como E/S de red o de archivos).
* **Ventajas**: Bajo costo de creación y cambio de contexto, compartición eficiente de memoria y recursos entre hilos.
* **Desventajas**: Limitada por el Global Interpreter Lock (GIL) en CPython, que previene la ejecución de múltiples hilos de Python al mismo tiempo en un solo proceso.

#### Biblioteca multiprocessing

‘multiprocessing‘, por otro lado, se enfoca en la creación de procesos. Cada proceso en multiprocessing tiene su propio espacio de memoria. Esto significa que pueden ejecutarse en paralelo real en sistemas con múltiples núcleos de CPU, superando la limitación del GIL.

* **Uso Principal**: Ideal para tareas intensivas en CPU que requieren paralelismo real.
* **Ventajas**: Capacidad para realizar cálculos intensivos en paralelo, aprovechando múltiples núcleos de CPU.
* **Desventajas**: Mayor costo en recursos y complejidad en la comunicación entre procesos debido a espacios de memoria separados.

#### Diferencias Clave

* **Modelo de Ejecución**: ‘threading‘ ejecuta hilos en un solo proceso compartiendo el mismo espacio de memoria, mientras ‘multiprocessing‘ ejecuta múltiples procesos con memoria independiente.
* **Uso de CPU**: ‘multiprocessing‘ es más adecuado para tareas que requieren mucho cálculo y pueden beneficiarse de múltiples núcleos de CPU, mientras que ‘threading‘ es mejor para tareas limitadas por E/S.
* **Global Interpreter Lock (GIL)**: ‘threading‘ está limitado por el GIL en CPython, lo que restringe la ejecución en paralelo de hilos, mientras que ‘multiprocessing‘ no tiene esta limitación.
* **Gestión de Recursos**: ‘threading‘ es más eficiente en términos de memoria y creación de hilos, pero ‘multiprocessing‘ es más eficaz para tareas aisladas y seguras en cuanto a datos.

#### Conclusión threading y multiprocesing

Entender y utilizar adecuadamente ‘threading‘ y ‘multiprocessing‘ es crucial para optimizar aplicaciones Python, especialmente en términos de rendimiento y eficiencia. La elección entre ambas depende de las necesidades específicas de la tarea, como el tipo de carga de trabajo (CPU-intensiva vs E/S-intensiva) y los requisitos de arquitectura de la aplicación.

---

Codigo: **Ejemplo de uso de libreria threading**

```python
#!/usr/bin/env python3
import os, threading, time
os.system("cls" if os.name == "nt" else "clear")

def tarea(num_tarea):
    print(f"\n[+] Hilo {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Hilo {num_tarea} finalizando")

thread1 = threading.Thread(target=tarea, args=(1,)) # target=funcion, args=el valor que mandemos, recibe tuplas, en caso de un valor considerar la coma ','
thread2 = threading.Thread(target=tarea, args=(2,)) # target=funcion, args=el valor que mandemos, recibe tuplas, en caso de un valor considerar la coma ','

thread1.start() # Corremos los dos hilos en paralelo
thread2.start() # Corremos los dos hilos en paralelo

thread2.join() # Esperamos que los hilos finalizen
thread1.join() # Esperamos que los hilos finalizen

print(f"\n[+] Los hilos han finalizado exitosamente")
```

---

Codigo: **Ejemplo de uso de libreria multiprocesing**

```python
#!/usr/bin/env python3
import os, multiprocessing, time
os.system("cls" if os.name == "nt" else "clear")

def tarea(num_tarea):
    print(f"\n[+] Proceso {num_tarea} iniciando")
    time.sleep(2)
    print(f"\n[+] Proceso {num_tarea} finalizando")


if __name__ == '__main__':
    
    proceso1 = multiprocessing.Process(target=tarea, args=(1,))
    proceso2 = multiprocessing.Process(target=tarea, args=(2,))

    proceso1.start()
    proceso2.start()

    proceso1.join()
    proceso2.join()

    print(f"\n[+] Los hilos han finalizado exitosamente")
```

---

Codigo: **Ejemplo de solicitud a paginas web sin emplear hilos**

```python
#!/usr/bin/env python3
import os, requests, threading, time
os.system("cls" if os.name == "nt" else "clear")

dominios = ["https://google.es", "https://xvideos.com", "https://wikipedia.org", "https://yahoo.com"]

start_time = time.time()

for url in dominios:
    response = requests.get(url)
    print(f"[+] URL [{url}]: {len(response.content)} bytes\n")

end_time = time.time()

print(f"[+] Tiempo total transcurrido: {end_time - start_time}")
```

---

Codigo: **empleando hilos threading**

```python
#!/usr/bin/env python3
import os, requests, threading, time
os.system("cls" if os.name == "nt" else "clear")

def realizar_peticion(url):
    response = requests.get(url)
    print(f"[+] URL [{url}]: {len(response.content)} bytes\n")

dominios = ["https://google.es", "https://xvideos.com", "https://wikipedia.org", "https://yahoo.com"]

start_time = time.time()

hilos = []
for url in dominios:
    hilo = threading.Thread(target=realizar_peticion, args=(url,))
    hilo.start()
    hilos.append(hilo)

for hilo in hilos:
    hilo.join()

end_time = time.time()

print(f"[+] Tiempo total transcurrido: {end_time - start_time}")
```

---

Codigo: **Ejemplo con multiprocessing**

```python
#!/usr/bin/env python3
import os, requests, multiprocessing, time
os.system("cls" if os.name == "nt" else "clear")

def realizar_peticion(url):
    response = requests.get(url)
    print(f"[+] URL [{url}]: {len(response.content)} bytes\n")

dominios = ["https://google.es", "https://xvideos.com", "https://wikipedia.org", "https://yahoo.com"]

if __name__ == "__main__":

    start_time = time.time()

    procesos = []
    for url in dominios:
        proceso = multiprocessing.Process(target=realizar_peticion, args=(url,))
        proceso.start()
        procesos.append(proceso)

    for proceso in procesos:
        proceso.join()

    end_time = time.time()

    print(f"[+] Tiempo total transcurrido: {end_time - start_time}")
```

## Desarrollo de aplicaciones de escritorio con Python

### Introducción a las interfaces gráficas de usuario (GUI)

Tkinter es una biblioteca estándar de Python para la creación de interfaces gráficas de usuario (GUI). Es una interfaz de programación para ‘Tk‘, un toolkit de GUI que es parte de Tcl/Tk. Tkinter es notable por su simplicidad y eficiencia, siendo ampliamente utilizado en aplicaciones de escritorio y herramientas educativas.

#### ¿Por qué Tkinter?

* **Facilidad de Uso**: Tkinter es amigable para principiantes. Su estructura sencilla y clara lo hace ideal para aprender los conceptos básicos de la programación de GUI.
* **Portabilidad**: Las aplicaciones creadas con Tkinter pueden ejecutarse en diversos sistemas operativos sin necesidad de modificar el código.
* **Amplia Disponibilidad**: Al ser parte de la biblioteca estándar de Python, Tkinter está disponible por defecto en la mayoría de las instalaciones de Python, lo que elimina la necesidad de instalaciones adicionales.

En esta sección del curso, nos sumergiremos en el mundo de Tkinter, empezando con una introducción detallada que nos permitirá entender y utilizar sus múltiples funcionalidades. A través de proyectos prácticos, aplicaremos estos conocimientos para construir desde aplicaciones simples hasta interfaces más complejas, proporcionando una base sólida para cualquiera interesado en el desarrollo de GUI con Python.

### Desarrollo de aplicaciones GUI con Tkinter (1/8)

#### Tkinter: Explorando Componentes Clave

1 tk.Label

* **Descripción**: ‘tk.Label‘ es un widget en Tkinter utilizado para mostrar texto o imágenes. El texto puede ser estático o actualizarse dinámicamente.
* **Uso Común**: Se usa para añadir etiquetas informativas en una GUI, como títulos, instrucciones o información de estado.
* **Características Clave**:
    **text**: Para establecer el texto que se mostrará.
    **font**: Para personalizar la tipografía.
    **bg y fg**: Para establecer el color de fondo (bg) y de texto (fg).
    **image**: Para mostrar una imagen.
    **wraplength**: Para especificar a qué ancho el texto debería envolverse.

2 mainloop()

* **Descripción**: ‘mainloop()‘ es una función esencial en Tkinter que ejecuta el bucle de eventos de la aplicación. Este bucle espera eventos, como pulsaciones de teclas o clics del mouse, y los procesa.
* **Importancia**: Sin ‘mainloop()‘, la aplicación GUI no responderá a eventos y parecerá congelada. Es lo que mantiene viva la aplicación.

3 pack()

* **Descripción**: ‘pack()‘ es un método de geometría usado para colocar widgets en una ventana.
* **Funcionalidad**: Organiza los widgets en bloques antes de colocarlos en la ventana. Los widgets se “empaquetan” en el orden en que se llama a ‘pack()‘.
* **Características Clave**:
    **side**: Para especificar el lado de la ventana donde se ubicará el widget (por ejemplo, top, bottom, left, right).
    **fill**: Para determinar si el widget se expande para llenar el espacio disponible.
    **expand**: Para permitir que el widget se expanda para ocupar cualquier espacio adicional en la ventana.

4 grid()

* **Descripción**: ‘grid()‘ es otro método de geometría utilizado en Tkinter para colocar widgets.
* **Funcionalidad**: Organiza los widgets en una cuadrícula. Se especifica la fila y la columna donde debe ir cada widget.
    **Características Clave**:
        **row y column**: Para especificar la posición del widget en la cuadrícula.
        **rowspan y columnspan**: Para permitir que un widget ocupe múltiples filas o columnas.
        **sticky**: Para determinar cómo se alinea el widget dentro de su celda (por ejemplo, N, S, E, W).

#### Conclusión de tkinter 1/8

Estos componentes de Tkinter (tk.Label, mainloop(), pack(), grid()) son fundamentales para la creación de aplicaciones GUI eficientes y atractivas. Comprender su funcionamiento y saber cómo implementarlos adecuadamente es crucial para cualquier desarrollador que busque crear interfaces de usuario interactivas y funcionales con Python y Tkinter.

---

Codigo: **Ejemplo con pack()**

```python

#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

def accion_de_boton():
    os.system("cls" if os.name == "nt" else "clear")
    print("[+] Se ha presionado el botón\n")
    
# Para representar widgets en las ventanas hay tres métodos, pack(), grid(), place()

root = tk.Tk() # Instanciamos el objeto raiz para crear la ventana
root.title("YOU HAVE BEEN PWND HAHAHA") # Establecemos el titulo de la ventana

label1 = tk.Label(root, text="Hola mundo", bg="blue") # Se crea la etiqueta
label1.pack(fill=tk.X) # fill=tk.X es para que el widget ocupe todo el espacio sobre x

label2 = tk.Label(root, text="Etiqueta 2", bg="red")
label2.pack(fill=tk.X)

label3 = tk.Label(root, text="Etiqueta 3", bg="green")
label3.pack(side=tk.LEFT, fill=tk.Y) # side es para establecer de que lado se posicionará y con fill decimos que ocupará todo el eje Y

label4 = tk.Label(root, text="Etiqueta 4", bg="yellow")
label4.pack(side=tk.RIGHT, fill=tk.Y) # side es para establecer de que lado se posicionará y con fill decimos que ocupará todo el eje Y

label5 = tk.Label(root, text="Etiqueta 5", bg="violet")
label5.pack(side=tk.BOTTOM, fill=tk.Y) # side es para establecer de que lado se posicionará y con fill decimos que ocupará todo el eje Y

button1 = tk.Button(root, text="Présioname y verás como se tensa", command=accion_de_boton) # command = accion que queremos llevar acabo con el boton
button1.pack()

root.mainloop()
```

---

Codigo: **Ejemplo con grid()**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

def accion_de_boton():
    os.system("cls" if os.name == "nt" else "clear")
    print("[+] Se ha presionado el botón\n")
    
# Para representar widgets en las ventanas hay tres métodos, pack(), grid(), place()

root = tk.Tk() # Instanciamos el objeto raiz para crear la ventana
root.title("YOU HAVE BEEN PWND HAHAHA") # Establecemos el titulo de la ventana

label1 = tk.Label(root, text="Hola mundo", bg="blue") # Se crea la etiqueta
label2 = tk.Label(root, text="Etiqueta 2", bg="red")
label3 = tk.Label(root, text="Esta es una prueba de texto en etiqueta de tkinter", bg="green")
label4 = tk.Label(root, text="Etiqueta 4", bg="yellow")
label5 = tk.Label(root, text="Etiqueta 5", bg="violet")
button1 = tk.Button(root, text="Présioname y verás como se tensa", command=accion_de_boton) # command = accion que queremos llevar acabo con el boton

label1.grid(row=0, column=0) # lo posiciona arriba a la izquierda
label2.grid(row=0, column=1) # lo posiciona arriba a la derecha
label3.grid(row=1, column=0, columnspan=2) # 

root.mainloop()
```

### Desarrollo de aplicaciones GUI con Tkinter (2/8)

#### Tkinter: Profundizando en Componentes y Gestión de Layout

1. place()

    Descripción: ‘place()‘ es un método de gestión de geometría en Tkinter que permite posicionar widgets en ubicaciones específicas mediante coordenadas x-y.
    Características Clave:
        ‘x’ y ‘y’: Especifican la posición del widget en términos de coordenadas.
        width y height: Definen el tamaño del widget.
        anchor: Determina desde qué punto del widget se aplican las coordenadas (por ejemplo, ‘nw‘ para esquina superior izquierda).
        Posiciones Relativas: Se pueden utilizar valores relativos (por ejemplo, ‘relx‘, ‘rely‘) para posicionar widgets en relación con el tamaño de la ventana, lo que hace que la interfaz sea más adaptable al cambiar el tamaño de la ventana.

2. tk.Entry()

    Descripción: ‘tk.Entry()‘ es un widget en Tkinter que permite a los usuarios introducir una línea de texto.
    Uso Común: Ideal para campos de entrada de texto como nombres de usuario, contraseñas, etc.
    Funcionalidades Clave:
        get(): Para obtener el texto del campo de entrada.
        delete(): Para borrar texto del campo de entrada.
        insert(): Para insertar texto en una posición específica.

3. tk.Button()

    Descripción: ‘tk.Button()‘ es un widget que los usuarios pueden presionar para realizar una acción.
    Uso Común: Ejecutar una función o comando cuando se hace clic en él.
    Características Clave:
        text: Define el texto que aparece en el botón.
        command: Establece la función que se llamará cuando se haga clic en el botón.

4. geometry()

    Descripción: ‘geometry()‘ es una función que define las dimensiones y la posición inicial de la ventana principal.
    Funcionalidad: Permite especificar el tamaño y la ubicación de la ventana en el formato ‘ancho x alto + X + Y‘.
    Importancia: Es fundamental para establecer el tamaño inicial de la ventana y su posición en la pantalla.

5. tk.Text()

    Descripción: ‘tk.Text()‘ es un widget que permite la entrada y visualización de múltiples líneas de texto.
    Uso Común: Ideal para campos de texto más extensos, como áreas de comentarios, editores de texto, etc.
    Funcionalidades Clave:
        Similar a ‘tk.Entry()‘, pero diseñado para manejar texto de varias líneas.
        Permite funciones como copiar, pegar, seleccionar texto.

Conclusión

Estos componentes y funciones (place(), tk.Entry(), tk.Button(), geometry(), tk.Text()) son esenciales en la construcción de interfaces de usuario ricas y funcionales con Tkinter. Proporcionan la flexibilidad necesaria para crear aplicaciones GUI interactivas y atractivas, adaptándose a una amplia gama de necesidades de diseño de interfaz.

---

Codigo: **Ejemplo con place()**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

def accion_de_boton():
    os.system("cls" if os.name == "nt" else "clear")
    print("[+] Se ha presionado el botón\n")
    
# Para representar widgets en las ventanas hay tres métodos, pack(), grid(), place()

root = tk.Tk() # Instanciamos el objeto raiz para crear la ventana
root.title("YOU HAVE BEEN PWND HAHAHA") # Establecemos el titulo de la ventana

label1 = tk.Label(root, text="Hola mundo", bg="blue") # Se crea la etiqueta
label2 = tk.Label(root, text="Etiqueta 2", bg="red")
label3 = tk.Label(root, text="Esta es una prueba", bg="green")
label4 = tk.Label(root, text="Etiqueta 4", bg="yellow")
label5 = tk.Label(root, text="Etiqueta 5", bg="violet")
button1 = tk.Button(root, text="Présioname y verás como se tensa", command=accion_de_boton) # command = accion que queremos llevar acabo con el boton

label1.place(x=20, y=20) # lo posiciona arriba a la izquierda
label2.place(relx=0.8, rely=0.2) # lo posiciona arriba a la derecha
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # 

root.mainloop()
```

---

Codigo: **Ejemplo para crear la geometria de la ventana**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

root = tk.Tk()
root.title("YOU HAVE BEEN PWND HAHAHA")
root.geometry("480x240") # Creamos la proporcion de la ventana

label1 = tk.Label(root, text="Hola mundo", bg="blue")
label2 = tk.Label(root, text="Etiqueta 2", bg="red")
label3 = tk.Label(root, text="Esta es una prueba", bg="green")
label1.place(x=20, y=20)
label2.place(relx=0.8, rely=0.2)
label3.place(relx=0.5, rely=0.5, anchor=tk.CENTER) # 

root.mainloop()
```

---

Codigo: **Ejemplo entry()**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

def get_data():
    os.system("cls" if os.name == "nt" else "clear")
    data = entry1.get()
    print(f"\n[+] Datos introducidos por el usuario: {data}")

root = tk.Tk()
root.geometry("480x240")
root.title("Entry() Widget -> YOU WILL BE PWND")

entry1 = tk.Entry(root)
entry1.pack(pady=25, padx=15, fill=tk.Y) # Con relacion al borde superior

buton1 = tk.Button(root, text="Recoger datos de entrada", command=get_data)
buton1.pack(padx=15, fill=tk.X)

root.mainloop()
```

---

Codigo: **Ejemplo con text()**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

def get_data(*args):
    os.system("cls" if os.name == "nt" else "clear")
    data = entry1.get("3.0", tk.END) # 3.0 hace referencia a que de la fila 3 en adelante leera los datos, tk.END hace referencia hasta el final
    print(f"\n[+] Datos introducidos por el usuario: {data}")

root = tk.Tk()
root.geometry("720x480")
root.title("Entry() Widget -> YOU WILL BE PWND")

entry1 = tk.Text(root)
entry1.pack(pady=15, padx=15, fill=tk.X) # Con relacion al borde superior

buton1 = tk.Button(root, text="Recoger datos de entrada", command=get_data)
buton1.pack(padx=15, fill=tk.X)

root.mainloop()
```

### Desarrollo de aplicaciones GUI con Tkinter (3/8)

Tkinter: Explorando Widgets Avanzados y Funcionalidades de Diálogo

1. Frame()

    Descripción: ‘Frame()‘ es un widget en Tkinter utilizado como contenedor para otros widgets.
    Uso Común: Organizar el layout de la aplicación, agrupando widgets relacionados.
    Características Clave:
        Actúa como un contenedor invisible que puede contener otros widgets.
        Útil para mejorar la organización y la gestión del layout en aplicaciones complejas.

2. Canvas()

    Descripción: ‘Canvas()‘ es un widget que proporciona un área para dibujar gráficos, líneas, figuras, etc.
    Funciones de Dibujo:
        create_oval(): Crea figuras ovales o círculos. Los parámetros especifican las coordenadas del rectángulo delimitador.
        create_rectangle(): Dibuja rectángulos. Los parámetros definen las coordenadas de las esquinas.
        create_line(): Permite dibujar líneas. Se especifican las coordenadas de inicio y fin de la línea.
    Uso Común: Crear gráficos, interfaces de juegos, o elementos visuales personalizados.

3. Menu()

    Descripción: ‘Menu()‘ se utiliza para crear menús en una aplicación Tkinter.
    Uso Común: Añadir barras de menús con opciones como ‘Archivo‘, ‘Editar‘, ‘Ayuda‘, etc.
    Características Clave:
        Se pueden crear menús desplegables y menús contextuales.
        Los menús pueden contener comandos, opciones de selección y otros submenús.

4. messagebox

    Descripción: ‘messagebox‘ es un módulo en Tkinter que proporciona ventanas emergentes de diálogo.
    Funciones Comunes:
        showinfo(), showwarning(), showerror(): Muestran mensajes informativos, de advertencia y de error, respectivamente.
    Uso Común: Informar al usuario sobre eventos, confirmaciones, errores o advertencias.

5. filedialog

    Descripción: ‘filedialog‘ es un módulo que ofrece diálogos para seleccionar archivos y directorios.
    Funciones Clave:
        askopenfilename(): Abre un cuadro de diálogo para seleccionar un archivo para abrir.
        asksaveasfilename(): Abre un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo para guardar.
        askdirectory(): Permite al usuario seleccionar un directorio.
    Uso Común: Integrar la funcionalidad de apertura y guardado de archivos en aplicaciones.

Conclusión

El dominio de estos widgets y módulos (Frame(), Canvas(), Menu(), messagebox, filedialog) es crucial para desarrollar aplicaciones GUI interactivas y completas en Tkinter. Cada uno aporta funcionalidades específicas que permiten crear interfaces de usuario más ricas y dinámicas, adaptadas a una amplia variedad de necesidades.

---

Codigo: **frame**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

root = tk.Tk()
root.title("FRAMES IN TKINTER")
root.geometry("720x480")

frame1 = tk.Frame(root, bg="blue", bd=5)
frame1.place(relx=0.5, rely=0.5,anchor=tk.CENTER)

label1 = tk.Label(frame1, text="Label1", bg="green")
label2 = tk.Label(frame1, text="Label2", bg="red")
label1.pack(fill=tk.X)
label2.pack(fill=tk.X)

root.mainloop()
```

---

Codigo: **canva**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

root = tk.Tk()
root.title("CANVAS IN TKINTER")
root.geometry("720x480")

canvas1 = tk.Canvas(root, width=480, height=240, bg="white")
canvas1.pack(pady=15)

oval = canvas1.create_oval(50, 50,150,150,fill="red")
rect = canvas1.create_rectangle(300, 50, 450, 100, fill="green")
line = canvas1.create_line(50, 100, 100,220,fill="blue")

root.mainloop()
```

---

Codigo: **menu con messagebox**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import messagebox

os.system("cls" if os.name == "nt" else "clear")

root = tk.Tk()
root.title("MENU IN TKINTER")
root.geometry("720x480")

def accion_menu():
    messagebox.showinfo("menu","Menu se ha tensado la cosa")

barra_menu = tk.Menu(root) # Creamos la barra de menu
root.config(menu=barra_menu) # Incorporamos la barra a la ventana

menu1 = tk.Menu(barra_menu, tearoff=0) # Agregamos la primera opcion a la barra
barra_menu.add_cascade(label="Menu", menu=menu1) # Mostramos menu1 dentro de la barra

menu1.add_command(label="Opcion 1") # Agregamos submenus al menu
menu1.add_command(label="Opcion 2") # Agregamos submenus al menu 

menu2 = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Extras", menu=menu2)
menu2.add_command(label="Se tensa")
menu2.add_command(label="Se tensa de lo lindo", command=accion_menu)

root.mainloop()
```

---

Codigo: **menu con filedialog y un boton**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import filedialog

os.system("cls" if os.name == "nt" else "clear")

root = tk.Tk()
root.title("MENU IN TKINTER")
root.geometry("240x120")

def abrir_archivo():
    ruta_archivo = filedialog.askopenfilename()
    print(f"\n[+] Ruta absoluta del archivo: {ruta_archivo}")

boton = tk.Button(root, text="Abrir archivo", command=abrir_archivo)
boton.pack(pady=20)

root.mainloop()
```

### Desarrollo de aplicaciones GUI con Tkinter (4/8)

En esta clase, abordaremos un proyecto que consolidará todo lo aprendido hasta ahora en Tkinter: la creación de nuestro propio editor de texto, similar al Bloc de Notas.

Este será un excelente ejercicio para aplicar nuestras habilidades en un contexto práctico y realista, permitiéndonos ver cómo los componentes individuales de Tkinter se unen para formar una aplicación funcional.

Nuestro editor de texto incluirá funcionalidades básicas como:

* Crear un nuevo archivo
* Abrir y editar archivos existentes
* Guardar los cambios
* Cerrar la aplicación

Para esto, haremos uso de varios widgets y técnicas de Tkinter que hemos estudiado, como ‘tk.Text‘ para el área de edición, ‘Menu()‘ para la barra de menús y ‘filedialog‘ para la gestión de archivos.

Adoptaremos un enfoque de Programación Orientada a Objetos (POO) en este proyecto. Utilizaremos clases para estructurar nuestro código, lo que nos permitirá dividir la funcionalidad de la aplicación en bloques lógicos y reutilizables. Este método no solo facilitará la organización y gestión del código, sino que también nos proporcionará una sólida base para el mantenimiento y la escalabilidad futura del proyecto.

Este proyecto no solo nos permitirá practicar la integración de los diferentes componentes y módulos de Tkinter, sino que también nos dará la oportunidad de experimentar con el diseño de interfaces de usuario y el manejo de archivos de texto.

### Desarrollo de aplicaciones GUI con Tkinter (5/8)

En esta clase, continuaremos con nuestro proyecto del editor de texto, con el objetivo de finalizarlo. Hasta ahora, hemos logrado implementar funciones clave como la creación, edición, guardado y apertura de archivos de texto. En esta sesión, nos enfocaremos en pulir nuestra aplicación, asegurándonos de que todas las funcionalidades trabajen de manera fluida y eficiente.

Una vez que hayamos completado y perfeccionado nuestro editor de texto, daremos un paso adelante en nuestro aprendizaje con el inicio de un nuevo y fascinante proyecto: la creación de una calculadora con interfaz gráfica interactiva. Este proyecto nos permitirá aplicar y expandir aún más nuestros conocimientos en Tkinter, abordando nuevos desafíos y explorando diferentes aspectos de la creación de GUIs.

En la calculadora, implementaremos funciones básicas como:

* Sumar
* Restar
* Multiplicar
* Dividir

Así como una interfaz de usuario intuitiva que permita a los usuarios interactuar fácilmente con la aplicación. Este proyecto no solo reforzará nuestras habilidades en Tkinter y la programación orientada a objetos, sino que también nos brindará la oportunidad de abordar problemas de lógica de programación y diseño de interfaces de usuario.

Con estos dos proyectos, nuestro editor de texto y la calculadora, estaremos no solo consolidando nuestros conocimientos teóricos, sino también ganando experiencia práctica valiosa en el desarrollo de aplicaciones de escritorio con Python y Tkinter. Estos proyectos nos servirán como excelentes ejemplos de lo que podemos lograr y serán una base sólida para futuros proyectos más complejos.

---

Codigo: **app de notas**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import filedialog, messagebox
os.system("cls" if os.name == "nt" else "clear")

class SimpleTextEditor:
    def __init__(self, root):
        self.root = root
        self.text_area = tk.Text(self.root)
        self.text_area.pack(fill=tk.BOTH, expand=1)
        self.current_open_file = ""

    def new_file(self):
        self.text_area.delete("1.0", tk.END)
        self.current_open_file = ""
    
    def open_file(self):
        filename = filedialog.askopenfilename()

        if filename:
            self.text_area.delete("1.0", tk.END)
            with open(filename, "r") as file:
                self.text_area.insert("1.0", file.read())

            self.current_open_file = filename

    def save_file(self):
        if not self.current_open_file:
            new_file_path = filedialog.asksaveasfilename()

            if new_file_path:
                self.current_open_file = new_file_path
            else:
                return
            
        with open(self.current_open_file, "w") as file:
            file.write(self.text_area.get("1.0", tk.END))

    def quit_confirm(self):
        if messagebox.askokcancel("Salir", "Estas seguro que deseas salir?"): # Me devuelve True o False por consola
            self.root.destroy()
       
root = tk.Tk()
root.title("Aplicacion de toma de nota")
root.geometry("700x500")

editor = SimpleTextEditor(root)

menu_bar = tk.Menu(root)
menu_options = tk.Menu(menu_bar, tearoff=0)

menu_options.add_command(label="Nuevo", command=editor.new_file)
menu_options.add_command(label="Abrir", command=editor.open_file)
menu_options.add_command(label="Guardar", command=editor.save_file)
menu_options.add_command(label="Salir", command=editor.quit_confirm)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Archivo", menu=menu_options)

root.mainloop()
```

### Desarrollo de aplicaciones GUI con Tkinter (6/8)

En esta clase, seguiremos avanzando con nuestro proyecto de la calculadora con interfaz gráfica. Nos enfocaremos en perfeccionar la funcionalidad y el diseño de la aplicación, asegurando que cada elemento opere de manera efectiva y que la interfaz sea intuitiva y atractiva.

Esta sesión nos brinda la oportunidad de aplicar de manera práctica nuestros conocimientos en Tkinter y la programación orientada a objetos, avanzando hacia la finalización de nuestro proyecto.

### Desarrollo de aplicaciones GUI con Tkinter (7/8)

En esta clase, seguiremos avanzando con nuestro proyecto de la calculadora con interfaz gráfica. Nos enfocaremos en perfeccionar la funcionalidad y el diseño de la aplicación, asegurando que cada elemento opere de manera efectiva y que la interfaz sea intuitiva y atractiva.

Esta sesión nos brinda la oportunidad de aplicar de manera práctica nuestros conocimientos en Tkinter y la programación orientada a objetos, avanzando hacia la finalización de nuestro proyecto.

### Desarrollo de aplicaciones GUI con Tkinter (8/8)

En esta clase, damos por concluido nuestro emocionante proyecto de la calculadora con interfaz gráfica. Esta sesión representa no solo la culminación de nuestro trabajo en este proyecto específico, sino también la consolidación de las habilidades y conocimientos que hemos adquirido y desarrollado a lo largo de las clases anteriores.

Durante esta sesión final, haremos una revisión exhaustiva de nuestro proyecto, asegurándonos de que todas las funcionalidades estén trabajando sin problemas y que la interfaz de usuario sea tan intuitiva y atractiva como lo planeamos. Será el momento de hacer los ajustes finales, resolver cualquier problema pendiente y posiblemente añadir algunas características adicionales que puedan enriquecer aún más nuestra aplicación.

También dedicaremos tiempo a reflexionar sobre el proceso de desarrollo, discutiendo lo que aprendimos, los desafíos que enfrentamos y cómo los superamos. Esta discusión será valiosa para entender mejor nuestras experiencias de aprendizaje y cómo podemos aplicar estos conocimientos en proyectos futuros.

Al final de la clase, celebraremos el logro de haber creado una calculadora funcional y bien diseñada desde cero, utilizando Tkinter y los principios de la programación orientada a objetos. Este proyecto no solo ha fortalecido nuestras habilidades técnicas, sino que también ha mejorado nuestra capacidad de pensamiento crítico y resolución de problemas en el ámbito del desarrollo de software.

* **Ver el manual de ASCII para saber los eventos de teclado**

---

Codigo: **Calculadora**

```python
#!/usr/bin/env python3
import os
import tkinter as tk
os.system("cls" if os.name == "nt" else "clear")

class Calculadora:
    def __init__(self, master):
        self.master = master
        self.display = tk.Entry(master, width=15, font=("Arial", 23), bd=10, insertwidth=1, bg="#6495d3", justify="right")
        self.display.grid(row=0, column=0, columnspan=4)
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0

        row = 1
        col = 0

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        for button in buttons:
            self.build_button(button, row, col)
            col += 1

            if col > 3:
                col = 0
                row += 1

        self.master.bind("<Key>", self.key_press) # Detecta el teclado

    def key_press(self, event):
        key = event.char
        if key == "\r":
            self.calculate()
            return
        elif key == "\x08":
            self.clear_display
            return
        elif key == "\x1b":
            self.master.quit()
            return

        self.click(key)

    def clear_display(self):
        self.display.delete(0, tk.END)
        self.op_verification = False
        self.current = ""
        self.op = ""
        self.total = 0
    
    def calculate(self):
        if self.current and self.op:
            if self.op == "/":
                self.total /= float(self.current)
            if self.op == "*":
                self.total *= float(self.current)
            if self.op == "+":
                self.total += float(self.current)
            if self.op == "-":
                self.total -= float(self.current)

        self.display.delete(0, "end")
        self.display.insert("end", round(self.total,3))
    
    def click(self, button):
        if self.op_verification:
            self.op_verification = False

        self.display.insert("end", button)

        if button in "0123456789" or button == ".":
            self.current += button
        else:
            if self.current:
                if not self.op:
                    self.total = float(self.current)
            
            self.current = ""

            self.op_verification = True
            self.op = button

        print(f"\n[+] Has presionado: {button}")
        print(f"[+] La primera combinacion es: {self.current}")
        print(f"[+] Status op_verification: {self.op_verification}")
        print(f"[+] Tipo de operacion que deseo efectuar: {self.op}")
        print(f"[+] Total: {self.total}")


    def build_button(self, button, row, col):
        if button == "C":
            b = tk.Button(self.master, text=button, width=8, command= lambda: self.clear_display())
        elif button == "=":
            b = tk.Button(self.master, text=button, width=8, command=lambda: self.calculate())
        else:
            b = tk.Button(self.master, text=button, width=8, command=lambda: self.click(button))

        b.grid(row=row, column=col)

       
root = tk.Tk()
root.title("Aplicacion de toma de calculadora")

my_gui = Calculadora(root)

root.mainloop()
```

### Desarrollo de aplicaciones GUI avanzado con CustomTkinter

CustomTkinter es una extensión de la conocida biblioteca Tkinter de Python, diseñada para facilitar la creación de interfaces gráficas de usuario (GUI) con un estilo más moderno y personalizable. A continuación, te detallo sus características y diferencias con respecto a Tkinter tradicional:

#### **Características de CustomTkinter**

* **Estilo Moderno y Personalizable**: CustomTkinter ofrece widgets con un diseño más moderno y atractivo en comparación con los estándares de Tkinter. Estos widgets pueden personalizarse ampliamente en términos de colores, formas y efectos visuales.
* **Facilidad de Uso**: Mantiene la simplicidad y facilidad de uso de Tkinter, permitiendo a los desarrolladores crear interfaces gráficas de manera intuitiva, pero con un aspecto visual más atractivo y profesional.
* **Compatibilidad**: Es compatible con el código Tkinter existente, lo que permite a los desarrolladores mejorar las interfaces de aplicaciones existentes sin necesidad de reescribir todo desde cero.
* **Widgets Mejorados**: Incluye versiones mejoradas de los widgets estándar de Tkinter, como botones, etiquetas, campos de texto, etc., con mejoras en la interactividad y el diseño.

#### **Diferencias con Tkinter**

* **Diseño Visual**: La diferencia más notable es el estilo visual. CustomTkinter proporciona un aspecto más moderno y elegante, mientras que Tkinter tiene un aspecto más tradicional y básico.
* **Personalización de Widgets**: CustomTkinter permite una mayor personalización en la apariencia de los widgets, como temas oscuros, bordes redondeados, y efectos de animación, que no están disponibles directamente en Tkinter estándar.
* **Facilidad de Transición**: Aunque CustomTkinter es una extensión, los desarrolladores familiarizados con Tkinter encontrarán la transición suave, ya que muchos de los conceptos y estructuras son similares.
* **Comunidad y Soporte**: Tkinter, al ser una biblioteca más antigua y establecida, tiene una comunidad más grande y una amplia gama de recursos y documentación. CustomTkinter, siendo más nuevo, está en proceso de crecimiento en términos de comunidad y recursos disponibles.

En resumen, CustomTkinter se posiciona como una excelente opción para los desarrolladores que buscan mejorar la estética y la funcionalidad de sus interfaces gráficas en Python, manteniendo al mismo tiempo la simplicidad y la familiaridad de Tkinter.

### Chat Multiusuario con GUI y Cifrado E2E (1/5)

En esta clase, nos enfocaremos en construir un chat multiusuario desde cero, utilizando conceptos avanzados como threading y socket para gestionar la comunicación en tiempo real. Se empleará Tkinter para crear una interfaz gráfica intuitiva, permitiendo a varios usuarios conectarse y conversar de manera efectiva.

A lo largo de la clase, aprenderemos cómo estas herramientas pueden ser integradas para desarrollar una aplicación de chat robusta y funcional, explorando tanto la programación de back-end como de front-end para una experiencia de usuario completa.

### Chat Multiusuario con GUI y Cifrado E2E (2/5)

En esta clase, nos enfocaremos en construir un chat multiusuario desde cero, utilizando conceptos avanzados como threading y socket para gestionar la comunicación en tiempo real. Se empleará Tkinter para crear una interfaz gráfica intuitiva, permitiendo a varios usuarios conectarse y conversar de manera efectiva.

A lo largo de la clase, aprenderemos cómo estas herramientas pueden ser integradas para desarrollar una aplicación de chat robusta y funcional, explorando tanto la programación de back-end como de front-end para una experiencia de usuario completa.

### Chat Multiusuario con GUI y Cifrado E2E (3/5)

En esta clase, nos enfocaremos en construir un chat multiusuario desde cero, utilizando conceptos avanzados como threading y socket para gestionar la comunicación en tiempo real. Se empleará Tkinter para crear una interfaz gráfica intuitiva, permitiendo a varios usuarios conectarse y conversar de manera efectiva.

A lo largo de la clase, aprenderemos cómo estas herramientas pueden ser integradas para desarrollar una aplicación de chat robusta y funcional, explorando tanto la programación de back-end como de front-end para una experiencia de usuario completa.

### Chat Multiusuario con GUI y Cifrado E2E (4/5)

En esta clase, nos enfocaremos en construir un chat multiusuario desde cero, utilizando conceptos avanzados como threading y socket para gestionar la comunicación en tiempo real. Se empleará Tkinter para crear una interfaz gráfica intuitiva, permitiendo a varios usuarios conectarse y conversar de manera efectiva.

A lo largo de la clase, aprenderemos cómo estas herramientas pueden ser integradas para desarrollar una aplicación de chat robusta y funcional, explorando tanto la programación de back-end como de front-end para una experiencia de usuario completa.

### Chat Multiusuario con GUI y Cifrado E2E (5/5)

En esta etapa final, daremos los toques finales a nuestro chat multiusuario, centrándonos en la seguridad y privacidad de las conversaciones. Utilizaremos la librería SSL y herramientas como OpenSSL para implementar un cifrado robusto.

Aprenderemos cómo integrar estas tecnologías en nuestro chat para asegurar que las comunicaciones entre usuarios sean seguras y privadas. Esta sesión es crucial para entender la importancia del cifrado en aplicaciones de mensajería y cómo aplicarlo efectivamente en proyectos reales.

A continuación, se proporcionan los comandos utilizados en la clase:

* **openssl genpkey -algorithm RSA -out server-key.key -aes256**

Esta instrucción genera una nueva clave privada RSA. La opción ‘-algorithm RSA‘ especifica el uso del algoritmo RSA. ‘-out server-key.key‘ indica que la clave generada se guardará en un archivo llamado ‘server-key.key‘. La opción ‘-aes256‘ significa que la clave privada será cifrada usando el algoritmo AES-256, lo que añade una capa de seguridad al requerir una contraseña para acceder a la clave.

* **openssl req -new -key server-key.key -out server.csr**

Esta línea crea una nueva Solicitud de Firma de Certificado (CSR) utilizando la clave privada RSA que generaste. ‘-new‘ indica que se trata de una nueva solicitud, ‘-key server-key.key‘ especifica que se usará la clave privada almacenada en ‘server-key.key‘, y ‘-out server.csr‘ guarda la CSR generada en un archivo llamado ‘server.csr‘. La CSR es necesaria para solicitar un certificado digital a una Autoridad Certificadora (CA).

* **openssl x509 -req -days 365 -in server.csr -signkey server-key.key -out server-cert.pem**

Este comando genera un certificado autofirmado basado en la CSR. ‘-req‘ indica que se está procesando una CSR, ‘-days 365‘ establece la validez del certificado por un año, ‘-in server.csr‘ especifica la CSR de entrada, ‘-signkey server-key.key‘ utiliza la misma clave privada para firmar el certificado, y ‘-out server-cert.pem‘ guarda el certificado generado en un archivo llamado ‘server-cert.pem‘.

* **openssl rsa -in server-key.key -out server-key.key**

Este comando se utiliza para quitar la contraseña de una clave privada RSA protegida. ‘-in server-key.key‘ especifica el archivo de la clave privada cifrada como entrada, y ‘-out server-key.key‘ indica que la clave privada sin cifrar se guardará en el mismo archivo. Al ejecutar este comando, se te pedirá la contraseña actual de la clave privada. Una vez proporcionada, OpenSSL generará una versión sin cifrar de la clave privada y la guardará en el mismo archivo, sobrescribiendo la versión cifrada.

Este paso se hace a menudo para simplificar la automatización en entornos donde ingresar una contraseña manualmente no es práctico. Sin embargo, es importante ser consciente de que al eliminar la contraseña, la clave privada se vuelve más vulnerable al acceso no autorizado.

---

Codigo: **server.py**

```python
#!/usr/bin/env python3

import socket, threading
import tkinter as tk

def client_thread(client_socket, clients, usernames):

    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username

    print(f"\n[+] El usuario {username} se ha conectado al chat")

    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] El usuario {username} ha entrado al chat\n\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message == "!usuarios":
                client_socket.sendall(f"\n[+] Listado de usuarios disponibles: {', '.join(usernames.values())}\n\n".encode())
                continue
            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break
    
    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]

def server_program():

    host = "localhost"
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen()

    print(f"\n[+] El servidor esta en escucha de conexiones entrantes...")

    clients = []
    usernames = {}

    while True:

        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        print(f"\n[+] Se ha conectado un nuevo cliente: {address}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()
    
    server_socket.close()

if __name__ == "__main__" :
    server_program()
```

---

Codigo: **client.py**

```python
#!/usr/bin/env python3

import socket, threading
from tkinter import * 
from tkinter.scrolledtext import ScrolledText

def send_message(client_socket, username, text_widget, entry_widget):
    message = entry_widget.get()
    client_socket.sendall(f"{username} > {message}".encode())

    entry_widget.delete(0, END)
    text_widget.configure(state="normal")
    text_widget.insert(END, f"{username} > {message}\n")
    text_widget.configure(state="disable")


def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            text_widget.configure(state="normal")
            text_widget.insert(END, message)
            text_widget.configure(state="disable")

        except:
            break

def list_users_request(client_socket):
    client_socket.sendall("!usuarios".encode())

def exit_request(client_socket, username, window):

    client_socket.sendall(f"\n[!] El usuario ha abandonado el chat\n".encode())
    client_socket.close()

    window.quit()
    window.destroy()

def client_program():

    host = "localhost"
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    username = input(f"\n[+] Introduce tu usuario: ")
    client_socket.sendall(username.encode())

    window = Tk()
    window.title("Chat")

    text_widget = ScrolledText(window, state="disabled")
    text_widget.pack(padx=5, pady=5)

    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=2, fill=BOTH, expand=1)

    entry_widget = Entry(frame_widget, font=("Arial", 14))
    entry_widget.bind("<Return>", lambda _: send_message( client_socket, username, text_widget, entry_widget))
    entry_widget.pack(side=LEFT, fill=X, expand=1)

    button_widget = Button(frame_widget, text="Enviar", command=lambda: send_message( client_socket, username, text_widget, entry_widget))
    button_widget.pack(padx=5, pady=5, side=RIGHT)

    users_widget = Button(window, text="Listar usuarios", command=lambda: list_users_request(client_socket))
    users_widget.pack(padx=5, pady=5)

    exit_widget = Button(window, text="Salir", command=lambda: exit_request(client_socket, username, window))
    exit_widget.pack(padx=5, pady=5)

    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()

    window.mainloop()
    client_socket.close()

if __name__ == "__main__":
    client_program()
```
