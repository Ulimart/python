resource "aws_key_pair" "carokeypair" {
  key_name   = "carokeypair"
  public_key = "${file(var.PATH_TO_PUBLIC_KEY)}"
}
