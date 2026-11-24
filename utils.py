def fetch_data (url):
    import requests
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {
            "error":True
        }
        
        
def generate_json(data, file):
    import json
    with open(f'{file}', 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)

