# Terraform

## ¿Qué es Terraform?

Terraform es una herramienta de código abierto "Infraestructura como código", creada por HashiCorp.

*HCL* => Hashicorp Configuration Languaje
*Human-redable* => Cualquier usuario puede leerlo

Herramienta para construir, modificar y versionar nuestra infraestructura.

1. Open source
2. Creada por HAshicorp (Vagrant, packer) en 2014
3. Escrita en Go (Checar esta parte)
4. Diseñada para ser flexible y modular

Se diseño para poder acoplar muchos proveedores y piezas de amazon, azure, data dog, tener todos al mismo tiempo y en el mismo repositorio.

###   *Características Clave*

- Infraestructura como código => En terraform los cambios son versionados
- Planes de ejecución
- Grafo de recursos (Checar)
- Cambios automatizados


####  ***Infraestructura como código con Terraform***

En terraform los cambios están versionados debido a que se tienen dentro de un fichero de configuración en el cual estará toda la infaestructura.

*¿A qué cambios me refiero?*
Al crear nuevas máquinas o un servidor con una base de datos "x" al añadirle algo más.

##### *Ventajas de la infraestructura como código*

- Control de versiones (Pull request)
- Integración continua
- Conocimiento compartido y documentado
- Automatización

#### ***Planes de Ejecución***

La ventaja de terraform es que configura a modo de que te avise cada paso ue debe hacer antes de ejecutarlo.

Ejemplo:
Se le configura para que avise lo que va a ejecutar previo a realizarlo.
- Se creará una máquina:
Terraform avisará los cambios que se aplicarán, si llevas a cabo ciertos cambios podrían destruir tu máquina, etc.

### ***Puntos claves de terraform***

Estos son cuatro:

1. ***Resourses*** : 
La infra se construye con recursos; ejemplo: s3, balanceador de carga

2. ***Providers*** : 
Responsables del ciclo de vida de un recurso; ejemplo: en amazon, un provider es el responsable del tiempo de vida de una lamda o de un s3.

                *** PROVIDERS MAS IMPORTANTES ***

- AWS
- Azure
- Google Cloud
- Difital Cloud
- Data dog
- Heroku
- Linode
- Github
- Kubernetes

3. ***State*** : Muy importante, es el estado de nestra infra. Ambiente de desarrollo???

4. ***Modulos*** : Auydan a ahorrar líneas de trabajo.
Ejemplo: Si quiero crear 10 recursos con un solo módulo, puedo repetirlo y se soluciona.
Hacer una función que ayude a agilizar el trabajo.

Service plan: Sirve para crear apps, maquinas, servidores, etc.
- Los archivos de terraform se guardaran con la extensión *.tf*
- Lenguaje: *HCL*
- Se puede ocupar json, pero hashicorp creó el HCL para una lectura más sencilla.

### ***Comandos importantes***

*terraform init*
Inicia la instancia o la configuración de terraform descarga paquetería.

*terraform plan* 
Baja el estado de mi infra para compararlo con lo que se le pidió que hiciera, así muestra las diferencias que hay.

*terraform apply*
Sirve para aplicar cambios requeridos y btener la configuración deseada; o predeterminar el grupo de acciones que se deben realizar en el terraform plan.
