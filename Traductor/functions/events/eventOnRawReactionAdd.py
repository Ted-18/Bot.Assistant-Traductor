from deep_translator import GoogleTranslator

import settings.settingColors as settingColors

# Init BotAssistant
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()

#En List of all languages emoji with name
languages = {
    '🇷🇺': 'russian',
    '🇧🇾': 'belarusian',
    '🇺🇦': 'ukrainian',
    '🇰🇿': 'kazakh',
    '🇦🇲': 'armenian',
    '🇦🇿': 'azerbaijani',
    '🇹🇯': 'tajik',
    '🇰🇬': 'kyrgyz',
    '🇲🇩': 'moldavian',
    '🇺🇿': 'uzbek',
    '🇺🇸': 'english',
    '🇺🇲': 'english',
    '🇬🇧': 'english', 
    '🇨🇦': 'english',

    '🇫🇷': 'french',
    '🇩🇪': 'german',
    '🇮🇹': 'italian',
    '🇪🇸': 'spanish',
    '🇨🇳': 'chinese (simplified)',
    '🇯🇵': 'japanese',  
    '🇹🇭': 'thai',  
    '🇰🇷': 'korean', 
    '🇬🇷': 'greek', 
    '🇷🇴': 'romanian', 
    '🇮🇳': 'hindi', 
    '🇳🇱': 'dutch',  
    '🇮🇸': 'icelandic',
    '🇩🇰': 'danish', 
    '🇸🇪': 'swedish', 
    '🇳🇴': 'norwegian', 
    '🇫🇮': 'finnish',
    '🇧🇬': 'bulgarian', 
    '🇵🇹': 'portuguese', 
    '🇹🇷': 'turkish', 
    '🇵🇱': 'polish', 
    '🇸🇾': 'arabic',
    '🇯🇴': 'arabic',
    '🇱🇧': 'arabic',  
    '🇰🇼': 'arabic',  
    '🇦🇪': 'arabic',  
    '🇧🇭': 'arabic', 
    '🇪🇬': 'arabic',  
    '🇸🇦': 'arabic',  
    '🇮🇶': 'arabic', 

}

async def onRawReactionAdd(payload):

    # Get the channel of the message
    channel = bot.get_channel(payload.channel_id)

    # Get the message
    message = await channel.fetch_message(payload.message_id)

    # Get the member who reacted
    member = payload.member


    # Create the variable for the language
    language = None


    # Check if the message is a bot message
    if member.bot:
        return

    # If the message has no text, send a message to the user
    if message.content == "":
        return
    
    # If the emoji was added twice return
    for reaction in message.reactions:
        if reaction.emoji == payload.emoji.name:
            if reaction.count > 1:
                return
    

    # If the message is not in the list of languages, send a message to the user
    if payload.emoji.name in languages:
        language = languages[payload.emoji.name]
    else:
        return

    translated = GoogleTranslator(source='auto', target=language).translate(message.content)


    embed = discord.Embed(
        title="Translation in " + payload.emoji.name,
        description=translated,
        color=settingColors.discordEmbed
    )

    # Add user name and user id to the embed
    embed.set_footer(text=member.name, icon_url=member.display_avatar)

    await channel.send(embed=embed)