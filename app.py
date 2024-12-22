from flask import Flask, render_template, request, send_file
import yt_dlp
from io import BytesIO

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
        'outtmpl': '-',  # Output ke stdout, tidak menyimpan ke file lokal
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(url, download=True)

            # Mengambil data video yang diunduh ke dalam memori
            video_data = ydl.prepare_filename(result)
            video_file = BytesIO(video_data.encode('utf-8'))  # Gunakan BytesIO untuk menyimpan data di memori
            
            # Menemukan ekstensi file video
            extension = result.get('ext', 'mp4')

            # Mengirimkan file video langsung tanpa menyimpannya di disk
            return send_file(video_file, as_attachment=True, download_name=f"{result['title']}.{extension}", mimetype=f"video/{extension}")
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
