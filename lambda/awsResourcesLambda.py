import json
import os
import logging
from discord_webhook import DiscordWebhook

# Set up logging for debugging through CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    try:
        # Log incoming event for debugging
        logger.info(f"Received event: {json.dumps(event, indent=2)}")

        # Extract event details
        event_account = event.get("account", "could not retrieve account")  # Account performing AWS resource changes
        event_type = event.get("detail-type", "could not retrieve event type")  # Triggered event type
        event_service = event.get("source", "could not retrieve service")  # AWS service modified (e.g., S3)
        event_resources = event.get("detail", {})  # Modified resource information (e.g., S3 Bucket)

        # Construct the Discord message
        message = (
            f"**Event Type:** {event_type}\n"
            f"**User Account ID:** {event_account}\n"
            f"**Service Used:** {event_service}\n"
            f"**Resource State:**\n```json\n{json.dumps(event_resources, indent=2)}\n```"
        )

        # Send the message to Discord
        webhook_url = "Your discord webhook URL"  # Replace with your Discord webhook URL
        webhook = DiscordWebhook(url=webhook_url, content=message)
        response = webhook.execute()

        # Log the Discord webhook response
        logger.info(f"Discord webhook response: {response}")

        return {
            'statusCode': 200,
            'body': json.dumps('Message delivered to Discord successfully')
        }

    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Internal server error')
        }