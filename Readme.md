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
CodeMentor-Pro-AI/
│
├── app.py                         # Main Flask backend
├── templates/
│   ├── index.html                 # Upload & input form
│   └── result.html                # Result viewer
│
├── utils/                         # Modular utility functions
│   ├── email_utils.py
│   ├── whatsapp_utils.py
│   ├── telegram_utils.py
│   ├── cloudinary_utils.py
│   ├── translate_utils.py
│   └── tts_utils.py
│
├── .env                           # API keys & config
├── requirements.txt               # Python dependencies
├── static/                        # (optional) for CSS/JS if needed
└── README.md                      # Documentation



---

## 📦 Requirements

Install all dependencies using pip:

```bash
pip install -r requirements.txt

# ✅ Requirements for CodeMentor Pro – AI Code Assistant

## Core Backend
- flask
- python-dotenv
- requests
- pdfkit

## Translation & Audio
- googletrans==4.0.0rc1
- gtts

## Communication
- twilio
- cloudinary
- python-telegram-bot

## Optional (PDF Gen & Media Conversion)
- wkhtmltopdf (install manually)


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