# 🧠 CodeMentor Pro - AI Code Assistant 🚀

CodeMentor Pro is a powerful AI assistant that analyzes your code and generates professional summaries using the `CodeLlama` model via Ollama.  
It delivers insights with translations (Hindi + Spanish), generates a PDF report, text-to-speech MP3, and sends results directly to your **email**, **WhatsApp**, and **Telegram**.

---

## 🚀 Features

- 🔍 Analyze code with natural language questions
- 🧠 Powered by `CodeLlama` (via Ollama API)
- 🌐 Multilingual summaries (Hindi, Spanish)
- 📄 Auto-generate PDF report of results
- 🔊 Convert summary to MP3 using TTS
- 📧 Email with PDF + MP3 attachment
- 📱 WhatsApp media sharing (via Twilio API)
- 📲 Telegram message + file delivery
- 🧾 Upload code files or paste directly
- 🖥️ Simple and clean UI using HTML/CSS and Flask for backend.

---

## 🔧 Project Structure

# CodeMentor-Pro-AI_Assistant/
│
├── app.py # Flask backend
├── .env # Secrets (API keys, tokens)
├── templates/
│ ├── index.html # UI form page
│ └── result.html # Result display
├── utils/
│ ├── email_utils.py # Send email with attachments
│ ├── whatsapp_utils.py # WhatsApp via Twilio
│ ├── telegram_utils.py # Telegram message & files
│ ├── translate_utils.py # Google Translate API
│ ├── tts_utils.py # gTTS/pyttsx3 voice generator
│ └── cloudinary_utils.py # Upload files to Cloudinary


---

## 📦 Requirements

Install all dependencies using pip:

```bash
pip install -r requirements.txt

Flask==3.0.3
requests==2.32.3
python-dotenv==1.0.1
pdfkit==1.0.0
cloudinary==1.39.1
gtts==2.5.1
pyttsx3==2.90
twilio==9.0.1
python-telegram-bot==13.15
googletrans==4.0.0-rc1

.env Folder

file contains sensitive information like API keys and tokens. Make sure to add your own credentials there.

EMAIL_SENDER=your_email@example.com
EMAIL_PASSWORD=your_password
CLOUDINARY_API_KEY=xxx
CLOUDINARY_API_SECRET=xxx
CLOUDINARY_CLOUD_NAME=xxx
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_USER_ID=xxx
TWILIO_SID=xxx
TWILIO_AUTH_TOKEN=xxx
TWILIO_PHONE_NUMBER=+1415xxxxxxx
WKHTMLTOPDF_PATH=C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe


💡 Example Usage
Open the web app and paste code or upload .py/.js/.txt file.

Ask your question, e.g.:

"Explain this code and find any performance issue."

Get result summary + Hindi/Spanish translation.

PDF & MP3 auto-generated.

Results sent via:

📧 Email with attachments

📱 WhatsApp link

📲 Telegram message + files

✨ Benefits
Helps you understand code in your language

Saves time with instant AI feedback

Useful for students, developers, reviewers

Get document-ready output without manual editing


👨‍💻 Author
Aryan Patel
GitHub | LinkedIn



🔮 Future Additions (Ideas)

✅ Add support for more languages (French, German, etc.)

✅ GitHub Gist integration for storing & sharing summaries

✅ Code error detection & fix suggestions

✅ Code complexity/efficiency scoring

✅ Real-time collaborative code feedback