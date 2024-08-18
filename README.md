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

# challanges
1. I faced aproblem with the authorization and actually couldnot reach any Api
2. I did two scripts one for manual testing by adding a fuction that gets project_id and then added another script for webhook testing.
3. Regarding webhook testing my approcah was to use ngrok to expose your local server to the internet, providing a public URL that PlanRadar can send webhook requests to then Configure the Webhook on PlanRadar
Log in to PlanRadar and go to Settings → Account → Webhooks, Create a new webhook and set the target URL to the ngrok public URL obtained earlier. but i faces aproblem is expossing the url to br public 
