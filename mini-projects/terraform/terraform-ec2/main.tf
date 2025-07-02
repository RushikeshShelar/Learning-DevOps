provider "aws" {
    region = "ap-south-1"
}

resource "aws_security_group" "devops_sg" {
    name        = "devops_security_group"
    description = "Allow SSH and HTTP access"

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"] # Allow SSH from anywhere

    }
}

resource "aws_instance" "devops_ec2" {
    ami = "ami-0f918f7e67a3323f0" # Ubuntu 24.04 LTS
    instance_type = "t2.micro"
    key_name = "Rushi-Laptop-EC2"
    security_groups = [aws_security_group.devops_sg.name]

    tags = {
        Name = "DevOps-EC2"
    }
}


resource "aws_s3_bucket" "devops_bucket" {
    bucket = "rushi-devops-aws-s3-bucket"

    tags = {
        Name        = "My bucket"
        Environment = "Dev"
    }
}

