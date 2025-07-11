import os
import json
import requests
import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import pdfkit
from flask import Flask, request, render_template, send_file
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
app = Flask(__name__)

# ---------- Utility Imports ----------
from utils.email_utils import send_summary_email_with_attachments
from utils.cloudinary_utils import upload_to_cloudinary
from utils.whatsapp_utils import send_whatsapp_media
from utils.telegram_utils import send_telegram_message, send_telegram_file
from utils.translate_utils import translate_text
from utils.tts_utils import generate_tts


# ---------- LLM Analysis ----------
def analyze_code_with_ollama(code, question):
    prompt = f"Analyze this code and answer:\n{question}\n\nCode:\n{code}"
    data = {
        "model": "PatelCoder",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(
        "http://localhost:11434/api/generate",
        headers={'Content-Type': 'application/json'},
        data=json.dumps(data)
    )
    return json.loads(response.text)['response'] if response.status_code == 200 else f"Error: {response.text}"

# ---------- PDF Generator (EN + HI only) ----------
def generate_pdf(summary, hindi, output_path="summary.pdf"):
    html_content = f"""
    <html>
    <head><style>body {{ font-family: Arial; line-height: 1.6; }}</style></head>
    <body>
        <h1 style="color:#007BFF;">🧠 CodeMentor Pro - AI Code Summary</h1>
        <h2>💡 AI Response (English):</h2>
        <p>{summary}</p>
        <h2>🔁 Hindi Translation:</h2>
        <p>{hindi}</p>
        <hr>
        <footer><p style="text-align:center;">Generated by Aryan Patel - CodeMentor Pro</p></footer>
    </body>
    </html>
    """
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    pdfkit.from_file("temp.html", output_path, configuration=config)
    os.remove("temp.html")
    return output_path

# ---------- Main Route ----------
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        whatsapp_number = request.form['whatsapp']
        question = request.form['question'].strip()
        code_input = request.form.get('code_input', '').strip()
        uploaded_files = request.files.getlist('codefile')

        # 📥 Get code from input or file
        code_content = code_input
        if not code_input and uploaded_files:
            for file in uploaded_files:
                code_content += file.read().decode('utf-8') + "\n"

        if not code_content:
            return "⚠️ Please paste code or upload file."

        # 🤖 AI Summary
        summary = analyze_code_with_ollama(code_content, question)

        # 🌐 Hindi Translation
        translated_hi = translate_text(summary, "hi")

        # 📄 Generate PDF (EN + HI only)
        pdf_path = generate_pdf(summary, translated_hi)
        pdf_url = upload_to_cloudinary(pdf_path)

        # 🔊 Generate TTS Audio
        mp3_path = generate_tts(summary)
        mp3_url = upload_to_cloudinary(mp3_path)

        # ✉️ Email (with PDF & MP3)
        send_summary_email_with_attachments(
            subject="Your AI Code Summary",
            body=summary,
            receiver_email=email,
            attachments=[pdf_path, mp3_path]
        )

        # 📱 WhatsApp (PDF + MP3 links)
        send_whatsapp_media(whatsapp_number, pdf_url)
        send_whatsapp_media(whatsapp_number, mp3_url)

        # 📲 Telegram (Text + Attachments)
        send_telegram_message(summary)
        send_telegram_file(pdf_path, filename="CodeMentorPro_Summary.pdf")
        send_telegram_file(mp3_path, filename="CodeMentorPro_Summary.mp3")

        return render_template("result.html",
                               summary=summary,
                               pdf_link=pdf_url,
                               audio_path=mp3_url,
                               hindi_summary=translated_hi)

    return render_template("index.html")

# 📂 File download (optional)
@app.route('/download/<filename>')
def download_file(filename):
    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
