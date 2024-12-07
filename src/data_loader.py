import os
import json
import pandas as pd
import logging
from typing import List, Union, Dict

logger = logging.getLogger(__name__)

async def load_data_sources(sources: List[str]) -> List[str]:
    """
    Asynchronously load and validate data sources
    
    Args:
        sources (List[str]): Paths to data sources
    
    Returns:
        List[str]: Validated data source paths
    """
    validated_sources = []
    
    for source in sources:
        try:
            # Check file existence
            if not os.path.exists(source):
                logger.warning(f"Data source not found: {source}")
                continue
            
            # Validate file type and content
            if source.endswith('.json'):
                with open(source, 'r') as f:
                    data = json.load(f)
                    if not data:
                        logger.warning(f"Empty JSON file: {source}")
                        continue
            
            elif source.endswith('.csv'):
                df = pd.read_csv(source)
                if df.empty:
                    logger.warning(f"Empty CSV file: {source}")
                    continue
            
            validated_sources.append(source)
            logger.info(f"Validated data source: {source}")
        
        except (json.JSONDecodeError, pd.errors.EmptyDataError) as e:
            logger.error(f"Error processing {source}: {e}")
    
    if not validated_sources:
        raise ValueError("No valid data sources found")
    
    return validated_sources

def preprocess_data(data: Union[pd.DataFrame, Dict]) -> pd.DataFrame:
    """
    Preprocess and standardize input data
    
    Args:
        data (Union[pd.DataFrame, Dict]): Input data
    
    Returns:
        pd.DataFrame: Preprocessed and standardized DataFrame
    """
    if isinstance(data, dict):
        df = pd.DataFrame([data])
    elif isinstance(data, pd.DataFrame):
        df = data.copy()
    else:
        raise TypeError("Unsupported data type. Must be dict or DataFrame")
    
    # Remove rows with missing critical information
    df.dropna(subset=['month', 'revenue', 'cost'], inplace=True)
    
    # Ensure numeric columns
    numeric_columns = ['revenue', 'cost']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Sort by month if possible
    if 'month' in df.columns:
        df.sort_values('month', inplace=True)
    
    return df