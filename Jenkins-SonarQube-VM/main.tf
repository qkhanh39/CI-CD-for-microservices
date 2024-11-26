resource "aws_instance" "web" {
  ami = var.ami_id
  instance_type = var.instance_type
  key_name = aws_key_pair.key_pair_for_web_instance.key_name
  
}

resource "aws_key_pair" "key_pair_for_web_instance" {
  key_name = "my_key_pair"
  public_key = ""
}