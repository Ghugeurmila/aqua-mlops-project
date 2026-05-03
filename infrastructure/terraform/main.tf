resource "aws_security_group" "water_sg" {
  name = "water-level-sg"
  ingress { from_port = 5000; to_port = 5000; protocol = "tcp"; cidr_blocks = ["0.0.0.0/0"] }
  ingress { from_port = 8000; to_port = 8000; protocol = "tcp"; cidr_blocks = ["0.0.0.0/0"] }
}
