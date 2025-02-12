import telegram


def post_image_name(entered_value, token, chat_id):
    bot = telegram.Bot(token=token)
    with open("images/{0}".format(entered_value), "rb") as photo:
        bot.send_photo(
                       chat_id=chat_id,
                       photo=photo
                       )
