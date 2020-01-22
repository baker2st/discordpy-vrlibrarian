import discord
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
# 接続に必要なオブジェクトを生成
client = discord.Client()
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_voice_state_update(member, before, after):
    if member.guild.id == 615477382857621504:
        stream_channel = client.get_channel(668677645545898003)
        alert_channel = client.get_channel(668586484462387233)
        stream = discord.utils.find(VoiceState.self_stream, stream_channel)
        if stream:
            msg = f'{member.name} が {after.channel.name} でキラー配信を開始しました！'
            await alert_channel.send(msg)
client.run(token)

@bot.command()
async def Okama(ctx):
    await ctx.send('かまおかま！？')

bot.run(token)
