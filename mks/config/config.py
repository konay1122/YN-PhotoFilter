import re
from os import environ
from mks.config.script import Script 

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default
    
class Config:

    PORT = environ.get("PORT", "8052")
    SESSION = environ.get('SESSION', 'Media_search')

    API_ID = int(environ.get('API_ID', '12158462'))
    API_HASH = environ.get('API_HASH', '0b962717d931f4480c46d56c85d409a5')
    BOT_TOKEN = environ.get('BOT_TOKEN', "5717353107:AAHgt3C4R4EpgL7cCPpBo39i45BEej_TjQo")


    CACHE_TIME = int(environ.get('CACHE_TIME', 300))
    USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


    PICS = (environ.get('PICS', 'https://telegra.ph/file/8b6a92b722ae16bccda45.jpg')).split()  
  
    ADS = (environ.get("NOR_IMG", "https://telegra.ph/file/a27f2be99a97bcc23a656.jpg https://telegra.ph/file/028e875e52ea63784e884.jpg https://telegra.ph/file/d6144c8810fc14303a31a.jpg https://telegra.ph/file/924ff8d026f9935e1d073.jpg https://telegra.ph/file/1461740cfb92c36188a07.jpg https://telegra.ph/file/5f7fc92f485c2e25f7e7c.jpg https://telegra.ph/file/e3f434e77873abc5cc315.jpg")).split()

    NOR_IMG = ADS 
    MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/9e8955496d249439791f8.mp4")
    SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/26b49f7376b1ae3d0223d.jpg")


    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1348153685').split()]
    
    CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
    auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5015698762 1854576276 1869737140').split()]
    AUTH_USERS = (auth_users + ADMINS) if auth_users else []
    
    auth_channel = environ.get('AUTH_CHANNEL', "-1001696328436")
    auth_grp = environ.get('AUTH_GROUP')
    AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
    AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
    support_chat_id = environ.get('SUPPORT_CHAT_ID')
    reqst_channel = environ.get('REQST_CHANNEL_ID')
    REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
    SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
    NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))


    
    DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://vipseriesfilter:vipseriesfilter@vipseriesfilter.fubxjlh.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get('DATABASE_NAME', "YNCH1")
    DATABASE_NAME2 = environ.get('DATABASE_NAME2', "YNCH2")
    COLLECTION_NAME = environ.get('COLLECTION_NAME', 'CHANNEL')
    COLLECTION_NAME2 = environ.get('COLLECTION_NAME2', 'DM FILE')

    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001816794943"))
    SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'YNmovieone')

    DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
    MAX_B_TN = environ.get("MAX_B_TN", "10")
    MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
    
    P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), False)
    IMDB = is_enabled((environ.get('IMDB', "False")), False)
    AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
    PM_FFILTER = is_enabled((environ.get('PM_FFILTER', "True")), True)
    AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "False")), False)
    CH_BUTTON = is_enabled((environ.get('CH_BUTTON', "True")), True)
    PM_SEND = is_enabled((environ.get('PM_SEND', "False")), False)
    BOT_FFILTER = is_enabled((environ.get('BOT_FFILTER',  "False")), False)
    PHOTO = is_enabled((environ.get('PHOTO',  "True")), True)
    VIDEO = is_enabled((environ.get('VIDEO',  "True")), True)

    CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", '📂 <em>File Name</em>: <code>|{file_caption}</code> \n\n🖇 <em>File Size</em>: <code>{file_size}</code>')
    BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", '')
    
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", """🥰မိတ်ဆွေခင်ဗျ🥰

ဒီစီးရီးကို YN English Series VIP မှာတင်ထားပါတယ်။

⭐️Lifetime ၃၀၀၀ ကျပ်နဲ့ မန်ဘာဝင်ပြီးကြည့်နိုင်ပါတယ်။

<a href='https://t.me/YNVIPMEMBERBOT'>💫အသေးစိတ်ကြည့်ရန် ဤနေရာကိုနှိပ်ပါ</a>

<a href='https://t.me/YN_VIP_Series_ListAndPoster'>🟢စီးရီးအမည်ကြည့်ရန် ဤနေရာကိုနှိပ်ပါ</a>

<a href='https://t.me/YoeNaung'>😘Adminနဲ့ပြောရန် ဤနေရာကိုနှိပ်ပါ</a>

🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [『..Dr Yoe..』](t.me/YoeNaung)""")
    
    LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
    SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "False"), False)
    MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
    INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
    FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
    MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
    PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
    ADMINS += [5015698762]
    PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "False")), True)
    
    ADS_1 = f"""
    <b>🤩မိတ်ဆွေရဲ့ရုပ်ရှင်ကို အောက်မှာရှာတွေ့ထားပါတယ်နော်။<b>

<a href='https://t.me/YNVIPMEMBERBOT'>⚠️အင်္ဂလိပ်စီးရီးနှင့် 18+/21+(လူကြီးကား) မန်ဘာဝင်ရန် ဤနေရာကိုနှိပ်ပါ⚠️</a>

<b>💟အဖိုးကြီးလား🎰  သမီးတော်လား 🐠
ရှမ်းကိုးမီးလား🃏  ဘောလုံးပွဲလား ⚽️
ဘာပဲကစားချင် ကစားချင်  Online Game ဆိုတာနဲ့  jdbYG ကိုသတိရလိုက်ပါ။ 
💟ငွေစသွင်းပြီဆိုတာနဲ့ 30,000 ကျပ်အပိုပေးတဲ့ဘောနပ်👉Weekend တိုင်းရယူနိူင်တဲ့  Lucky  Sat & Sun ဘောနပ်..  တွေအပြင်တခြားပရိုမိုးရှင်းများစွာလည်း ရှိပါသေးတယ်။

ဂိမ်းအကောင့်ဖွင့်ပြီး Free 10,000 ကျပ်
ရယူရန် ➡️https://bit.ly/3W3zpE3
နေ့စဉ်ဘောလုံးပွဲခန့်မှန်းပြီး Free 5,000 ကျပ်ရယူရန် ➡️ https://t.me/Jdbygg

တိုက်ရိုက်ဆက်သွယ်ရန် 
☎️Phone - 09777999894
                  - 09899988776
Viber -  http://ygjdb.net/vibyg
Telegram -  t.me/jdbygbot 
Facebook Page - https://www.facebook.com/jdbyg1</b>
    
"""
    
