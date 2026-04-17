# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official

from pyrogram import Client, filters
from pyrogram.types import Message
from database.db import db
from config import ERROR_MESSAGE
import os

@Client.on_message(filters.command("set_thumb") & filters.private)
async def set_thumb(client: Client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply_text("**__Reply to a photo to set it as custom thumbnail.__**")

    # photo is a Photo object — .file_id on it is the LARGEST available size,
    # which is what we want to store and later re-download at full quality.
    file_id = message.reply_to_message.photo.file_id

    await db.set_thumbnail(message.from_user.id, file_id)

    await message.reply_text("**__Custom Thumbnail Set Successfully ✅__**")
# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official

@Client.on_message(filters.command(["view_thumb", "see_thumb"]) & filters.private)
async def view_thumb(client: Client, message: Message):
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
        await message.reply_photo(photo=thumb, caption="**__Your Custom Thumbnail__**")
    else:
        await message.reply_text("**__You haven't set any custom thumbnail.__**")

@Client.on_message(filters.command(["del_thumb", "delete_thumb"]) & filters.private)
async def del_thumb(client: Client, message: Message):
    thumb = await db.get_thumbnail(message.from_user.id)
    if not thumb:
        return await message.reply_text("**__You don't have a custom thumbnail to delete.__**")
    
    await db.del_thumbnail(message.from_user.id)
    await message.reply_text("**__Custom Thumbnail Deleted Successfully 🗑__**")

@Client.on_message(filters.command("thumb_mode") & filters.private)
async def thumb_mode(client: Client, message: Message):
    # This might be to toggle between default/custom/no thumbnail.
    # For now, just a placeholder explaining usage.
    await message.reply_text("**__Thumbnail Mode: Custom (Default if set).__**\nUse /set_thumb and /del_thumb to manage.")

# Rexbots
# Don't Remove Credit
# Telegram Channel @RexBots_Official
