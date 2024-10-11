import requests
import json

def login_and_get_ticket(url, username, password):
    # Payload with login credentials
    payload = {
        "username": username,
        "password": password
    }
    
    # Send POST request to login and get the service ticket
    response = requests.post(url, data=json.dumps(payload), headers={'Content-Type': 'application/json'})
    
    if response.status_code in [200, 201]:
        # Extract the service ticket from the response
        data = response.json()
        service_ticket = data.get("response", {}).get("serviceTicket")
        if service_ticket:
            print(f"Service Ticket ID: {service_ticket}")
            return service_ticket
        else:
            print("Service Ticket ID not found in the response.")
            return None
    else:
        print(f"Login failed with status code {response.status_code}. Response: {response.text}")
        return None

def get_network_devices(base_url, service_ticket):
    # Construct the URL for retrieving network devices
    url = f"{base_url}/network-device"
    
    # Headers with the service ticket for authorization
    headers = {
        'X-Auth-Token': service_ticket
    }
    
    # Send GET request to retrieve network devices
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        # Print and return the network devices in a readable format
        devices = response.json()
        print("Network Devices:", json.dumps(devices, indent=4))
        return devices
    else:
        print(f"Failed to retrieve network devices. Status code: {response.status_code}. Response: {response.text}")
        return None

if __name__ == "__main__":
    # Base URL and login credentials
    base_url = "http://localhost:58000/api/v1"
    login_url = f"{base_url}/ticket"
    username = "admin"
    password = "Ssjcoe123@#"
    
    # Step 1: Login and get the service ticket
    service_ticket = login_and_get_ticket(login_url, username, password)
    print(service_ticket)
    
    # Step 2: Use the service ticket to retrieve network devices
    if service_ticket:
        get_network_devices(base_url, service_ticket)
    else:
        print("Unable to retrieve network devices without a service ticket.")
