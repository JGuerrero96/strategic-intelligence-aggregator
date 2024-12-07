import asyncio
import logging
from dotenv import load_dotenv

from src.agents import StrategicIntelligenceAggregator
from src.data_loader import load_data_sources

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def main():
    load_dotenv()
    
    try:
        # Define local data sources
        data_sources = [
            'data/market_data_sample.json',
            'data/competitor_info_sample.csv'
        ]
        
        # Load and validate data sources
        validated_sources = await load_data_sources(data_sources)
        
        # Initialize Intelligence Aggregator
        intelligence_system = StrategicIntelligenceAggregator(
            data_sources=validated_sources,
            embedding_model='local_embedding_model',
            llm_model='local_llm_model'
        )
        
        # Load and vectorize data
        await intelligence_system.load_and_vectorize_data()
        
        # Generate strategic report
        query = "AI technology investment trends in enterprise software"
        strategic_report = intelligence_system.generate_strategic_report(query)
        
        # Log and display results
        logger.info("Strategic Report Generated Successfully")
        print(strategic_report)
    
    except Exception as e:
        logger.error(f"Error in main execution: {e}")

if __name__ == '__main__':
    asyncio.run(main())