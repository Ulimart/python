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

### ***Algo más de Terrform***

- Con esta herramienta podemos definir y desplegar la infra desde código fuente.

- Los módulos nos ayudan a no repetir la infra, lo cual no se escribirá el código más veces,

### ***Añadiendo más a la definición de Terraform***

- Herramiento de orquestación de códifo abierto desarrollado por Hashicorp, nos permite definir nuestra infra como código.

- Usa un lenguaje de programación declarativo y simple

- Tiene soporte para una gran cantidad de proveedores de infra local o en la nube.

- Terraform no se limita a un proveedor específico

- Sintaxis simple y unificada que permite administrar casi cualquier recurso en lugar de requerir que se utilicen herramientas independientes para cada plataforma y servicio.

- Las config que se realizan en terraform puede ser compartida y reutilizable.

- Terraform puede suplir a *cloudformation*

- Tiene facilidad para trabajar con varios prov

- Salva estados; al crear una plantilla creamos el edo que queremos que tenga nuestra infra.

- Si al entrar a la plataforma y se hacen cambios, al correr algún comando de terraform, este compara lo realizado con lo anterior.

- Es muy bueno para versionar infra.

- Se puede tener versionado en:

        - s3
        - repositorio git

##### *Beneficios de Terraform*

- Administra infra considerablemente grandes o puede administrar una sola app.

- El modelo de su centro de datos puede ser versionado, lo que esta forma es más sencillo de observar el progreso de nuestro servicio y controlar los cambios.

##### *Desventajas*

- Delay al momento de las actualizaciones

***CLI*** => Command-line interface, se espera que los comandos de terraform se corran en este.

***IaaS*** => Infra como servicio, Infrastruture as a Service

***PaaS*** => Plataforma como servicio, Platform as a Service

***SaaS*** => Software como servicio, Software as a Service