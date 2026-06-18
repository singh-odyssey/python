"""
Sendblue SMS/iMessage API Service
Handles all API interactions with Sendblue
"""
import requests
from typing import Optional, Dict, Any
from config.env import Config


class SendblueAPIException(Exception):
    """Custom exception for Sendblue API errors"""
    pass


class SendblueSMSService:
    """
    Service for sending SMS/iMessage via Sendblue API
    Supports sending to phone numbers with automatic fallback cascade:
    iMessage → RCS → SMS
    """
    
    BASE_URL = "https://api.sendblue.co/api"
    
    def __init__(self):
        """Initialize with credentials from config"""
        Config.validate()
        self.api_key = Config.SENDBLUE_API_KEY
        self.api_secret = Config.SENDBLUE_API_SECRET
        self.from_number = Config.SENDBLUE_PHONE_NUMBER
    
    def _get_headers(self) -> Dict[str, str]:
        """
        Get request headers with authentication
        
        Returns:
            Dict containing authentication headers
        """
        return {
            'sb-api-key-id': self.api_key,
            'sb-api-secret-key': self.api_secret,
            'Content-Type': 'application/json'
        }
    
    def send_message(
        self,
        to_number: str,
        message: str,
        media_url: Optional[str] = None,
        send_style: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Send a message via Sendblue API
        
        Args:
            to_number: Recipient phone number in E.164 format (e.g., +15551234567)
            message: Message content (max 18,996 characters)
            media_url: Optional URL of media to attach (image, video, audio, file)
            send_style: Optional iMessage effect (celebration, fireworks, lasers, love, etc.)
        
        Returns:
            API response dictionary containing message details
            
        Raises:
            SendblueAPIException: If API request fails
        """
        payload = {
            'number': to_number,
            'from_number': self.from_number,
            'content': message
        }
        
        # Add optional parameters if provided
        if media_url:
            payload['media_url'] = media_url
        if send_style:
            payload['send_style'] = send_style
        
        try:
            response = requests.post(
                f"{self.BASE_URL}/send-message",
                json=payload,
                headers=self._get_headers(),
                timeout=10
            )
            
            # Raise exception for non-2xx status codes
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            error_msg = f"Failed to send message: {str(e)}"
            if hasattr(e, 'response') and e.response is not None:
                try:
                    error_detail = e.response.json()
                    error_msg += f"\nAPI Response: {error_detail}"
                except:
                    error_msg += f"\nStatus: {e.response.status_code}"
            raise SendblueAPIException(error_msg)
    
    def check_imessage_support(self, phone_number: str) -> bool:
        """
        Check if a phone number supports iMessage
        
        Args:
            phone_number: Phone number in E.164 format
            
        Returns:
            True if iMessage is supported, False otherwise
            
        Raises:
            SendblueAPIException: If API request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/evaluate-service",
                params={'number': phone_number},
                headers=self._get_headers(),
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            return data.get('service') == 'iMessage'
            
        except requests.exceptions.RequestException as e:
            raise SendblueAPIException(f"Failed to check iMessage support: {str(e)}")
    
    def get_available_lines(self) -> Dict[str, Any]:
        """
        Get all available phone lines
        
        Returns:
            API response with available phone lines
            
        Raises:
            SendblueAPIException: If API request fails
        """
        try:
            response = requests.get(
                f"{self.BASE_URL}/lines",
                headers=self._get_headers(),
                timeout=10
            )
            response.raise_for_status()
            
            return response.json()
            
        except requests.exceptions.RequestException as e:
            raise SendblueAPIException(f"Failed to fetch phone lines: {str(e)}")


def validate_phone_number(phone_number: str) -> bool:
    """
    Validate phone number format (basic E.164 validation)
    
    Args:
        phone_number: Phone number to validate
        
    Returns:
        True if format is valid, False otherwise
    """
    # Basic E.164 format: +1-15 digits
    import re
    pattern = r'^\+\d{1,15}$'
    return bool(re.match(pattern, phone_number))
