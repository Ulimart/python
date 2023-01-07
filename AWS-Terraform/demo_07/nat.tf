# nat gw
resource "aws_eip" "nat" { ### para poder tener el natgateway se necesita una IP estática EIP, en amazon lo llaman IP estática
  vpc = true
}

resource "aws_nat_gateway" "nat-gw" { ### 
  allocation_id = "${aws_eip.nat.id}"
  subnet_id     = "${aws_subnet.caro-main-public-1.id}"
  depends_on    = [aws_internet_gateway.caro-main-gw]
}

# VPC setup for NAT
resource "aws_route_table" "caro-main-private" {
  vpc_id = "${aws_vpc.caro-main.id}"
  route {
    cidr_block     = "0.0.0.0/0"
    nat_gateway_id = "${aws_nat_gateway.nat-gw.id}"
  }

  tags = {
    Name = "caro-main-private-1"
  }
}

# route associations private  
resource "aws_route_table_association" "caro-main-private-1-a" {  ### esto es completamente opcional si se quiere crear una subnet totalmente privada, no se debería agregar esta parte. 
  subnet_id      = "${aws_subnet.caro-main-private-1.id}"  ### toda esta seccion lo que hará es que se asocia con 
  route_table_id = "${aws_route_table.caro-main-private.id}"
}

##resource "aws_route_table_association" "main-private-2-a" {
##  subnet_id      = aws_subnet.main-private-2.id
##  route_table_id = aws_route_table.main-private.id
##}

##resource "aws_route_table_association" "main-private-3-a" {
##  subnet_id      = aws_subnet.main-private-3.id
##  route_table_id = aws_route_table.main-private.id
##}

