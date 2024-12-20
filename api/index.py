from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

# Konfigurasi SMTP
SMTP_SERVER = "smtp.yourdomain.com"  # Ganti dengan server SMTP Anda
SMTP_PORT = 587
EMAIL_USER = "support@fankyxd.xyz"   # Email pengirim
EMAIL_PASSWORD = "password_email_anda"  # Password email pengirim

# Fungsi Kirim Email
def send_email(sender_name, sender_email, message):
    subject = "Pesan Baru dari Website"
    body = f"Nama: {sender_name}\nEmail: {sender_email}\n\nPesan:\n{message}"

    msg = MIMEText(body)
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_USER  # Pesan dikirim ke email Anda sendiri
    msg['Subject'] = subject

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, EMAIL_USER, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# Endpoint untuk Kirim Pesan
@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        return jsonify({"error": "Semua bidang harus diisi"}), 400

    # Kirim email
    if send_email(name, email, message):
        return jsonify({"message": "Pesan berhasil dikirim"})
    else:
        return jsonify({"error": "Gagal mengirim pesan"}), 500

# Gunakan serverless WSGI
from werkzeug.middleware.proxy_fix import ProxyFix
app.wsgi_app = ProxyFix(app.wsgi_app)
