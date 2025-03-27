import discord
from module import ViewPart
# from module.custom import ViewPart 如果不做__init__的話
class MusicGUI(ViewPart):
        
    @discord.ui.button(label="⏮",style=discord.ButtonStyle.grey, custom_id="previous_button",row=0)
    async def previous(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass
    
    @discord.ui.button(label="▶", style=discord.ButtonStyle.blurple, custom_id="play_pause_button", row=0)
    async def play_pause(self, interaction: discord.Interaction, button: discord.ui.Button):
    # 切換按鈕的標籤
        button.label = "⏸" if button.label == "▶" else "▶"
        # 更新視圖
        await interaction.response.edit_message(view=self)
    
    @discord.ui.button(label="⏭",style=discord.ButtonStyle.grey, custom_id="next_button",row=0)
    async def next(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass
    
    @discord.ui.button(label="⏹",style=discord.ButtonStyle.green, custom_id="stop_button",row=0)
    async def stop(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass
    
    @discord.ui.button(label="🔁",style=discord.ButtonStyle.green, custom_id="repeat_button",row=0)
    async def repeat(self,interaction:discord.Interaction,button:discord.ui.Button):
        pass
    
class GuildSettingGUI(ViewPart):
    pass
    