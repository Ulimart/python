#                   ***LOAD BALANCER (LB/ELB)**

Ya que se tiene instancias autoescalables, es recomendable tener un LB por delante.

El AWS ***Elastic Load Balancer (ELB)***, distribuye autmóticamente el tráfico entrante entre varias instancias de EC". 

*Características del ELB:*

  - Se escala cuando recibe más tráfico

  - Hace *healthcheck* de las instancias

  - Si no pasa el *healthcheck*, no se enviará tráfico a esta.

  - Añade automáticamente las nuevas instancias agregadas al ASG y comienza el *healthcheck* de esta.

  - Puede usarse como terminador SSL 

     - Descarga el cifrado fuera de las instancias EC2, así cuando se visita un sitio web con un ELB por delante, este hará la encriptación y el tráfico entre las instancias y el ELB no necesita ser encriptado ya que esa es la red interna.

     - AWS puede gestionar los certificados SSL, los certificados serán gratuitos.

  - Pueden repartise en múltiples zonas de disponibilidad para una mayor tolerancia de fallos. Es decir, si una zona falla por completo, el ELB seguirá funcionando en otra zona.

  - En general, tendrá mayores niveles de tolerancia de fallos en el tráfico ruta (DUDA)

  - Se compara con Nginx/HAProxy, perooo AWS te ofrece el servicio de ELB, hay dos tipo de LB:

     i) El clasico Load Balancer (ELB)
       
         - Este enruta el tráfico basado en la información de red, por ejemplo: 
            
            - envia todo el tráfico desde el puerto 80 (HTTP) hacia el puerto 8080 (que sería el puerto de la aplicación)

     i) Aplication Load Balancer (ALB)
        
         - Enruta el tráfico basado en la información a nivel de aplicación, por ejemplo:

            - puedes enrutar una api y una website (algo.com) a diferentes instancias EC2. Así quue dependiendo de la ruta que se escriba en el navegador, podría terminar en una instancia diferente.