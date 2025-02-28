import json
import os
import boto3
import requests

# Load environment variables
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def lambda_handler(event, context):
    message = event['Records'][0]['Sns']['Message']
    
    payload = {
        "text": f":rotating_light: *OpsAlert Notification* :rotating_light:\n{message}"
    }

    headers = {'Content-Type': 'application/json'}
    
    # Send message to Slack
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(payload), headers=headers)

    return {
        "statusCode": response.status_code,
        "body": json.dumps("Alert sent to Slack successfully")
    }

