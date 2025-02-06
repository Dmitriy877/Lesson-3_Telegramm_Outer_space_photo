import requests
import os
import os.path
import argparse
from dotenv import load_dotenv
from save_picture_script import save_picture
from file_resolution_script import file_resolution

directory_nasa = "images"
filename_nasa = "nasa_image"
amount_pictures = 5


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Создает директорию images и сохраняет в нее фотографии
         компании nasa. Введите количество загружаемых фотографий как аргумент,
        если аргумент не  указан будет загружено 5 фотографий"""

    )
    parser.add_argument('amount_nasa_pictures', nargs='?')
    return parser


def nasa_pictures(amount_nasa_pictures, token):
    api_nasa_metod_url = 'https://api.nasa.gov/planetary/apod'
    payload = {"api_key": token,
               "count": amount_nasa_pictures
               }
    response = requests.get(api_nasa_metod_url, params=payload)
    response.raise_for_status
    picture_nasa_url_list = response.json()
    picture_number_list = []
    for picture_number, picture in enumerate(picture_nasa_url_list):
        picture_link = picture_nasa_url_list[picture_number]["url"]
        picture_number_list.append(picture_link)

    for picture_number, picture_url in enumerate(picture_number_list):
        file_type_nasa = file_resolution(picture_url)
        path = "{0}/{1}{2}{3}".format(directory_nasa,
                                      filename_nasa,
                                      picture_number,
                                      file_type_nasa
                                      )
        save_picture(picture_url, path)


def main():

    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]

    os.makedirs(directory_nasa, exist_ok=True)

    parser = create_parser()
    amount_nasa_pictures = parser.parse_args()

    if amount_nasa_pictures.amount_nasa_pictures:
        nasa_pictures(amount_nasa_pictures.amount_nasa_pictures, token)
    else:
        nasa_pictures(amount_pictures, token)


if __name__ == "__main__":
    main()
      
