import discord
class ViewPart(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)  # 預設不超時