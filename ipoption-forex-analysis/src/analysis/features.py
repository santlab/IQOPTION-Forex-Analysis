from typing import List
import pandas as pd

def generate_features(data: pd.DataFrame) -> pd.DataFrame:
    """
    Generate features from market data for analysis and model training.

    Parameters:
    data (pd.DataFrame): The input market data containing price and volume information.

    Returns:
    pd.DataFrame: A DataFrame containing the original data along with the generated features.
    """
    # Example feature: Moving Average
    data['moving_average'] = data['close'].rolling(window=14).mean()

    # Example feature: Price Change
    data['price_change'] = data['close'].pct_change()

    # Example feature: Volume Change
    data['volume_change'] = data['volume'].pct_change()

    # Add more features as needed
    # ...

    return data

def feature_selection(data: pd.DataFrame, features: List[str]) -> pd.DataFrame:
    """
    Select specific features from the DataFrame.

    Parameters:
    data (pd.DataFrame): The input DataFrame with generated features.
    features (List[str]): List of feature names to select.

    Returns:
    pd.DataFrame: A DataFrame containing only the selected features.
    """
    return data[features]