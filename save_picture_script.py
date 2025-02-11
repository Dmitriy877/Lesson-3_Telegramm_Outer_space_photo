import requests


def save_picture(picture_url, path, payload=""):
    response = requests.get(picture_url, params=payload)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)
