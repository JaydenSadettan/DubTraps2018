from flask import Flask, render_template, request, send_from_directory
# from flaskext.uploads import UploadSet, configure_uploads, IMAGES
import os
# from ReadImage import ReadImage

app = Flask(__name__)
# photos = UploadSet('photos', IMAGES)

# app.config['UPLOADED_PHOTOS_DEST'] = 'static/tmp'
# configure_uploads(app, photos)


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # if request.method == 'POST' and 'photo' in request.files:
    #     filename = photos.save(request.files['photo'])
    #     return result()
    return render_template('upload.html')


# @app.route('/result', methods=['GET', 'POST'])
# def result():
#     image = []
#     for filename in os.listdir('Static/tmp'):
#         image.append(os.path.join('Static/tmp', filename))
#
#     user_stats = ReadImage(image[0], local=True)
#     os.remove(image[0])
#
#     return str(user_stats.dict)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html,'), 404


if __name__ == "__main__":
    app.run(debug=True)