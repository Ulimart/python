provider "aws" {
  access_key = " "
  secret_key = " "
  region     = "us-west-1"
}

resource "aws_instance" "caro" {
  ami           = "ami-0454207e5367abf01"
  instance_type = "t2.micro"
}
