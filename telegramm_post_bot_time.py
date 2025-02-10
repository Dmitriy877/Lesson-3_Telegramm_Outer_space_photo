import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse

images = os.listdir(r"images")


def create_parser():
    parser = argparse.ArgumentParser(
        description="""Данный скрипт принимает в качестве аргумента время 
        через которе публиковать картинку из директории images (время указывать 
        в часах), если время не указано публикует картинку раз в 4 часа, после 
        публикаии всех картинок директории перемешивает картинки и начинает 
        публикацию заново.""",
        argument_default=4
        )
    parser.add_argument("post_time",
                        nargs="?",
                        default=4,
                        type=int
                        )
    return parser


def photo_post(entered_value, token, chat_id):
    post_time_hours = entered_value * 3600
    while (True):
        for image in images:
            bot = telegram.Bot(token=token)
            bot.send_photo(chat_id=chat_id,
                           photo=open("images/{0}".format(image),
                                      "rb"))
            time.sleep(post_time_hours)
        random.shuffle(images)


def main():
    load_dotenv()
    token = os.environ["TELEGRAMM_API_KEY"]
    chat_id = "@OuterSpacePhoto"

    parser = create_parser()
    entered_value = parser.parse_args()
    photo_post(entered_value.post_time, token, chat_id)


if __name__ == "__main__":
    main()
