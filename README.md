# Guardians of the Ancient Kingdom

## 1. Descripción del proyecto

**Guardians of the Ancient Kingdom** es un proyecto desarrollado en Python que simula combates entre personajes de un reino fantástico. Su objetivo es aplicar los principios de la programación orientada a objetos (POO) mediante clases, herencia, encapsulamiento, abstracción y polimorfismo.

El sistema cuenta con tres tipos de personajes: guerrero, mago y arquero. Cada uno tiene atributos y una habilidad de ataque propia. Los combates se desarrollan por turnos hasta que se determina un ganador o se produce un empate.

## 2. Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

```text
Guardians-of-the-Ancient-Kingdom/
├── personajes.py
├── main.py
└── README.md
```

- **`personajes.py`:** contiene las clases de los personajes, sus validaciones, las habilidades de ataque y la clase encargada de gestionar los combates.
- **`main.py`:** crea los personajes, ejecuta las pruebas de validación y habilidades, y comprueba el funcionamiento del sistema de combate.
- **`README.md`:** documenta el proyecto, su organización y su funcionamiento.

## 3. Clases del proyecto

### 3.1. Clase `Personaje`

Es la clase base abstracta de la que heredan los diferentes tipos de personajes. Define los atributos y comportamientos comunes.

**Atributos:**
- `nombre`: nombre del personaje.
- `vida`: puntos de vida actuales.
- `ataque`: valor de ataque del personaje.
- `defensa`: valor de defensa del personaje.

**Métodos principales:**
- `atacar(objetivo)`: método abstracto que cada subclase implementa según su habilidad.
- `recibir_danio(cantidad)`: aplica el daño recibido sin permitir que la vida sea negativa y devuelve el daño efectivo.
- `esta_vivo()`: comprueba si el personaje conserva puntos de vida.
- `mostrar_estado()`: muestra los atributos y el estado actual del personaje.

Los atributos se controlan mediante propiedades con validaciones para impedir valores no permitidos.

### 3.2. Clase `Guerrero`

Hereda de `Personaje` y aplica una bonificación del 20 % a su ataque antes de restar la defensa del objetivo.

**Cálculo del daño:**

`daño = máximo entre 0 y la parte entera de (ataque × 1.20 − defensa del objetivo)`

### 3.3. Clase `Mago`

Hereda de `Personaje`. Su habilidad consiste en infligir un daño igual a su valor de ataque, ignorando la defensa del objetivo.

**Cálculo del daño:**

`daño = ataque del mago`

### 3.4. Clase `Arquero`

Hereda de `Personaje`. Si su ataque supera la defensa del objetivo, inflige el doble de la diferencia entre ambos valores. Si no supera la defensa, no causa daño.

**Cálculo del daño:**

- Si `ataque > defensa`: `daño = 2 × (ataque − defensa)`.
- En caso contrario: `daño = 0`.

### 3.5. Clase `Combate`

Se encarga de administrar el enfrentamiento entre dos personajes.

**Atributos principales:**
- `personaje1` y `personaje2`: participantes del combate.
- `turno_actual`: personaje al que le corresponde actuar.
- `ganador`: personaje ganador, cuando existe.
- `empate`: indica si el combate terminó en empate.
- `rondas`: cantidad de rondas transcurridas.

**Métodos principales:**
- `iniciar()`: ejecuta el combate por turnos y determina su resultado.
- `cambiar_turno()`: alterna el personaje que debe actuar.
- `verificar_ganador()`: comprueba si el combate ha terminado y determina el resultado.
- `mostrar_resultado()`: muestra al ganador o informa del empate.

La clase comprueba que los participantes sean personajes válidos y evita que un personaje combata contra sí mismo.

## 4. Conceptos de programación orientada a objetos

### Abstracción

La clase `Personaje` representa las características comunes de todos los personajes sin definir una única forma de atacar. El método `atacar()` es abstracto porque cada tipo de personaje debe implementar su propio comportamiento.

En cambio, `recibir_danio()` está implementado en la clase base porque todos los personajes comparten las mismas reglas para recibir daño y reducir sus puntos de vida.

### Herencia

Las clases `Guerrero`, `Mago` y `Arquero` heredan los atributos, las validaciones y los métodos comunes de `Personaje`. Cada subclase especializa el comportamiento de ataque.

### Encapsulamiento

Los atributos se administran mediante propiedades y validaciones que controlan los valores asignados. Esto permite mantener la consistencia del estado de cada personaje.

### Polimorfismo

El método `atacar()` tiene una implementación diferente en cada subclase. La clase `Combate` puede solicitar un ataque sin tener que implementar por separado las reglas de cada tipo de personaje.

### Relaciones entre las clases

- **Herencia:** `Guerrero`, `Mago` y `Arquero` heredan de `Personaje`.
- **Asociación:** `Combate` interactúa con los participantes para ejecutar ataques, consultar su estado y determinar el resultado.
- **Agregación:** los personajes se crean fuera de `Combate` y se pasan como argumentos a su constructor. La clase de combate utiliza esos objetos sin crearlos directamente.

## 5. Reglas del sistema

### Validaciones de los atributos

- **Nombre:** debe ser un texto no vacío.
- **Vida:** debe ser un número entero entre 0 y 100.
- **Ataque:** debe ser un número entero positivo.
- **Defensa:** debe ser un número entero no negativo.

El daño recibido debe ser un entero no negativo. La vida nunca puede disminuir por debajo de cero y el método `recibir_danio()` devuelve el daño que efectivamente se pudo aplicar.

Además, un personaje derrotado no puede atacar y los personajes no pueden atacarse a sí mismos.

### Reglas del combate

1. El combate recibe dos personajes válidos.
2. Los participantes alternan sus turnos, comenzando por el primer personaje.
3. Cada personaje realiza como máximo un ataque por ronda.
4. Después de cada ataque se muestra el estado de ambos participantes.
5. El combate termina cuando se determina que un personaje ha sido derrotado.
6. Se produce un empate técnico cuando ambos personajes completan una ronda sin causar daño.
7. El combate tiene un límite máximo de 50 rondas. Si se alcanza sin determinar un ganador, termina en empate.

## 6. Ejecución del proyecto

### Requisitos

- Tener Python 3 instalado.
- No se requieren bibliotecas externas para ejecutar el proyecto.

### Instrucciones

1. Colocar `personajes.py` y `main.py` en la misma carpeta.
2. Abrir una terminal en esa carpeta.
3. Ejecutar el siguiente comando:

```bash
python main.py
```
o

```bash
python3 main.py
```

El programa ejecutará las pruebas definidas en `main.py`, mostrará los resultados de las validaciones y habilidades, y realizará los combates de prueba. Al finalizar correctamente, mostrará el mensaje de que todas las pruebas terminaron satisfactoriamente.

## 7. Pruebas realizadas

Las pruebas incluidas en `main.py` comprueban los siguientes comportamientos:

- Creación válida de personajes.
- Rechazo de nombres, vidas, ataques y defensas inválidos.
- Funcionamiento de las propiedades y el encapsulamiento.
- Cálculo del daño de cada tipo de personaje.
- Rechazo del daño negativo y control de la vida mínima.
- Restricciones para atacar a personajes derrotados o a uno mismo.
- Rechazo de objetivos y participantes inválidos.
- Detección del ganador y finalización del combate.
- Detección de empates técnicos.
- Detección de un ganador cuando uno de los participantes ya está derrotado al comenzar.

Las pruebas se ejecutan desde `main.py` y utilizan comprobaciones para verificar los resultados esperados.

## 8. Conclusión

El proyecto permite aplicar los principios fundamentales de la programación orientada a objetos mediante un sistema de combate que organiza los personajes en clases relacionadas entre sí. La herencia evita duplicar comportamientos comunes, el encapsulamiento permite validar los atributos, la abstracción define una estructura compartida y el polimorfismo permite que cada personaje ataque de acuerdo con sus propias reglas.

El resultado es un sistema organizado, validado y extensible que cumple el propósito de practicar la programación orientada a objetos en Python.
