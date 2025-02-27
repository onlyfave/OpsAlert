provider "aws" {
  region = "us-east-1"
}

resource "aws_sns_topic" "opsalert_topic" {
  name = "opsalert-topic"
}

resource "aws_lambda_function" "opsalert_lambda" {
  function_name    = "OpsAlertLambda"
  handler         = "lambda_function.lambda_handler"
  runtime         = "python3.9"
  role            = aws_iam_role.lambda_exec.arn
  filename        = "lambda_package.zip"
}

resource "aws_cloudwatch_metric_alarm" "high_cpu_alert" {
  alarm_name          = "HighCPUUtilization"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "CPUUtilization"
  namespace          = "AWS/EC2"
  period             = 300
  statistic         = "Average"
  threshold         = 80
  alarm_description  = "Triggers when CPU utilization exceeds 80%"
  alarm_actions      = [aws_sns_topic.opsalert_topic.arn]
}
