from flask import Blueprint, render_template, request, send_from_directory

import functions

loader_blueprint = Blueprint('loader_blueprint', __name__)



catalog_blueprint = Blueprint(
    'catalog_blueprint',
    __name__,
    template_folder='templates')

@loader_blueprint.route("/", methods=["GET", "POST"])
def page_post_form():
    """
    выводит страницу добовления поста
    :return: шаблон страницы
    """
    return render_template('post_form.html')

@loader_blueprint.route("/add", methods=["POST"])
def add_post():
    """
    загружает  пост и картинку
    обрабатывает ошибки разрешения
    :return: выводит либо информацию о загрузке или ошибку
    """
    # Получаем файл
    picture = request.files.get("picture")
    # Получаем имя файла у загруженного фала
    filename = picture.filename

    # текст поста
    task = request.form['content']

    # Если расширение файла в белом списке
    if functions.is_filename_allowed(filename):

        # Сохраняем картинку под родным именем в папку uploads
        picture.save(f"./uploads/{filename}")
        # записываем информацию о посте в json фаил
        functions.add_new_post(filename, task)

        return render_template("post_uploaded.html", task=task, filename=filename)
    else:
        extension = filename.split(".")[-1]
        return f"Тип файлов {extension} не поддерживается"









