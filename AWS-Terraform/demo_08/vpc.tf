# Internet VPC
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

# Subnets sólo habrá una subnet
resource "aws_subnet" "caro-main-public-1" {
  vpc_id                  = "${aws_vpc.caro-main.id}"
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = "true"
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-main-public-1"
  }
}

resource "aws_subnet" "caro-main-private-1" {
  vpc_id                  = "${aws_vpc.caro-main.id}"
  cidr_block              = "10.0.4.0/24"
  map_public_ip_on_launch = "false"
  availability_zone       = "us-west-1a"

  tags = {
    Name = "caro-main-private-1"
  }
}

### Internet GW
resource "aws_internet_gateway" "caro-main-gw" {
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
