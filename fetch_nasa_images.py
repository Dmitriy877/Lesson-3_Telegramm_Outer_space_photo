import requests
import os
import os.path
import argparse
from dotenv import load_dotenv
from save_picture_script import save_picture
from file_resolution_script import return_file_resolution

DIRECOTEY_NASA = "images"
FILENAME_NASA = "nasa_image"


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Создает директорию images и сохраняет в нее фотографии
         компании nasa. Введите количество загружаемых фотографий как аргумент,
        если аргумент не  указан будет загружено 5 фотографий""",
        argument_default=5

    )
    parser.add_argument('amount_pictures',
                        nargs='?',
                        default=5,
                        type=int)
    return parser


def download_nasa_pictures(entered_value, token):
    api_nasa_metod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {
        "api_key": token,
        "count": entered_value
    }
    response = requests.get(api_nasa_metod_url, params=payload)
    response.raise_for_status()
    picture_nasa_urls = response.json()
    pictures = []
    for picture_number, picture in enumerate(picture_nasa_urls):
        picture_link = picture_nasa_urls[picture_number]["url"]
        pictures.append(picture_link)

    for picture_number, picture_url in enumerate(pictures):
        file_type_nasa = return_file_resolution(picture_url)
        path = "{0}/{1}{2}{3}".format(
            DIRECOTEY_NASA,
            FILENAME_NASA,
            picture_number,
            file_type_nasa
        )
        save_picture(picture_url, path)


def main():

    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]

    os.makedirs(DIRECOTEY_NASA, exist_ok=True)

    parser = create_parser()
    entered_value = parser.parse_args()

    download_nasa_pictures(entered_value.amount_pictures,
                           token)


if __name__ == "__main__":
    main()
