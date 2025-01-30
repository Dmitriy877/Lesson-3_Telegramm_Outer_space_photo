import requests
import os
import os.path
from urllib.parse import urlsplit
from os.path import splitext
from dotenv import load_dotenv


directory_spacex = "images"
filename_spacex = "nubble"
file_type_spacex = ".jpeg"

directory_nasa = "images_nasa"
filename_nasa = "nasa_image"

directory_epic = "images_epic"
filename_epic = "epic_image"

flight_id = "5a9fc479ab70786ba5a1eaaa"


def save_picture(picture_url, path):
    response = requests.get(picture_url)
    response.raise_for_status()
    with open(path, "wb") as file:
        file.write(response.content)


def fetch_spacex_last_launch(flight_id):
    api_spacex_metod_url = 'https://api.spacexdata.com/v3/launches'
    payload = {"flight_id": flight_id}
    response = requests.get(api_spacex_metod_url, params=payload)
    response.raise_for_status()
    picture_spacex_url_list = response.json()[0]["links"]["flickr_images"]

    for picture_number, picture_url in enumerate(picture_spacex_url_list):
        path = "{0}/{1}{2}{3}".format(directory_spacex,
                                      filename_spacex,
                                      picture_number,
                                      file_type_spacex
                                      )
        save_picture(picture_url, path)


def nasa_pictures(amount_nasa_pictures):
    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]
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


def epic_pictures(amount_epic_pictures):
    load_dotenv()
    token = os.environ["NASA_EPIC_API_KEY"]
    payload = {"api_key": token}
    response = requests.get("https://api.nasa.gov/EPIC/api/natural/images", 
                            params=payload)
    response.raise_for_status
    epic_lists = response.json()
    picture_list = []

    for number, epic_list in enumerate(epic_lists):
        picture_name = epic_lists[number]["image"]
        picture_date = epic_lists[number]["date"].split(" ")[0]
        picture_date_url = picture_date.replace("-", "/")
        picture_link = """https://api.nasa.gov/EPIC/archive/natural/{0}/png/{1}.png?api_key={2}""".format(picture_date_url, picture_name, token)
        picture_list.append(picture_link)
        if amount_epic_pictures == number:
            break

    for picture_number, picture_url in enumerate(picture_list):
        file_type_epic = file_resolution(picture_url)
        path = "{0}/{1}{2}{3}".format(directory_epic,
                                      filename_epic,
                                      picture_number,
                                      file_type_epic
                                      )
        save_picture(picture_url, path)


def file_resolution(picture_url):
    path = urlsplit(picture_url).path
    file_resolution = splitext(path)[1]
    return file_resolution


def main():

    if not os.path.exists(directory_spacex):
        os.makedirs(directory_spacex)

    if not os.path.exists(directory_nasa):
        os.makedirs(directory_nasa)

    if not os.path.exists(directory_epic):
        os.makedirs(directory_epic)

    fetch_spacex_last_launch(flight_id)
    nasa_pictures(20)
    epic_pictures(5)


if __name__ == "__main__":
    main()
