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