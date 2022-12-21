#                   COMANDOS de TERRAFORM

Terraform está centrado en las *definiciones de recursos*, pero tiene un conjunto *limitado de herramientas* disponibles para modificar, importar y crear estas definiciones de recursos. Sin embargo, en cada nueva versión aparecen nuevas funciones que facilitan el manejo de los recursos.

Checar TERRAFORMING.

|Comando            |Descripción                                                                                |
|:-----:            |:----:                                                                                     |
|terraform apply    |Aplica el estado                                                                           |
|destroy            |Destruye el estado gestionado por terraform                                                |
|fmt                |Reescribe los archivos de configuración de Terraform a un formato y estilo canónico. Esto formatea el código. Por lo tanto, normalmente se utiliza este comando antes de confirmar los cambios para asegurarse de que el formato es correcto                                                                        |
|get                |Descarga y actualiza módulos                                                               |
|graph              |Se utiliza para crear una representación visula de una configuración o plan de ejecución. Así que si se tiene un montón de archivos Terraform se puede utilizar este comando y se creará una representación gráfica                                                                                                         |
|import [options] ADDRESS ID |Esta importación intentará encontrar el recurso de infra identificado con el ID e importará un estado en terraform.tfstate con la dirección ID del recurso                                        |

