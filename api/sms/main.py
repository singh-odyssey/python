"""
Sendblue SMS Terminal Application
Interactive terminal interface for sending SMS/iMessage messages
"""
import sys
from pathlib import Path
from services.sms_api import SendblueSMSService, SendblueAPIException, validate_phone_number


class SMSTerminalApp:
    """Terminal-based SMS application"""
    
    def __init__(self):
        """Initialize the SMS service"""
        try:
            self.sms_service = SendblueSMSService()
        except ValueError as e:
            print(f"❌ Configuration Error: {e}")
            sys.exit(1)
    
    def clear_screen(self):
        """Clear the terminal screen"""
        import os
        os.system('clear' if sys.platform != 'win32' else 'cls')
    
    def print_header(self):
        """Print application header"""
        print("=" * 60)
        print("📱 SENDBLUE SMS/IMESSAGE TERMINAL")
        print("=" * 60)
        print()
    
    def get_phone_number(self) -> str:
        """
        Get and validate phone number from user
        
        Returns:
            Valid phone number in E.164 format
        """
        while True:
            phone_number = input("📞 Enter recipient phone number (E.164 format, e.g., +15551234567): ").strip()
            
            if not phone_number:
                print("❌ Phone number cannot be empty. Please try again.\n")
                continue
            
            if not validate_phone_number(phone_number):
                print("❌ Invalid format. Use E.164 format: +1XXXXXXXXXX\n")
                continue
            
            return phone_number
    
    def get_message(self) -> str:
        """
        Get message content from user
        
        Returns:
            Message text (max 18,996 characters)
        """
        print("\n💬 Enter your message (press Enter twice when done):")
        print("-" * 60)
        
        lines = []
        empty_line_count = 0
        
        while True:
            line = input()
            
            if line == '':
                empty_line_count += 1
                if empty_line_count >= 2:
                    break
                lines.append(line)
            else:
                empty_line_count = 0
                lines.append(line)
        
        message = '\n'.join(lines).strip()
        
        if not message:
            print("❌ Message cannot be empty. Please try again.\n")
            return self.get_message()
        
        if len(message) > 18996:
            print(f"❌ Message too long! Max 18,996 characters. Current: {len(message)}\n")
            return self.get_message()
        
        return message
    
    def get_media_url(self) -> str:
        """
        Optionally get media URL from user
        
        Returns:
            Media URL or empty string
        """
        media = input("\n📎 Attach media URL? (optional, press Enter to skip): ").strip()
        return media if media else None
    
    def confirm_send(self, to_number: str, message: str) -> bool:
        """
        Confirm message details before sending
        
        Args:
            to_number: Recipient phone number
            message: Message content
            
        Returns:
            True if user confirms, False otherwise
        """
        print("\n" + "=" * 60)
        print("📋 CONFIRM MESSAGE DETAILS")
        print("=" * 60)
        print(f"To: {to_number}")
        print(f"Message ({len(message)} chars):")
        print("-" * 60)
        print(message[:200] + "..." if len(message) > 200 else message)
        print("-" * 60)
        
        while True:
            confirm = input("\n✓ Send message? (y/n): ").strip().lower()
            if confirm in ['y', 'yes']:
                return True
            elif confirm in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def send_sms(self, to_number: str, message: str, media_url: str = None):
        """
        Send SMS message through Sendblue API
        
        Args:
            to_number: Recipient phone number
            message: Message content
            media_url: Optional media URL
        """
        try:
            print("\n📤 Sending message...")
            
            result = self.sms_service.send_message(
                to_number=to_number,
                message=message,
                media_url=media_url
            )
            
            print("\n✅ SUCCESS!")
            print("=" * 60)
            print(f"Message sent to: {to_number}")
            print(f"Message ID: {result.get('message_id', 'N/A')}")
            print(f"Status: {result.get('status', 'SENT')}")
            print("=" * 60)
            
        except SendblueAPIException as e:
            print("\n❌ FAILED TO SEND MESSAGE")
            print("=" * 60)
            print(f"Error: {e}")
            print("=" * 60)
    
    def send_another(self) -> bool:
        """
        Ask if user wants to send another message
        
        Returns:
            True if user wants to continue, False to exit
        """
        while True:
            choice = input("\n📩 Send another message? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'")
    
    def run(self):
        """Main application loop"""
        self.clear_screen()
        
        try:
            while True:
                self.print_header()
                
                # Get recipient phone number
                to_number = self.get_phone_number()
                
                # Get message content
                message = self.get_message()
                
                # Get optional media
                media_url = self.get_media_url()
                
                # Confirm before sending
                if not self.confirm_send(to_number, message):
                    print("❌ Message cancelled.")
                    if not self.send_another():
                        break
                    self.clear_screen()
                    continue
                
                # Send the message
                self.send_sms(to_number, message, media_url)
                
                # Ask if user wants to send another
                if not self.send_another():
                    break
                
                self.clear_screen()
        
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            sys.exit(0)
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            sys.exit(1)


def main():
    """Entry point for the application"""
    app = SMSTerminalApp()
    app.run()


if __name__ == "__main__":
    main()
