resource "aws_instance" "caro-public-ins" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"

  ### the VPC subnet
  subnet_id = "${aws_subnet.caro-public-sb.id}"

  ### the security group
  vpc_security_group_ids = ["${aws_security_group.allow-ssh.id}"]

  ### the public SSH key
  key_name = "${aws_key_pair.carokeypair.key_name}"

  tags = {
    Name = "caro-public-ins"
  }
}

resource "aws_instance" "caro-private-ins" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"

  ### the VPC subnet
  subnet_id = "${aws_subnet.caro-private-sb.id}"

  ### the security group
  vpc_security_group_ids = ["${aws_security_group.allow-ssh.id}"]

  ### the public SSH key
  key_name = "${aws_key_pair.carokeypair.key_name}"

  tags = {
    Name = "caro-private-ins"
  }
}