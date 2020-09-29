import json
import os
import discord
from discord.ext import commands

with open("config.json") as f:
    data = json.load(f)
    token = data["token"]
    prefix = data["prefix"]
activity = discord.Activity(
    name=".help", type=discord.ActivityType.watching
)  # Activity
embed_color = discord.Color(0x38C25D)

client = commands.Bot(command_prefix=commands.when_mentioned_or(prefix))
client.max_messages = 30

def check_folders():
    folders = ("cogs", "utils")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)

check_folders()

async def check_folders():
    folders = ("cogs", "utils")
    for folder in folders:
        if not os.path.exists(folder):
            print("Creating " + folder + " folder...")
            os.makedirs(folder)

async def delmsg(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        return False
    else:
        try:
            await ctx.message.delete()
            return True
        except discord.Forbidden:
            return False


@client.event
async def on_connect():
    await client.change_presence(
        activity=discord.Activity(
            name="initializing", type=discord.ActivityType.playing
        ),
        status=discord.Status.online,
    )


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=activity)
    print(f"{client.user}")
    print(f"Guild count: {len(client.guilds)}")


@client.event
async def on_message(message):
    author = message.author
    if author.bot:
        return
    await client.process_commands(message)


# Cogs
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        if file.startswith("_"):
            continue
        else:
            client.load_extension(f"cogs.{file[:-3]}")

for file in os.listdir("./utils"):
    if file.endswith(".py"):
        if file.startswith("_"):
            continue
        else:
            client.load_extension(f"utils.{file[:-3]}")

client.run(token)
