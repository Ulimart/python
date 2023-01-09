variable "AWS_REGION" {
  default = "us-west-1"
}

variable "PATH_TO_PRIVATE_KEY" {
  default = "/sicretsss/carokey"
}

variable "PATH_TO_PUBLIC_KEY" {
  default = "/sicretsss/carokey.pub"
}

variable "AMIS" {
  type = map
  default = {
    us-west-1 = "ami-0454207e5367abf01"
    us-west-2 = "ami-06b94666"
    eu-west-1 = "ami-844e0bf7"
  }
}
