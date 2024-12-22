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
        'format': 'best',  # Pilih format terbaik
        'outtmpl': '-',  # Menyimpan hasil ke stdout (output stream)
        'noplaylist': True,  # Jangan mengunduh playlist
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Mengunduh video
            info_dict = ydl.extract_info(url, download=True)

            # Menyimpan video ke memori (BytesIO)
            video_data = ydl.prepare_filename(info_dict)  # Menyimpan data video ke BytesIO
            video_file = BytesIO(video_data.encode('utf-8'))  # Convert ke BytesIO

            # Tentukan ekstensi file video
            extension = info_dict.get('ext', 'mp4')

            # Kirimkan video ke pengguna
            return send_file(video_file, as_attachment=True, download_name=f"{info_dict['title']}.{extension}", mimetype=f"video/{extension}")
    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
