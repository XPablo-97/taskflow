terraform {
    required_providers {
        aws = {
            source = "hashicorp/aws"
            version = "~> 5.0"
        }
    }
}
provider "aws" {
  region  = "eu-central-1"
  profile = "ADMIN-887540997584"

  default_tags {
    tags = {
      owner = "pablo.duarte@zoi.tech"
    }
  }
}