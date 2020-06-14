import discord

client = discord.Client()

# for general troubleshooting
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return

    if message.author.top_role.permissions.administrator or "FANTASY ADMIN" in str(message.author.roles).upper():
        # selected over looping through names attribute of the list of roles for speed
