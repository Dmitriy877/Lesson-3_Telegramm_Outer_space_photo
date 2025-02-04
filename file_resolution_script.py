from urllib.parse import urlsplit
from os.path import splitext


def file_resolution(picture_url):
    path = urlsplit(picture_url).path
    file_resolution = splitext(path)[1]
    return file_resolution
