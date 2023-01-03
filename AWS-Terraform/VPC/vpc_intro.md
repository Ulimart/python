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

