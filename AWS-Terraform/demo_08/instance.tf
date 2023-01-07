resource "aws_instance" "caro" {
  ami           = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type = "t2.micro"

  ### the VPC subnet
  subnet_id = "${aws_subnet.caro-main-public-1.id}"

  ### the security group
  vpc_security_group_ids = ["${aws_security_group.allow-ssh.id}"]

  ### the public SSH key
  key_name = "${aws_key_pair.carokeypair.key_name}"
}