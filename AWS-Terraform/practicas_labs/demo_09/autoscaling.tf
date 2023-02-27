resource "aws_launch_configuration" "launchconfig" {
  name_prefix     = "caro-launchconfig"
  image_id        = "${lookup(var.AMIS, var.AWS_REGION)}"
  instance_type   = "t2.micro"
  key_name        = "${aws_key_pair.carokeypair.key_name}"
  security_groups = ["${aws_security_group.allow-ssh.id}"]
}

resource "aws_autoscaling_group" "group-autoscaling" {
  name                      = "group-autoscaling"
  vpc_zone_identifier       = [aws_subnet.caro-public-sb.id]
  launch_configuration      = aws_launch_configuration.launchconfig.name
  min_size                  = 1
  max_size                  = 2
  health_check_grace_period = 300 ### segundos
  health_check_type         = "EC2"
  force_delete              = true

  tag {
    key                 = "Name"
    value               = "caro_instance"
    propagate_at_launch = true
  }
}