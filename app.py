from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.main import main_blueprint
from loader.loader import loader_blueprint


POST_PATH = r'C:\PyProjects\weather_bot\venv\lesson12_project_source_v3-master\posts.json'
UPLOAD_FOLDER = r'C:\PyProjects\weather_bot\venv\lesson12_project_source_v3-master\uploads\images'


app = Flask(__name__)
app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run(debug=True)

