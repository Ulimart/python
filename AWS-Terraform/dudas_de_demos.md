#                   Dudas de las demos que se están haciendo

***DEMO 01***
### LOOKUP

REgresa el valor de un solo elemento de una variable *map*, dada su *key*. Si la *key* no existe, su lugar te regresa el valos por default.


***DEMO 02***
### APT: Advanced Package Tool
 
Elemento de línea de comandos creados por el proyecto Debian con el objetivo de permitirle a los usuarios de gestionar y administrar los paquetes de sus distribuciones de Linux Debian, así como sus derivados, incluidos *ubuntu* y Linux Mint.

Dentro de las funciones principales de este comando, se puede encontrar que Linux APT te permite instalar, actualizar, eliminar paquetes o programas del sistema en Linux, entre otras funciones.

Principales comandos apt-get:

- *apt-get install {package}* : funciona para instalar programas o paquetes.

- *apt-get reinstall {package}* : cumple la función de reinstalar un paquete completo desde cero, en caso de que este presente algún problema en su funcionamiento.

- *apt-get update {package}* : comando diseñado para actualizar los paquetes del sistema.

- *apt-get remove {package}* : se encarga de eliminar los paquetes instalados, pero deja sus archivos de configuración.

- *apt-get remove -purge {package}* : este comando remueve por completo un programa o paquete, incluyendo también, sus archivos de configuración asociados.

- *apt-get update* : usado para actualizar los paquetes.

- *apt-get upgrade* : funciona para actualizar el sistema de Linux, incluyendo los paquetes de seguridad.

- *apt-get dist-upgrade* : encargado de actualizar las distribuciones de Linux.


### COALESCE

Esta función toma cualquier número de argumentos y devuelve el primero que no es nulo o una cadena vacía.

Todos los argumentos deben ser del mismo tipo. Terraform intentará convertir los argumentos que no coincidan en el tipo más general al que se pueden convertir todos los argumentos, o devolverá un error si los tipos son incompatibles. El tipo de resultado es el mismo que el tipo de todos los argumentos.

Ejemplo:

- coalesce("a","b") 
    a
- coalesce(" ","b")
    b
- coalesce("1","2")
    1

Terraform intenta seleccionar un tipo de resultado al que se puedan convertir todos los argumentos, por lo que mezclar tipos de argumentos puede producir resultados sorprendentes debido a las reglas de conversión automática de tipos de Terraform:

- coalesce(1, "hello")
    1
- coalesce(true, "hello")
    true
- coalesce({}, "hello")

    Error: Error in function call

    Call to function "coalesce" failed: all arguments must have the same type.
