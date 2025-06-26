from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

def send_whatsapp_media(to_number, media_url):
    try:
        client = Client(os.getenv("TWILIO_ACCOUNT_SID"), os.getenv("TWILIO_AUTH_TOKEN"))
        from_whatsapp = f"whatsapp:{os.getenv('TWILIO_FROM')}"
        to_whatsapp = f"whatsapp:{to_number}"  # Must include +91 or country code
        client.messages.create(
            body="📎 Your CodeMentor Pro file:",
            from_=from_whatsapp,
            to=to_whatsapp,
            media_url=[media_url]
        )
        return "✅ WhatsApp media sent!"
    except Exception as e:
        return f"❌ WhatsApp error: {e}"

