# Autómata para validar una cadena de asignación de variable

Este es un autómata que valida si una cadena de texto corresponde a una asignación de variable en la siguiente forma: una secuencia de dígitos seguida de una letra, seguida de un signo igual, seguida de una cadena de texto entre comillas dobles.

## Definición del vocabulario

Para este autómata, se definen los siguientes conjuntos de caracteres:

- `digitos`: una secuencia de dígitos del 0 al 9.
- `signos`: el signo igual (`=`).
- `numeros`: una secuencia de dígitos del 0 al 9.

Se define el conjunto `digitosLetra` como la unión de los conjuntos `digitos` y `numeros`.

## Definición del autómata

El autómata consta de los siguientes estados:

- `state 0`: estado inicial, espera un dígito.
- `state 1`: espera una secuencia de dígitos y letras, seguida de un signo igual.
- `state 2`: espera el inicio de la cadena de texto, es decir, una comilla doble.
- `state 3`: espera una secuencia de letras y dígitos que conforman la cadena de texto.
- `state 4`: espera un carácter que forme parte de la cadena de texto o una comilla doble de cierre.
- `state 5`: estado final, la cadena de texto terminó.

## Funcionamiento del autómata

El autómata comienza en el `state 0` y espera un dígito. A partir de ahí, se va moviendo entre estados en función de los caracteres que va leyendo de la cadena de texto que se le pasa como entrada. Si en algún momento el autómata lee un carácter que no está permitido según las reglas del vocabulario, se detiene y devuelve un resultado negativo.

Si la cadena de entrada es válida, el autómata llegará al `state 5`, que indica que la cadena de texto está bien formada. En este punto, el autómata devuelve un resultado positivo y la cadena de texto validada.

## Uso del autómata

El autómata se puede utilizar mediante la función `runAutomata`, que toma como entrada una cadena de texto y devuelve un diccionario con los siguientes elementos:

- `resp`: un booleano que indica si la cadena es válida o no.
- `charRecorridos`: una cadena de texto que indica hasta qué punto el autómata recorrió la cadena de entrada antes de detenerse.
- `cadena`: la cadena de entrada.

A continuación se muestran algunos ejemplos de uso:

