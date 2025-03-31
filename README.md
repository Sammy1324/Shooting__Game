# Shooting__Game
https://github.com/Sammy1324/Shooting__Game.git
Desarrollo de un Juego de Disparos en Python utilizando Programación Orientada a Objetos (POO)

 

En este ejercicio, desarrollarás un juego utilizando Python, aplicando los principios de programación orientada a objetos (POO). El juego será un clásico juego de disparos, en el cual manejarás un personaje principal y deberás disparar a enemigos mientras esquivas sus disparos. El objetivo es convertir a los enemigos en estrellas y avanzar en el juego.

 

Estructura del proyecto

En este proyecto, modelarás cada uno de los elementos del juego como una clase en Python, siguiendo la estructura de clases que se describe a continuación:

Entity: Clase base que representa cada elemento del juego.
Character: Clase que representa cualquier personaje con vida dentro del juego. Hereda de la clase Entity.
Player: Clase que representa al jugador principal. Hereda de la clase Character.
Opponent: Clase que representa a los enemigos. Hereda de la clase Character.
Shot: Clase que representa los disparos realizados por un personaje (Player u Opponent). Hereda de la clase Entity.
Game: Clase principal que representa el juego en su totalidad.
 

Clases y Métodos a Implementar

Entity:
Métodos: move(), draw()
Atributos: x, y, image
Character (Hereda de Entity):
Métodos: move(), shoot(), collide()
Atributos: lives, is_alive
Player (Hereda de Character):
Métodos: move(), shoot()
Atributos: score, lives (inicialmente 3)
Opponent (Hereda de Character):
Métodos: move(), shoot()
Atributos: is_star (booleano que indica si ha sido convertido en estrella)
Shot (Hereda de Entity):
Métodos: move(), hit_target()
Game:
Métodos: start(), update(), end_game()
Atributos: score, player, opponent, is_running
 

 

 

3. ![image](https://github.com/user-attachments/assets/68ee5e93-9d26-4c64-8bf0-fd763b653266)



 

Requisitos

Debes implementar las siguientes funcionalidades en el juego:

 

Registro de Puntuación: Cada vez que el jugador convierta a un enemigo en estrella, debe incrementarse su puntuación.
 

Sistema de Vidas: El jugador debe tener 3 vidas. Si es alcanzado por un disparo enemigo, pierde una vida. El juego termina cuando las vidas llegan a 0.
 

Jefe Final: Si el jugador derrota a un enemigo, aparece un jefe final que se mueve el doble de rápido.
 

Pasos para Implementar:

 

Añadir el atributo score a la clase Game para reflejar la puntuación del jugador (inicialmente 0).
 

Modificar el método collide() de la clase Opponent para que sume un punto a la puntuación cuando el jugador le alcance con un disparo.


Añadir el atributo lives a la clase Player (inicialmente 3). Restar una vida cada vez que el jugador sea alcanzado por un disparo enemigo.
Si las vidas llegan a 0, el juego debe terminar.
Si le quedan vidas, el jugador debe renacer después de un breve tiempo.
 

Mostrar Puntuación y Vidas en Pantalla: Implementa un método en la clase Game para mostrar la puntuación y las vidas del jugador en todo momento.
 

Crear una clase Boss que herede de Opponent, sobreescribiendo los métodos necesarios para representar al jefe final.


 

Modificar el método remove_opponent() en la clase Game para que, cuando el jugador derrote a un enemigo, aparezca el jefe final.
 

Modificar el método end_game() para mostrar un mensaje de victoria si el jugador derrota al jefe final y tiene más de 0 vidas.
