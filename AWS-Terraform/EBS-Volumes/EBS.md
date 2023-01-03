#                       EBS 

EBS => Elastic Block Storage

Servicio ofrecido por AWS. 

- En el caso de la instancia t2 micro con su AMI, añade automáticamente ocho gigabytes de almacenamiento EBS. 

- Algunos tipos de instancias tienen almacenamiento local en la propia instancia, que se denomina almacenamiento efímero. Este tipo de almacenamiento siempre se pierde cuando se termina la instancia.

Hay dos tipos de almacenamiento:

1. EBS

2. Local

El volumen raíz de almacenamiento EBS de 8GB que viene con la instancia también está configurado para ser elimindo automáticamente cuando la instancia es terminada.

Se puede añadir un volumen de almacenamiento EBS extra. El cual se mantendrá hasta que se le indique a AWS que sea eliminado. Es decir, se puede eliminar la instancia y el volumen seguirá existiendo.

El EBS se puede añadir mediante un recurso de terraform y luego adjuntarse a la instancia.

Este volumen se le debe de determinar:

        - zona de disponibilidad

        - tamaño en GB

        - tipo, los cuales pueden ser:

(BUSCAR LOS TIPOS DE EBS)
