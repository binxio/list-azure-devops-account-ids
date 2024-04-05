import requests

from azure.identity import DefaultAzureCredential

# Authenticate using configured Azure credential. Use
# az cli to ease personal account authentication.
print("Fetching default Azure credentials..")
cred = DefaultAzureCredential()
azure_token = cred.get_token("https://management.core.windows.net/")

print("Listing Azure DevOps accounts..")
response = requests.get(
    url="https://app.vssps.visualstudio.com/_apis/accounts",
    headers={
        "Authorization": f"Bearer {azure_token.token}"
    })

response.raise_for_status()

print("Found the following accounts: ")
for account in response.json():
    print(f'Name={account["AccountName"]}, Id={account["AccountId"]}')