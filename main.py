import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for file in ctx.message.attachments:
            file_name = file.filename
            file_url = file.url
            await file.save(f'{file_name}')
            await ctx.send(f'File disimpan atas nama {file_name}')
            hasil = get_class('keras_model.h5', 'labels.txt', file_name)

            if hasil[0] ==  '90s\n' and hasil[1] >= 0.6:
                await ctx.send('Ini Adalah Foto Perkotaan Pada Periode di Bawah Tahun 2000')
                await ctx.send('Info lainnya..')
            elif hasil[0] == 'Modern\n' and hasil[1] >= 0.6:
                await ctx.send('Ini Adalah Foto Perkotaan pada Periode Masa Kini')
                await ctx.send('Info lainnya..')
            else:
                await ctx.send('Gambar Tidak Valid!')

    else:
        await ctx.send('Anda Tidak Mengirim File Apapun !!')


bot.run("MTEzNDEwNTc2MDYwMzg0MDU5NQ.Gtr1IA.Xrh1H0yAtjtsIdxiMDAP1OmJKlN_6-K3_b6WqQ")