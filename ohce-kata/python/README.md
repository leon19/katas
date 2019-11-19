# [Ohce Kata](http://garajeando.blogspot.com/2016/05/the-ohce-kata-short-and-simple-exercise.html)

`ohce` es una aplicación cli que muestra en pantalla los datos que ha introducidos por el usuario en orden inverso.

A pesar de ser una aplicación sencilla `ohce` sabe hacer lo siguiente:

1. Cuando inicias `ohce`, muestra un mensaje de bienvenida dependiendo de la hora actual:

   - Entre las **6.00** y las **12.00**, `ohce` te dará la bienvenida diciendo **¡Buenos días [nombre]!**
   - Entre las **12.00** y las **20.00**, `ohce` te dará la bienvenida diciendo **¡Buenas tardes [nombre]!**
   - Entre las **20.00** y las **6.00**, `ohce` te dará la bienvenida diciendo **¡Buenas noches [nombre]!**

2. Cuando los datos que se introducen son un palíndromo, a `ohce` le gustará y, además de mostrar en pantalla los datos en orden inverso, también mostrará el mensaje **¡Bonita palabra!**

3. `ohce` sabe cuando debe detener la aplicación, solo debes escribir **Stop!**, y la aplicación responderá **¡Adiós [name]!**

Este es un ejemplo de usar `ohce` (por la mañana):

```sh
$ ./ohce Lorens
> ¡Buenos días Lorens!
$ hola
> aloh
$ oto
> oto
> ¡Bonita palabra!
$ stop
> pots
$ Stop!
> ¡Adiós Lorens!
```
