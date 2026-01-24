import requests
import pathlib
import json
import datetime
import logging
from pathlib import Path
from datetime import datetime


# 1. Logging Timestamp
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s | %(levelname)s: %(message)s'
)

logging.info('Format defined as a timestamp')

# 2. Receive API Data and Verify errors
def fetch_produts_from_api(url):
    try:
        response = requests.get(url, timeout = 10)
        response.raise_for_status()

        logging.info('GET successful')
        return response.json()
    
    except requests.exceptions.RequestException as e:
        logging.error(f'Connection error: {e}')
        return None

          
# 3. Save Raw Data with timestamp
def save_raw_data(data):
    if data is None:
        logging.warning('No data received to save')
        return
    
    try:
        folder = Path('data/bronze')

        folder.mkdir(parents = True, exist_ok = True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_name = f"products_{timestamp}.json"
        file_path = folder / file_name

        with open(file_path, 'w', encoding = 'utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii = False)

        logging.info(f'Data saved successfully at {file_path}')
    
    except Exception as e:
        logging.error(f'Error saving data: {e}')


URL_API = 'https://dummyjson.com/products'
products = fetch_produts_from_api(URL_API)

if products:
    save_raw_data(products)



        