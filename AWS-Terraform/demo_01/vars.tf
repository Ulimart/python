variable "AWS_ACCESS_KEY"{
}

variable "AWS_SECRET_KEY"{
}

variable "AWS_REGION"{
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
