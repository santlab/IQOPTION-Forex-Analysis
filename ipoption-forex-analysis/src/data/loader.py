import pandas as pd
import numpy as np

class DataLoader:
    def __init__(self, source):
        self.source = source

    def load_data(self):
        # Load market data from the specified source
        if self.source == 'csv':
            return self.load_from_csv()
        elif self.source == 'api':
            return self.load_from_api()
        else:
            raise ValueError("Unsupported data source")

    def load_from_csv(self):
        # Load data from a CSV file
        data = pd.read_csv('market_data.csv')
        return self.prepare_data(data)

    def load_from_api(self):
        # Load data from an API (placeholder for actual API call)
        data = self.fetch_data_from_api()
        return self.prepare_data(data)

    def fetch_data_from_api(self):
        # Placeholder for API fetching logic
        # This should be replaced with actual API call and data retrieval
        return pd.DataFrame({
            'timestamp': pd.date_range(start='2023-01-01', periods=100, freq='D'),
            'price': np.random.rand(100) * 100
        })

    def prepare_data(self, data):
        # Prepare and clean the data for analysis
        data['timestamp'] = pd.to_datetime(data['timestamp'])
        data.set_index('timestamp', inplace=True)
        return data

# Example usage:
# loader = DataLoader(source='csv')
# market_data = loader.load_data()