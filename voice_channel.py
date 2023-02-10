import discord

# Set your Discord account credentials
TOKEN = "your-token"

# Connect to Discord
client = discord.Client()

# Set the voice command to listen for
command = "join voice"

@client.event
async def on_ready():
    print("Logged in as")
    print(client.user.name)
    print(client.user.id)
    print("------")

@client.event
async def on_message(message):
    # Wait for a voice command
    if message.content == command:
        # Join the voice channel
        channel = message.author.voice.channel
        await channel.connect()

client.run(TOKEN)

