import discord , random
from discord.ext import commands
from bot_system import *
from typing import *
from stat_system import *

TOKEN: str = 'your token here'

intents = discord.Intents.default()
intents.message_content = True

prefix = bot_prefix()

game = discord.Game('TRPG BOT')
bot = commands.Bot(command_prefix = f'{prefix}', status = discord.Status.online, activity = game,intents = intents)

@bot.event
async def on_ready():
    global user_data
    user_data = load_stat()
    print('Welcome to New TRPG World')

@bot.event()
async def on_guild_join():
    global guildID
    guildID = discord.guild()


@bot.command(aliases=['주사위'])
async def roll(ctx, number:int):
    await ctx.send(f'🎲 주사위를 굴려서 {random.randint(1,int(number))}이(가) 나왔습니다. (D{number})')

@roll.error
async def roll_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('❌ 변수 오류 발생!\n변수가 너무 적거나 많거나 타입이 알맞지 않습니다.\n알맞은 타입 : int / 알맞은 개수 : 1')
    else:
        await ctx.send('😵알수 없는 오류가 발생했습니다.')

@bot.command(aliases=['가입','register'])
async def join_rpgsys(ctx):
    await ctx.send(create_data(ctx.author,ctx.author.id))

@bot.command(aliases=['stat','스탯'])
async def stat_rpgsys(ctx):
    if ctx.author.id in user_data:
        user = ctx.author.id
        embed = discord.Embed(title='나의 스탯', description=f'{ctx.author}님의 기본 스탯입니다.', color=0x00ffa5)
        embed.add_field(name='체력',value=f'{user_data[user][1]}',inline=False)
        embed.add_field(name='마나',value=f'{user_data[user][2]}',inline=False)
        embed.add_field(name='골드',value=f'{user_data[user][3]}',inline=False)
        embed.add_field(name='경험치',value=f'{user_data[user][4]}',inline=False)
        embed.add_field(name='레벨',value=f'{user_data[user][5]}',inline=False)
        embed.set_thumbnail(url=ctx.message.author.avatar)
        await ctx.send(embed=embed)
    else:
        await ctx.send('🚫사용자 데이터의 접근할수 없습니다. 가입 명령어를 이용해 RPG 시스템에 가입해주세요.')

@bot.command(aliases=['접두사','prefix'])
async def prfx(ctx):
    await ctx.send(f'현재 접두사 : {prefix}')

@bot.command(aliases=['접두사변경','changeprefix'])
async def setprefix(ctx, prefix):
    bot.command_prefix = prefix
    await ctx.send(f"Prefix changed to ``{prefix}``")

@setprefix.error
async def prfxchn_error(ctx,error):
    if isinstance(error, commands.BadArgument):
        await ctx.send('❌ 변수 오류 발생!\n변수가 너무 적거나 많거나 타입이 알맞지 않습니다.\n알맞은 타입 : char / 알맞은 개수 : 1')
    else:
        await ctx.send('😵알수 없는 오류가 발생했습니다.')

bot.run(TOKEN)