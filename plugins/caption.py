async def handleCaption(_, bot):
    if _.message.reply_to_message is not None:
        
        file_caption = _.message.text or ""
        await _.message.reply_copy(_.effective_user.id,message_id = _.message.reply_to_message.message_id,caption = file_caption)
