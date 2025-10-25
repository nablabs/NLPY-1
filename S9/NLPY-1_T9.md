# Tarea Guiada: Calculadora con Tkinter

## Objetivo
Aprender a crear interfaces gráficas en Python usando **tkinter**, construyendo paso a paso una calculadora funcional.

---

## ¿Qué es Tkinter?

**Tkinter** es la biblioteca estándar de Python para crear interfaces gráficas (GUI). Es fácil de usar y viene incluida con Python, ¡no necesitas instalar nada adicional!

### Conceptos básicos:
- **Ventana (Window)**: La ventana principal de tu aplicación
- **Widgets**: Los elementos visuales (botones, etiquetas, campos de texto, etc.)
- **Grid/Pack**: Métodos para organizar los widgets en la ventana

---

## Paso 1: Crear la Ventana Principal

Empecemos creando una ventana vacía. Este es el primer paso para cualquier aplicación con tkinter.

```python
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

# Iniciar el loop de la aplicación
ventana.mainloop()
```

### ¿Qué hace este código?
- `tk.Tk()`: Crea la ventana principal
- `title()`: Establece el título que aparece en la barra superior
- `geometry()`: Define el tamaño de la ventana (ancho x alto)
- `resizable(False, False)`: Impide que el usuario cambie el tamaño
- `mainloop()`: Mantiene la ventana abierta esperando interacciones

**Ejecuta este código y verás una ventana vacía. ¡Tu primera GUI!**

---

## Paso 2: Agregar la Pantalla de la Calculadora

Ahora vamos a agregar una pantalla donde se mostrarán los números y resultados.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

# Variable para almacenar la expresión matemática
expresion = ""

# Función para actualizar la expresión
def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

# Variable de texto para la pantalla
texto_pantalla = tk.StringVar()

# Crear la pantalla (Entry)
pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

ventana.mainloop()
```

### ¿Qué hace este código?
- `expresion = ""`: Variable global que guarda lo que el usuario escribe
- `StringVar()`: Tipo especial de tkinter para manejar texto dinámico
- `Entry()`: Widget de campo de texto (nuestra pantalla)
  - `textvariable`: Conecta el Entry con texto_pantalla
  - `font`: Define la fuente y tamaño del texto
  - `bd`: Grosor del borde
  - `width`: Ancho del campo
  - `justify='right'`: Alinea el texto a la derecha
- `grid()`: Coloca el widget usando un sistema de cuadrícula
  - `row=0, column=0`: Posición (fila 0, columna 0)
  - `columnspan=4`: El widget ocupa 4 columnas
- `actualizar_expresion()`: Función que agrega valores a la expresión

**Ejecuta el código. Ahora verás una pantalla, pero aún no puedes escribir en ella.**

---

## Paso 3: Crear los Botones Numéricos

Vamos a crear los botones del 0 al 9. Usaremos un bucle para no repetir código.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

texto_pantalla = tk.StringVar()

pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Crear botones numéricos
botones_numeros = []
posiciones = [
    (1, 0), (1, 1), (1, 2),  # 7, 8, 9
    (2, 0), (2, 1), (2, 2),  # 4, 5, 6
    (3, 0), (3, 1), (3, 2),  # 1, 2, 3
]

# Crear botones del 1 al 9
for i, (fila, columna) in enumerate(posiciones):
    numero = 9 - i  # Empezar desde 9 y bajar
    if i < 3:
        numero = 7 + i  # Primera fila: 7, 8, 9
    elif i < 6:
        numero = 4 + (i - 3)  # Segunda fila: 4, 5, 6
    else:
        numero = 1 + (i - 6)  # Tercera fila: 1, 2, 3
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)
    botones_numeros.append(boton)

# Botón 0 (más ancho)
boton_0 = tk.Button(ventana, text="0", font=('Arial', 18), 
                   width=11, height=2,
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
```

### ¿Qué hace este código?
- **Lista de posiciones**: Define dónde va cada botón (fila, columna)
- `Button()`: Crea un botón
  - `text`: El texto que muestra el botón
  - `font`: Fuente y tamaño
  - `width` y `height`: Dimensiones del botón
  - `command`: Función que se ejecuta al hacer clic
- `lambda x=numero`: Función anónima que captura el valor del número
  - Sin `lambda`, todos los botones tendrían el mismo valor
  - `x=numero` "congela" el valor actual en cada iteración
- El botón 0 tiene `columnspan=2` para ser más ancho

**Ejecuta el código. Ahora puedes hacer clic en los números y verlos en la pantalla.**

---

## Paso 4: Agregar Operadores Matemáticos

Ahora agregaremos los botones para sumar, restar, multiplicar y dividir.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

texto_pantalla = tk.StringVar()

pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botones numéricos
posiciones = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_0 = tk.Button(ventana, text="0", font=('Arial', 18), 
                   width=11, height=2,
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botones de operadores
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

ventana.mainloop()
```

### ¿Qué hace este código?
- **Lista de operadores**: Tuplas con (símbolo_visual, operador_real)
  - '÷' se muestra, pero se guarda '/' (que Python entiende)
  - '×' se muestra, pero se guarda '*'
- Los operadores se colocan en la **columna 3** (la última)
- `row=i+1`: Empieza desde la fila 1 (fila 0 es la pantalla)

**Ejecuta el código. Ahora puedes escribir operaciones como "7+5" o "9×3".**

---

## Paso 5: Implementar el Botón de Igual (=)

Este es el botón más importante: calcula el resultado de la expresión.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

# Función para calcular el resultado
def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
        expresion = resultado
    except:
        texto_pantalla.set("ERROR")
        expresion = ""

texto_pantalla = tk.StringVar()

pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botones numéricos
posiciones = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_0 = tk.Button(ventana, text="0", font=('Arial', 18), 
                   width=11, height=2,
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botones de operadores
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

# Botón de igual
boton_igual = tk.Button(ventana, text="=", font=('Arial', 18), 
                       width=5, height=2,
                       command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

ventana.mainloop()
```

### ¿Qué hace este código?
- `calcular()`: Nueva función que hace la magia
  - `eval(expresion)`: Evalúa la expresión matemática como código Python
  - `try-except`: Maneja errores (como dividir por cero)
  - Si hay error, muestra "ERROR" y limpia la expresión
  - Si funciona, muestra el resultado y lo guarda (para seguir operando)
- El botón "=" llama a `calcular()` cuando se hace clic

**Nota sobre `eval()`**: En aplicaciones reales, `eval()` puede ser peligroso si evalúa código no confiable. Para una calculadora personal está bien.

**Ejecuta el código. ¡Ya puedes hacer cálculos! Prueba: 15+27, 100÷4, 6×7**

---

## Paso 6: Agregar el Botón de Limpiar (C)

Necesitamos una forma de borrar la pantalla y empezar de nuevo.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
        expresion = resultado
    except:
        texto_pantalla.set("ERROR")
        expresion = ""

# Función para limpiar la pantalla
def limpiar():
    global expresion
    expresion = ""
    texto_pantalla.set("")

texto_pantalla = tk.StringVar()

pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botones numéricos
posiciones = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_0 = tk.Button(ventana, text="0", font=('Arial', 18), 
                   width=11, height=2,
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Botones de operadores
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

boton_igual = tk.Button(ventana, text="=", font=('Arial', 18), 
                       width=5, height=2,
                       command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

# Botón de limpiar
boton_limpiar = tk.Button(ventana, text="C", font=('Arial', 18), 
                         width=5, height=2,
                         command=limpiar)
boton_limpiar.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()
```

### ¿Qué hace este código?
- `limpiar()`: Función simple que:
  - Resetea `expresion` a una cadena vacía
  - Limpia la pantalla (`texto_pantalla.set("")`)
- El botón "C" (Clear) se coloca en la fila 4, columna 3

**Ejecuta el código. Ahora puedes limpiar la pantalla con el botón C.**

---

## Paso 7: Agregar el Punto Decimal

Para hacer operaciones con decimales, necesitamos el punto (.).

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
        expresion = resultado
    except:
        texto_pantalla.set("ERROR")
        expresion = ""

def limpiar():
    global expresion
    expresion = ""
    texto_pantalla.set("")

texto_pantalla = tk.StringVar()

pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24), 
                    bd=10, insertwidth=4, width=14, justify='right')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botones numéricos
posiciones = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_0 = tk.Button(ventana, text="0", font=('Arial', 18), 
                   width=5, height=2,
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, padx=5, pady=5)

# Botón de punto decimal
boton_punto = tk.Button(ventana, text=".", font=('Arial', 18), 
                       width=5, height=2,
                       command=lambda: actualizar_expresion('.'))
boton_punto.grid(row=4, column=1, padx=5, pady=5)

# Botones de operadores
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18), 
                     width=5, height=2,
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

boton_igual = tk.Button(ventana, text="=", font=('Arial', 18), 
                       width=5, height=2,
                       command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

boton_limpiar = tk.Button(ventana, text="C", font=('Arial', 18), 
                         width=5, height=2,
                         command=limpiar)
boton_limpiar.grid(row=4, column=3, padx=5, pady=5)

ventana.mainloop()
```

### ¿Qué hace este código?
- Cambiamos el botón 0: ahora solo ocupa 1 columna (quitamos `columnspan`)
- Agregamos el botón "." en la fila 4, columna 1
- El punto se agrega a la expresión como cualquier otro carácter

**Ejecuta el código. Ahora puedes hacer operaciones como 3.14×2 o 10÷3**

---

## Paso 8: Mejorar el Diseño con Colores

Hagamos la calculadora más atractiva visualmente.

```python
import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)
ventana.configure(bg='#2b2b2b')  # Fondo oscuro

expresion = ""

def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
        expresion = resultado
    except:
        texto_pantalla.set("ERROR")
        expresion = ""

def limpiar():
    global expresion
    expresion = ""
    texto_pantalla.set("")

texto_pantalla = tk.StringVar()

# Pantalla con colores
pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24, 'bold'), 
                    bd=10, insertwidth=4, width=14, justify='right',
                    bg='#1a1a1a', fg='#00ff00', insertbackground='#00ff00')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Botones numéricos con estilo
posiciones = [
    (1, 0), (1, 1), (1, 2),
    (2, 0), (2, 1), (2, 2),
    (3, 0), (3, 1), (3, 2),
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18, 'bold'), 
                     width=5, height=2,
                     bg='#404040', fg='white', activebackground='#505050',
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

boton_0 = tk.Button(ventana, text="0", font=('Arial', 18, 'bold'), 
                   width=5, height=2,
                   bg='#404040', fg='white', activebackground='#505050',
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, padx=5, pady=5)

boton_punto = tk.Button(ventana, text=".", font=('Arial', 18, 'bold'), 
                       width=5, height=2,
                       bg='#404040', fg='white', activebackground='#505050',
                       command=lambda: actualizar_expresion('.'))
boton_punto.grid(row=4, column=1, padx=5, pady=5)

# Botones de operadores con color naranja
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18, 'bold'), 
                     width=5, height=2,
                     bg='#ff9500', fg='white', activebackground='#ffad33',
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

boton_igual = tk.Button(ventana, text="=", font=('Arial', 18, 'bold'), 
                       width=5, height=2,
                       bg='#ff9500', fg='white', activebackground='#ffad33',
                       command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

boton_limpiar = tk.Button(ventana, text="C", font=('Arial', 18, 'bold'), 
                         width=5, height=2,
                         bg='#d4d4d2', fg='black', activebackground='#e8e8e6',
                         command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

ventana.mainloop()
```

### ¿Qué hace este código?
- `configure(bg='#2b2b2b')`: Fondo oscuro para la ventana
- **Pantalla**:
  - `bg='#1a1a1a'`: Fondo negro
  - `fg='#00ff00'`: Texto verde (estilo matriz)
  - `insertbackground`: Color del cursor
- **Botones numéricos**:
  - `bg='#404040'`: Fondo gris oscuro
  - `activebackground`: Color cuando se presiona
- **Operadores**: Color naranja (#ff9500) para destacar
- **Botón C**: Ahora es más grande (`columnspan=4`, `sticky='ew'`)
  - `sticky='ew'`: Se expande de este (east) a oeste (west)

**Ejecuta el código. ¡Ahora tu calculadora se ve profesional!**

---

## TAREA FINAL: Implementa una Funcionalidad Adicional

Ahora es tu turno de agregar una característica nueva. Aquí tienes **3 opciones** (elige una):

### Opción 1: Botón de Borrar (⌫)
Crea un botón que borre el último carácter ingresado (como la tecla backspace).

**Pistas**:
- Crea una función `borrar_ultimo()` que modifique `expresion`
- Usa `expresion[:-1]` para obtener todos los caracteres excepto el último
- Coloca el botón donde prefieras en el grid

### Opción 2: Botón de Porcentaje (%)
Crea un botón que convierta el número actual en porcentaje (divide entre 100).

**Pistas**:
- Crea una función `calcular_porcentaje()`
- Si la expresión es un número, divídelo entre 100
- Actualiza la pantalla con el resultado

### Opción 3: Botón de Cambio de Signo (+/-)
Crea un botón que cambie el signo del número actual (positivo ↔ negativo).

**Pistas**:
- Crea una función `cambiar_signo()`
- Si la expresión no empieza con '-', agrégalo
- Si ya empieza con '-', quítalo
- O mejor aún: multiplica por -1 el último número

---

## Requisitos de la Tarea Final

1. **Implementa UNA de las tres opciones** (o crea tu propia idea)
2. **Escribe comentarios** explicando qué hace tu código
3. **Prueba tu funcionalidad** para asegurarte de que funciona
4. **Aplica un color diferente** a tu nuevo botón para que destaque

### Ejemplo de estructura para tu solución:

```python
# Mi función personalizada
def mi_nueva_funcion():
    global expresion
    # Tu código aquí
    pass

# Mi nuevo botón
mi_boton = tk.Button(ventana, text="?", font=('Arial', 18, 'bold'), 
                    width=5, height=2,
                    bg='#color_elegido', fg='white',
                    command=mi_nueva_funcion)
mi_boton.grid(row=?, column=?, padx=5, pady=5)
```

---

## Lo que has aprendido

¡Felicidades! Has aprendido a:

- Crear ventanas con tkinter  
- Usar widgets (Entry, Button)  
- Organizar elementos con el sistema `grid()`  
- Manejar eventos con `command`  
- Usar variables globales y StringVar  
- Trabajar con funciones lambda  
- Personalizar colores y estilos  
- Crear una aplicación funcional completa  

---

## Tips Adicionales

### Para seguir mejorando tu calculadora:
- Agrega soporte para paréntesis
- Implementa un historial de operaciones
- Agrega funciones científicas (sin, cos, sqrt)
- Permite usar el teclado (con `bind()`)
- Guarda el historial en un archivo

### Recursos para aprender más:
- [Documentación oficial de tkinter](https://docs.python.org/3/library/tkinter.html)
- Prueba otras bibliotecas GUI: PyQt, Kivy, CustomTkinter
- Explora `ttk` (themed tkinter) para widgets más modernos

---

## ¡A programar!

Toma el código del **Paso 8** como base y agrega tu funcionalidad personalizada. Recuerda:
- **Experimenta**: No tengas miedo de probar cosas nuevas
- **Comenta tu código**: Ayuda a otros (y a ti mismo) a entenderlo
- **Prueba constantemente**: Ejecuta el código después de cada cambio
- **Diviértete**: La programación es creativa y divertida

**¡Buena suerte!**

---

## Código Final Completo

A continuación se presenta el código completo y funcional de la calculadora con todas las características implementadas:

```python
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Calculadora")
ventana.geometry("400x500")
ventana.resizable(False, False)
ventana.configure(bg='#2b2b2b')

# Variable global para almacenar la expresión matemática
expresion = ""

# Función para actualizar la expresión en la pantalla
def actualizar_expresion(valor):
    global expresion
    expresion += str(valor)
    texto_pantalla.set(expresion)

# Función para calcular el resultado
def calcular():
    global expresion
    try:
        resultado = str(eval(expresion))
        texto_pantalla.set(resultado)
        expresion = resultado
    except:
        texto_pantalla.set("ERROR")
        expresion = ""

# Función para limpiar la pantalla
def limpiar():
    global expresion
    expresion = ""
    texto_pantalla.set("")

# Variable de texto para la pantalla
texto_pantalla = tk.StringVar()

# Crear la pantalla de la calculadora
pantalla = tk.Entry(ventana, textvariable=texto_pantalla, font=('Arial', 24, 'bold'), 
                    bd=10, insertwidth=4, width=14, justify='right',
                    bg='#1a1a1a', fg='#00ff00', insertbackground='#00ff00')
pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Crear botones numéricos del 1 al 9
posiciones = [
    (1, 0), (1, 1), (1, 2),  # 7, 8, 9
    (2, 0), (2, 1), (2, 2),  # 4, 5, 6
    (3, 0), (3, 1), (3, 2),  # 1, 2, 3
]

for i, (fila, columna) in enumerate(posiciones):
    if i < 3:
        numero = 7 + i
    elif i < 6:
        numero = 4 + (i - 3)
    else:
        numero = 1 + (i - 6)
    
    boton = tk.Button(ventana, text=str(numero), font=('Arial', 18, 'bold'), 
                     width=5, height=2,
                     bg='#404040', fg='white', activebackground='#505050',
                     command=lambda x=numero: actualizar_expresion(x))
    boton.grid(row=fila, column=columna, padx=5, pady=5)

# Botón 0
boton_0 = tk.Button(ventana, text="0", font=('Arial', 18, 'bold'), 
                   width=5, height=2,
                   bg='#404040', fg='white', activebackground='#505050',
                   command=lambda: actualizar_expresion(0))
boton_0.grid(row=4, column=0, padx=5, pady=5)

# Botón de punto decimal
boton_punto = tk.Button(ventana, text=".", font=('Arial', 18, 'bold'), 
                       width=5, height=2,
                       bg='#404040', fg='white', activebackground='#505050',
                       command=lambda: actualizar_expresion('.'))
boton_punto.grid(row=4, column=1, padx=5, pady=5)

# Botones de operadores
operadores = [
    ('÷', '/'),
    ('×', '*'),
    ('-', '-'),
    ('+', '+'),
]

for i, (simbolo, operador) in enumerate(operadores):
    boton = tk.Button(ventana, text=simbolo, font=('Arial', 18, 'bold'), 
                     width=5, height=2,
                     bg='#ff9500', fg='white', activebackground='#ffad33',
                     command=lambda x=operador: actualizar_expresion(x))
    boton.grid(row=i+1, column=3, padx=5, pady=5)

# Botón de igual
boton_igual = tk.Button(ventana, text="=", font=('Arial', 18, 'bold'), 
                       width=5, height=2,
                       bg='#ff9500', fg='white', activebackground='#ffad33',
                       command=calcular)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

# Botón de limpiar
boton_limpiar = tk.Button(ventana, text="C", font=('Arial', 18, 'bold'), 
                         width=5, height=2,
                         bg='#d4d4d2', fg='black', activebackground='#e8e8e6',
                         command=limpiar)
boton_limpiar.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky='ew')

# Iniciar el loop principal de la aplicación
ventana.mainloop()
```

Este código está listo para ejecutar y contiene todas las funcionalidades básicas de una calculadora:
- Números del 0 al 9
- Operaciones básicas: suma (+), resta (-), multiplicación (×), división (÷)
- Punto decimal (.) para números decimales
- Botón de igual (=) para calcular resultados
- Botón de limpiar (C) para reiniciar
- Diseño moderno con colores personalizados
- Manejo de errores (muestra "ERROR" si la operación no es válida)

**¡Copia este código, ejecútalo y luego agrega tu funcionalidad personalizada!**
