from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/run-script', methods=['POST'])
def run_script():
    # Memanggil skrip Python
    result = subprocess.run(['python', 'script.py'], capture_output=True, text=True)
    return jsonify(output=result.stdout)

if __name__ == '__main__':
    app.run(debug=True)
