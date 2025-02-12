import os
from dotenv import load_dotenv
import random
import time
import argparse
from telegramm_post_image import post_image


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента время 
        через которе публиковать картинку из директории images (время указывать 
        в часах), если время не указано публикует картинку раз в 4 часа, после 
        публикаии всех картинок директории перемешивает картинки и начинает 
        публикацию заново.""",
        argument_default=4
        )
    parser.add_argument(
                        "post_time",
                        nargs="?",
                        default=4,
                        type=int
                        )
    return parser


def photo_post(post_time, token, chat_id, images):
    post_time_hours = post_time * 3600
    while (True):
        for image in images:
            post_image(image, token, chat_id) 
            time.sleep(post_time_hours)
        random.shuffle(images)


def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_API_KEY"]
    chat_id = os.environ["TELEGRAMM_CHAT_ID"]
    images = os.listdir(r"images")

    parser = create_parser()
    args = parser.parse_args()
    photo_post(args.post_time, token, chat_id, images)


if __name__ == "__main__":
    main()
