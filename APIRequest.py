import requests
import pandas as pd
import json
import os
from config import BASE_URL, ENDPOINT

base_url = BASE_URL
endpoint = ENDPOINT

def get_base_url(base_url, endpoint, page):
    response = requests.get(f"{base_url}{endpoint}?page={page}")
    return response.json()

new_results = []
def get_all_characters(base_url, endpoint):
    page = 1
    while True:
        json = get_base_url(base_url, endpoint, page)
        if 'results' not in json:
            break
        for i in json['results']:
            new_JsonData = {
                'id': i['id'],
                'name': i['name'],
                'status': i['status'],
                "image": i['image']
            }
            new_results.append(new_JsonData)
        page += 1
    return new_results

def get_character_data(page):
    json = get_base_url(base_url, endpoint, page)
    for i in json['results']:
        new_JsonData = {
            'id': i['id'],
            'name': i['name'],
            'status': i['status'],
            "image": i['image']
        }
        new_results.append(new_JsonData)
    return new_results

def save_to_json(data, filename="characters.json"):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Data saved to {filename}")

data = get_all_characters(base_url, endpoint)
df = pd.DataFrame(data)

if __name__ == "__main__":
    print(df.head())
    save_to_json(data)
