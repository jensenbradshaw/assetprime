import discord
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

tree = discord.app_commands.CommandTree(client)

@tree.command(name = "runs", description = "List the Moon Knight runs")
async def runs_command(interaction):
    await interaction.response.send_message("Moon Knight (1980)\nFist of Khonshu: Moon Knight (1985)\nMarc Spector: Moon Knight (1989)\nMoon Knight: Resurrection War (1998)\nMoon Knight: High Strangers (1999)\nMoon Knight: The Bottom (2006)\nVengeance of the Moon Knight (2009)\nMoon Knight (2011)\nMoon Knight: From the Dead (2014)\nMoon Knight: Welcome to New Egypt (2016)\nMoon Knight: Midnight Mission (2021)")

@tree.command(name = "annuals", description = "List the Moon Knight annuals")
async def runs_command(interaction):
    await interaction.response.send_message('Moon Knight Annual (2007)\nMoon Knight Annual (2019)\nMoon Knight Annual (2022)')

@tree.command(name = "limited", description = "List the Moon Knight limited series")
async def runs_command(interaction):
    await interaction.response.send_message('Moon Knight Special Edition (1983)\nShadowland: Moon Knight (2010)\nMoon Knight: Black, White & Blood (2022)')

@tree.command(name = "oneshots", description = "List the Moon Knight one shots")
async def runs_command(interaction):
    await interaction.response.send_message('Moon Knight: Divided We Fall (1992)\nMarc Spector: Moon Knight Special Edition (1992)\nMoon Knight: Silent Knight (2008)\nMoon Knight Saga (2009)\nDevil\'s Reign: Moon Knight (2022)')

@tree.command(name = "teamups", description = "List the Moon Knight team ups")
async def runs_command(interaction):
    await interaction.response.send_message('Ms. Marvel & Moon Knight (2022)')

@client.event
async def on_ready():
    await tree.sync()
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('ap!help'):
        await message.channel.send('Commands:\n  ap!runs\n  ap!annuals\n  ap!limited\n  ap!oneshots\n  ap!teamups')

    elif message.content.startswith('ap!runs'):
        await message.channel.send('Moon Knight (1980)\nFist of Khonshu: Moon Knight (1985)\nMarc Spector: Moon Knight (1989)\nMoon Knight: Resurrection War (1998)\nMoon Knight: High Strangers (1999)\nMoon Knight: The Bottom (2006)\nVengeance of the Moon Knight (2009)\nMoon Knight (2011)\nMoon Knight: From the Dead (2014)\nMoon Knight: Welcome to New Egypt (2016)\nMoon Knight: Midnight Mission (2021)')

    elif message.content.startswith('ap!annuals'):
        await message.channel.send('Moon Knight Annual (2007)\nMoon Knight Annual (2019)\nMoon Knight Annual (2022)')

    elif message.content.startswith('ap!limited'):
        await message.channel.send('Moon Knight Special Edition (1983)\nShadowland: Moon Knight (2010)\nMoon Knight: Black, White & Blood (2022)')

    elif message.content.startswith('ap!oneshots'):
        await message.channel.send('Moon Knight: Divided We Fall (1992)\nMarc Spector: Moon Knight Special Edition (1992)\nMoon Knight: Silent Knight (2008)\nMoon Knight Saga (2009)\nDevil\'s Reign: Moon Knight (2022)')

    elif message.content.startswith('ap!teamups'):
        await message.channel.send('Ms. Marvel & Moon Knight (2022)')

client.run(os.getenv('TOKEN'))