from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)

from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('Y2UuAgi/bc4WdberD8e1IkEOJSzd0wFepokgM+LV2QdVuz5ll+sBo+rKG8xjJApTiQmoGlhP0AQ/9anLlc+2i0K0gfHQInI7iu14xNkGUg3aZI3ry11t3a6VU/noC4w5OFH3ie3BrJq9GQnGcevmWQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('d46ff916260630f6ed023338a7c33976')


# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'
# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    #event有什麼資料？詳見補充

    line_bot_api.reply_message(
        event.reply_token, TextSendMessage(text='Hi! Welcome to LSTORE.'))
    
if __name__ == "__main__":
    app.run()