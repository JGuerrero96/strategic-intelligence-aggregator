import pytest
from src.agents import StrategicIntelligenceAgent, CompetitorAnalysisAgent, MarketTrendAgent

class TestAgents:
    def setup_method(self):
        """Setup method to initialize agents before each test"""
        self.strategic_agent = StrategicIntelligenceAgent()
        self.competitor_agent = CompetitorAnalysisAgent()
        self.market_trend_agent = MarketTrendAgent()
    
    def test_strategic_intelligence_agent_initialization(self):
        """Test initialization of Strategic Intelligence Agent"""
        assert self.strategic_agent is not None, "Strategic Intelligence Agent should be initialized"
        assert hasattr(self.strategic_agent, 'analyze'), "Agent should have an analyze method"
    
    def test_competitor_analysis_agent_initialization(self):
        """Test initialization of Competitor Analysis Agent"""
        assert self.competitor_agent is not None, "Competitor Analysis Agent should be initialized"
        assert hasattr(self.competitor_agent, 'analyze_competitors'), "Agent should have a competitor analysis method"
    
    def test_market_trend_agent_initialization(self):
        """Test initialization of Market Trend Agent"""
        assert self.market_trend_agent is not None, "Market Trend Agent should be initialized"
        assert hasattr(self.market_trend_agent, 'identify_trends'), "Agent should have a trend identification method"
    
    def test_strategic_agent_analysis(self):
        """Test strategic intelligence analysis method"""
        # Mock data or use sample data from data loader
        mock_market_data = [
            {'company': 'TechCorp', 'market_share': 0.25, 'revenue': 1000000, 'growth_rate': 0.15},
            {'company': 'InnovateSolutions', 'market_share': 0.18, 'revenue': 750000, 'growth_rate': 0.12}
        ]
        
        analysis_result = self.strategic_agent.analyze(mock_market_data)
        
        assert analysis_result is not None, "Strategic analysis should return a result"
        assert isinstance(analysis_result, dict), "Analysis result should be a dictionary"
        assert 'key_insights' in analysis_result, "Analysis result should have key insights"
    
    def test_competitor_analysis(self):
        """Test competitor analysis method"""
        mock_competitor_data = [
            {'company_name': 'TechCorp', 'industry': 'Technology', 'headquarters': 'San Francisco', 'annual_revenue': 1000000},
            {'company_name': 'InnovateSolutions', 'industry': 'Software', 'headquarters': 'New York', 'annual_revenue': 750000}
        ]
        
        competitor_insights = self.competitor_agent.analyze_competitors(mock_competitor_data)
        
        assert competitor_insights is not None, "Competitor analysis should return insights"
        assert isinstance(competitor_insights, list), "Competitor insights should be a list"
        assert len(competitor_insights) > 0, "Competitor insights list should not be empty"
    
    def test_market_trend_identification(self):
        """Test market trend identification method"""
        mock_market_data = [
            {'company': 'TechCorp', 'market_share': 0.25, 'revenue': 1000000, 'growth_rate': 0.15},
            {'company': 'InnovateSolutions', 'market_share': 0.18, 'revenue': 750000, 'growth_rate': 0.12}
        ]
        
        market_trends = self.market_trend_agent.identify_trends(mock_market_data)
        
        assert market_trends is not None, "Market trend identification should return trends"
        assert isinstance(market_trends, dict), "Market trends should be a dictionary"
        assert 'emerging_trends' in market_trends, "Market trends should have emerging trends"
        assert 'growth_patterns' in market_trends, "Market trends should have growth patterns"
