from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import requests

import os

app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:path>')
def serve_file(path):
    return send_from_directory('.', path)

# --- CONFIGURATION ---
# Email Settings (School Details)
EMAIL_ADDRESS = "newachieverscience@gmail.com" 
EMAIL_PASSWORD = "your-app-password"    # Google Account -> Security -> App Passwords
RECEIVER_EMAIL = "newachieverscience@gmail.com"

# WhatsApp Settings
SCHOOL_PHONE = "919428242460"
ADMIN_PHONE = "919428242460" 

# IMPORTANT: To send WhatsApp messages automatically from the backend, 
# you MUST get a free API Key from CallMeBot. 
# Instructions: Send "I allow callmebot to send me messages" to +34 621 07 33 86 on WhatsApp.
WHATSAPP_API_KEY = "YOUR_API_KEY_HERE" 

@app.route('/submit', methods=['POST'])
def submit_admission():
    try:
        data = request.json
        student_name = data.get('studentName', 'N/A')
        phone = data.get('phone', 'N/A')
        standard = data.get('standard', 'N/A')
        
        # 1. Prepare Content
        subject = f"New Admission: {student_name}"
        body = f"New Student Inquiry:\n\nName: {student_name}\nPhone: {phone}\nClass: {standard}\nMedium: {data.get('medium')}\nMessage: {data.get('message')}"

        # 1b. SAVE TO LOCAL FILE (Safety Backup)
        with open("inquiries.txt", "a", encoding="utf-8") as f:
            f.write(f"\n--- {student_name} ({phone}) ---\n{body}\n----------------------\n")
        print(f"✅ Data saved to inquiries.txt")

        # 2. Send Email
        try:
            if EMAIL_PASSWORD != "your-app-password":
                msg = MIMEMultipart()
                msg['From'] = EMAIL_ADDRESS
                msg['To'] = RECEIVER_EMAIL
                msg['Subject'] = subject
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
                server.quit()
                print("✅ Email sent to School.")
        except Exception as e:
            print(f"❌ Email Error: {e}")

        # 3. Automatic WhatsApp Notification (to School & Admin)
        if WHATSAPP_API_KEY != "YOUR_API_KEY_HERE":
            wa_text = f"🎓 *New Admission Inquiry*\n\n*Student:* {student_name}\n*Phone:* {phone}\n*Class:* {standard}\n*Status:* Received via Website"
            
            # Send to School
            requests.get(f"https://api.callmebot.com/whatsapp.php?phone={SCHOOL_PHONE}&text={wa_text.replace(' ', '+')}&apikey={WHATSAPP_API_KEY}")
            # Send to Admin (You)
            requests.get(f"https://api.callmebot.com/whatsapp.php?phone={ADMIN_PHONE}&text={wa_text.replace(' ', '+')}&apikey={WHATSAPP_API_KEY}")
            print("✅ Automatic WhatsApp alerts sent.")

        return jsonify({"status": "success", "message": "Details sent automatically"}), 200

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    # Run the server on port 5000
    app.run(debug=True, port=5000)
