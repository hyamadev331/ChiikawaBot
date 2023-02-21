from linebot import LineBotApi
from linebot.models import TextSendMessage
import os

def send_message(text):
  # トークン設定
  LINE_CHANNEL_ACCESS_TOKEN = "os.getenv('LINE_CHANNEL_ACCESS_TOKEN')
  line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)

  #実行
  line_bot_api.broadcast(TextSendMessage(text=text))
