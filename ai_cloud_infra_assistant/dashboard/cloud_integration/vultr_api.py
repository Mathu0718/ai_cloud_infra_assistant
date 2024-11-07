import requests

API_KEY = '7AYP2CKIWSGGX2MRJHRHVOPBCHHUX6QLZI4Q'
BASE_URL = 'https://api.vultr.com/v2'

headers = {
    'Authorization': f'Bearer {API_KEY}',
    'Content-Type': 'application/json'
}

def list_instances():
    # Your code to fetch instances
    try:
        # Replace with actual API call to fetch instances from Vultr
        instances = vultr_api.get_instances()  # Make sure this is a list or an empty list
        return instances if instances else []  # Return an empty list if instances is None
    except Exception as e:
        print(f"Error fetching instances: {e}")
        return []  # Return an empty list in case of error

def create_instance(region, plan, os_id):
    data = {
        "region": region,
        "plan": plan,
        "os_id": os_id
    }
    response = requests.post(f'{BASE_URL}/instances', json=data, headers=headers)
    return response.json() if response.status_code == 202 else None

def delete_instance(instance_id):
    response = requests.delete(f'{BASE_URL}/instances/{instance_id}', headers=headers)
    return response.status_code == 204
