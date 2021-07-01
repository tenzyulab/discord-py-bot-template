from time import monotonic

from discord import Message
from discord.ext.commands import Bot, Cog, Context, command


class Ping(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    async def ping(self, ctx: Context) -> None:
        """check the connection and response time"""
        tmp = monotonic()
        message: Message = await ctx.reply("Calculating...")
        latency = (monotonic() - tmp) * 1000
        await message.edit(content=f"Pong! Response time is **{int(latency)}** ms.")


def setup(bot: Bot) -> None:
    bot.add_cog(Ping(bot))
