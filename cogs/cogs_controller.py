from discord.ext.commands import Bot, Cog, Context, command


class CogsController(Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot: Bot):
        self.bot = bot

    async def cog_check(self, ctx: Context):
        if await ctx.bot.is_owner(ctx.author):
            return True
        await ctx.reply("You cannot run this command.")
        return False

    @command(name="load")
    async def load_cog(self, ctx: Context, cog: str):
        self.bot.load_extension(f"cogs.{cog}")
        await ctx.reply(f"Loaded Extension: {cog}")

    @command(name="unload")
    async def unload_cog(self, ctx: Context, cog: str):
        self.bot.unload_extension(f"cogs.{cog}")
        await ctx.reply(f"Unloaded Extension: {cog}")

    @command(name="reload")
    async def reload_cog(self, ctx: Context, cog: str):
        self.bot.reload_extension(f"cogs.{cog}")
        await ctx.reply(f"Reloaded Extension: {cog}")


def setup(bot: Bot):
    bot.add_cog(CogsController(bot))
