from colorthief import ColorThief
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "static/"


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/colors', methods=['POST', 'GET'])
def get_colors():
    image = request.files['file']
    filename = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    full_image_path = f"static/{image.filename}"

    color_thief = ColorThief(full_image_path)
    top_colors = color_thief.get_palette(color_count=11)
    return render_template("colors.html", image=full_image_path, top_colors=top_colors)


if __name__ == '__main__':
    app.run(debug=True)
