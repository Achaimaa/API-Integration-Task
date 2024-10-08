import requests
import json
import logging

logging.basicConfig(level=logging.DEBUG)
# Configuration
API_TOKEN = '7c7d162ef7700753d61334fe91d36268694dc6da1cb770a001d24af1f08483ed7249fac66bdd338af756ec7d9349ab70e06cb57b0108866d9394657b7bd303211cf5e87d2f94dd3fa199c4981ab98af6'
BASE_URL = 'https://www.planradar.com'
CUSTOMER_ID = 1319144  # Replace with your actual customer ID

HEADERS = {
    'X-PlanRadar-API-Key': API_TOKEN,
    'Content-Type': 'application/json'
}
#response = requests.get(f'{BASE_URL}/api/v1/user', headers=HEADERS)
#print(response.status_code)
#print(response.json())
def create_project():
    # Simulate project creation
    project_id = 2  # Replace with actual project ID
    return project_id

def create_form(project_id):
    url = f'{BASE_URL}/api/v1/{CUSTOMER_ID}/projects/{project_id}/ticket_types_project'

    data = {
        "data": {
            "attributes": {
                "ticket-type-id": "xmwp",  
                "required-fields": [
                    "string" 
                ]
            }
        },
        "included": [
            {
                "type": "lists-ticket-types",
                "attributes": {
                    "list-id": "gwgw",  
                    "field-name": "tf29b038634ac7d062",  
                    "list-items": [
                        "string"  
                    ],
                    "allow-multiple-selection": False
                }
            }
        ]
    }
    
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        
        # Print the entire response for debugging
        print('Response Status Code:', response.status_code)
        print('Response Content:', response.content.decode())  # Decode bytes to string
        
        response.raise_for_status()  # Raises HTTPError for bad responses
        
  
        response_data = response.json()
        print('Response JSON:', response_data)
        
        # Adjust based on the actual response structure
        if isinstance(response_data.get('data'), list) and response_data['data']:
            return response_data['data'][0].get('id', None)  
        else:
            print('No data or empty response')
            return None
        
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        return None
    except requests.exceptions.RequestException as req_err:
        print(f'Request error occurred: {req_err}')
        return None
    except Exception as err:
        print(f'Other error occurred: {err}')
        return None



def create_layer(project_id):
    url = f'{BASE_URL}/api/v1/{CUSTOMER_ID}/projects/{project_id}/components'
    data = {
        "data": [
            {
                "attributes": {
                    "file": {
                        "link": "https://example.com/sample.pdf",
                        "name": "sample.pdf",
                        "type": "application/pdf"
                    },
                    "file-name": "sample.pdf",
                    "file-content-type": "application/pdf",
                    "is-base64": False,
                    "layers": [
                        {
                            "page": 1,
                            "name": "Layer 1",
                            "rotation": 0,
                            "parent-id": "parent-layer-id",
                            "order": 1,
                            "reposition-tickets": True,
                            "component-id": "component-id",
                            "model-id": "model-id",
                            "model-title": "Model Title"
                        }
                    ]
                }
            }
        ]
    }

    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        print('Response Content:', response.content)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print('Response Content:', response.content)
    except Exception as err:
        print(f'Other error occurred: {err}')
    else:
       # return response.json()
        return response.json()['data']['id']

def create_ticket(project_id, form_id, layer_id):
    url = f'{BASE_URL}/api/v1/{CUSTOMER_ID}/projects/{project_id}/tickets'
    
    data = {
        "data": {
            "attributes": {
                "subject": "Sample Ticket",  
                "ticket-type-id": form_id,
                "parent-id": None,
                "status-id": "status",  
                "component-id": layer_id,
                "priority-id": "priority",  
                "assigned-to-id": None,
                "due-date": "2024-08-31",  
                "extension-date": None,
                "typed-values": {},
                "subscribers": [],
                "progress": 0,
                "plan-x": 0,
                "plan-y": 0,
                "uuid": None
            }
        }
    }

    
    #return response.json()['data']['id']
    try:
        response = requests.post(url, headers=HEADERS, data=json.dumps(data))
        print(f'Request Method: POST')
        print(f'Request URL: {url}')
        print(f'Request Body: {json.dumps(data)}')
        print(f'Response Status Code: {response.status_code}')
        print(f'Response Headers: {response.headers}')
        print(f'Response Content: {response.content.decode()}')

        response.raise_for_status()

        response_data = response.json()
        print("Response JSON:", response_data)

        if isinstance(response_data.get('data'), list) and len(response_data['data']) > 0:
            ticket_id = response_data['data'][0].get('id', None)
            print(f'Ticket created with ID: {ticket_id}')
            return ticket_id
        else:
            print('No data or unexpected response format:', response_data)
            print('Ticket created with ID: None')
            return None
    except requests.exceptions.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
        print('Response Content:', response.content.decode())
        print('Ticket created with ID: None')
    except json.JSONDecodeError as json_err:
        print(f'JSON decode error occurred: {json_err}')
        print('Response Content:', response.content.decode())
        print('Ticket created with ID: None')
    except Exception as err:
        print(f'Other error occurred: {err}')
        print('Ticket created with ID: None')
def main():
    project_id = create_project()
    form_id = create_form(project_id)
    layer_id = create_layer(project_id)
    #ticket_id = create_ticket(project_id, form_id, layer_id)
    ticket_id = create_ticket(project_id, 1, 2)
   

if __name__ == '__main__':
    main()
