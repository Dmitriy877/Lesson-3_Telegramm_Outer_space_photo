import requests
import os
import os.path
import argparse
from save_picture_script import save_picture

DIRECTORY_SPACEX = "images"
FILENAME_SPACEX = "spacex_image"
FILE_TYPE_SPACEX = ".jpeg"


def create_parser():
    parser = argparse.ArgumentParser(
       description=""" Сохраняет фотографии с запуска компании spacex. 
       Введите id запуска как аргумент, если id запуска
       не указан будут загружены фотографии с последнего запуска. 
       Если фотографии при запуске не были сделаны будет выведено сообщение
       об этом"""
        )
    parser.add_argument('flight_id',
                        nargs='?',
                        type=str)
    return parser


def fetch_spacex_certain_launch_images(flight_id):
    api_spacex_metod_url = 'https://api.spacexdata.com/v3/launches'
    payload = {"flight_id": flight_id.flight_id}
    response = requests.get(api_spacex_metod_url, params=payload)
    response.raise_for_status()
    picture_spacex_urls = response.json()[0]["links"]["flickr_images"]

    for picture_number, picture_url in enumerate(picture_spacex_urls):
        path = "{0}/{1}{2}{3}".format(DIRECTORY_SPACEX,
                                      FILENAME_SPACEX,
                                      picture_number,
                                      FILE_TYPE_SPACEX
                                      )
        save_picture(picture_url, path)


def fetch_spacex_latest_launch_images():
    api_spacex_metod_url = 'https://api.spacexdata.com/v5/launches/latest'
    response = requests.get(api_spacex_metod_url)
    response.raise_for_status()
    picture_spacex_urls = response.json()[0]["links"]["flickr_images"]

    for picture_number, picture_url in enumerate(picture_spacex_urls):
        path = "{0}/{1}{2}{3}".format(DIRECTORY_SPACEX,
                                      FILENAME_SPACEX,
                                      picture_number,
                                      FILE_TYPE_SPACEX
                                      )
        save_picture(picture_url, path)


def main():

    os.makedirs(DIRECTORY_SPACEX, exist_ok=True)
    parser = create_parser()
    flight_id = parser.parse_args()

    if flight_id.flight_id:
        fetch_spacex_certain_launch_images(flight_id)
    else:
        try:
            fetch_spacex_latest_launch_images()
        except KeyError:
            print("""Во время запуска фотографии не были сделаны! 
                Укажите id запуска""")
 

if __name__ == "__main__":
    main()
