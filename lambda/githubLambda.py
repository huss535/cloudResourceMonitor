import json
from discord_webhook import DiscordWebhook
import os
import logging

logger = logging.getLogger() # Set up logging for debugging through cloudwatch
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        
        github_payload = json.loads(event['body']) #  the GitHub webhook payload from the event body
        logger.info(f"Received event: {json.dumps(event, indent=2)}")
        
        headers = event.get('headers', {})
        event_type = headers.get('X-GitHub-Event') or headers.get('x-github-event', 'unknown_event') # Get the triggered event name

        action = github_payload.get('action', 'unknown_action')  # Get the github action (e.g., opened, closed)

        repo_name = github_payload.get('repository', {}).get('full_name', 'unknown_repo') #get repo where change occured
        sender = github_payload.get('sender', {}).get('login', 'unknown_user') # get user who performed change

    
    
       # Send the message to Discord
        webhook_url = "Your discord webhook URL"  # Replace with your Discord webhook URL
       
        message = f"{sender} {action} a {event_type} in {repo_name}"

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