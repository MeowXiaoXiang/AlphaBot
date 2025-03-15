import discord
from discord.ext import commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="測試指令", description="測試指令")
    async def test_command(self, interaction: discord.Interaction):
        await interaction.response.send_message("測試指令")

async def setup(bot):
    await bot.add_cog(Basic(bot))
