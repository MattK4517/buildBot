## Discord Bot testing
# bot.py
#ID 740331291869970452
import discord
import pandas as pd
print(discord.__version__)  # check to make sure at least once you're on the right version!

token = open("token.txt", "r").read()  # I've opted to just save my token to a text file. 

client = discord.Client()  # starts the discord client.


def Build(god, role):
    build_file = 'Smite Builds.xlsx'
    role = role.lower()
    if role in ["solo"]:
        build = pd.read_excel(build_file, index_col=0, sheet_name=0)
    elif role in ["jungle","jg"]:
        build = pd.read_excel(build_file, index_col=0, sheet_name=1)
    elif role in ["mid"]:
        build = pd.read_excel(build_file, index_col=0, sheet_name=2)
    elif role in ["sup", "supp", "support"]:
        build = pd.read_excel(build_file, index_col=0, sheet_name=3)
    elif role in ["adc"]:
        build = pd.read_excel(build_file, index_col=0, sheet_name=4)
        
    finalbuild = ""
    size = build.shape
    y=0
    n=0
    x = build.iterrows()
    godSelect = next(x) 
    while n < size[0] and godSelect[0][:] != god:
        godSelect = next(x)
        n+=1
    while godSelect[0][:].lower() == god.lower() and y < 13:
        if y < 1:
            finalbuild = finalbuild + "**Start:** "+(godSelect[1][y]) +" | "
        elif y == 1:
            finalbuild = finalbuild +"\n**Typical Build:** "
        elif y > 1 and y < 9:
            finalbuild = finalbuild + (godSelect[1][y]) +" | "
        elif y == 9:
            finalbuild = finalbuild[:-3]+"**Situtional Items:** " + godSelect[1][y] + "\n**Relics:** "
        elif y == 10:
            finalbuild = finalbuild + godSelect[1][y] + " |\n**Situtional Relics:** "
        elif y > 10:
            finalbuild = finalbuild + godSelect[1][y] + " | "
        y += 1
    return finalbuild
    
@client.event  # event decorator/wrapper. More on decorators here: https://pythonprogramming.net/decorators-intermediate-python-tutorial/
async def on_ready():  # method expected by client. This runs once when connected
    print(f'We have logged in as {client.user}')  # notification of login.

@client.event
async def on_message(message):  # event that happens per any message.

    # each message has a bunch of attributes. Here are a few.
    # check out more by print(dir(message)) for example.
    print(f"{message.channel}: {message.author}: {message.author.name}: {message.content}")

    if "!logout" in message.content.lower():
        await client.close()
    if "!build" in message.content.lower():
        m = message.content.split(" ")
        god = m[1]
        role = m[2]
        print(god)
        print(role)
        print(m)
        
        await message.channel.send(Build(god, role))

client.run(token)
