import discord
def returnimage(message,path):
    if message == 'tinponya' or message == 'tinpo':
        file=discord.file(path+'/res/tin.mp4')
    return(file)