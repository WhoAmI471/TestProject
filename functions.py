import json


POST_PATH = r"C:\PyProjects\weather_bot\venv\lesson12_project_source_v3-master\posts.json"


def load_posts():
    with open (POST_PATH, 'r', encoding='utf-8') as file:
        posts = json.load(file)
    return posts


def uploads_posts(posts):
    with open(POST_PATH, 'w', encoding='utf-8') as file:
        json.dump(posts, file, indent=4, ensure_ascii=False)



