from google.cloud import bigquery
import sys
import os

# Add the project root directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import PROJECT_ID, DATASET_ID, TABLE_ID

class BigQueryLoader:
    def __init__(self):
        self.client = bigquery.Client(project=PROJECT_ID)
        self.table_id = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

    def create_dataset_if_not_exists(self):
        """Create the dataset if it doesn't exist"""
        dataset_ref = self.client.dataset(DATASET_ID)
        try:
            self.client.get_dataset(dataset_ref)
        except Exception:
            dataset = bigquery.Dataset(dataset_ref)
            dataset.location = "US"
            self.client.create_dataset(dataset)

    def create_table_schema(self):
        """Define the table schema"""
        schema = [
            bigquery.SchemaField("id", "INTEGER"),
            bigquery.SchemaField("title", "STRING"),
            bigquery.SchemaField("price", "FLOAT"),
            bigquery.SchemaField("category", "STRING"),
            bigquery.SchemaField("description", "STRING"),
            bigquery.SchemaField("image", "STRING"),
            bigquery.SchemaField("rating", "RECORD", fields=[
                bigquery.SchemaField("rate", "FLOAT"),
                bigquery.SchemaField("count", "INTEGER")
            ]),
            bigquery.SchemaField("collected_at", "TIMESTAMP"),
            bigquery.SchemaField("price_tier", "STRING"),
            bigquery.SchemaField("price_percentile", "FLOAT"),
            bigquery.SchemaField("price_vs_category_avg", "FLOAT")
        ]
        return schema

    def load_data(self, df):
        """Load data into BigQuery"""
        self.create_dataset_if_not_exists()
        
        # Configure the load job
        job_config = bigquery.LoadJobConfig(
            schema=self.create_table_schema(),
            write_disposition="WRITE_APPEND"
        )

        # Load the data
        job = self.client.load_table_from_dataframe(
            df, self.table_id, job_config=job_config
        )
        job.result()  # Wait for the job to complete 