#                   MODULOS

Usos de los módulos:

    - Mejor organización

    - Con estos puedes usar modulos de terceros, ejemplo: 
        
            -Los que se almacenan en algun repo de Github

    - Reusar partes del código, ejemplo:

            - Configurar una red en AWS - VPC. 
    
    Al haber escrito los recursos en terraform, se agregan en un módulo y reusarlos para otro proyecto o porque estás usando múltiples regiones en AWS.

###         Módulo desde Github

Para usar un módulo externo, en este caso será desde Git:

        module "nombre del modulo" {
            source = "link donde se encuentra dicho modulo"
        }

Para el caso del link donde tenemos el módulo debe llevar: ***dirección(github.com)/usuario/repositorio git***

###         Módulo desde un folder local

Cuando tienes el código en desde un local folder, se debe implementar esto:

        module "nombre del modulo"{
            source = "./carpeta donde se encuentra el modulo"
        }

Al agregarle el ./ hará que terraform busque en esa carpeta. También en allí mismo se pueden agregar argumentos al módulo:

        module "nombre del modulo"{
            source       = "./carpeta donde se encuentra el modulo"
            region       = "us-west-1"
            ip-range     = "IP/xx"
            cluster-size = "5"
        }

Cuando terraform entra a la carpeta del módulo, se encontrarán archivos terraform, en el ejemplo del curso que tomo tienen los siguientes:

        1. vars.tf

                variable "region" {} 
                variable "ip-range" {}
                variable "cluster-size" {}
        
        En este archivo se declara un rango de IP de la región y el tamaño del cluster, ya que son los parámetros de entrada.

        2. cluster.tf (este debe de agregarse ya qeue se añadió en los argumentos)

                resource "aws_instance" "instance-1" {}
                resource "aws_instance" "instance-2" {}
                resource "aws_instance" "instance-3" {}
                resource "aws_instance" "instance-4" {}
                resource "aws_instance" "instance-5" {}

        En este caso vamos a añadir las 5 instancias que van a crear nuestro cluster.

        3. output.tf

                output "aws-cluster" {
                    value = "${aws_instance.instance-1.public_ip},${aws_instance.instance-2.public_ip}..."
                }
        
        Este nos devolverá información al código principal. El valor que se va a obtener será de la IP pública de cada instancia que compone el cluster. Así en el módulo principal se puede utilizar la variable aws-cluster, ya que esta tendrá los valores de las IPs públicas del cluster.

Para poder ver la lista de las IPs, se agregará un el siguiente recurso en el módulo principal:

        output "nombre" {
            value = "${module.nombre del modulo.aws-cluster}"
        }

Puede usarse cualquier variable, este sólo fue un ejemplo de que se le puede dar salida a algo en la pantalla y podría ser para cualquier recurso.