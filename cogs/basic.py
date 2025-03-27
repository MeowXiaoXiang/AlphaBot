import discord
from discord.ext import commands
import yt_dlp
from loguru import logger
import asyncio
from discord import app_commands

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="搜尋音樂", description="搜尋音樂並顯示結果")
    @app_commands.describe(keyword="輸入音樂關鍵字")
    async def search_music(self, interaction: discord.Interaction, keyword: str):
        await interaction.response.defer()  # 延遲回應，避免互動超時

        options = {
            "default_search": "auto",
            "extract_flat": True,
            "quiet": True,
            "no_warnings": True,
        }

        try:
            with yt_dlp.YoutubeDL(options) as ytdl:
                info = await asyncio.to_thread(ytdl.extract_info, f"ytsearch5:{keyword}", download=False)
                entries = info.get("entries", [])[:5]  # 取得前五個結果

                embed = discord.Embed(title=f"YouTube 搜尋結果：{keyword}", color=discord.Color.blue())
                for index, entry in enumerate(entries, start=1):
                    embed.add_field(
                        name=f"{index}. {entry['title']}",
                        value="",  # 不需要網址
                        inline=False,
                    )

                await interaction.followup.send(embed=embed)

        except Exception as e:
            logger.error(f"Error during search: {e}")
            await interaction.followup.send("搜尋過程中發生錯誤！", ephemeral=True)

async def setup(bot):
    await bot.add_cog(Basic(bot))