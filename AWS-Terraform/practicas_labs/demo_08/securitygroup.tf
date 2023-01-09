resource "aws_security_group" "allow-ssh" {
  vpc_id      = "${aws_vpc.caro.id}"
  name        = "allow-ssh"
  description = "este SEG permitira la conexion ssh y todo el trafico de salida"
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
