#                   TERRAFORM STATE

Terraform guarda el estado remoto de la infraestructura en un archivo llamado:
                    - ***terraform.tfstate***

Este archivo tiene una copia de seguridad del estado anterior, este archivo se llama:
                    - ***terraform.tfstate.backup***

Cuando se ejecuta el terraform apply, se crean ambos archivos, esto ayuda a mantener el seguimiento del estado remoto. Si llega a cambiar el estado remoto y ejecutas el apply de nuevo, terraform hará los cambios para cumplir con el estado remoto correcto. Por ejemplo:
                - Al terminar una instancia gestionada por terraform, al volver a aplicar el apply, esta instancia se iniciará de nuevo.

Se puede quedar con el terraform.tfstate en el control de versiones con el uso de git (por ejemplo). Lo cual dará un historial del terraform.tfstate, el cual es un gran archivo JSON. Esto permitirá colaborar con otros miembros del equipo/proyecto. Sin embargo, se pueden tener conflictos con *git* al trabajar al mismo tiempo dos miembros del equipo/proyecto, por lo que se debe de hacer *git push* y *git pull* para asegurarse de que se está trabajando en la últmia versión.

El estado local trabajará bien al principio, pero cuando el proyecto crece, lo más recomendable es que se guarde de manera remota. Para ser guardado de manera remota se usando el *backend functionality* en terraform.

- El backend por defecto se llama *local backend*, es ell archivo de estado que se ha utilizado hasta ahora. 

- Otros backends que pueden ser usados:
            - s3, este tiene un mecanismo de bloqueo que usa Dynamo DB en Amazon.
            - consult, este también tiene un mecanismo de bloqueo.
            - terraform enterprise, esta es una solución comercial

- El uso del *backend functionality* tiene beneficios, los cuales son:
            - Trabajo en equipo: Permitirá la colaboración, el estado remoto siempre estará disponible para todo el equipo. Si tu backend soporta el bloqueo como el *s3* y *consult*, entonces no habrá problemas y sólo una persona podrá actualizar el archivo de estado al mismo tiempo.

            - El archivo de estado tampoco se almacenará localmente y la info sensible ya no estará disponible localmente, sino remotamente.

            - Algunos backends permiten operaciones remotas. El *terraform apply* se ejecutará de forma remota. A este tipo de backends se les llama mejorados.

Hay dos pasos para configurar el estado remoto:
            1. Se añade código al archivo.tf
            2. Se ejecuta el proceso de inicialización