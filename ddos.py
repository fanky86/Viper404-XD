from flask import Flask, render_template, request, jsonify
import random
import time
from urllib.parse import urlparse

app = Flask(__name__)

# Halaman utama untuk menerima input dari pengguna
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menangani pengunduhan dan memulai tugas
@app.route('/attack', methods=['POST'])
def attack():
    url = request.form.get('url')
    thread_count = int(request.form.get('threads'))
    duration = int(request.form.get('duration'))

    if not url or thread_count <= 0 or duration <= 0:
        return jsonify({"error": "Invalid input"}), 400

    # Jalankan proses serangan atau tugas sesuai parameter
    # Di sini kita hanya memberikan respon sebagai contoh, bukan serangan DoS.
    response = {
        "message": f"Serangan dimulai pada {url} dengan {thread_count} threads selama {duration} detik."
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
