# Sendblue SMS Terminal Application

A terminal-based application for sending SMS/iMessage messages using the Sendblue API.

## Features

- 📱 Send SMS, iMessage, and RCS messages
- 🎯 Automatic fallback cascade (iMessage → RCS → SMS)
- 💬 Interactive terminal interface
- ✅ Phone number validation
- 📎 Optional media attachment support
- 🔒 Secure credential management with environment variables

## Prerequisites

1. **Sendblue Account** - Free tier available
   ```bash
   npm install -g @sendblue/cli
   sendblue setup
   ```

2. **Python 3.7+**

3. **Add a Contact** (on free plan)
   - Have the contact send a message to your Sendblue number first
   - On paid plans, you can message anyone directly

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Sendblue Credentials

Get your Sendblue API credentials:
```bash
sendblue show-keys  # API key and secret
sendblue lines      # Your phone number
```

Create a `.env` file in the project root:
```bash
cp .env.example .env
```

Edit `.env` and fill in your credentials:
```
SENDBLUE_API_KEY=your_api_key_here
SENDBLUE_API_SECRET=your_api_secret_here
SENDBLUE_PHONE_NUMBER=+15559876543
```

### 3. Run the Application

```bash
python main.py
```

## Usage

1. Launch the application: `python main.py`
2. Enter the recipient's phone number in E.164 format (e.g., `+15551234567`)
3. Type your message (press Enter twice when done)
4. Optionally attach media by providing a URL
5. Confirm the message details
6. Message is sent!

## Project Structure

```
sms/
├── main.py                 # Terminal application entry point
├── config/
│   └── env.py             # Environment configuration
├── services/
│   └── sms_api.py         # Sendblue API service
├── requirements.txt        # Python dependencies
├── .env.example           # Example environment file
└── .env                   # Your actual credentials (not in git)
```

## API Features

### Message Sending
- **Text**: Send text-only messages
- **Media**: Attach images, videos, audio, or files
- **Effects**: Add iMessage effects (celebration, fireworks, lasers, etc.)

### Supported Message Types
- **iMessage** - For Apple devices
- **RCS** - For Android (rich media support)
- **SMS** - Fallback for devices without iMessage/RCS

### Message Status
Messages go through these statuses:
`REGISTERED → PENDING → QUEUED → ACCEPTED → SENT → DELIVERED`

## Phone Number Format

All phone numbers must be in **E.164 format**:
- Start with `+` and country code
- US Example: `+1 (555) 123-4567` → `+15551234567`
- UK Example: `+44 (20) 7946 0958` → `+442079460958`

## Troubleshooting

### "Missing required environment variables"
- Make sure you created `.env` file
- Verify all three variables are filled in
- Check for typos in variable names

### "Failed to send message"
- Confirm the recipient is in E.164 format
- On free plan: recipient must have texted your number first
- Check your API credentials in Sendblue dashboard

### "iMessage not supported"
- The recipient may not have an Apple device
- Message will automatically fall back to RCS or SMS
- No additional cost for fallback

## Additional Resources

- [Sendblue Docs](https://docs.sendblue.com)
- [Python SDK](https://docs.sendblue.com/getting-started/client-packages)
- [API Reference](https://docs.sendblue.com/api/)
- [Webhook Setup](https://docs.sendblue.com/getting-started/webhooks)

## License

This project uses the Sendblue API for message delivery.
