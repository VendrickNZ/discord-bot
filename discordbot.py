import discord
import random
from discord.ext import commands
from discord.utils import get

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)
disc_client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_member_join(ctx):
    role = discord.utils.get(ctx.guild.roles, name = "new monkeys")
    await ctx.add_roles(role)

@client.event
async def on_member_remove(member):
    print("{} has left the server".format(member))

@client.command()
async def ping(ctx):
    await ctx.send("Pong! {}ms".format(round(client.latency * 1000)))

@client.command()
async def test(ctx, arg):
    await ctx.send(arg)

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
                "It is decidedly so.",
                "Without a doubt.",
                "Yes - definitely.",
                "You may rely on it.",
                "As I see it, yes.",
                "Most likely.",
                "Outlook good.",
                "Yes.",
                "Signs point to yes.",
                "Reply hazy, try again.",
                "Ask again later.",
                "Better not tell you now.",
                "Cannot predict now.",
                "Concentrate and ask again.",
                "Don't count on it.",
                "My reply is no.",
                "My sources say no.",
                "Outlook not so good.",
                "Very doubtful."]
    await ctx.send("Question: {}\nAnswer: {}".format(question, random.choice(responses)))

@client.command()
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount)


@client.event
async def on_message(message):
    if message.content.startswith('.greet'):
        channel = message.channel
        await channel.send('Say hello!')

        def check(m):
            return m.content == 'hello' and m.channel == channel

        msg = await client.wait_for('message', check=check)
        await channel.send('Hello {.author}!'.format(msg))






client.run('Nzc0NDc4OTU5NTQ2ODU5NTYx.X6YXvQ.nYkEFty_F5rKCOKftzT4tQAL7CY')