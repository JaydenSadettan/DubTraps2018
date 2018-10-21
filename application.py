from flask import Flask, render_template, request, flash
from werkzeug.utils import secure_filename
import os
from ReadImage import ReadImage

app = Flask(__name__)
UPLOAD_FOLDER = 'static/tmp'
# app.config['UPLOADED_PHOTOS_DEST'] = 'static/tmp'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['photo']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
        return result()
    return render_template("upload.html")


@app.route('/result', methods=['GET', 'POST'])
def result():
    image = []
    for filename in os.listdir('Static/tmp'):
        image.append(os.path.join('Static/tmp', filename))

    user_stats = ReadImage(image[0], local=True)
    os.remove(image[0])
    s = user_stats._getdata
    return '''<html> <head>    
    <link rel="stylesheet" 
    href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" 
    integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
    </head><body>''' + s + "</body></html>"

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html,'), 404


if __name__ == "__main__":
    app.run(debug=True)