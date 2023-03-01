### ***Demo 03***

Después de hacer pruebas y comprender como trabajar con el server de cloud gurú, se creó una VPC (Virtual Private Cloud), la cual yo la asocio con una cerca, la cual va a "proteger" todo lo que esté dentro de ella.

Los archivos dentro de esa demo:

- *instance.tf*

- *provider.tf*

- *vars.tf*

Los primeros archivos son casi iguales a los que tenemos en la primera demo, lo que va a diferenciar es que en instance.tf se agrega los recursos que se van a ligar a la instancia y en vars.tf se agregarán las keys que se crearon.

- *key.tf* => Este archivo nos ayudará a conectar, de manera segura, por medio de SSH

- *securitygroup.tf* => Es necesario crear un security group para poder tener la conexión SSH y el tráfico de salida de la VPC.

- *nat.tf* => Contiene los recursos de:

    - Ip estática => La cual se debe de ligar con la VPC

    - Getaway 

    - Route table

- *vpc.tf* => Los recursos que se crean son las subnets, pública y privada, y la creación de la VPC, así como el ligarse con los recursos creados en el archivo de nat.

