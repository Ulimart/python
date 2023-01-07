resource "aws_security_group" "allow-ssh" {
  vpc_id      = "${aws_vpc.caro-main.id}"
  name        = "allow-ssh"
  description = "este SEG permitirá la conexión ssh y todo el tráfico de salida"
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "allow-ssh"
  }
}
