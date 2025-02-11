import requests
import os
import os.path
import argparse
from dotenv import load_dotenv
from save_picture_script import save_picture
from file_resolution_script import return_file_resolution


DIRECORY_EPIC = "images"
FILENAME_EPIC = "epic_image"


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Создает директорию images и сохраняет в нее фотографии
         компании epic. Введите количество загружаемых фотографий как аргумент,
        если аргумент не  указан будет загружено 5 фотографий""",
        argument_default=5
    )
    parser.add_argument('amount_pictures',
                        nargs='?',
                        default=5,
                        type=int)
    return parser


def download_epic_pictures(entered_value, token):
    payload = {"api_key": token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", 
                            params=payload)
    response.raise_for_status()
    epic_urls = response.json()
    pictures = []

    for number, epic_list in enumerate(epic_urls):
        picture_name = epic_urls[number]["image"]
        picture_date = epic_urls[number]["date"].split(" ")[0]
        picture_date_url = picture_date.replace("-", "/")
        picture_link = "https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png".format(picture_date_url, picture_name)
        pictures.append(picture_link)
        if entered_value == number:
            break

    for picture_number, picture_url in enumerate(pictures):
        file_type_epic = return_file_resolution(picture_url)
        path = "{0}/{1}{2}{3}".format(
            DIRECORY_EPIC,
            FILENAME_EPIC,
            picture_number,
            file_type_epic
        )
        save_picture(picture_url, path, payload)


def main():

    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]

    os.makedirs(DIRECORY_EPIC, exist_ok=True)

    parser = create_parser()
    entered_value = parser.parse_args()

    download_epic_pictures(entered_value.amount_pictures,
                           token)


if __name__ == "__main__":
    main()
