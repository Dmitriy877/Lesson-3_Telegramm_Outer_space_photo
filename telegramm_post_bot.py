import telegram
import os
from dotenv import load_dotenv
load_dotenv()


token = os.environ["TELEGRAMM_API_KEY"]
chat_id = "@OuterSpacePhoto"
text = "Hello"

bot = telegram.Bot(token=token)
bot.send_message(chat_id=chat_id, text=text)
