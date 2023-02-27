### Internet VPC
resource "aws_vpc" "caro-main" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  enable_classiclink   = "false"
  tags = {
    Name = "caro-main"
  }
}

### Subnets, para esta demo decidí solo hacer una
resource "aws_subnet" "caro-main-public-1" {
  vpc_id                  = "${aws_vpc.caro-main.id}"
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = "true"  ### esto es para que se le dé uan IP pública en el lanzamiento
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-main-public-1"
  }
}

resource "aws_subnet" "caro-main-private-1" {
  vpc_id                  = "${aws_vpc.caro-main.id}"
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = "false" ### se le asigna false porque de esta manera sólo tendrá una IP privada
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-main-private-1"
  }
}

### Internet GW, nos servirá porque la subred pública necesita estar conectada al internet de las cosas
resource "aws_internet_gateway" "caro-main-gw" {  ### por lo que este recurso creará una puerta de enlace de internet en esta VPC
  vpc_id = "${aws_vpc.caro-main.id}"

  tags = {
    Name = "caro-main"
  }
}

# route tables
resource "aws_route_table" "caro-main-public" {
  vpc_id = "${aws_vpc.caro-main.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.caro-main-gw.id}"
  }

  tags = {
    Name = "caro-main-public-1"
  }
}

# route associations public
resource "aws_route_table_association" "caro-main-public-1-a" {
  subnet_id      = "${aws_subnet.caro-main-public-1.id}"
  route_table_id = "${aws_route_table.caro-main-public.id}"
}
