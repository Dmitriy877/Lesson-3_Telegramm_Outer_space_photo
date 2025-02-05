import telegram
import os
from dotenv import load_dotenv
import random
import argparse
load_dotenv()


token = os.environ["TELEGRAMM_API_KEY"]
chat_id = "@OuterSpacePhoto"
images_list = os.listdir(r"images")


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('image_name', nargs='?')
    return parser


def post_image_name(image_name):
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(image_name),
                              "rb"))


def post_random_image():
    bot = telegram.Bot(token=token)
    bot.send_photo(chat_id=chat_id,
                   photo=open("images/{0}".format(random.choice(images_list)),
                              "rb"))

    
def main():

    parser = createParser()
    image_name = parser.parse_args()

    if image_name.image_name:
        post_image_name(image_name.image_name)
    else:
        post_random_image()  


if __name__ == "__main__":
    main()
