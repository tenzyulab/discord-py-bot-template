from pathlib import Path
from traceback import print_exc

from discord.ext.commands import (
    BadArgument,
    Bot,
    CheckFailure,
    CommandNotFound,
    when_mentioned_or,
)

import const


class MyBot(Bot):
    def __init__(self):
        super().__init__(command_prefix=when_mentioned_or(const.BOT_PREFIX))
        print(f"Starting {const.BOT_NAME}")

        for cog in Path("cogs/").glob("*.py"):
            try:
                self.load_extension("cogs." + cog.stem)
                print(f"Loaded Extension: {cog.stem}.py")
            except Exception:
                print_exc()

    async def on_ready(self):
        print("logged in as:", self.user.name, self.user.id, "\n")

    async def on_command_error(self, ctx, error):
        ignore_errors = (
            BadArgument,
            CheckFailure,
            CommandNotFound,
        )
        if isinstance(error, ignore_errors):
            return
        await ctx.send(error)


if __name__ == "__main__":
    bot = MyBot()
    bot.run(const.DISCORD_BOT_TOKEN)
