import telegram


def post_image(image, token, chat_id):
    bot = telegram.Bot(token=token)
    with open("images/{0}".format(image), "rb") as photo:
        bot.send_photo(
                       chat_id=chat_id,
                       photo=photo
                       )
