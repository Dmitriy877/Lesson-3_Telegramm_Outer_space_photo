import requests
import os
import os.path
import argparse
from save_picture_script import save_picture

directory_spacex = "images"
filename_spacex = "spacex_image"
file_type_spacex = ".jpeg"


def create_parser():
    parser = argparse.ArgumentParser(
       description=""" Сохраняет фотографии с запуска компании spacex. 
       Введите id запуска как аргумент, если id запуска
       не указан будут загружены фотографии с последнего запуска. 
       Если фотографии при запуске не были сделаны будет выведено сообщение
       об этом"""
        )
    parser.add_argument('flight_id', nargs='?')
    return parser


def fetch_spacex_images(flight_id):
    if flight_id.flight_id:
        api_spacex_metod_url = 'https://api.spacexdata.com/v3/launches'
        payload = {"flight_id": flight_id.flight_id}
        response = requests.get(api_spacex_metod_url, params=payload)
        response.raise_for_status()
        picture_spacex_urls = response.json()[0]["links"]["flickr_images"]

        for picture_number, picture_url in enumerate(picture_spacex_urls):
            path = "{0}/{1}{2}{3}".format(directory_spacex,
                                          filename_spacex,
                                          picture_number,
                                          file_type_spacex
                                          )
            save_picture(picture_url, path)

    else:
        try:
            api_spacex_metod_url = 'https://api.spacexdata.com/v5/launches/latest'
            response = requests.get(api_spacex_metod_url)
            response.raise_for_status()
            picture_spacex_urls = response.json()[0]["links"]["flickr_images"]

            for picture_number, picture_url in enumerate(picture_spacex_urls):
                path = "{0}/{1}{2}{3}".format(directory_spacex,
                                              filename_spacex,
                                              picture_number,
                                              file_type_spacex
                                              )
            save_picture(picture_url, path)
        except KeyError:
            print("Во время запуска фотографии не были сделаны! Укажите id запуска")
 
 
def main():

    os.makedirs(directory_spacex, exist_ok=True)

    parser = create_parser()
    flight_id = parser.parse_args()
    fetch_spacex_images(flight_id)


if __name__ == "__main__":
    main()
