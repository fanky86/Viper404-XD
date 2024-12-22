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
        'quiet': True,  # Menonaktifkan output console
        'noplaylist': True,  # Jangan mengunduh playlist
        'extractaudio': False,  # Jangan hanya mengunduh audio
        'outtmpl': '-',  # Menyimpan hasil ke stdout (output stream) untuk diproses
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Mengunduh video
            info_dict = ydl.extract_info(url, download=True)

            # Mendapatkan URL file video yang diunduh
            video_url = info_dict['url']
            
            # Menyimpan file video ke dalam memori (BytesIO)
            video_data = BytesIO()
            
            # Mengunduh video secara langsung dan menyimpan ke memori
            with yt_dlp.YoutubeDL({'outtmpl': '-'}) as ydl_mem:
                ydl_mem.download([url])
                with open(ydl_mem.prepare_filename(info_dict), 'rb') as f:
                    video_data.write(f.read())
            
            video_data.seek(0)  # Set pointer ke awal
            extension = info_dict.get('ext', 'mp4')  # Menentukan ekstensi file

            # Kirimkan file video langsung ke pengguna
            return send_file(video_data, as_attachment=True, download_name=f"{info_dict['title']}.{extension}", mimetype=f"video/{extension}")

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
