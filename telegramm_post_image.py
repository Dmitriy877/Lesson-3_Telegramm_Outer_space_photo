import telegram


def post_image_name(entered_value, token, chat_id):
    with open("images/{0}".format(entered_value), "rb") as photo:
        bot = telegram.Bot(token=token)
        bot.send_photo(
                       chat_id=chat_id,
                       photo=photo
                       )
