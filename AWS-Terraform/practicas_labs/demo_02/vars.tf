variable "AWS_ACCESS_KEY" {
}

variable "AWS_SECRET_KEY" {
}

variable "AWS_REGION" {
  default = "us-west-1"
}

variable "AMIS"{
  type    = map
  default = {
    us-west-1 = "ami-0454207e5367abf01" ### ESTA ES!!!
    us-west-2 = "ami-0688ba7eeeeefe3cd"
    eu-west-1 = "ami-0f29c8402f8cce65c"
  }
}

variable "PATH_TO_PRIVATE_KEY" {
  default = "/sicretsss/mykey"
}

variable "PATH_TO_PUBLIC_KEY" {
  default = "/sicretsss/mykey.pub"
}

variable "INSTANCE_USERNAME" {
  default = "ubuntu"
}