#                   VPC

En AWS existen las VPC default, las cuales son creadas por AWS para levantar/lanzar instancias. En las anteriores demos, al levantar una intancia, esta era lanzada en la VPC default.

- La VPC aísla las instancias a nivel de red. Es decir, tienes tu propia red privada en la nube.

- Como buena práctica es siempre levantar una instancia dentro de una VPC. Usando:

        - VPC default

        - VPC creada por uno mismo, la cual será gestionada por *Terraform*

- También está la *EC2-Classic*, que es una gran red en la que todos los clientes de AWS pueden lanzar sus instancias. Sin embargo, es una mejor práctica lanzar todo en una VPC.
Algunos proveedores de nube, como DigitalOcean, no tienen algo como VPC, sino se parece más a una EC2-Classic, donde se tiene sólo una gran red y si no configuras bien el firewall entonces alguien podría acceder a los servicios.

- Por lo anterior, es mejor se puede llegar a la conclusión de que es mejor usar una VPC, ya que se mantiene completamente todo aislado de otras redes.

- Tanto para pequeños a medianas configuraciones, una VPC (por región) será adecuada para las necesidades. 

- Una instancia lanzada en una VPC jamás se comunicará con una instancia de otra VPC utilizando sus direcciones IP privadas. 

        - Estas podrían comunicarse sólo usando su IP pública, no es la mejor practica.

        - En caso que se necesite comunicar diferentes VPCs entre sí, se podrían enlazar mediante peering o VPC peering.

La mejor practica es que dentro de una VPC se agreguen instancias y entre ellas se comuniquen, es lo más seguro.

Este es un ejemplo de como se vería una VPC con diferentes instancias:

INSERTAR LA MUGROSA IMAGEN.

- En AWS, se comienza creando la VPC para después poder harce el deploy de las instancias o bases de datos. Las instancias se lanzan en cualquiera de las subredes disponibles en la zona, pero se debe de especificar al momento de crear maquina virtual.

- Se crean los rangos de las subredes, 10.X.X.X/Y

En el caso de la Y, se puede elegir 8, 16, 24, 32.

 8  => 16,777,214   Full range

 16 => 65,536       Acceso más grande 
 
 24 => 256          Quizás para un proyecto pequeño, ¿está es la ip de casa?

 32 => 1            Single host

- ***Subredes privadas***

Al configurar una VPC, las direcciones IP que son usadas son todas subredes privadas, es decir direcciones privadas. Las cuales no puedes ser utilizadas en internet, sólo de forma privada dentro de la VPC, en una red doméstica o en oficina. 

Regresando a la VPC

En cada **Zona disponible** que compone la VPC tiene su propia subred pública y privada.

Podrás preguntarte: ¿A qué se refiere con *Zona disponible*? 

Bueno, la zona disponible o availability zone son las zonas que se encuentran dentro de la región, estás se dividen en letras, ejemplo:

        Región => eu-west-1

        Availavility Zone => a, b y c

        eu-west-1a, eu-west-1b y eu-west-1c

Estas subredes tienen su propio rango IP. En el caso de las subredes públicas, estas están conectadas a un *Internet Gateway*. Estas instancias también tendrán una dirección IP pública que les permitirá ser accesibles desde internet de las cosas.
Las instancias públicas tendrán la dirección IP privada y pública.

Las instancias lanzadas en la subred privada no tendrán la dirección IP pública, por lo que no serán accesibles desde el internet de las cosas. 

- *Net Gateway* permitirá la comunicación de las instancias privadas para comunicarse con el exterior pero no de afuera hacia adentro.

Las instancias públicas pueden llegar a las instancias privadas porque están dentro de la misma VPC. Esto es posible si se establece un firewall para permitir el tráfico de uno a otro.

Normalmente, es usado las subredes públicas para los servicios o aplicaciones a internet. Para el caso de las bases de datos, los servicios de caché y los backends van en la subred privada. 

Si se utiliza un *Load Balancer (LB)*, este comunmente se coloca en las subredes públicas. Por lo que el *LB* es a lo que se puede conecta desde internet y puede conectarse internamente a instancia en las subredes privadas.