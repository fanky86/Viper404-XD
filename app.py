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
        'quiet': True,  # Menonaktifkan output console
        'noplaylist': True,  # Jangan mengunduh playlist
    }

    try:
        # Mengunduh video ke memori menggunakan yt-dlp
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_url = info_dict['url']  # URL file video yang diunduh

            # Unduh file video dan simpan ke dalam memori (BytesIO)
            video_data = BytesIO()
            with yt_dlp.YoutubeDL({'outtmpl': '-'}) as ydl:
                ydl.download([url])
                with open(ydl.prepare_filename(info_dict), 'rb') as f:
                    video_data.write(f.read())
            
            video_data.seek(0)  # Reset pointer ke awal untuk dikirimkan
            extension = info_dict.get('ext', 'mp4')  # Menentukan ekstensi file

            # Kirimkan file video langsung ke pengguna
            return send_file(video_data, as_attachment=True, download_name=f"{info_dict['title']}.{extension}", mimetype=f"video/{extension}")

    except Exception as e:
        return f"Terjadi kesalahan: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
