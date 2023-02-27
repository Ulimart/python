#                IAM

- Gestión de identidad y acceso de AWS.

- Servicio que ayuda a controlar el acceso a los servicios de AWS

- Se pueden crear:

    - Roles

    - Grupos de usuarios

### Usuarios

- Pueden tener grupos. 

    - El grupo "administradores" pueden dar privilegios de admin a los usuarios.

- Pueden autenticarse

    - Usando el nombre de usuario y contraseña. Opcionalmente, con el uso de un token se tiene la autentificación multifactor, llamada **MFA**, se utiliza el software compatible con google authenticator.

    - Se puede utilizar un access key y una secret key (API keys), estas son usadas en las demos anteriores.

### Roles

Los roles son importantes ya que pueden dar los usuarios y servicios acceso temporal que normalmente no tendrían.

Los roles pueden ser atachados a las EC2, desde allí el usuario o servicio pueden obtener las credenciales de acceso. Con el uso de esas credenciales, el usuario/servici pueden asumir el rol que le da permiso para hacer algo. 

Ejemplo:

- Se creará un rol para un bucket, nombre: *"bucket-access"*, y se le asignará dicho rol a una instancia EC2 al momento del arranque.

- Los permisos del rol son: lectura y escritura, estos serán para los elementos que se tengan en ese bucket.

- Al momento de conectarse, se asumirá el rol de acceso al bucket y sin usar las credenciales personales.

- Ahora se puede leer y escribir en ese bucket

- En vez de que un usuario utilice *aws-cli*, un servicio también puede asumir un rol.

- El servicio necesita implementar el **AWS SDK**

- Si se intenta accesar a un s3 bucket, se hará una llamada a la API de AWS. 

- Si los roles están configurados para esta instancia, la API de AWS dará las claves de acceso para asumir el rol.

- Después de eso, la API se usaría igual que cuando se tienen las credenciales normales/personales. 

En resumen, cuando se utiliza  AWS SDK, en el background se accederá a otro servicio de AWS (VOLVER A CHECAR)

Es importante tener en cuenta que los role IAM sólo funcionan en instancias EC2 y no en instancias fuera de AWS; es decir, que si se tiene un servicio fuera de AWS, no se podrá asumir el rol, ya que los *roles IAM* sólo funcionan *dentro de la red de AWS*.

Se necesita renovar las credenciales de acceso temporal, ya que sólo son válidas por un tiempo definido. 

    - El AWS SDK se ocuprá de esto.

### ***Permisos***

¿Por qué se crean los usuarios y grupos?

Los usuarios representan a una persona dentro del proyecto/organización. Estos usuarios se pueden agrupar juntos.  

Entonces, los usuarios y grupos se crean para poder permitir el uso de las cuentas de AWS, así que se les otorga permisos. 

Para hacer esto posible se les asigna mediante una un documento json una política de IAM. En esta política se describe que tienen permitido hacer y en que grupo se encuentran los usuario.

En AWS se aplica un principio llamado *principio de privilegio mínimo*. ENtonces no dará más permisos de los que necesita el usuario.

### Creación

- Para crear un grupo de *IAM administratos* en AWS, se genera el grupo y este se adjunta a la politica Administrator en AWS. O sea, se tiene un grupo y las politicas que ya creadas en AWS, y se pueden adjuntar.

Ejemplo:

                resource "aws_iam_group" "administrators" {  ## se crea el grupo y se le asigna un nombre
                  name = "administrators"
                }
                       ## este se va a adjuntar a la política, ya que el grupo no tiene NI UN ACCESO
                resource "aws_iam_policy_attachment" "administrators-attach" {
                  name       = "administrators-attach"
                  groups     = [aws_iam_group.administrators.name]
                  policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess"  ## Este es el nombre de la política, la cual ya estaba creada en AWS
                }

- Cualquier usuario añadido a este grupo tendrá acceso de admiiiiiiiiiiiiiiiiiiiiiiiiiiiiin!!!!!!

- Es importante tener en cuenta que se pueden crear *políticas personalizadas*.

Ejemplo:

                resource "aws_iam_group" "administrators" {  ## a este grupo se le adjuntará una política personalizada
                  name = "administrators"
                }

                resource "aws_iam_group_policy" "my_developer_policy" {
                  name = "my_administrators_policy"
                  role = aws_iam_group.administrators.id
                  policy = <<EOF
                {
                  "Version": "2012-10-17",
                  "Statement": [ ## se va a crear un statement policy, este debe de contener los 3 puntos de abajo
                   {
                     "Effect": "Allow", ## permite o deniega
                     "Action": "*",     ## Esto es para *todo*, ya que tiene el *
                     "Resource": "*"    ## En este caso es para *todos* los recursos
                   }
                  ]
                }
                EOF
                }

- Esta política va a permitir cada acción a cada recurso de AWS, a esto se le llamará *acceso de admin* :)

- Por último, se crea un usuario y le asignará un grupo. Bueeeeeeeeeeeeeeeeeeeeeeeno en este ejemplo se crearon dos usuarios:

                resource "aws_iam_user" "admin1" {
                  name = "admin1"
                }

                resource "aws_iam_user" "admin2" {
                  name = "admin2"
                }

                resource "aws_iam_group_membership" "administrators-users" {  ## aqui se añade los usuarios a los grupos
                  name = "administrators-users"
                  users = [
                    "${aws_iam_user.admin1.name}",
                    "${aws_iam_user.admin2.name}",
                  ]
                  group = aws_iam_group.administrators.name
                }
