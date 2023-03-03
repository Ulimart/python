### ***Demo 05***

Esta demo sólo trabajó con *IAM*, por lo que los archivos que se crearon fueron:

- vars.tf

- providers.tf

- iam.tf

Es importante destacar que los archivos de variables y providers son los que siempre deben de crearse, ya que el provider (se le puede nombrar de diferente manera) es el que indica con el proveedor con el que se va a trabajar. 

Terraform no solo se usa para crear infra en AWS.

Sólo se trabajó con el IAM para entender lo que es un *ROL* y un *USUARIO*.

- **IAM**: Identity and Access Management, gestión de identidad y acceso.

Nos va a ayudar a controlar el acceso a los recursos de AWS. Aquí se crean los usuarios y se asignan a ciertos grupos, por ejemplo, al accesar en AWS se requiere crear una cuenta, la cual se llama usuario raíz, por lo que allí se usó IAM.

Sin embargo, esa cuenta no debe de ser compartida ni usarla como cualquier cuenta, por lo que es mejor crear usuarios en IAM. Por ejemplo, el grupo de *X* puede dar los privilegios de admin a unos sus usuarios.

## Usuarios

Los usuarios se pueden agrupar si es que tiene sentido que pertenezcan al mismo grupo. 

Ejemplo:

Tenemos a A, B, C, D, E y F

- Grupo de Desarrollo: A, B y C

- Grupo de Operaciones: D y E

- Grupo de Auditoria: C y D

Los grupos solo contienen usuarios, puede pasar que algunos usuarios no pertenezcan a un grupo, como el caso de *E*, no es la mejor prática pero hay ciertos casos así.

También hay casos que algunos usuarios pertenecen a varios grupos, por ejemplo *C* y *D*. 

Los usuarios pueden **autenticarse** de diferentes maneras:

- Nombre de usuario y una contraseña

    - Opcional, el uso de un token: MFA, utilizando el software compatible con Google Authenticator

- Llave API: *Secret ket* y *Access Key*, estas son las que he usado en las demos anteriores

Los usuarios y los grupos son creados para poder usar las cuentas AWS y otorgarles ciertos permisos. Los cuales son asignados a documentos JSON llamados *políticas*. Estas simplemente son una descripción de lo se que permite a un usuario hacer o lo que un grupo y todos los usuarios que pertenecen a este tiene permitido hacer.

En AWS, se aplica un principio llamado ***principio de privilegio mínimo***. En este no das más permisos de los que necesita un usuario; es decir, si un usuario o grupo sólo necesita acceso a tres servicios, sólo se creerá un permiso para ese usuario o grupo.

Para retomar y abarcar más, el uso más común del IAM es manejar:

- Usuarios

- Grupos

- Roles

- Credenciales de Usuarios

- Políticas de contraseñas de usuarios

- MFA (Multi-factor Authentication)

- Llaves de API para el acceso de CLI

En el caso del usuario raíz, este tiene los derechos y access completos de administrador de cada parte de la cuenta. Si se crea algún usuario adicional en esta cuenta, *NO* tendrá los accesos a los recursos de AWS, sólo para poder loggearse a la cuenta. Por lo que aquí se debería crear un usuario con ciertos permisos.

## Roles

Los roles pueden dar a los usuarios/servicios un acceso temporal que normalmente no tendrían, estos pueden ser adjuntados a las instancias EC2. Por lo que desde esa instancia, un usuario o servicio puede obtener las credenciales de acceso; Usando esas credenciales el usuario/servicio puede asumir el rol que le da permiso para hacer algo. Ejemplo:

- Se crea el rol *mybucket-access* y se le asigna el rol a una instancia EC2 al momento del arranque. Los permisos de este rol serán:

    - Leer

    - Escribir

Cuando accesas a la instancia, asumirás el rol *mybucket-access*, sin necesidad de usar tus propias credenciales, por lo que estás usando unas *credenciales temporales*, las cuales parecen las credenciales normales. Ahora podrás leer y escribir elementos en el bucket que esté atachado a ese rol, quizás en tus propias credenciales no tengas esos permisos, por lo que con el sólo hecho de loggearte a esa instancia ya los tienes. 

- En vez de usar el *AWS-CLI*, un servicio puede asumir un rol, para que esto ocurra se necesita implementar el *SDK* de AWs. Al intentar acceder a los buckets, se hará una llamada a la API de AWS. 
Si los roles están configurados para esta instancia, la API le dara las *access keys* temporales que serán las necesarias para asumir ese rol. 
Después de eso, la API se usará igual que cuando se tienen las credenciales normales

***Esto aun no lo entiendo al 100, necesito más practica y hacer más ejercicios***


**Nota**: Es importante tener en cuenta que los roles sólo funcionan en las intancias dentro de AWS, todas las que se encuentran fuera no funciona. Así como es necesario renovar las credenciales de acceso temporal.

## Grupo

Para crear un grupo "X" de IAM en AWS, se debe de generar un grupo y adjuntarle la política, muchas políticas ya están creadas en AWS.
   