#                   ELB hecho en Terraform

En este documento se va a repasar un **ELB**, se comenzará con el *Clásico*

Este es un claro ejemplo de como se puede construir uno en *terraform*

                resource "aws_elb" "my-elb" { <= comenzamos con un recurso
                  name            = "my-elb"
                  subnets         = ["${aws_subnet.main-public-1.id, aws_subnet.main-public-2.id}"] <= Si se una una *VPC* (lo cual es MUY RECOMENDABLE), se definen las subredes donde estará el ELB. Es importante recordar que este *ELB* se unirá a las *subredes públicas*.                
                  security_groups = ["${aws_security_group.elb-securitygroup.id}"] <= se definirá un grupo de seguridad, el cual va a permitir el puerto 80 y 443 para SSL. Lo que hará que cuando alguien accesa a la sitio web, pasa através del ELB, entonces se necesita ser aceptado por el puerto 80 para el tráfico normal.
                
                  listener {
                    instance_port     = 80 <= aqui el puerto de la instancia                    
                    instance_protocol = "http" <= y el protocolo
                    lb_port           = 80 <= al observar el puerto y el protocolo del LB son iguales que el de la instancia., por lo que el tráfico entrará por el puerto 80 y será reenviado a la instancia por medio del puerto 80. 
                    lb_protocol       = "http"
                  }

                  health_check { 
                    healthy_threshold   = 2 <= Al añadirse una nueva instancia debe de tene, al menos, dos *healthy checks* antes de que el tráfico se envie a ella.
                    unhealthy_threshold = 2 <= Si una instancia activa es monitorada dos veces y estos chequeos no era saludable, entonces el LB no enviará más tráfico a esta.
                    timeout             = 3 <= esto es en segundos                    
                    target              = "HTTP:80/" <= aquí se comprobará, es decir, se hará una conexión, se entrará al sitio web y se comprobará si la página principal es saludable. Se puede agregar *"/health.php"* o *"/health.html"* para hacer comprobaciones de salud en una página especifíca.                    
                    interval            = 30 <= en segundos, tiempo para comprobar si la instancia está healthy.
                }

                  instances = ["${aws_instance.example-instance.id}"] <= lista de instancias, esta línea es opcional. Por lo que este ELB se puede añadir a un ASG. Así que puedes tener una lista estática o un ASG.                
                  cross_zone_load_balancing   = true <= significa se permitirá el equilibrrio de carga entre zonas; es decir, que podemos tener una instancia en una subred, pero el ELB que maneja el tráfico en otra subred.                 
                  connection_draining         = true <= esto sirve para darle un tiempo de espera a la eliminación de la instancia, ya que puede que durante ese tiempo siga recibiendo información.                
                  connection_draining_timeout = 400 <= Con este tiempo (segundos) vamos a asegurar que ya dejará de pasar contenido.
                
                  tags = {
                    Name = "my-elb"
                  }
                }