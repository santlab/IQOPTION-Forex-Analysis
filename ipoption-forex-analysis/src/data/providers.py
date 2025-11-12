from typing import Any, Dict
import requests

class MarketDataProvider:
    def __init__(self, api_key: str, base_url: str):
        self.api_key = api_key
        self.base_url = base_url

    def fetch_data(self, symbol: str, timeframe: str, limit: int = 100) -> Dict[str, Any]:
        url = f"{self.base_url}/data?symbol={symbol}&timeframe={timeframe}&limit={limit}&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()

    def get_historical_data(self, symbol: str, timeframe: str, limit: int = 100) -> Dict[str, Any]:
        return self.fetch_data(symbol, timeframe, limit)

    def get_live_data(self, symbol: str) -> Dict[str, Any]:
        url = f"{self.base_url}/live?symbol={symbol}&api_key={self.api_key}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()