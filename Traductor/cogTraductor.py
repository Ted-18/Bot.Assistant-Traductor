# ADDON IMPORTS
import addons.Traductor.init as init

import addons.Traductor.functions.commands.commandRequirements as commandRequirements
import addons.Traductor.functions.events.eventOnRawReactionAdd as eventOnRawReactionAdd

# BOTASSISTANT IMPORTS
from services.serviceLogger import Logger
from services.serviceDiscordLogger import discordLogger as DiscordLogger
from settings.settingBot import debug

# INIT BOT VARIABLES
import services.serviceBot as serviceBot
discord = serviceBot.classBot.getDiscord()
discordCommands = serviceBot.classBot.getDiscordCommands()
commands = serviceBot.classBot.getCommands()
bot = serviceBot.classBot.getBot()



class Traductor(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

    # EVENTS
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        await eventOnRawReactionAdd.onRawReactionAdd(payload)

    groupTraductor = discordCommands.SlashCommandGroup("traductor", "🔶 Group of commands to manage the Traductor addon.")

    # Verify if the bot has the prerequisites permissions
    @groupTraductor.command(name="requirements", description="Check the prerequisites permissions of the addon.")
    async def cmdPermissions(self, ctx: commands.Context):
        await DiscordLogger.info(ctx, init.cogName, ctx.author.name + " has used the requirements command.", str(ctx.command))
        await commandRequirements.checkRequirements(ctx)        


def setup(bot):
    Logger.debug("Loading cog: " + init.cogName)
    bot.add_cog(Traductor(bot))
    
    