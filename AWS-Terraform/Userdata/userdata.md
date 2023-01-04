#                   USERDATA

Estos se utilizan para hacer cualquier personalización en el momento del lanzamiento. Es decir, los userdata se ejecutarán cuando se lance una instancia y **no** cuando se reinicie.

Ejemplos de lo que podría personalizarce en un lanzamiento:

    - Instalar algún software extra

    - Preparar la instancia para que se una a un clúster

    - Ejecutar comandos/scripts

    - Montar/agregar volúmenes

Terraform permite agregar userdata el recurso *aws_instance*

    - String, esto es para comandos simples

    - Templates, sirve para instrucciones más complejas

- Ejemplo de *string*

                resource "aws_instance" "caro"{
                    ...
                    user_data = "#!/bin/bash\nwget http://swupdate.openvpn.org/as/openvpn-as-2.1.2-Ubuntu14.amd_64.deb\ndpkg -i openvpn-as-2.1.2-Ubuntu14.amd_64.deb"
                }

El punto de esa línea es que se instalará un servidor de aplicaciones OpenVPN, por lo que en ese string viene un script.

En ese *script* se va a descargar (wget) desde el sitio web de openvpn el paquete de la vpn. Esto instalará un vpn al momento del arranque.

- Ejemplo de un *template*

                resource "aws_instance" "caro"{
                    ...
                    user_data = "${data.template_cloudinit_config.cloudinit-example.rendered}"
                }

En este caso se usa una variable como userdata, la cua se refiere a una configuración de cloud init que será renderizada.

Se debe de tener la configuración de cloud init en otro archivo y su script.

**cloudini.tf**

                provider "clouinit"{}

                data "template_file" "init_script"{
                  template = "{$file("scripts/init.cfg")}"
                  vars{
                    region = "${var.AWS_REGION}"
                  }
                }

                data "template_cloudinit_config""cloudinit-example"{
                  
                  gzip = false
                  base64_encode =false

                  part{
                    filename = "init.config"
                    content_type = "text/cloud-config"
                    content = "${data.template_file.init_script.rendered}
                  }
                }

**scripts/init.cfg**

                #cloud-config

                repo_date: true
                repo_upgrade: all

                packages:
                  - docker

                output:
                  all: '| tee -a /var/log/clou-init-output.log'