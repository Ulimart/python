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

***DEMO 03***

### >>
Cuando se usa doble ese simbolo significa que agrega más info al archivo, NO REEMPLAZA

### >
Esto SÍ REEMPLAZA info, así que si se requiere sobreescribir es mejor usar este simbolo

***DEMO_05***
El protocolo *TCP* es utilizado por HTTP, FTP o SSH (el que estoy utilizando para esta demo)

Para tener en cuenta los diferentes tipos de puertos:

- ***Puerto 0*** : 
TCP en realidad no usa el puerto 0 para la comunicación de red, pero este puerto es bien conocido por los programadores de redes. 
Los programas de socket TCP usan el puerto 0 por convención para solicitar que el sistema operativo elija y asigne un puerto disponible. Esto evita que un programador tenga que elegir ("codificar") un número de puerto que podría no funcionar bien para la situación.

- ***Puerto 21*** : 
El puerto 21 por norma general se usa para las conexiones a servidores FTP en su canal de control, siempre que no hayamos cambiado el puerto de escucha de nuestro servidor FTP o FTPES.

- ***Puerto 22*** : 
Por norma general este puerto se usa para conexiones seguras ***SSH*** y SFTP, siempre que no hayamos cambiado el puerto de escucha de nuestro servidor SSH.

- ***Puerto 23*** : 
Telnet, sirve para establecer conexión remotamente con otro equipo por la línea de comandos y controlarlo. Es un *protocolo NO seguro* ya que la autenticación y todo el tráfico de datos se envía sin cifrar.

- ***Puerto 25*** :  
El puerto 25 es usado por el protocolo SMTP para él envió de correos electrónicos, también el mismo protocolo puede usar los puertos 26 y 2525.

- ***Puerto 53:*** 
Es usado por el servicio de DNS, Domain Name System.

- ***Puerto 80:***
Este puerto es el que se usa para la navegación web de forma no segura HTTP.
- ***Puerto 101:***
Este puerto es usado por el servicio Hostname y sirve para identificar el nombre de los equipos.

- ***Puerto 110:***
Este puerto lo usan los gestores de correo electrónico para establecer conexión con el protocolo POP3.

- ***Puerto 123:***
Es un puerto utilizado por el NTP o Protocolo de tiempo en red, es uno de los protocolos más importantes a nivel de redes, ya que se utiliza para mantener los dispositivos sincronizados en Internet. Podemos incluso considerarlo vital, ya que, debido a la precisión de los relojes, facilitan mucho la interrelación de problemas de un dispositivo a otro.

- ***Puertos 137, 138 y 139:***
Estos puertos son utilizados por el Protocolo NetBIOS o NBT, lo habréis escuchado mucho si trabajáis en redes en Windows, ya que ha sido durante mucho tiempo el protocolo TCP principal para interconectar los equipos que están bajo este sistema operativo, lógicamente se utiliza en la mayoría de las veces en combinación con el IP utilizando así la famosa combinación TCP/IP que todos conocemos.

- ***Puerto 143:***
El puerto 143 lo usa el *protocolo IMAP* que es también usado por los gestores de correo electrónico.

- ***Puerto 179:***
Es el puerto utilizado por el Protocolo de puerta de enlace fronteriza o BGP por sus siglas en inglés, es otro protocolo muy importante a nivel de redes, ya que, en su mayoría, es utilizado por los proveedores de servicio para ayudar a mantener las enormes tablas de enrutamiento que existen hoy en día. 
También es utilizado para procesar las inmensas cantidades de tráfico en las redes, por lo que es uno de los protocolos más utilizados en las redes públicas.

- ***Puerto 194:***
Aunque herramientas como aplicaciones de mensajería para teléfonos inteligentes y servicios como Slack y Microsoft Teams han reducido el uso de Internet Relay Chat, IRC sigue siendo popular entre personas de todo el mundo. Por defecto, IRC usa el puerto 194.

- ***Puerto 443:***
Este puerto es también para la *navegación web*, pero en este caso usa el *protocolo HTTPS* que es seguro y utiliza el protocolo TLS por debajo.

- ***Puerto 445:***
Este puerto es compartido por varios servicios, entre el más importante es el Active Directory.

- ***Puerto 587:**
Este puerto lo usa el protocolo SMTP SSL y, al igual que el puerto anterior sirve para el envío de correos electrónicos, pero en este caso de forma segura.

- ***Puerto 591:***
Es usado por Filemaker en alternativa al puerto 80 HTTP.

- ***Puerto 853:***
Es utilizado por DNS over TLS.

- ***Puerto 990:***
Si utilizamos FTPS (FTP Implícito) utilizaremos el puerto por defecto 990, aunque se puede cambiar.

- ***Puerto 993:***
El puerto 993 lo usa el protocolo IMAP SSL que es también usado por los gestores de correo electrónico para establecer la conexión de forma segura.

- ***Puerto 995:***
Al igual que el anterior puerto, sirve para que los gestores de correo electrónico establezcan conexión segura con el protocolo POP3 SSL.

- ***Puerto 1194:***
Este puerto está tanto en TCP como en UDP, es utilizado por el popular protocolo OpenVPN para las redes privadas virtuales.

- ***Puerto 1723:***
Es usado por el protocolo de VPN PPTP.

- ***Puerto 1812:***
Utilizado tanto con TCP como con UDP, y sirve para autenticar clientes en un servidor RADIUS.

- ***Puerto 1813:***
Se utiliza tanto con TCP como con UDP, y sirve para el accounting en un servidor RADIUS.

- ***Puerto 2049:***
Utilizado por el protocolo NFS para el intercambio de ficheros en red local o en Internet.

- ***Puertos 2082 y 2083:***
Utilizado por el popular CMS cPanel para la gestión de servidores y servicios, dependiendo de si se usa HTTP o HTTPS, se utiliza uno u otro.

- ***Puerto 3074:***
Lo usa el servicio online de videojuegos de Microsoft Xbox Live.

- ***Puerto 3306:***
Puerto usado por las bases de datos MySQL.

- ***Puerto 3389:***
Es el puerto que usa el escritorio remoto de Windows, muy recomendable cambiarlo.

- ***Puerto 4662 TCP y 4672 UDP:***
Estos puertos los usa el mítico programa eMule, que es un programa para descargar todo tipo de archivos.

- ***Puerto 4899:***
Este puerto lo usa Radmin, que es un programa para controlar remotamente equipos.

- ***Puerto 5000:***
Puerto de control del popular protocolo UPnP, y que por defecto, siempre deberíamos desactivarlo en el router para no tener ningún problema de seguridad.

- ***Puertos 5400, 5500, 5600, 5700, 5800 y 5900:***
Son usados por el programa VNC, que también sirve para *controlar equipos remotamente*.

- ***Puertos 6881 y 6969:***
Son usados por el programa BitTorrent, que sirve para e intercambio de ficheros.

- ***Puerto 8080:***
Puerto alternativo al *puerto 80 TCP* para servidores web, normalmente se utiliza este puerto en *pruebas*.

- ***Puertos 51400:***
Es el puerto utilizado de manera predeterminada por el programa Transmission para descargar archivos a través de la red BitTorrent.

- ***Puerto 25565:***
Puerto usado por el famoso videojuego Minecraft.

### VPC

VPC => Red Privada Virtual
