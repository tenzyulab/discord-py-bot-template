from pathlib import Path
from traceback import print_exc

from discord.ext.commands import Bot, when_mentioned_or

import const


# https://discordpy.readthedocs.io/ja/latest/intents.html
# from discord import Intents


class MyBot(Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=when_mentioned_or(const.BOT_PREFIX),
            # intents=Intents.all()
        )
        print("Launching...")

        for cog in Path("cogs/").glob("*.py"):
            try:
                self.load_extension(f"cogs.{cog.stem}")
                print(f"Loaded Extension: {cog.stem}")
            except Exception:
                print_exc()

    async def on_ready(self) -> None:
        print(f"Logged in as: {self.user}")


if __name__ == "__main__":
    bot = MyBot()
    bot.run(const.DISCORD_BOT_TOKEN)
