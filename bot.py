import config
import discord
from discord import app_commands
import random
import datetime
#test
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

def run():
    @tree.command(name = "hello", description = "Hey!", guild=discord.Object(id=config.guild_id))
    async def hello(interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.name}!")

    @tree.command(name = "joined_at", description = "Date someone joined in ISO format and UTC time", guild=discord.Object(id=config.guild_id))
    async def joined(interaction: discord.Interaction, member: discord.Member):
        date = member.joined_at
        date = datetime.datetime.strftime(date,"%Y-%m-%d %H:%M:%S")
        msg = f"{member.name} joined at {date} UTC"
        await interaction.response.send_message(msg)

    @tree.command(name = "dice", description = "Rolls a dice", guild=discord.Object(id=config.guild_id)) 
    async def dice(interaction: discord.Interaction):
        results = random.randint(1,6)
        await interaction.response.send_message(results)

    @tree.command(name = "coin", description = "Flips a coin", guild=discord.Object(id=config.guild_id))
    async def coin(interaction: discord.Interaction):
        results = "Heads" if random.randint(1,2) == 1 else "Tails"
        await interaction.response.send_message(results)

    @client.event
    async def on_ready():
        await tree.sync(guild=discord.Object(id=config.guild_id))
        print("Ready!")

    client.run(config.token)

run()