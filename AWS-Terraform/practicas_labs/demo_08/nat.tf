# nat gw
resource "aws_eip" "nat" { ### para poder tener el natgateway se necesita una IP estática EIP, en amazon lo llaman IP estática
  vpc = true
  tags = {
    Name = "caro-eip"
  }
}

resource "aws_nat_gateway" "nat-gw" { ### 
  allocation_id = "${aws_eip.nat.id}"
  subnet_id     = "${aws_subnet.caro-public-sb.id}"
  depends_on    = [aws_internet_gateway.caro-gw]
  tags = {
    Name = "caro-nat-gw"
  }
}

# VPC setup for NAT
resource "aws_route_table" "caro-private-rt" {
  vpc_id = "${aws_vpc.caro.id}"
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = "${aws_nat_gateway.nat-gw.id}"
  }

  tags = {
    Name = "caro-private-nat"
  }
}

# route associations private  
resource "aws_route_table_association" "caro-private-rt-asoc" {  ### esto es completamente opcional si se quiere crear una subnet totalmente privada, no se debería agregar esta parte. 
  subnet_id      = "${aws_subnet.caro-private-sb.id}"  ### toda esta seccion lo que hará es que se asocia con 
  route_table_id = "${aws_route_table.caro-private-rt.id}"
}



