import json
from json import JSONDecodeError

# Создаем множество расширений
ALLOWED_EXTENSIONS = { 'jpeg', 'png'}


def get_all_post():
    """
    получение списка из json фаила
    и обработка ошибок
    :return: список постов
    """
    try:
        with open('posts.json', 'r', encoding='utf-8') as file:
            json_file = json.load(file)
        return json_file
    except FileNotFoundError:
        # Будет выполнено, если файл не найден
        print("Файл не найден")
    except JSONDecodeError:
        # Будет выполнено, если файл найден, но не превращается из JSON
        print("Файл не удается преобразовать")


def strip_punctuation_ru(string):
    """
    удаление знаков припинания из строки
    :param string: текст
    :return: строку без знаков припинания
    """
    # знаки припинания
    punctuations = '''!()—[]{};:'"\,<>./?@#$%^&*_~'''
    # пустая строка
    new_string = ""
    # цикл удаления знаков припинания
    for char in string:
        if char in punctuations:
            new_string += ' '
        else:
            new_string += char
    new_string = new_string.replace(" - ", " ")
    return " ".join(new_string.split())


def search_for_posts(query):
    """
    поиск постов по ключевому слову
    :param query: ключевое слово
    :return: список постов
    """
    # все посты
    all_post = get_all_post()
    # пустой список
    search_posts = []
    for post in all_post:
        siring = strip_punctuation_ru(post["content"])
        if query.lower() in siring.lower().split():
            search_posts.append(post)
    return search_posts

def add_new_post(filename, task):
    """
    записывает данные о новом посте
    :param filename: название картинки
    :param task: текст поста
    :return: ничего
    """
    # информация о посте
    temporary_dictionary = {'pic': f"./uploads/{filename}", "content": task}
    # все посты
    file_post = get_all_post()
    # добовление информации о новом посте
    file_post.append(temporary_dictionary)
    # запись этой информации в json фаил
    with open('posts.json', 'w', encoding='utf-8') as fout:
        json.dump(file_post, fout, ensure_ascii=False, sort_keys=True, indent=4)



def is_filename_allowed(filename):
    """
    проверка разрешения фаила
    :param filename: имя фаилы с разрешением
    :return: результат проверки
    """
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


