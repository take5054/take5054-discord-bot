import discord,random,antigravity,os,re,time,asyncio
import phasmo,genshinday,valorantAA
from discord import app_commands,ui
from discord.ext import tasks,commands
from discord.channel import VoiceChannel
from datetime import datetime,date
from yt_dlp import YoutubeDL

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
slash = app_commands.CommandTree(client)
f = open('token.txt','r')
TOKEN = f.read()
f.close
f = open('channel_ID.txt', 'r')
CHANNEL_ID = f.read()
f.close
ver = '0.8.0α'
voiceChannel: VoiceChannel
vol = 1
path = os.path.dirname(__file__)

@client.event
async def on_ready():
    print(ver)
    await client.change_presence(activity=discord.Game(name='/help', type=1))
    await slash.sync()
    loop.start()

@slash.command(name='help',description='ヘルプ')
async def help(ctx):
    embed = discord.Embed(title='**Help**',color=0xeee657)
    embed.add_field(name='開発元',value='discord:たけ#0808')
    embed.add_field(name='',value='Twitter:https://twitter.com/take5054',inline=False)
    embed.add_field(name='コマンド一覧',value='',inline=False)
    for command in slash.walk_commands():
        embed.add_field(name='/'+command.name,value='',inline=False)
    await ctx.response.send_message(embed=embed)

@slash.command(name='ph',description='Phasmophobia証拠別判定方法 ナイトメア以上  書式：/ph 証拠1証拠2')
async def phasmo_command(ctx,text:str):
    embed = discord.Embed(title='Phasmophobia',color=0xeee657)
    embed.add_field(name='判別方法', value=phasmo.phasmo(text,path))
    await ctx.response.send_message(embed=embed)

@slash.command(name='genshin',description='今日の天賦素材、武器突破素材')
async def genshin(ctx):
    today = date.today()
    embedVar = discord.Embed(title='今日の天賦素材 武器突破素材',color=0xeee657)
    embedVar.add_field(name='天賦',value='')
    j=-1
    for i in range(4):
        embedVar.add_field(name=genshinday.genshin_tenpu(i,path,today),value=genshinday.genshin_tenpu(j,path,today),inline=False)
        j-=1
    embedVar.add_field(name='武器突破素材', value='',inline=False)
    j=-1
    for i in range(4):
        embedVar.add_field(name=genshinday.genshin_buki(i,path,today),value='',inline=False)
        embedVar.add_field(name='☆5',value=genshinday.genshin_buki(j,path,today),inline=False)
        j-=1
        embedVar.add_field(name='☆4',value=genshinday.genshin_buki(j,path,today),inline=False)
        j-=1
    await ctx.response.send_message(embed=embedVar)

@slash.command(name='aa',description='VALORANTチャット用のアスキーアートを出力します 数字ショートカット：1.GG 2.GGWP 3.MIC MUTED 4.NICE 5.NT 6.GGEZ 7.OPPAI 8...~12まで')
async def aa(ctx,text:str):
    temp = valorantAA.aa(text,path)
    await ctx.response.send_message(temp)

@slash.command(name='vol',description='再生される音楽の音量を調節します  書式：/vol 設定したい音量 or now')
async def volume(ctx,text:str):
    global vol
    if 'now' in text:
        await ctx.response.send_message(f'now volume = {vol}')
    else:
        temp = int(re.sub(r'\D','',text))
        if temp <= 100:
            vol = temp
            await ctx.response.send_message(f'successfully volume = {vol}')
        else:
            await ctx.response.send_message('100以下の数値を入力')

@slash.command(name='play',description='youtubeを再生します。書式：/play URL')
async def play(ctx,url:str):
    global vol
    global voiceChannel
    if os.path.isfile('./test.mp3'):
        os.remove('./test.mp3')
    await ctx.response.send_message(f'now volume = {vol}')
    ydl_opts = {'outtmpl': 'test.mp3','format': 'bestaudio'}    # DL条件
    # 動画のURLを指定
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download(url)
    if not ctx.guild.voice_client:
        voiceChannel = await VoiceChannel.connect(ctx.user.voice.channel)
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source='./test.mp3'), volume=vol/100)
    ctx.guild.voice_client.play(source)

@slash.command(name='dc', description='botをVCから退出させる')
async def dc(ctx):
    await ctx.guild.voice_client.disconnect()

@client.event
async def on_message(message):
    global vol
    global voiceChannel
    if message.author.bot:
        return
    if message.content == 'ver':
        await message.channel.send(ver)
    else:
        return

@tasks.loop(seconds=60)
async def loop():
    # 現在の時刻
    now = datetime.now().strftime('%H:%M')
    channel = client.get_channel(CHANNEL_ID)
    '''if now == '03:30':
        await channel.send('334の時間だよ！ https://time.is/ja/')
    if now == '00:00':
        await channel.send('日付が変わったよ！')'''
    if now == '01:00':
        await channel.send('ログインボーナスが更新されたよ！\nhttps://webstatic-sea.mihoyo.com/ys/event/signin-sea/index.html?act_id=e202102251931481&lang=ja-jp')
    if now == '05:00':
        today = date.today()
        embedVar = discord.Embed(title='今日の天賦素材 武器突破素材',color=0xeee657)
        embedVar.add_field(name='天賦',value='')
        j=-1
        for i in range(4):
            embedVar.add_field(name=genshinday.genshin_tenpu(i,path,today),value=genshinday.genshin_tenpu(j,path,today),inline=False)
            j-=1
        embedVar.add_field(name='武器突破素材', value='',inline=False)
        j=-1
        for i in range(4):
            embedVar.add_field(name=genshinday.genshin_buki(i,path,today),value='',inline=False)
            embedVar.add_field(name='☆5',value=genshinday.genshin_buki(j,path,today),inline=False)
            j-=1
            embedVar.add_field(name='☆4',value=genshinday.genshin_buki(j,path,today),inline=False)
            j-=1
        await channel.send(embed=embedVar)

client.run(TOKEN)