terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.92"
    }
  }

  required_version = ">= 1.2"
}



provider "aws" {
  region = "ap-south-1" # Mumbai
}

resource "aws_instance" "example" {
  ami           = "ami-0f918f7e67a3323f0" # Ubuntu 20.04 LTS // us-east-1
  instance_type = "t2.micro"
}
