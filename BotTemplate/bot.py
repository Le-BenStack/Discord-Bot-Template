import discord
from discord.ext import commands
from discord import app_commands
import os
import config

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")
    try:
        # Sync all commands
        await bot.tree.sync()
        print("Slash commands have been synced successfully.")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def setup_hook():
    # Load all commands
    for file in os.listdir("./commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")

# Start the bot
bot.run(config.TOKEN)