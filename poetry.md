#                       POETRY

### ***¿Qué es poetry?***

Herramienta que ayuda a gestionar dependencia de paquetes para la parte de construcción y publicación.

### ***Características***

- Pyproject.toml como fichero de dependencias

- Lock de dependencias, marca las dependencias usadas en el desarrollo del proyecto/paquete

- Gestión de entornos virtuales dentro de la misma herramienta

- Exportación de requierments.txt, es decir que de .toml => .txt para un sistema antiguo o para otro sistema

- Shell Completition, es el autocompletado (creo que es con el tab) 

- Python version management con pyenv, se refiere a que puede pasar de version 

- Package publishing, o sea que ayuda a la construcción y publicación de paquetes mucho más fácil.

### ***Instalación***

*pip install poetry*

*curl...* (Agregar linea)

- Para *actualizarlo*

*poetry self update*

### ***Comandos más usados***

Creación del proyecto desde cero

- *poetry new (name)*

Este agrega carpetas, fichero .toml, etc etc

Si ya se llega a tener un proyecto/paquete y se quiere incorporar poetry en él, primero se coloca en la carpeta de ese proyecto y se ejecuta el siguiente comando:

- *poetry init*

Para la gestión de dependencias se modifica el fichero *pyproject.toml*, tiene apartados en el que se encuentran las dependencias y si se requiere modificar alguno: 

- *poetry add (nombre de la dependencia)*

***Dev Dependencies***

- Se crean dependencias *sólo en el entorno de desarrollo*, no serán incluidas en el de construcción y desplieguem, por lo que hay que descargar librerias.

- Util para librerias test. linters o de tipo estático

- Se debe usar el prefijo **-D** 

Comando:

- ***poetry add -D (nombre)***

***Entornos virtuales***

- Poetry detectará si hay entornos virtuales por lo que se asociará a el

- En caso de no tener un entorno viertual, lo creará

- Para ejecutar comandos en el entorno virtual hay varias formas:

    - Lanzar comandos directamente:

        ***poetry run python my_script.py***  (CHECAR)
    
    - Entrar directamente en shell

        ***poetry shell***

- ***poetry.lock***

Esto previene que se instale la última versión de las dependencias y dentro del fichero lock se guarda la referencia y su has code. Este fichero es recomendable incluirlo en el repositorio porque mantendrá la versión que se desea.

*Instalando dependencias*

- ***poetry install***

Lo primero que hará poetry es buscar el fichero .lock, si existe ese archivo poetry instalará la dependencia de ese fichero y si no se tiene el .lock, entonces poetry instalará la última versión y agregará ese archivo.

*Construcción de proyecto*

- ***poetry build***

Se usa ese comando para construir el proyecto y al estar todo configurado en el fichero pyproject.toml ya no hay más que hacer.
Se creará una carpeta llamada *dist*, en ella contendrá los ficheros *sdist* y *wheel*

*Publicación*

- ***poetry publish***

Con este comando se subirá el paquete al pypi, se necesitan credenciales, certificados, etc. 

Se tienen parámetros para escocger el repositorio, ya sea público (pypi indez es por default) o privado. También se puede simular la publicación con el comando **--dry-run**

- ***poetry config***

Ayuda a settear valores en el fichero de configuración

- ***poetry export***

Esporta el requirements.txt

- ***poetry check***

Comprueba la estructura del pyproject.toml

- ***poetry search***

Busca paquetes en indices remotos, públicos o privados


