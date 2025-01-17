import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_collector import WalmartDataCollector
from src.data_processor import WalmartDataProcessor
from src.bigquery_loader import BigQueryLoader
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main():
    try:
        # Collect data
        logger.info("Starting data collection...")
        collector = WalmartDataCollector()
        raw_data = collector.collect_data()
        logger.info(f"Collected {len(raw_data)} products")

        # Process data
        logger.info("Processing data...")
        processor = WalmartDataProcessor(raw_data)
        processed_data = processor.clean_data()
        processed_data = processor.add_analytics_columns()
        logger.info("Data processing completed")

        # Load to BigQuery
        logger.info("Loading data to BigQuery...")
        loader = BigQueryLoader()
        loader.load_data(processed_data)
        logger.info("Data successfully loaded to BigQuery")

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 