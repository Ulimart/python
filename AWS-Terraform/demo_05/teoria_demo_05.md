#                   DATASOURCES

Para algunos proveedores, en este caso me voy a enfocar en AWS, terraform proporciona datasources. Estos facilitan información dinámica. 
    - AWS dispone de muchos datos en un formato estructurado mediante su API. Por lo que terraform expone está info usando los datasources. Ejemplo:
        - Listas de AMIs
        - Listas de Zonas de disponibilidad.

Estos dos ejemplos son info dinámica, ya que cambia. Se puede usar como parte del input de terraform. Otro ejemplo, es un datasource que da todas las direcciones IP en uso por AWS. 
    - El tener la lista de IPs ayuda a filtrar el tráfico basado en una región de AWS, ya que se sabrá que dirección IP está en uso en alguna región de interés. Es decir, sólo se permitiría ciertas direcciones de la lista de IP.

En relación con la filtración de tráfico en AWS, se puede usar los *security groups* (SG). 
    - El tráfico entrante y saliente se puede filtrar por:
            - Protocolo (TCP, UDP, ICMP)
            - Rango de IP (puede ser 1 - 1000 IPs)
            - Puertos (SSH => 22, HTPP => 80)
    
