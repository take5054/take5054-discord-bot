import discord
from discord import ui

class MHWModal(ui.Modal, title='MHW:I Monster Info'):
    name = ui.TextInput(label='Name')

    async def on_submit(self, interaction: discord.Interaction):
        if 'イヴェルカーナ' in self.name:
          await interaction.response.send_message('!?')

        #await interaction.response.send_message(f'Thanks for your response, {self.name}!')