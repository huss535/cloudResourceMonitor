# Cloud Resource Monitor

A cloud-based solution for monitoring cloud resources and GitHub repository changes, logging them directly into a Discord channel.

## Key Files

- **`python.zip`**: The zip file containing the Discord Python layer for AWS Lambda.
- **`lambda/awsResourcesLambda.py`**: Lambda function for processing AWS resource changes and logging them to a Discord channel.
- **`lambda/githubLambda.py`**: Lambda function for processing GitHub repository changes and logging them to a Discord channel.

## Full Walkthrough

For a detailed guide on how to set this up, check out my Medium article:  
[Automate GitHub and AWS Resource Notifications to Discord](https://medium.com/@efar3200/automate-github-and-aws-resource-notifications-to-discord-6257d07ebf79)