import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='ricky', help='Responds with a random quote from Ricky')
async def ricky(ctx):
    ricky_quotes = [
        "Save me some of those sweet empowered chicken things.",
        "Don't judge a cover of a book by its look.",
        "A link is only as long as your longest strong chain.",
        "It's all water under the fridge.",
        "One man's garbage is another man person's good un-garbage.",
        "Survival of the fitness, boys.",
        "I feel like my brain is short circulating.",
        "The thing is, in order to stop breakin' the law is we gotta break the law just for a couple of minutes, and then we're gonna be done, retired.",
        "I'd like to make a request under the People's Freedom of Choices and Voices Act to be able to smoke an' swear in your courtroom.",
        "What are you doin' using your big school words; just use normal people words and I'll understand what you're talkin' about.",
        "A lot of people might say I'm stupid; I don't know; I don't think I am. I'm probably smarter than that, I mean. This thing here's smarter than me, I guess, but it has a battery.",
        "When you're growing up, you gotta do illegal things once in a while, have a bit of fun and maturinate into a better person.",
        "I mean how many fathers can give a nine-year-old daughter a car? I'm just happy I'm in a position where I can do something like that.",
        "It's gonna happen anyway whether you are or you're not."
    ]

    response = random.choice(ricky_quotes)
    await ctx.send(response)

bot.run(TOKEN)
