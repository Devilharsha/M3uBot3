from pyrogram import Client, filters
from utils import check_user, multi_rec, getChannels

app = Client(
    "Bloo_Rec_Bot",
    bot_token = "6295287643:AAEqPJ4hp3oOOShXOqsn0JFXe1sB8DfL1eI",
    api_id = 7931165,
    api_hash = "5a2e46d1e6deb1456c75aa743bc8e0e6"
)



@app.on_message(filters.incoming & filters.command(['multirec']) & filters.incoming & filters.text)
def multirec_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return

    if len(message.text.split()) < 3:
        message.reply_text("<b>Syntax: </b>`/multirec [channelName] [duration] | [filename]`")
        return

    multi_rec(app, message)

@app.on_message(filters.incoming & filters.command(['channels']) & filters.text)
def show_channels_handler(app, message):

    auth_user = check_user(message)
    if auth_user is None:
        return


    getChannels(app, message)


@app.on_message(filters.command(['start']) & filters.text)
def start_handler(app, message):

    if len(message.text.split()) < 3:
        message.reply_text("<b>A Mega Recording Telegram bot by Team Disney Cartoons</b>\n\n<b>Made with Love by @Free_De_La_Hoya_Official</b>")
        return
    # Don't remove Conan76 from here, Resepct the Developer...
    
app.run()
