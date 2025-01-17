import requests
import pandas as pd
from datetime import datetime
import time
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import API_BASE_URL, MAX_RETRIES, RETRY_DELAY

class WalmartDataCollector:
    def fetch_products(self):
        """Fetch products from Walmart API with retry mechanism"""
        for attempt in range(MAX_RETRIES):
            try:
                response = requests.get(API_BASE_URL)
                response.raise_for_status()
                return response.json()
            except requests.exceptions.RequestException as e:
                if attempt == MAX_RETRIES - 1:
                    raise Exception(f"Failed to fetch data after {MAX_RETRIES} attempts: {str(e)}")
                time.sleep(RETRY_DELAY)

    def collect_data(self):
        """Collect all product data and return as DataFrame"""
        products = self.fetch_products()
        df = pd.DataFrame(products)
        df['collected_at'] = datetime.now()
        return df 