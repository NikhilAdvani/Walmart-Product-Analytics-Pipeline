from dotenv import load_dotenv
import os

load_dotenv()

# API Configuration
API_BASE_URL = "https://fakestoreapi.com/products"

# BigQuery Configuration
PROJECT_ID = os.getenv("GCP_PROJECT_ID")
DATASET_ID = "walmart_analytics"
TABLE_ID = "product_data"

# Data Collection Configuration
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds 