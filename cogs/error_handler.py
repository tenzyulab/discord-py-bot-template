from discord.ext.commands import (
    BadArgument,
    Bot,
    Cog,
    CommandError,
    CommandNotFound,
    Context,
    MissingPermissions,
)


class ErrorHandler(Cog):
    def __init__(self, bot):
        self.bot = bot

    @Cog.listener()
    async def on_command_error(self, ctx: Context, error: CommandError):
        ignore_errors = (
            BadArgument,
            CommandNotFound,
        )
        if isinstance(error, ignore_errors):
            return

        if isinstance(error, MissingPermissions):
            missing = ", ".join(error.missing_perms)
            await ctx.send(f"You don't have {missing} permission(s).")


def setup(bot: Bot):
    bot.add_cog(ErrorHandler(bot))
