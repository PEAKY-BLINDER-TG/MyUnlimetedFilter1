import pyrogram

import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = llogging.getLogger("pyrogram").setLevel(logging.WARNING)ogging.getLogger(__name__)

from pyrogram import Client 

if __name__ == "__main__" :
    plugins = dict(
        root="tg_bot"
    )
    mt_botz = Client(
        "MT ID BOT",
        bot_token=os.environ.get("TOKEN"),
        api_id="1517558",
        api_hash="7f6fbfd179b27e8f6188dccff9c196ee",
        plugins=plugins,
        workers=100
    )
    mt_botz.run()
