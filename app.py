import os
from flask import Flask, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint


POST_PATH = 'posts.json'
UPLOAD_FOLDER = '/uploads/images'


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)
app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), '/uploads/images')


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)
