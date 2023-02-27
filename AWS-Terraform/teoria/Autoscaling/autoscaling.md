#                   ***AUTOSCALING***

En AWS se creanm los autoscaling groups para añadir/eliminar automáticamente instancias cuando se llega a determinados umbrales. 

Por ejemplo, si se tiene mucha afluencia en alguna app, el autoscaling ayudará a ampliar el numero de instancias en esos momentos. Esto puede llevarse a cabo basándose en el uso del CPU, la memoria o el ancho de banda.

###  ***Configuración:***

- Al menos se deben de configurar dos recursos

    - Configuración de lanzamiento, en donde se especificará las propiedades de la instancia

        - ID de la AMI
        
        - Grupo de seguridad

    - Un autoscaling group, se especificará las propiedades de la escala

        - minimo de instancias

        - máximo de instancias

        - health checks

    Ya que si una instancia deja de funcionar, el autoscaling iniciará una nueva.

El siguiente paso es tener un *autoscaling policy*

    - Una política es activada en función a un threshold, que sería Cloudwatch, cuando el treshold es activado el autoscaling policy será ejecutada.

    - Ejemplo:

        - Si el uso del CPU es mayor al 20%, entonces la se activará la alarma y se aumentará el numero de instancias

        - En el caso que el uso del CPU sea menor al 5%, la alarma se activará y se reduciría una instancia

Se debe de tener en cuenta que el aumento o reducción es configurable

La Configuración del autoscaling debe de ser creada, tomando como ejemplo:

                resource "aws_launch_configuration" "example-launchconfig" { ## esta será la config de lanzamiento
                  name_prefix     = "example-launchconfig" <= se debe especificar el prefijo del nombre
                  image_id        = "${lookup(var.AMIS, var.AWS_REGION)}" <= también el ID de AMI que será lanzada, será el mismo ID cuando se lanzan múltiples instancias.
                  instance_type   = "t2.micro"
                  key_name        = "${aws_key_pair.mykeypair.key_name}" <= Se deben de tener las llaves
                  security_groups = ["${aws_security_group.allow-ssh.id}"] <= Los grupos de seguridad
                }

                resource "aws_autoscaling_group" "example-autoscaling" { <= ahora se configurará el grupo
                  name                      = "example-autoscaling" <= nombre
                  vpc_zone_identifier       = ["${aws_subnet.main-public-1.id}", "${aws_subnet.main-public-2.id}] <= Se debe especificar el identificador de la zona de la VPC, aquí solo se marca en que subredes se van a lanzar las instancias. También se detalla multiples subredes y en cual de ellas irán las instancias.
                  launch_configuration      = "${aws_launch_configuration.example-launchconfig.name}" <= esta se relaciona con la configuración de lanzamiento, que es la de arriba
                  min_size                  = 1 <= es el numero de instancias, así que sería una , así comenzaría con 1 instancia y luego tendría que ocurrir otro evento de escalado para que llegue a dos (máx)
                  max_size                  = 2 <= acá el máximo de instancias serían dos
                  health_check_grace_period = 300 <= este es un perido en segundos, por lo que son 5 minutos
                  health_check_type         = "EC2" <= el tipo de chequeo de salud, normalmente lo hae el Load Balancer, pero hasta aquí no tenemos, así que usaremos  EC2
                  force_delete              = true <= cuando las instancias son expulsadas del autoscaling serán eliminadas automáticamente

                  tag { <= esto nos servirá que cada vez que se genere otra instancia se le especificará, automáticamente, un nombre
                    key                 = "Name"
                    value               = "ec2 instance"
                    propagate_at_launch = true
                  }
                }

Hasta aquí no tenemos una politica por lo que si se requiere un escalado, tendría que ser manual. Si queremos un aumento dinámico o disminución de instancias, se debe de crear una política. La cual se generará por medio de terraform.

## AutoScaling Group (ASG)

                resource "aws_autoscaling_policy" "example-cpu-policy" {
                  name                   = "example-cpu-policy" <= esta politica es para el CPU, la cual se vinculará al ASG
                  autoscaling_group_name = "${aws_autoscaling_group.example-autoscaling.name}" <= este el el ASC al cual se vinculará
                  adjustment_type        = "ChangeInCapacity" <= En cuanto se active la política, hará un ajuste en la capacidad.
                  scaling_adjustment     = "1" <= El cual será sólo uno, si se requiere una reducción se tendría que poner un "-1"
                  cooldown               = "300" <= período en el que NO se pueden producir eventos de escalamiento
                  policy_type            = "SimpleScaling" <= indica el tipo de política 
                }

Se puede crear la alarma de CloudWatch

                resource "aws_cloudwatch_metric_alarm" "example-cpu-alarm" {
                  alarm_name          = "example-cpu-alarm"
                  alarm_description   = "example-cpu-alarm"
                  comparison_operator = "GreaterThanOrEqualToThreshold" <= Se compara la utilización del CPU mayor o igual que los thresholds
                  evaluation_periods  = "2" <= se van a comparar dos periodos de evaluación, por lo que se va a tomar la media de dos periodos y luego compararlos, por lo que tiene que ser más alto que un threshold.
                  metric_name         = "CPUUtilization" <= por lo que se va a nombrar así 
                  namespace           = "AWS/EC2"
                  period              = "120" <= segundos
                  statistic           = "Average"
                  threshold           = "30" <= esto es en porcentaje, por lo que debe de ser 30%, si la media es mayor a ese % durante el periodo estipulado arriba (120s) para los periodos de evaluación (2), la alarma se disparará y tendremos el autoscaling

                  dimensions = {
                    "AutoScalingGroupName" = "${aws_autoscaling_group.example-autoscaling.name}" <= se especifica el nombre del ASG 
                }

                  actions_enabled = true
                  alarm_actions   = ["${aws_autoscaling_policy.example-cpu-policy.arn}"] <= Acción de la alarma donde se hace referencia a la política
                }

Ahora, si se requiere una alerta, como por ejemplo un correo, cuando se invoca el AS se tendrá que crear un SNS (Simple Notification Service). Así que se creará un recurso:

                resource "aws_sns_topic" "example-sns" {
                 name         = "sg-sns" <= se le asigna un nombre
                 display_name = "example ASG SNS topic" 
                } 

Es importante mencionar que se debe de usar la consola de AWS porque la suscipción por correo no está dentro de las recursos de terraform, porque sólo obtienes el identificador del ARN 