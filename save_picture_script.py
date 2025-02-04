import requests


def save_picture(picture_url, path):
    response = requests.get(picture_url)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)
