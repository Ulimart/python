# Internet VPC
resource "aws_vpc" "caro" {
  cidr_block           = "10.0.0.0/16"
  instance_tenancy     = "default"
  enable_dns_support   = "true"
  enable_dns_hostnames = "true"
  enable_classiclink   = "false"
  tags = {
    Name = "caro-vpc"
  }
}

# Subnets 
resource "aws_subnet" "caro-public-sb" {
  vpc_id                  = "${aws_vpc.caro.id}"
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = "true" ### esto es para que se le dé una IP pública en el lanzamiento
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-public-sb"
  }
}

resource "aws_subnet" "caro-private-sb" {
  vpc_id                  = "${aws_vpc.caro.id}"
  cidr_block              = "10.0.2.0/24"
  map_public_ip_on_launch = "false" ### se le asigna false porque de esta manera sólo tendrá una IP privada
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-private-sb"
  }
}

### Internet GW, nos servirá porque la subred pública necesita estar conectada al internet de las cosas
resource "aws_internet_gateway" "caro-gw" { ### por lo que este recurso creará una puerta de enlace de internet en esta VPC
  vpc_id = "${aws_vpc.caro.id}"

  tags = {
    Name = "caro-gw"
  }
}

# route tables
resource "aws_route_table" "caro-public-rt" {
  vpc_id = "${aws_vpc.caro.id}"
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.caro-gw.id}"
  }

  tags = {
    Name = "caro-public-rt"
  }
}

# route associations public
resource "aws_route_table_association" "caro-public" {
  subnet_id      = "${aws_subnet.caro-public-sb.id}"
  route_table_id = "${aws_route_table.caro-public-rt.id}"
}
