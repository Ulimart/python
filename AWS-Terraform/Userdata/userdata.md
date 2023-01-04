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

                provider "clouinit"{} ## para este ejemplo cambiamos AWS => CLOUDINIT

                data "template_file" "init_script"{  ## aquí sale el "content"
                  template = "{$file("scripts/init.cfg")}" ## se utilizará un templatefile para hacer referencia a otro script
                  vars{
                    region = "${var.AWS_REGION}" ## agregamos una variable como *ejemplo* para tomar en cuenta que si se pueden agregar, en este caso no será usada.
                  }
                }

                data "template_cloudinit_config""cloudinit-example"{ ## este es el recurso que será un template
                  
                  gzip = false ## le decimos que no usaremos ni gzip y base64, estos son diferentes formatos de esta nube 
                  base64_encode =false  ##para este caso quedo como como texto

                  part{  ## contiene una parte
                    filename = "init.cfg"  ## el nombre del archivo
                    content_type = "text/cloud-config" ##el tipo del contenido y su tipo de contenido es un texto
                    content = "${data.template_file.init_script.rendered} ## este contenido viene de la parte de arriba, es una linea anidada +  la parte de renderización. Aquí va a leer el siguiete archivo
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

¿Qué significa lo que tenemos arriba?

Al crearse el cloudinit, se tomará este como provider y utilizar un templatefile que referencia a un script. Es