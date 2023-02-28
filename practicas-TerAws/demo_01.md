### Primera Demo

La primera práctica que hice fue levantar una instancia con terraform, para probar que mi configuración e instalación fueron correctas.

Dividí mi práctica en cuatro archivos de terraform

1. instance.tf => Este contiene el recurso de instancia y el tag para ponerle nombre a la instancia

2. provider.tf => Se debe de agregar el proveedor con el que vamos a trabajar en terraform, para este caso es AWS

3. vars.tf => Este archivo contiene las variables que necesita la instancia, las cuales son:

    - ami

    - region

4. outputs.tf => EL archivo de salida nos va a servir para que al momento de crear la instancia nos muestre en la pantalla el ID y la IP pública de la instancia. Cabe aclarar que esto no es necesario para la creación de la instancia pero nos ayuda para tener la ip y no entrar a la consola AWS a buscar la ip de la instancia por si queremos conectarnos a ella via ssh.