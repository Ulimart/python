#               SOFTWARES
En este punto ya tenemos levantada una instancia (demo_01), pero necesitamos que tenga algún software. La imagen que se utilizó no trae ni un software.
Hay dos maneras de agregar softwares a la instancia:
    1. Crear una AMI presonalizada y agruparle un software a la imagen.
        - *Packer* es una herramienta de gran ayuda para estos casos.
    
    2. Arrancar las AMIs estandarizadas, lo que se hizo en la demo_01, y luego instalarle el software que se necesite. ¿Cómo?
        - Cargando archivos
        - Usando remote exec, así se ejecutan archivos y scripts
        - Usar herramientas de autamatización como chef, puppet, ansible.

###             File Uploads

File uploads es una manera fácil de subir archivos o scripts, en conjunto con remoter-exec, el cual lo ejecutará.
El provisioner usará SSH (linux) o WinRM (windows). En el caso de esta demo, vamos a anular el SSH que viene predeterminado, por lo que se usará *connection*.

En el caso de AWS, se necesitará keypairs, pr lo que se necesitará otro recurso llamado *aws_key_pairs*, por lo q crearán una clave pública y privada.

La *clave pública* es la que se va a subir a AWS, por eso se debe definir en el *instance.tf*, para el caso de la *clave privada* se usará para iniciar sesión y se agrega en *connection*.

Después de iniciar sesión con las llaves, ahora se ejecutará el script usando *remote-exec*. El *+x* significa que es ejecutable.

###             KEY

Para crear las llaves se usará en la consola la siguiente línea:
                            ***ssh-keygen -f (nombre)***

Tendremos dos llaves:

- Pública => (nombre)
- Privada => (nombre).pub

###             SSH

Se debe de abrir el acceso al SSH de la instancia, por lo que se necesita un grupo de seguridad, el cual estará explicado más adelanta. Sin embargo, se puede (momentaneamente) generar un security group manualmente desde la consola de AWS. 

- AWS manually

    1. Checar que estemos en la región correcta
    2. Seleccionar VPC
    3. Ya se tiene un security group determinado (default)
    4. Cambiar la inbound rules
    5. Dar acceso a la ip address personal
        5.1 Agregar otra regla
        5.2 type => ALL TCP
        5.3 agregar ip address + /32, el 32 es un rango 
