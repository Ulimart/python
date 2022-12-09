#              UNDERSTANDING TERRAFORM HCL

Es importante tener en cuenta que los archivos para terraform deben de terminar con *.tf*
Checar código *proof_01*

#              FIRST STEPS IN TERRAFORM & AWS

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
