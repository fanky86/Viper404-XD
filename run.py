from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

# Halaman utama dengan form untuk memicu script Python
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk menjalankan script Python
@app.route('/run-script', methods=['POST'])
def run_script():
    # Jalankan script Python
    output = subprocess.run(['python3', 'yourscript.py'], capture_output=True, text=True)
    
    # Tampilkan output script di halaman baru
    return f"<h1>Output Script:</h1><pre>{output.stdout}</pre>"

if __name__ == '__main__':
    app.run(debug=True)
