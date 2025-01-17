import pandas as pd
import numpy as np

class WalmartDataProcessor:
    def __init__(self, df):
        self.df = df

    def clean_data(self):
        """Clean and prepare the data"""
        # Remove duplicates
        self.df = self.df.drop_duplicates(subset=['id'])
        
        # Convert price to numeric
        self.df['price'] = pd.to_numeric(self.df['price'], errors='coerce')
        
        # Clean category names
        self.df['category'] = self.df['category'].str.lower().str.strip()
        
        # Add derived columns
        self.df['price_tier'] = pd.qcut(self.df['price'], q=4, labels=['Budget', 'Economy', 'Premium', 'Luxury'])
        
        return self.df

    def add_analytics_columns(self):
        """Add additional columns for analysis"""
        # Add price percentile
        self.df['price_percentile'] = self.df['price'].rank(pct=True)
        
        # Add category average price
        category_avg = self.df.groupby('category')['price'].transform('mean')
        self.df['price_vs_category_avg'] = self.df['price'] - category_avg
        
        return self.df 