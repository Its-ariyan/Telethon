import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "6435225"))
    API_HASH = os.environ.get("API_HASH", "4e984ea35f854762dcde906dce426c2d")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5786222700:AAEipo7r2TkYkvpxCm7wFHIl_NiQio_cvSA")
    OWNER_ID = os.environ.get("OWNER_ID", "NixaXD")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKsBu1vbqe1IxCKdZ79oKiL1JZMYh46HZ6VcaprzanKuCbyInnbvKFJBBh5Wh10ji2_7w_X5MUvInLw7P4KhA4cYUUQ4XJBMM5sDedtFWA7iMzx6l08HX0TNWHerZDYmMr0X3gsYIr6B0RcZ6Wxmi5sSOLCwiX7e512XGRnFjvMzaWpp-WBRu8qB4CgVZTLra2bTxfcjvV0g8jxKFiUnTwBd77gc8FvcWGRe8GoAu7Mme2Ln2PZcUlggmxRpKhy2FQ7wvO2wj7DXiueDpEfHML8GWyLX95JgGgrOHXPGmNf31AAhyhJVmes98dU634qY2EfTNcYfnCrXg_ULcOB237zxWSA=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SankiXClonerBot")
    SUPPORT = os.environ.get("SUPPORT", "SankiWorldMF") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "NixaWorld") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "5470233619")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', True) # Change it to "True"
