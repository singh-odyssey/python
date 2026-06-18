"""
Environment configuration for Sendblue API
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """Configuration class for Sendblue API credentials"""
    
    SENDBLUE_API_KEY = os.getenv('SENDBLUE_API_KEY')
    SENDBLUE_API_SECRET = os.getenv('SENDBLUE_API_SECRET')
    SENDBLUE_PHONE_NUMBER = os.getenv('SENDBLUE_PHONE_NUMBER')
    
    @classmethod
    def validate(cls):
        """Validate that all required credentials are configured"""
        missing = []
        
        if not cls.SENDBLUE_API_KEY:
            missing.append('SENDBLUE_API_KEY')
        if not cls.SENDBLUE_API_SECRET:
            missing.append('SENDBLUE_API_SECRET')
        if not cls.SENDBLUE_PHONE_NUMBER:
            missing.append('SENDBLUE_PHONE_NUMBER')
        
        if missing:
            raise ValueError(
                f"Missing required environment variables: {', '.join(missing)}\n"
                f"Please create a .env file in the project root with your Sendblue credentials.\n"
                f"See .env.example for reference."
            )
