import os
from dotenv import load_dotenv

if os.path.exists("config.env"):
    load_dotenv("config.env")
else:
    load_dotenv()


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


class Config(object):
    API_ID = int(os.environ.get("API_ID", "20114039"))
    API_HASH = os.environ.get("API_HASH", "87297b8f3cc8fc9bbce591ad30da5896")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7653632933:AAHgBSp_5Yy5qxreFRmzjow4VP7VwQFJ9kE")
    DATABASE_NAME = os.environ.get("DATABASE_NAME", "tg_bot")
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://chiruedizz:WmzSiQlS35fLDImn@cluster0.4o4zl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    OWNER_ID = int(os.environ.get("OWNER_ID","8172163893"))
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002274225498"))
    WEB_SERVER = is_enabled(os.environ.get("WEB_SERVER", "False"), False)
    THUMBNAILS = list(map(str, os.environ.get("THUMBNAILS", "").split()))

    # Constants
    CANCEL_DATA = {}
    PROCESS_DATA = {}


class Script(object):
    START_MESSAGE = (
        " {mention}\n\nSend any link or set of links in a txt file to download them."
    )
    DEV_MESSAGE = """👋 Hey there, I'm 𝄟⃝🐬BHUMIHAR🐬 – your go-to Telegram bot developer!

🤖 Love having bots that do the heavy lifting for you? That's my jam! I'm all about crafting super cool and custom Telegram bots that make your life a breeze.

✨ **What I Do**

- **Bot Magic:** From automating tasks to interactive games, I create bots that do it all. Seriously, ask me anything!
- **Tailored to You:** Your bot, your rules. I'll whip up a bot that's as unique as you are.
- **Chill Vibes:** I keep your data super safe, so you can relax and enjoy the bot party.
- **Always Improving:** Telegram evolves, and my bots grow with it. I'm here to keep things fresh and fab.

Ready for your own bot buddy? Ping me on [Telegram](https://telegram.me/Reason_Someone) or check out me on [GitHub](https://github.com/The_real_xTaR). Wanna hire me? Find me on [Fiverr](https://www.fiverr.com/The_real_xTaR)!

Let's bot up and have some fun! 🤘"""
    HELP_MESSAGE = os.environ.get("HELP_MESSAGE", "Help message")
    PROGRESS_MESSAGE = """**╔════❰ Uploading ❱══❍
║╭━➣
║┣⪼  Progress:-  {percentage}%
║┣ 
║┣⪼ {progress}
║┣
║┣⪼《{finished} of {total}》
║┣ 
║┣⪼ Speed:- {speed}/s
║┣ 
║┣⪼ ETA:- {eta} 
║╰━➣ @Thebhumihar
╚════════════════❍**"""
    NEW_USER_MESSAGE = """#NewUser

🆔 User ID: `{user_id}`
👤 User: {mention}
"""
    DOWNLOADING = """📥 ᴅᴏᴡɴʟᴏᴀᴅɪɴɢ 📥 :- {start_index}/{end_index}

📝 Name » {link_no}) » {name}

Original Index: {orginal_start_index}/{orginal_end_index}

[𝄟⃝🐬BHUMIHAR🐬](https://t.me/BHUMIHAR_BOTSS)"""

    DEFAULT_CAPTION = """[📁] File_ID : {file_index}

𖤓 𝐓ɪᴛʟᴇ  : {file_name}

🗃 𝐒𝐢𝐳𝐞 : {file_size}

📚 Bᴀᴛᴄʜ Nᴀᴍᴇ : {batch_name}

Dᴏᴡɴʟᴏᴀᴅᴇᴅ Bʏ : [𝄟⃝🐬BHUMIHAR🐬](https://t.me/BHUMIHAR_BOTSS)"""


    CAPTION_CB = """**Set Caption

➢ Available Variables 👇**

┌🎴 𝐍𝐚𝐦𝐞 : `{file_name}`
├🗃 𝐒𝐢𝐳𝐞 : `{file_size}`
├⚙️ 𝐄𝐱𝐭𝐞𝐧𝐬𝐢𝐨𝐧 : `{file_extension}`
├🧭 𝐃𝐮𝐫𝐚𝐭𝐢𝐨𝐧 : `{file_duration}`
├🖇 𝐋𝐢𝐧𝐤 : `{file_url}`
├🔢 𝐈𝐧𝐝𝐞𝐱 : `{file_index}`
├🗳 𝐁𝐚𝐭𝐜𝐡 𝐍𝐚𝐦𝐞 : `{batch_name}`

==============================

➢ Current:
`{current_caption}`

==============================

➢ **Default:**
`{default_caption}`

➢ **Status:** {status}"""
