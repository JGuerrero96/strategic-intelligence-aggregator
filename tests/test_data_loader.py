import pytest
import os
import json
import pandas as pd
from src.data_loader import DataLoader

class TestDataLoader:
    def setup_method(self):
        """Setup method to initialize DataLoader before each test"""
        self.data_loader = DataLoader()
    
    def test_load_market_data(self):
        """Test loading market data JSON file"""
        market_data = self.data_loader.load_market_data()
        
        # Assert that market data is loaded correctly
        assert isinstance(market_data, list), "Market data should be a list"
        assert len(market_data) > 0, "Market data should not be empty"
        
        # Check if each item has expected keys
        expected_keys = ['company', 'market_share', 'revenue', 'growth_rate']
        for item in market_data:
            for key in expected_keys:
                assert key in item, f"Missing {key} in market data"
    
    def test_load_competitor_data(self):
        """Test loading competitor information CSV file"""
        competitor_data = self.data_loader.load_competitor_data()
        
        # Assert that competitor data is a pandas DataFrame
        assert isinstance(competitor_data, pd.DataFrame), "Competitor data should be a pandas DataFrame"
        assert not competitor_data.empty, "Competitor data should not be empty"
        
        # Check expected columns
        expected_columns = ['company_name', 'industry', 'headquarters', 'annual_revenue']
        for column in expected_columns:
            assert column in competitor_data.columns, f"Missing {column} in competitor data"
    
    def test_data_file_existence(self):
        """Verify that data files exist"""
        data_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
        
        market_data_path = os.path.join(data_dir, 'market_data_sample.json')
        competitor_data_path = os.path.join(data_dir, 'competitor_info_sample.csv')
        
        assert os.path.exists(market_data_path), "Market data file does not exist"
        assert os.path.exists(competitor_data_path), "Competitor data file does not exist"
    
    def test_data_parsing(self):
        """Test parsing of sample data files"""
        # Test JSON parsing
        market_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'market_data_sample.json')
        with open(market_data_path, 'r') as f:
            market_data = json.load(f)
        
        assert isinstance(market_data, list), "JSON parsing failed for market data"
        
        # Test CSV parsing
        competitor_data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'competitor_info_sample.csv')
        competitor_data = pd.read_csv(competitor_data_path)
        
        assert not competitor_data.empty, "CSV parsing failed for competitor data"