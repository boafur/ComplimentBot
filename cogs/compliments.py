import random
import discord
from discord.ext import commands

compliments = [
    "Your ability to recall random factoids at just the right time is impressive.",
    "You're a great listener.",
    "How is it that you always look great, even in sweatpants?",
    "Everything would be better if more people were like you!",
    "I bet you sweat glitter.",
    "You were cool way before hipsters were cool.",
    "That color is perfect on you.",
    "Hanging out with you is always a blast.",
    "You always know -- and say -- exactly what I need to hear when I need to hear it.",
    "You help me feel more joy in life.",
    "You may dance like no one's watching, but everyone's watching because you're an amazing dancer!",
    "Being around you makes everything better!",
    'When you say, "I meant to do that," I totally believe you.',
    "When you're not afraid to be yourself is when you're most incredible.",
    "Colors seem brighter when you're around.",
    "You're more fun than a ball pit filled with candy. (And seriously, what could be more fun than that?)",
    "That thing you don't like about yourself is what makes you so interesting.",
    "You're wonderful.",
    "You have cute elbows. For reals!",
    "Jokes are funnier when you tell them.",
    "You're better than a triple-scoop ice cream cone. With sprinkles.",
    "When I'm down you always say something encouraging to help me feel better.",
    "You are really kind to people around you.",
    "You're one of a kind!",
    "You help me be the best version of myself.",
    "If you were a box of crayons, you'd be the giant name-brand one with the built-in sharpener.",
    "You should be thanked more often. So thank you!!",
    "Our community is better because you're in it.",
    "Someone is getting through something hard right now because you've got their back. ",
    "You have the best ideas.",
    "You always find something special in the most ordinary things.",
    "Everyone gets knocked down sometimes, but you always get back up and keep going.",
    "You're a candle in the darkness.",
    "You're a great example to others.",
    "Being around you is like being on a happy little vacation.",
    "You always know just what to say.",
    "You're always learning new things and trying to better yourself, which is awesome.",
    "If someone based an Internet meme on you, it would have impeccable grammar.",
    "You could survive a Zombie apocalypse.",
    "You're more fun than bubble wrap.",
    "When you make a mistake, you try to fix it.",
    "Who raised you? They deserve a medal for a job well done.",
    "You're great at figuring stuff out.",
    "Your voice is magnificent.",
    "The people you love are lucky to have you in their lives.",
    "You're like a breath of fresh air.",
    "You make my insides jump around in the best way.",
    "You're so thoughtful.",
    "Your creative potential seems limitless.",
    "Your name suits you to a T.",
    "Your quirks are so you -- and I love that.",
    "When you say you will do something, I trust you.",
    "Somehow you make time stop and fly at the same time.",
    "When you make up your mind about something, nothing stands in your way.",
    "You seem to really know who you are.",
    "Any team would be lucky to have you on it.",
    'In high school I bet you were voted "most likely to keep being awesome."',
    "I bet you do the crossword puzzle in ink.",
    "Babies and small animals probably love you.",
    "If you were a scented candle they'd call it Perfectly Imperfect (and it would smell like summer).",
    "There's ordinary, and then there's you.",
    "You're someone's reason to smile.",
    "You're even better than a unicorn, because you're real.",
    "How do you keep being so funny and making everyone laugh?",
    "You have a good head on your shoulders.",
    "Has anyone ever told you that you have great posture?",
    "The way you treasure your loved ones is incredible.",
    "You're really something special.",
    "Thank you for being you.",
]

async def delmsg(ctx):
    if isinstance(ctx.channel, discord.DMChannel):
        return False
    else:
        try:
            await ctx.message.delete()
            return True
        except discord.Forbidden:
            return False

class Compliments(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(description="Send a random compliment")
    async def compliment(self, ctx, user: discord.Member = None):
        await ctx.trigger_typing()
        author = ctx.author
        choice = random.choice(compliments)
        msg = await ctx.send(f"{choice}")
        if user is None:
            a = ctx.author
        else:
            a = user
        await msg.edit(content=f"{a.mention}, {choice}")


def setup(bot):
    bot.add_cog(Compliments(bot))
