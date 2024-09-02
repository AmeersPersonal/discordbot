import discord
import asyncio
from discord.ext import commands

import time
import random



intents = discord.Intents.default()
intents.message_content = True
token = '' 


MY_GUILD = discord.Object(id='')
GUILD2 = discord.Object(id= '')


bot = commands.Bot(command_prefix="$", help_command= None, intents=intents )


@bot.event
async def start_up():
    print(f" bot {bot.owner_id} user {bot.shard_id}")

@bot.command()
async def ping(ctx):
    await ctx.send("hi")

@bot.command()
async def mes(ctx, guild_id, channel_id, *message):
    message = ' '.join(message)


    try:

        for guilds in bot.guilds:
            if guilds == bot.get_guild(int(guild_id)):
                channel = bot.get_channel(int(channel_id))
                await channel.send(message)
        

    except ValueError:
        await ctx.send("guild_id or channel_id is not int")




@bot.command()
async def grab_ip(ctx, user:str):
    await ctx.send("hacking into main frame")
    time.sleep(10)
    ip_address = ".".join(str(random.randint(0, 255)) for _ in range(4))
    await ctx.send(f"IP Address: {ip_address} for <@{user}>")




bot.run(token=token )

