from flask import Flask, render_template, request, send_from_directory
import pytesseract
from PIL import Image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def base_static(filename):
    return send_from_directory(app.root_path, filename)

@app.route('/extract_text', methods=['POST'])
def extract_text():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    
    if file.filename == '':
        return "No selected file"

    img = Image.open(file)
    extracted_text = pytesseract.image_to_string(img)
    
    return render_template('result.html', text=extracted_text)

if __name__ == '__main__':
    app.run(debug=True)

