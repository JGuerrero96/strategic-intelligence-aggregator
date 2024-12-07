import asyncio
import logging
from typing import List, Dict, Any

import pandas as pd
from chromadb import Client
from sentence_transformers import SentenceTransformer

from .data_loader import load_data_sources, preprocess_data
from .utils import generate_insights, calculate_metrics

class StrategicIntelligenceAggregator:
    def __init__(
        self, 
        data_sources: List[str], 
        embedding_model: str = 'all-MiniLM-L6-v2',
        llm_model: str = 'local_llm'
    ):
        """
        Initialize Strategic Intelligence Aggregator
        
        Args:
            data_sources (List[str]): Paths to data sources
            embedding_model (str): Embedding model for vectorization
            llm_model (str): Local Language Model for analysis
        """
        self.logger = logging.getLogger(__name__)
        self.data_sources = data_sources
        
        # Initialize embedding model
        self.embedding_model = SentenceTransformer(embedding_model)
        
        # Initialize vector database
        self.chroma_client = Client()
        self.collection = self.chroma_client.create_collection(
            name="strategic_intelligence"
        )
        
        # Placeholder for LLM (to be implemented)
        self.llm_model = llm_model
    
    async def load_and_vectorize_data(self):
        """
        Asynchronously load and vectorize data sources
        """
        try:
            validated_sources = await load_data_sources(self.data_sources)
            
            for source in validated_sources:
                # Load and preprocess data
                if source.endswith('.json'):
                    with open(source, 'r') as f:
                        data = pd.read_json(f)
                else:
                    data = pd.read_csv(source)
                
                preprocessed_data = preprocess_data(data)
                
                # Vectorize data
                documents = preprocessed_data.to_dict('records')
                embeddings = self.embedding_model.encode(
                    [str(doc) for doc in documents]
                ).tolist()
                
                # Store in vector database
                self.collection.add(
                    embeddings=embeddings,
                    documents=[str(doc) for doc in documents],
                    ids=[str(i) for i in range(len(documents))]
                )
            
            self.logger.info("Data loaded and vectorized successfully")
        
        except Exception as e:
            self.logger.error(f"Error in data loading: {e}")
            raise
    
    def generate_strategic_report(
        self, 
        query: str, 
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Generate a strategic intelligence report
        
        Args:
            query (str): Strategic intelligence query
            top_k (int): Number of top results to retrieve
        
        Returns:
            Dict containing strategic insights
        """
        try:
            # Retrieve relevant documents
            query_embedding = self.embedding_model.encode([query])[0]
            results = self.collection.query(
                query_embeddings=[query_embedding],
                n_results=top_k
            )
            
            # Extract and process retrieved documents
            retrieved_docs = [
                eval(doc) for doc in results['documents'][0]
            ]
            
            # Generate insights
            insights = generate_insights(retrieved_docs, query)
            metrics = calculate_metrics(retrieved_docs)
            
            return {
                'query': query,
                'insights': insights,
                'metrics': metrics,
                'retrieved_documents': retrieved_docs
            }
        
        except Exception as e:
            self.logger.error(f"Error generating report: {e}")
            raise