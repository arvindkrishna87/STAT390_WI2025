import msal
from office365.graph_client import GraphClient

import requests

# Define your credentials
tenant_id = ""
client_id = ""
client_secret = ""

# Build the MSAL confidential client app
authority = f"https://login.microsoftonline.com/{tenant_id}"
app = msal.ConfidentialClientApplication(
    client_id,
    authority=authority,
    client_credential=client_secret,
)

# Get token
token_response = app.acquire_token_for_client(scopes=["https://graph.microsoft.com/.default"])

if "access_token" in token_response:
    # Use the access token to make an API request to Microsoft Graph
    headers = {
        "Authorization": "Bearer " + token_response["access_token"]
    }
    # Example: List shared files in OneDrive
    url = "https://graph.microsoft.com/v1.0/me/drive/sharedWithMe"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        shared_items = response.json().get('value', [])
        for item in shared_items:
            print(f"Name: {item['name']}, URL: {item['webUrl']}")
    else:
        print("Error fetching shared items:", response.status_code)
else:
    print("Authentication failed:", token_response.get("error_description"))
