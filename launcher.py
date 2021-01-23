import glob
import pathlib
from traceback import print_exc

from discord.ext import commands

import constant


class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or(constant.DISCORD_BOT_PREFIX)
        )
        print(f"Starting {constant.DISCORD_BOT_NAME}")

        for cog in pathlib.Path("cogs/").glob("*.py"):
            try:
                self.load_extension("cogs." + cog.stem)
                print(f"Loaded {cog.stem}.")
            except:
                print_exc()

    async def on_ready(self):
        user = self.user
        print("logged in as:", str(user), user.id)

    async def on_command_error(self, ctx, error):
        ignore_errors = (
            commands.CommandNotFound,
            commands.BadArgument,
            commands.CheckFailure,
        )
        if isinstance(error, ignore_errors):
            return
        await ctx.send(error)


if __name__ == "__main__":
    bot = MyBot()
    bot.run(constant.DISCORD_BOT_TOKEN)
