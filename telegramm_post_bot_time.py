import telegram
import os
from dotenv import load_dotenv
import random
import time
import argparse
load_dotenv()


token = os.environ["TELEGRAMM_API_KEY"]
chat_id = "@OuterSpacePhoto"
images = os.listdir(r"images")
bot = telegram.Bot(token=token)


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


def photo_post(post_time):
    post_time_hours = post_time * 3600
    while (True):
        for image in images:
            bot.send_photo(chat_id=chat_id,
                           photo=open("images/{0}".format(image),
                                      "rb"))
            time.sleep(post_time_hours)
        random.shuffle(images)


def main():

    parser = create_parser()
    post_time = parser.parse_args()
    photo_post(post_time.post_time)


if __name__ == "__main__":
    main()
