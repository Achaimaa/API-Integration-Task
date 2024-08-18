# API-Integration-Task
# Overview
This script automates the process of creating forms, layers, and tickets in PlanRadar. It uses the PlanRadar API to perform these tasks. The script assumes that you have access to a PlanRadar account and have created necessary API tokens and configurations.
# Prerequisites
Python 3.x: Ensure Python 3.x is installed on your machine.
Requests Library: Install the requests library if it's not already installed. You can install it using pip:
pip install requests
# Usage
Script Execution:

Run the script using Python:
python script_name.py
Replace script_name.py with the name of the script file.

# Functions:

create_project(): Simulates project creation. Modify this function to integrate with actual project creation if needed.
create_form(project_id): Creates a form in the specified project.
create_layer(project_id): Adds an empty layer to the specified project.
create_ticket(project_id, form_id, layer_id): Creates a ticket in the specified project using the given form and layer IDs.
# Error Handling
The script includes error handling for HTTP errors, request exceptions, and JSON decoding errors.
It prints detailed error messages to help diagnose issues with API requests.

# Challenges
I encountered a problem with authorization; the API refused to grant access even with the correct token, preventing successful access to the API. As a result, I developed two scripts:

Manual Testing Script: Includes a function to manually retrieve the project_id.
Webhook Testing Script: Intended to test webhooks by using ngrok to expose the local server to the internet, providing a public URL that PlanRadar can use to send webhook requests.
# Webhook Testing Approach
Using ngrok: I used ngrok to expose my local server to the internet, allowing it to receive webhook requests from PlanRadar.
Configuring the Webhook on PlanRadar: I attempted to configure a webhook in PlanRadar by navigating to Settings → Account → Webhooks and creating a new webhook with the target URL set to the ngrok public URL.
Unfortunately, I encountered issues with exposing the URL publicly, which hindered the webhook testing process.

# Conclusion
This script lays the groundwork for integrating with the PlanRadar API, but further work is required to resolve authorization issues and successfully test the webhook functionality.
