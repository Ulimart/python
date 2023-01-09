# ***Máscara de red***

Se define como una combinación de bits que funcionan para delimitar una red de ordenadores y dividir esta red en subredes. Este código de números es usado para realizar correctamente el proceso de transferencia de mensajes entre dispositivos en la misma subred. Y realiza sus labores en conjunto con el enrutador de una red.

También se encargá de indicarle a los diferentes dispositivos cómo está dividida la dirección IP, es decir, qué parte de esta es la correspondiente al número de la red, a la máscara de subred y al host y además, permite identificar fácilmente qué subred está siendo utilizada. 
Mediante esta herramienta, la máquina puede saber si debe enviar un paquete dentro o fuera de la red en la que permanece conectada.

### *Tipos de máscaras de red*

Los tipos de máscaras de red son utilizadas principalmente en las redes informáticas de internet. 
Cada clase de máscara manejan *diferentes longitudes*, suelen usarse con sistemas informáticos y redes de varios tamaños. Pueden ser divididas de acuerdo a sus partes fijas y variables.

- **Clase a**

Se refieren a los tipos de red que usan la máscara de red establecida de **255.0.0.0** y que tienen su *primer octeto* entre **0 a 127**.

- **Clase b**

Son las redes que utilizan la máscara predeterminada de **255.255.0.0**, y cuyo *primer octeto* se encuentra de de **128 a 191**.

- **Clase c**

Este tipo de redes usan una máscara de red de **255.255.255.0**, manejando el rango de **192 a 233** como su *primer octeto*.

- **Clase d y e**

Hace referencia al tipo de red que no utilizan ningún tipo de máscara. En el caso de la red **clase d**, esto ocurre debido a que está *enfocada en la multidifusión*, por lo que no necesita realizar una extracción de direcciones host para la dirección IP. Mientras que, la red **clase e** no utiliza máscaras de red porque su *uso es meramente experimental para R&D o estudio*.