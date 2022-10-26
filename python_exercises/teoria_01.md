                                                    GIT:

Git es un Sistema de Control de Versiones Distribuido (DVCS) utilizado para guardar diferentes versiones de un archivo (o conjunto de archivos) para que cualquier versión sea recuperable cuando lo desee.
También facilita el registro y comparación de diferentes versiones de un archivo. Esto significa que los detalles sobre qué cambió, quién cambió qué, o quién ha iniciado una propuesta, se pueden revisar en cualquier momento.

    Con referencia a "distribuido" significa que cuando le instruyes a Git que comparta el directorio de un proyecto, Git no sólo comparte la última versión del archivo. En cambio, distribuye cada versión que ha registrado para ese proyecto.

    En el caso de un Sistema de Control de Versiones (VCS) se refiere al método utilizado para guardar las versiones de un archivo para referencia futura. 
    El caso más usado para guardar las distintas versiones de un mismo archivo es, por ejemplo, hola01.py, hola02.py, hol03.py, etc. Pero esta forma de abordarlo es propenso a errores y inefectivo para proyectos grupales.
    Por lo que con esto podemos resaltar la importancia de Git, ay que usamos un sistema de control de versiones confiable y colaborativo.

                                            ESTADOS DE LOS ARCHIVOS:

En Git hay tres etapas primarias (condiciones) en las cuales un archivo puede estar:

1) Estado modificado (Modified)
Un archivo en el estado modificado es un archivo revisado – pero no acometido (sin registrar).

En otras palabras, archivos en el estado modificado son archivos que has modificado pero no le has instruido explícitamente a Git que controle.

2) Estado preparado (Staging)
Archivos en la etapa preparado son archivos modificados que han sido seleccionados – en su estado (versión) actual – y están siendo preparados para ser guardados (acometidos) al repositorio .git durante la próxima instantánea de confirmación.

Una vez que el archivo está preparado implica que has explícitamente autorizado a Git que controle la versión de ese archivo.

3) Estado confirmado (Commit)
Archivos en el estado confirmado son archivos que se guardaron en el repositorio .GIT exitosamente.

Por lo tanto un archivo confirmado es un archivo en el cual has registrado su versión preparada en el directorio (carpeta) Git.

Tip: tengamos en cuenta que el estado de un archivo determina la ubicación donde Git lo colocará.

                                        UBICACIÓN

¿Dónde se encuentran los archivos???
Existen tres lugares principales donde pueden residir las versiones de un archivo cuando se hace control de versiones con Git:

1) Directorio de trabajo (Working directory)
El directorio de trabajo es una carpeta local para los archivos de un proyecto. Esto significa que cualquier carpeta creada en cualquier lugar en un sistema es un directorio de trabajo.
    * Los archivos en el estado modificado residen dentro del directorio de trabajo.
    * El directorio de trabajo es distinto al directorio .git. Es decir, tu creas un directorio de trabajo mientras que Git crea un directorio .git.

2) Zona de preparación (Staging area or index)
La zona de preparación – técnicamente llamado “index”  en lenguaje Git  – es un archivo normalmente ubicado en el directory .git, que guarda información sobre archivos próximos a ser acometidos en el directorio .git.
    
3) Directorio Git
El directorio.git es la carpeta (también llamada "repositorio") que Git crea dentro del directorio de trabajo que le has instruido para realizar un seguimiento.
La carpeta .git también es donde Git guarda las bases de datos de objetos y metadatos de los archivos que le hayas instruido realizar un monitoreo.
    * El directorio.git es la vida de Git – es el item copiado cuando se clona un repositorio desde otra computadora (o desde una plataforma en línea como GitHub).
    * Los archivos en el estado acometido residen en el directorio Git.

En la imagen (flujo_git.png) se puede observar como es el flujo en git.

1) Modificar archivos en el directorio de trabajo. (Aquí estoy trabajando en la carpeta de mi lap)
   Observe que cualquier archivo que modifiques se convierte en un archivo en el estado modificado.
   
2) Prepare selectivamente los archivos que quieras confirmar al directorio .git. ()
   Observe que cualquier archivo que prepares (agregues) a la zona de preparación se convierte en un archivo en el estado preparado.  
   También tenga en cuenta que los archivos preparados todavía no están en la base de datos .git.
   Preparar significa que la información sobre el archivo preparado se incluye en un archivo (llamado "index") en el repositorio .git.
         
           En este caso hago "git add ." o "git add (nombre del archivo)" y te esta manera ya lo tendré en mi staging area. 

3) Confirme los archivos que has preparado en el directorio .git. 
   Es decir, guardar de manera permanente una "copia" de los archivos preparados en la base de datos .git.
   Observe que cualquier versión del archivo que confirmes al directorio .git se convierte en un archivo en el estado confirmado.

           Usamos git commit -m "(mesaje)" , es muy importante agregar, o buena practica, el comentario, así facilita el ver los cambios hechos.

                                        GITHUB:

Es una plataforma basada en la web donde los usuarios pueden alojar repositorios Git. Facilita compartir y colaborar fácilmente en proyectos con cualquier persona en cualquier momento.