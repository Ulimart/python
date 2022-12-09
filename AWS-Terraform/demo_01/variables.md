#                VARIABLES

- Debemos tomar en cuenta que todo en UN SOLO archivo no es la mejor practica

- Usar archivos de variables para ocultar contraseñas/secrets, por ejemplo: en el repositorio git no es lo mejor tener tus contraseñas.

- Usar variables para los archivos que puedan cambiar; así que es recomendable hacer archivos lo más genéricos posibles, de esta forma los elementos que puedan cambiar se van a pasar a variables.
Por ejemplo, las AMIs
    - Las AMIs son diferentes dependiendo la región, por lo que pasarlas a variables ayudará a que cambien cada vez que sea una región diferente.

-El uso de variables ayudan a que los archivos terraform sean más genéricos y puedan ser usandos para diferentes proyectos.

Ejemplo:

##                      INSTANCIA

Al crear una instancia (instance.tf), esta debe de contener el proveedor y los recursos.

    provider "aws"{
      access_key = "${var.AWS_ACCESS_KEY}"
      secret_key = "${var.AWS_SECRET_KEY}"
      region     = "${var.AWS_REGION}"
    }

    resource "aws_instance "example" {
        ami           = "ami-0d729a60"
        instance_type = "t2.micro"
    }

Se va a dividir el archivo anterior en: 

###        provider.tf => vars.tf => terraform.tfvars o vars.tfvars

¿Qué significa esto?

1. ***provider.tf***
El cual sólo va a contener los secrets/contraseñas y la región, los cuales no van a tener un valor escrito o por decirlo así, no estarán rellenos, si no van a referirse a variables.

    provider "aws"{
      access_key = "${var.AWS_ACCESS_KEY}"
      secret_key = "${var.AWS_SECRET_KEY}"
      region     = "${var.AWS_REGION}"
    }

2. ***vars.tf***
En este archivo se declararán las variables que no están "rellenas" en el provider.

    variable "AWS_ACCESS_KEY" {}
    variable "AWS_SECRET_KEY" {}
    variable "AWS_REGION" {
        default = "eu-west-1"
    }

Para el caso de la región estamos definendo el valor de una variable por defecto, mientas que para las keys no se les ha definido un valor, ya que las llaves están vacías.

3. ***terraform.tfvars/vars.tfvars***

En este archivo se van a guardar los valores de las keys, ya que estos valores son sensibles y no cualquiera puede conocerlos. También se pueden guardas todas las variables

    AWS_ACCESS_KEY = ""
    AWS_SECRET_KEY = ""
    AWS_REGION     = ""

Este archivo debe de agregarse en el git ignore, para que no esté en el repositorio gir, porque las claves de acceso y secreta JAMÁS deben de esar expuetas.
El AWS_REGION se puede dejar fuera ya que tenemos un valor por defector establecido en el anterior archivo. Sin embargo, si se desea eliminar el valor por default se puede agregar acá.

Después de que se separó el archivo *instance.tf*, sólo quedará el recurso. Pero, ¿Cómo quedaría ese archivo si movemos AMI a una variable?

###        instance.tf => vars.tf => terraform.tfvars o vars.tfvars

1.  ***instance.tf***
e modifica la el ID de la AMI por una de búsqueda:

    resource "aws_instance "example" {
        ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
        instance_type = "t2.micro"
    }

Esto se explica con que se buscará en una variable de región que ami le corresponde.

2. ***vars.tf***
Se va a modificar el archvo vars y se agrega la variable de AMIS:

    variable "AWS_ACCESS_KEY" {}
    variable "AWS_SECRET_KEY" {}
    variable "AWS_REGION" {
        default = "eu-west-1"
    }
    variable "AMIS" {
        type    = map
        default = {
          us-west-1 = "ami-0454207e5367abf01"
          us-west-2 = "ami-0688ba7eeeeefe3cd"
          eu-west-1 = "ami-0f29c8402f8cce65c"
        }
    }

SE agregó una variable tipo map, para conocer el tipo de AMI dependiendo la región se utiliza la siguiente liga: 
#####       https://cloud-images.ubuntu.com/locator/ec2/

Por lo que la búsqueda e la variable AMIS será así:
El primer parámetro es la propia variable AMIS y el segundo es la clave que se tiene que buscar, la cual se le asignó el nombre *AWS_REGION*.
En el caso de esta instancia:
            - ***región: eu-west-1***
            - ***ami : ami-0d729a60***
