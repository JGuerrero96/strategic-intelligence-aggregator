import logging
from typing import List, Dict, Any
import numpy as np
import pandas as pd

def generate_insights(documents: List[Dict], query: str) -> List[str]:
    """
    Generate strategic insights from retrieved documents
    
    Args:
        documents (List[Dict]): Retrieved documents
        query (str): Original query
    
    Returns:
        List of generated insights
    """
    insights = []
    
    try:
        # Basic trend analysis
        df = pd.DataFrame(documents)
        
        # Revenue trend
        revenue_trend = "Increasing" if df['revenue'].is_monotonic_increasing else \
                        "Decreasing" if df['revenue'].is_monotonic_decreasing else \
                        "Fluctuating"
        insights.append(f"Revenue Trend: {revenue_trend}")
        
        # Margin analysis
        df['margin'] = df['revenue'] - df['cost']
        avg_margin = df['margin'].mean()
        insights.append(f"Average Margin: ${avg_margin:.2f}")
        
        # Volatility assessment
        margin_volatility = df['margin'].std() / df['margin'].mean() * 100
        volatility_desc = (
            "Low" if margin_volatility < 10 else
            "Moderate" if margin_volatility < 25 else
            "High"
        )
        insights.append(f"Margin Volatility: {volatility_desc}")
        
        # Context-specific generation
        if 'investment' in query.lower():
            investment_insights = analyze_investment_trends(df)
            insights.extend(investment_insights)
        
        return insights
    
    except Exception as e:
        logging.error(f"Error generating insights: {e}")
        return ["Unable to generate comprehensive insights"]

def calculate_metrics(documents: List[Dict]) -> Dict[str, Any]:
    """
    Calculate comprehensive metrics from documents
    
    Args:
        documents (List[Dict]): Retrieved documents
    
    Returns:
        Dictionary of calculated metrics
    """
    try:
        df = pd.DataFrame(documents)
        
        metrics = {
            'total_revenue': df['revenue'].sum(),
            'total_cost': df['cost'].sum(),
            'average_revenue': df['revenue'].mean(),
            'average_cost': df['cost'].mean(),
            'revenue_growth_rate': calculate_growth_rate(df['revenue']),
            'cost_efficiency_ratio': (df['cost'].sum() / df['revenue'].sum()) * 100
        }
        
        return metrics
    
    except Exception as e:
        logging.error(f"Error calculating metrics: {e}")
        return {}

def calculate_growth_rate(series: pd.Series) -> float:
    """
    Calculate compound annual growth rate
    
    Args:
        series (pd.Series): Time series data
    
    Returns:
        Compound growth rate
    """
    try:
        start_value = series.iloc[0]
        end_value = series.iloc[-1]
        periods = len(series)
        
        growth_rate = (end_value / start_value) ** (1/periods) - 1
        return growth_rate * 100
    
    except Exception as e:
        logging.error(f"Growth rate calculation error: {e}")
        return 0.0

def analyze_investment_trends(df: pd.DataFrame) -> List[str]:
    """
    Provide specific insights for investment-related queries
    
    Args:
        df (pd.DataFrame): DataFrame with financial data
    
    Returns:
        List of investment-specific insights
    """
    investment_insights = []
    
    try:
        # Investment concentration
        if 'investment' in df.columns:
            total_investment = df['investment'].sum()
            avg_investment = df['investment'].mean()
            investment_insights.append(
                f"Total Investment: ${total_investment:,.2f}"
            )
            investment_insights.append(
                f"Average Investment: ${avg_investment:,.2f}"
            )
        
        return investment_insights
    
    except Exception as e:
        logging.error(f"Investment trend analysis error: {e}")
        return []