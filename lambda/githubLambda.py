import json
from discord_webhook import DiscordWebhook
import os
import logging

logger = logging.getLogger()  # Set up logging for debugging through CloudWatch
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        github_payload = json.loads(event['body'])  # Extract the Github webhook payload from the event body
        logger.info(f"Received event: {json.dumps(event, indent=2)}")

        headers = event.get('headers', {})
        event_type = headers.get('X-GitHub-Event') or headers.get('x-github-event', 'unknown_event')  # Get the triggered event name

        repo_name = github_payload.get('repository', {}).get('full_name', 'unknown_repo')  # Get repo where change occurred
        sender = github_payload.get('sender', {}).get('login', 'unknown_user')  # Get user who performed the change

        # Send the message to Discord
        webhook_url = "Your discord webhook URL"  # Replace with your Discord webhook URL
        message = f"{sender} triggered a branch/tag {event_type} event in repository: {repo_name}"

        webhook = DiscordWebhook(url=webhook_url, content=message)

        # Execute the webhook
        response = webhook.execute()

        # Check if the webhook was successful
        if response.status_code == 200:
            print("Message sent to Discord successfully!")
        else:
            print(f"Failed to send message to Discord. Status code: {response.status_code}")

        # Return a response to the caller (e.g., GitHub)
        return {
            'statusCode': 200,
            'body': json.dumps('Webhook processed successfully!')
        }

    except Exception as e:
        print(f"Error processing webhook: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps('Error processing webhook!')
        }