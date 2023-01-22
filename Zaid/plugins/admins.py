from telethon import events, Button
from Zaid import Zaid
from Zaid.status import *
from Config import Config
from telethon.tl.functions.channels import EditAdminRequest
from telethon.tl.types import ChatAdminRights
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

@Zaid.on(events.callbackquery.CallbackQuery(data="admin"))
async def _(event):

    await event.edit(ADMIN_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="play"))
async def _(event):

    await event.edit(PLAY_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])

@Zaid.on(events.callbackquery.CallbackQuery(data="clone"))
async def _(event):

    await event.edit(CLONE_TEXT, buttons=[[Button.inline("« Bᴀᴄᴋ", data="help")]])


ADMIN_TEXT = """
**✘ A module from which admins of the chat can use!**

‣ /end - To End music streaming.
‣ /skip - To Skip Tracks Going on.
‣ /pause - To Pause streaming.
‣ /resume - to Resume Streaming.
‣ /leavevc - force The Userbot to leave Vc Chat (Sometimes Joined).
‣ /playlist - to check playlists.
"""

PLAY_TEXT = """
**✘ A module from which users of the chat can use!**

‣ /play - To Play Audio from Else Reply to audio file.
‣ /vplay - To Stream Videos (HEROKU_MODE > Doesn't support).
"""

CLONE_TEXT = """
ᴄʟᴏɴᴇ ʏᴏᴜʀ ʙᴏᴛ 

ᴛʜᴇʏ ʜᴀᴠᴇ ᴛʜᴇ sᴀᴍᴇ ᴀʙɢ ʙᴏᴛ ғᴜɴᴄᴛɪᴏɴs, ᴜᴘᴅᴀᴛᴇs ᴀɴᴅ ᴅᴀᴛᴀʙᴀsᴇ.

ᴛᴏ ᴄʀᴇᴀᴛᴇ ᴀ ᴄʟᴏɴᴇ:
• ɢᴏ ᴛᴏ @BotFather
• sᴛᴀʀᴛ ɪᴛ ᴀɴᴅ ᴛʏᴘᴇ /newbot
• ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ's ɴᴀᴍᴇ
• ᴄʜᴏᴏsᴇ ʏᴏᴜʀ ᴄʟᴏɴᴇ's ᴜsᴇʀɴᴀᴍᴇ

• sᴇɴᴅ ᴛʜᴇ ʙᴏᴛғᴀᴛʜᴇʀ ᴍᴇssᴀɢᴇ ᴡɪᴛʜ ᴀᴘɪ ᴋᴇʏ ᴛᴏ @SankiXClonerBot 
 ( ᴍᴜsᴛ ʙᴇ ғᴏʀᴡᴀʀᴅ)

• ᴅᴏɴᴇ! ɴᴏᴡ ᴇɴᴊᴏʏ ʏᴏᴜʀ ʙᴏᴛ 👍
 
ɴᴏᴛᴇ- ᴀғᴛᴇʀ sᴏᴍᴇ ʜᴏᴜʀ ᴛʜᴇɴ sᴇʀᴠᴇʀ ʀᴇsᴛᴀʀᴛ ᴡɪʟʟ ʙᴇ ᴀɴᴅ ᴄʟᴇᴀʀ ᴏʟᴅ ᴀʟʟ ᴅᴀᴛᴀ ᴛʜᴇɴ ʏᴏᴜʀ ʙᴏᴛ sᴛᴏᴘ!
sᴏ ᴛʜᴇɴ ᴀɢᴀɪɴ ғᴏʀᴡᴀʀᴅ ʏᴏᴜʀ ʙᴏᴛ ᴛᴏᴋᴇɴ 
"""
