#               ATRIBUTOS

Terraform guarda los atributos de todos los recursos que crea, por ejemplo:
    - EL recurso de *aws_instance* tiene el atributo de public_ip

Estos atributos pueden ser consultados y emitidos. Lo cual pueden ser útil sólo para dar salida a info valiosa o para alimentar info a un software externo. 

Ejemplo:

Puede ser utilizado *output* para mostrar la dirección IP pública de un recurso de aws. Por lo que se agregaría al archivo de *instance.tf* la línea:

                                output "ip" {
                                  value = "${aws_instance.caro.private_ip}"
                                }
Para referirse a cualquier atributo especificando los soguientes elementos en su variable:

    - El tipo del recurso: aws_instance




al aplicarlo quedaría así:
![Output IP](https://github.com/Ulimart/python/tree/AWS-Terraform/AWS-Terraform/demo_03/output.png)

en la consola de AWS, se ve de está forma:
![Consola AWS](https://github.com/Ulimart/python/tree/AWS-Terraform/AWS-Terraform/demo_03/aws_ip.png)