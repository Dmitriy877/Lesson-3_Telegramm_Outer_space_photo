import requests
import os
import os.path
import argparse
from dotenv import load_dotenv
from save_picture_script import save_picture
from file_resolution_script import file_resolution


directory_epic = "images"
filename_epic = "epic_image"


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Создает директорию images и сохраняет в нее фотографии
         компании epic. Введите количество загружаемых фотографий как аргумент,
        если аргумент не  указан будет загружено 5 фотографий""",
        argument_default=5
    )
    parser.add_argument('entered_amount_pictures', nargs='?')
    return parser


def download_epic_pictures(entered_amount_pictures, token):
    load_dotenv()
    payload = {"api_key": token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", 
                            params=payload)
    response.raise_for_status
    epic_urls = response.json()
    pictures = []

    for number, epic_list in enumerate(epic_urls):
        picture_name = epic_urls[number]["image"]
        picture_date = epic_urls[number]["date"].split(" ")[0]
        picture_date_url = picture_date.replace("-", "/")
        picture_link = requests.get("https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png".format(picture_date_url, picture_name),
                                    params=payload)

        pictures.append(picture_link.url)
        if entered_amount_pictures == number:
            break

    for picture_number, picture_url in enumerate(pictures):
        file_type_epic = file_resolution(picture_url)
        path = "{0}/{1}{2}{3}".format(
            directory_epic,
            filename_epic,
            picture_number,
            file_type_epic
        )
        save_picture(picture_url, path)


def main():

    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]

    os.makedirs(directory_epic, exist_ok=True)

    parser = create_parser()
    entered_amount_pictures = parser.parse_args()

    download_epic_pictures(entered_amount_pictures.entered_amount_pictures,
                           token)


if __name__ == "__main__":
    main()
