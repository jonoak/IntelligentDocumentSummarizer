from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import io
from summarizer import get_summary

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads/'
ALLOWED_EXTENSIONS = {'txt', 'pdf'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        summary = get_summary(file_path)
        return render_template('index.html', summary=summary)
    return 'File type not allowed'

@app.route('/download', methods=['POST'])
def download_summary():
    summary = request.form['summary']
    summary_io = io.StringIO(summary)
    return send_file(io.BytesIO(summary_io.read().encode()), download_name='summary.txt', as_attachment=True, mimetype='text/plain')


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)