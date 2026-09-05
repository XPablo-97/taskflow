resource "aws_security_group" "rds" {
  name        = "taskflow-rds-sg"
  description = "RDS - solo acceso desde el bastion"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port       = 5432
    to_port         = 5432
    protocol        = "tcp"
    security_groups = [aws_security_group.bastion.id]
  }

  tags = {
    Name = "taskflow-rds-sg"
  }
}

resource "aws_db_subnet_group" "main" {
  name       = "taskflow-db-subnet-group"
  subnet_ids = [aws_subnet.private_a.id, aws_subnet.private_b.id]

  tags = {
    Name = "taskflow-db-subnet-group"
  }
}

resource "aws_db_instance" "main" {
  identifier     = "taskflow-db"
  engine         = "postgres"
  engine_version = "16"
  instance_class = "db.t3.micro"

  allocated_storage = 20
  storage_type      = "gp3"

  db_name  = "taskflow"
  username = "taskflow_admin"

  manage_master_user_password = true

  db_subnet_group_name   = aws_db_subnet_group.main.name
  vpc_security_group_ids = [aws_security_group.rds.id]
  publicly_accessible    = false
  multi_az                = false

  skip_final_snapshot = true
  deletion_protection  = false

  tags = {
    Name = "taskflow-db"
  }
}