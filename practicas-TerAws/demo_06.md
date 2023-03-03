### ***Demo 06***

En esta demo se va a crear:

- Instancia

- s3

- rol

- el perfil de instancia

- adjuntará la politica de rol al rol

- se asumirá el rol cuando se acceda en la instancia

Después de hacer levantar la infra, se accederá a la instancia por medio de ssh:

    - ssh -i <key> ubuntu@<ip publica>

La ip publica se puede obtener al terminar de levantarse la infra, ya que tenemos un output que arroja la ip.

A mi parecer es gran opción agregar un output cuando se levante infra, de esta manera al terminar el deploy tendremos datos necesarios para accesar o tener en cuenta para los siguientes pasos.

Al acceder a la instancia necesitamos instalar *AWSCLI*, de esta manera podemos trabajar desde la instancia y no la consola.

1. *sudo -s*, para ser usuario root y poder instalar

2. *apt-get update*, en el laboratorio que segui primero descarga pip y después hace el update, pero me di cuenta que es mejor primero hacer el update y después descargar

3. *apt-get install -y python3-pip python3-dev*, nos va a ayudar a descargar los paquetes

4. *pip install awscli*

    4.1 Este es opcional, si quieres comprobar que esta instalado, con sólo escribir aws debería salir las opciones que se tienen.

5. En este punto se van a hacer algunas pruebas para crear archivos, subirlos al s3

    ## Subir archivos:

    - aws s3 cp <nombre del archivo> s3://bucket-caro-2103/<nombre del archivo>

    ## Bajar archivos

    - aws s3 cp s3://bucket-caro-2103/<archivo que quieres descargar> <puedes mantener el mismo nombre del archivo o cambiarselo>

Después de esto yo creé archivos prueba, para subirlos y bajarlos, después guardé y bajé unos archivos para trabajar en python.