#              UNDERSTANDING TERRAFORM HCL

Es importante tener en cuenta que los archivos para terraform deben de terminar con *.tf*
Checar código *proof_01*

Existen archivos con *.tfvars*, estos archivos guardan las variables con las que se va a trabajar en un ambiente de pruebas.
De esta manera se evitará declarar los valores por defecto en cada una de las variables, ya que esto no es buena practica.

Cuando se cambia de proveedor, o utilizar un módulo o plugin, se debe de volver a ejecutar el terraform init.
De esta manera inicializa los glugins del proveedor.

#              FIRST STEPS IN TERRAsFORM & AWS

- AWS
    1. Abrir cuenta

    2. Crear usuario IAM admin, para así poder crear instancias y hacer cambios usando terraform
Tener en vuenta que Terraform se puede usar con otros proveedores de la nube.

- TERRAFORM
    1. Se genera un archivo de terraform para correr una instancia t2.micro y ejecutarla

    2. Para ejecutarla se usa: terraform apply

    3. Si se quiere probar la infra que se construira basada en los archivos de terraform, se usaría: terraform plan
        - terraform plan no va a aplicar algún cambio sino mostrará los cambios que se van a realizar; también puede ser usado como un archivo de salida y se podrá guardar los cambios en un archivo, el cual se puede usar para dichos cambios a la infra mediante terraform apply. 
        Los cambios pueden ser eliminados del archivo de terraform.

    4. La infra puede ser destruida si ya no es necesaria, con el comando: terraform destroy. De esta manera no se va a pagar extra por el uso de instancias en AWS.
    Es importante tener cuidado con este comando para el entorno de producción ya que eliminará todos los recursos.

#              TERRAFORM VARIABLE TYPES

- Variables simples de Terraform:
        - String
        - Numero (entero)
        - Booleano

- Tipos complejos de terraform
        - List(type) => List: [0,1,5,2]
        - Set(type)
        - Map(type) => {"key" = "value"}
        - Object({nombre = type})
        - Tuple([type,...])

a) En le caso de la *lista* siempre será ordenada, y te devolverá el valor como se tiene; es decir, no habrá otro orden diferente al original.

b) El *set* es similar a la lista, pero no mantiene el orden que se asigna y sólo toma valores únicos. Por ejemplo, si tenemos una lista => [5,1,1,2], el set => [1,2,5], en la salida terraform los ordena.

c) Un *objeto* es similar a un map, pero el elemento puede contener diferentes tipos, como string y numeros.

d) EL *Tuple* es similar a la *lista*,  sin embargo los elementos pueden contener diferentes tipos. Por ejemplo, un string, numero y booleano en un mismo elemento.

Los más usados (comunmente) son lista y map, mientras que los otros tipos son usados esporádicamente.

También, terraform puede elegir el tipo de variable, sólo se omite el type y terraform lo determinará basado en el valor asignado.

A MI PARECER, NO ES BUENA PRACTICA DEJAR VARIBLES SIN ASIGNAR.