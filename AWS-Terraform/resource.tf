#### Este documento servirá para crear un resource para trabajar en AWS
### Se elige ser proveedor
provider "aws" {

}

variable "AWS_REGION" {  ### La variable mencionada abajo se puede agregar acá o crear un archivo con .tfvars
  type = string
}

variable "AMIS" {
  type = map(string)
  default = {
    eu-west-1 = "my ami"
  }
}
## Ahora se van a agregar los atributos para este proveedor, comenzando con
## con resource
resource "aws_instance" "caro" {
  ami           = var.AMIS[var.AWS_REGION] ### en esta parte la ami (imagen) que busca dependiendo la región por eso se le añade la variable entre corchetes
  instance_type = "t2.micro"
}

### SE PUEDEN AGREGAR MAS RECURSOS, SÓLO SE TIENEN QUE LLAMAR DIFERENTE SI SON INSTANCIAS