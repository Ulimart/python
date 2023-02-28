### *¿Cómo trabajar en cloud gurú?*

Para trabajar con AWS y Terraform por medio de los servers de cloud gurú se pueden seguir los siguientes pasos:

1. En *Cloud Playground*, en la sección de *cloud servers*, allí es donde se creará el server. 
 
 - Distribución: Ubuntu 18.04 Bionic Beaver LTS

 - Size: Medium 

 - Tag, elegí un nombre que diferencie el server de otros

2. Se inicia el server

    2.1 Para conectarse al server se usa ssh:

        ssh cloud_user@<ip publica>

        La ip publica es la que proporciona cloud gurú

    2.2 Pide la contraseña que es la que también proporciona la plataforma, pero se debe de cambiar la contraseña (este es un paso guiado por el mismo server)

3. Para poder trabajar con ***Terraform*** se debe de instalar el *CLI* (Command Line Interface) de terraform:

    3.1 Bajar el paquete de Terraform:
     
        wget -c https://releases.hashicorp.com/terraform/0.13.4/terraform_0.13.4_linux_amd64.zip

    3.2 Descomprimir 

        unzip terraform_0.13.4_linux_amd64.zip

    3.3 Mover el binario en la ruta del sistema operativo

        sudo mv terraform /usr/sbin/

    3.4 Para corroborar en la consola escribimos

        terraform version

4. Para ***AWS*** se debe de repetir un caso similar al de Terraform, bajar *AWS CLI*

    4.1 Bajar el paquete 

        curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

    4.2 Descomprimir

        unzip awscliv2.zip

    4.3 Instalarlo

        sudo ./aws/install

        Nota: Los repositorios de AWS no son de terceros, puede pasar que no sea la última versión, por lo que se puede instalar de esta manera:

        sudo ./aws/install --bin-dir /usr/local/bin --install-dir /usr/local/aws-cli --update

    4.4 A diferencia de Terraform, el AWS CLI se debe de configurar, para hacer esto debemos de utilizar las credenciales que se encuentran en *Cloud Sandboxes*

    4.5 En consola se escribe *aws configure*, después te pedirá el *access_key*, el *secret_key* y la *region*, en el caso de las keys se utilizan las que nos proporciona cloud gurú y la región es *us-east-1*.

    4.6 Debido a que se te da tiempo límite en esta plataforma, el punto 4.5 se debe de hacer cada vez que te saque la sesión del aws sandox, ya que el *secret_key* cambia.
    Es importante tener en cuenta eso, ya que sin hacer la debida configuración, *NO* podremos trabajar en la nube.

