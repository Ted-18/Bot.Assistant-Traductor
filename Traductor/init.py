# Github informations
enableGithub = True
author = "Ted-18"
repository = "Bot.Assistant-Traductor"
version = "1.0.2"

# To activate this addon
cogEnabled = True

# Name of the addon
cogName = "traductor"

# Name of the file containing the cog
cogFile = "cogTraductor"

# List of packages required by the addon
packageDependencies = [
    "py-cord",
    "mysql-connector-python",
    "deep-translator"
]

# List of addons required by the addon
addonDependencies = [
    "Configuration"
]

# List of permissions required by the addon
addonPermissions = [
    "add_reactions",
    "manage_messages",
    "read_message_history",
    "send_messages"
]

commandPermissions = {
    # Permission to check the addon's permissions
    "cmdRequirements" : "discord.permission.manage_guild"
}