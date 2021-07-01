from discord.ext.commands import Bot, CheckFailure, Cog, CommandError, CommandNotFound, Context


class CommandErrorHandler(Cog):
    __slots__ = "bot"

    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError) -> None:
        ignore_errors = (CheckFailure, CommandNotFound)
        if isinstance(error, ignore_errors):
            return
        await ctx.reply(error)


def setup(bot: Bot) -> None:
    bot.add_cog(CommandErrorHandler(bot))
