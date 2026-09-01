resource "aws_ecr_repository" "api" {
    name = "taskflow-api"
    image_tag_mutability = "MUTABLE"

    image_scanning_configuration {
        scan_on_push = true
    }
}

resource "aws_ecr_repository" "worker" {
    name = "taskflow-worker"
    image_tag_mutability = "MUTABLE"

    image_scanning_configuration {
        scan_on_push = true
    }
}