import logging
from flask import Blueprint, render_template, request

import functions

main_blueprint = Blueprint('main_blueprint', __name__)

catalog_blueprint = Blueprint(
    'catalog_blueprint',
    __name__,
    template_folder='templates')

@main_blueprint.route("/")
def page_index():
    """
    стартовая страница
    :return: шаблон страницы
    """
    return render_template("index.html")

@main_blueprint.route("/search")
def search_post():
    """
    поиск поста по слову
    :return: список постов
    """
    logging.basicConfig(level=logging.INFO, filename='search.log', format='%(asctime)s [%(levelname)s] %(message)s')
    string_search = request.args['s']
    if string_search:

        all_post = functions.search_for_posts(string_search)
        logging.info(f"пользователь ищет слово {string_search}")
        if all_post:
            return render_template('post_list.html', all_post=all_post, string_search=string_search)
        else:
            return render_template('error_on_the_server.html')
    else:
        logging.info("пользователь не ввёл слово")
        return render_template('search_not_string.html')



