import logging

from flask import Flask, send_from_directory


from loader.views import loader_blueprint
from main.views import main_blueprint

POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

# Регистрируем первый блюпринт
app.register_blueprint(main_blueprint)

# И второй тоже регистрируем
app.register_blueprint(loader_blueprint, url_prefix='/post')

@app.route("/uploads/<path:path>")
def static_dir(path):
    """
    вывод загруженых картинов
    :param path:
    :return:
    """
    return send_from_directory("uploads", path)
app.run()

