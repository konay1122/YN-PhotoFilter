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

    PORT = environ.get("PORT", "8050")
    SESSION = environ.get('SESSION', 'Media_search')

    API_ID = int(environ.get('API_ID', '22270429'))
    API_HASH = environ.get('API_HASH', '3e2e8f8f0ae56bb0998c264c4ca243cb')
    BOT_TOKEN = environ.get('BOT_TOKEN', "6232389300:AAEe7lZuHhrgBQQse3FRMPA_chPsQCJCyak")


    CACHE_TIME = int(environ.get('CACHE_TIME', 300))
    USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))


    PICS = (environ.get('PICS', 'https://telegra.ph/file/8b6a92b722ae16bccda45.jpg')).split()  
  
    ADS = (environ.get("NOR_IMG", "https://telegra.ph/file/fa57407ba07037c1ec5eb.jpg https://telegra.ph/file/e58dc951765830a1c20f2.jpg https://telegra.ph/file/c4b864d6d02bf8c5a750d.jpg%20https://telegra.ph/file/c4afcd4b107f26ad524e6.jpg https://telegra.ph/file/aa075e75175fd8df01299.jpg https://telegra.ph/file/58800e3e7c61f7908de45.jpg https://telegra.ph/file/b2dfb2417f7bec3c4855e.jpg https://telegra.ph/file/22a5ef62ea1b28ca6cb2b.jpg")).split()

    NOR_IMG = ADS 
    MELCOW_VID = environ.get("MELCOW_VID", "https://graph.org/file/9e8955496d249439791f8.mp4")
    SPELL_IMG = environ.get("SPELL_IMG", "https://graph.org/file/26b49f7376b1ae3d0223d.jpg")


    ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '5015698762').split()]
    
    CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
    auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '5015698762 1854576276 1869737140').split()]
    AUTH_USERS = (auth_users + ADMINS) if auth_users else []
    
    auth_channel = environ.get('AUTH_CHANNEL', "")
    auth_grp = environ.get('AUTH_GROUP')
    AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
    AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
    support_chat_id = environ.get('SUPPORT_CHAT_ID')
    reqst_channel = environ.get('REQST_CHANNEL_ID')
    REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
    SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
    NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", False))


    
    DATABASE_URI = environ.get('DATABASE_URI', "mongodb+srv://sum64291:sum64291@cluster0.dnufyie.mongodb.net/?retryWrites=true&w=majority")
    DATABASE_NAME = environ.get('DATABASE_NAME', "WMC")
    DATABASE_NAME2 = environ.get('DATABASE_NAME2', "WMC2")
    COLLECTION_NAME = environ.get('COLLECTION_NAME', 'CHANNEL')
    COLLECTION_NAME2 = environ.get('COLLECTION_NAME2', 'DM FILE')

    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', "-1001917003256"))
    SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'https://t.me/WinterMovesRequestGroup')

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
    
    IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", """🏷 𝖳𝗂𝗍𝗅𝖾: <a href={url}>{title}</a> - {year} 

⭐️ 𝖱𝖺𝗍𝗂𝗇𝗀𝗌: {rating}/ 10  
🎭 𝖦𝖾𝗇𝖾𝗋𝗌: {genres} 

🎊 𝖯𝗈𝗐𝖾𝗋𝖾𝖽 𝖡𝗒 [『Thuta』](t.me/thuta2002)

""")
    
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
    
"""
    
