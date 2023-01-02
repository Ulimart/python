#                   VPC

En AWS existen las VPC default, las cuales son creadas por AWS para levantar/lanzar instancias. En las anteriores demos, al levantar una intancia, esta era lanzada en la VPC default.

- La VPC aísla las instancias a nivel de d. Es decir, tienes tu propia red privada en la nube.

- Como buena práctica es siempre levantar una instancia dentro de una VPC. Usando:

        - VPC default

        - VPC creada por uno mismo, la cual será gestionada por *Terraform*

- También está la *EC2-Classic*, que es una gran red en la que todos los clientes de AWS pueden lanzar sus instancias. Sin embargo, es una mejor práctica lanzar todo en una VPC. 
Algunos proveedores de nube, como DigitalOcean, no tienen algo como VPC, sino se parece más a una EC2-Classic, donde se tiene sólo una gran red y si no configuras bien el firewall entonces alguien podría acceder a los servicios.

- Por lo anterior, es mejor se puede llegar a la conclusión de que es mejor usar una VPC, ya que se mantiene completamente todo aislado de otras redes.

- 