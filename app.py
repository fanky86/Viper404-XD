from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    url = request.form.get('url')

    if not url:
        return "URL tidak valid", 400

    # Opsi untuk mengunduh video dengan kualitas terbaik
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',  # Folder penyimpanan sementara
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)

        # Menemukan file yang diunduh
        filename = f"downloads/{result['title']}.{result['ext']}"
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
    app.run(debug=True)
