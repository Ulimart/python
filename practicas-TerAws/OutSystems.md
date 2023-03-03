### Taggear instancias y leer/devolver tags

1. Se requería crear tags a la instancia en uso por medio de un código en powershell.

2. En el caso de que la instancia en uso tuviera tags, con un código en python, debían ser leídas e imprimirlas para ser utilizadas.

Este trabajo se debía de hacer en una instancia con un server de Windows 2019 Base, así fue el requerimiento. Para trabajar de manera más sencilla, se levantó la instancia en la consola de AWS.

Para poder entrar a la instancia, no fue por medio de SSH, sino por medio de *Cliente de RDP*:

- Se descarga el archivo de escritorio remoto

- Te pedirá la contraseña, la cual se obtiene con la key.pem

- Se conecta a una instancia que es identica a la que vemos en nuestras laptops.

A la instancia se le instaló python3.10, en el caso de powershell no fue necesario, ya que venía instalado.

No pude instalar visual studio code para trabajar, también se intentó con *atom* y *sublime*, pero tampoco pudimos, así que trabajamos con *Notepad*

1. **Taggear**

$accesskey = ' '
$secretkey = ' '
$region = ' ' 

#Create a new Amazon Powershell session
Initialize-AWSDefaultConfiguration -AccessKey $accesskey -SecretKey $secretKey -Region $region

#Get the ID of the EC2 instance you want to tag
$instanceId = ' '

#Define the tags yoy want to apply to the instance
#One tag
#$tags = New-Object Amazon.EC2.Model.Tag
#$tags.Key = "Name"
#$tags.Value = "caro_instance"

#Two or more tags
$tags = @()
$1tags=New-Object Amazon.EC2.Model.Tag;$1tags.Key = "Name";$1tags.Value = "caro_instance";$tags += $1tags
$2tags=New-Object Amazon.EC2.Model.Tag;$2tags.Key = "chilaquiles";$2tags.Value = "verdes";$tags += $2tags
Write-Host 'Hola2'
Write-Host $tags

#Use the New-EC2Tag command to tag the instance
New-EC2Tag -Resource $instanceId -Tag $tags
Write-Host 'Hello, world!'

2. **Leer/print**

import os
import sys 
import boto3
from boto3 import Session

os.environ['AWS_ACCESS_KEY'] = ' '
os.environ['AWS_SECRET_KEY'] = ' '
os.environ['REGION'] = ' '

AWS_ACCESS_KEY = os.environ.get('AWS_ACCESS_KEY')
AWS_SECRET_KEY = os.environ.get('AWS_SECRET_KEY')
REGION = os.environ.get('REGION')

session = boto3.Session(
    aws_access_key_id = AWS_ACCESS_KEY,
    aws_secret_access_key = AWS_SECRET_KEY,
    region_name=REGION
)

ec2 = session.client('ec2')

#Specify the instance ID for which you want to get the tag
instance_id = ' '

#Use the describe_tags method to get the tags for the specified instance
response = ec2.describe_tags(
    Filters=[
        {
            'Name':'resource-id',
            'Values': [
                instance_id,
            ],
        },
    ],
)

print('****************** The response is: *****************************', response)
#Extract the tag key-value pairs form the response
tags = {}
for tag in response['Tags']:
    tags[tag['Key']] = tag['Value']

#print the tags for the instance
print(f'Tags for instance {instance_id}:')
for key, value in tags.items():
    print(f'\t{key}:{value}')
print("hello world")
