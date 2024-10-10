import requests
import json

def login_and_get_ticket(login_url, username, password):
    """Log in to the SDN controller and retrieve the service ticket."""
    response = requests.post(login_url, json={"username": username, "password": password})
    
    if response.status_code == 201:
        ticket_info = response.json()
        service_ticket = ticket_info["response"]["serviceTicket"]
        print(f"Login successful! Service Ticket: {service_ticket}")
        return service_ticket
    else:
        print(f"Login failed with status code: {response.status_code}. Response: {response.text}")
        return None

def get_network_health(base_url, service_ticket):
    """Retrieve the network health information."""
    headers = {"X-Auth-Token": service_ticket}
    response = requests.get(f"{base_url}/assurance/health", headers=headers)

    if response.status_code == 200:
        health_info = response.json()
        print("Network Health Information:")
        print(json.dumps(health_info, indent=2))
    else:
        print(f"Failed to retrieve network health. Status code: {response.status_code}. Response: {response.text}")

if __name__ == "__main__":
    # Base URL and login credentials
    base_url = "http://localhost:58000/api/v1"
    login_url = f"{base_url}/ticket"
    username = "admin"
    password = "Ssjcoe123@#"
    
    # Step 1: Login and get the service ticket
    service_ticket = login_and_get_ticket(login_url, username, password)
    
    # Step 2: Use the service ticket to retrieve network health
    if service_ticket:
        get_network_health(base_url, service_ticket)
    else:
        print("Unable to proceed without a service ticket.")
