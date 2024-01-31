from discord.ext import commands
import random
import discord
from cogs.YTDL.YTDLSource import YTDLSource


class MusicCog(commands.Cog, name='Music Bot'):
    def __init__(self, bot):
        self.bot=bot
        
    @commands.command(name='join', help='tells LemonGeorge to join the voice channel')
    async def join(self, ctx):
        if not ctx.message.author.voice:
            await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        else:
            channel = ctx.message.author.voice.channel
            await channel.connect()
    
    @commands.command(name='leave', help='tells LemonGeorge to leave the voice channel')
    async def leave(self, ctx):
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
        else:
            await ctx.send("LemonGeorge is not connected to a voice channel")
        
    @commands.command(name='play-song', help='tells LemonGeorge to play a song')
    async def play(self, ctx, url):
        bot=ctx.bot
        try:
            server = ctx.message.guild
            voice_channel = server.voice_client
            async with ctx.typing():
                filename, title=await YTDLSource.from_url(url, loop=bot.loop)
                voice_channel.play(discord.FFmpegPCMAudio(executable="cogs\\YTDL\\ffmpeg-6.1-full_build\\bin\\ffmpeg.exe", source=filename))
            await ctx.send("**Now playing:** {}".format(title))
        except Exception as e:
            print(f"error: {e}")
            await ctx.send("LemonGeorge is not connected to a voice channel.")
    
    @commands.command(name='pause', help='tells LemonGeorge to pause a song')
    async def pause(self,ctx):
        voice_client=ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.pause()
        else:
            await ctx.send("LemonGeorge is not playing anything at the moment.")
    
    @commands.command(name='resume', help='tells LemonGeorge to resume the song')
    async def resume(self,ctx):
        voice_client=ctx.message.guild.voice_client
        if voice_client.is_paused():
            await voice_client.resume()
        else:
            await ctx.send("LemonGeorge was nto playing anything. Use play-song command to start a song.")
    
    @commands.command(name='stop', help='tells LemonGeorge to stop the song')
    async def stop(self,ctx):
        voice_client=ctx.message.guild.voice_client
        if voice_client.is_playing():
            await voice_client.stop()
        else:
            await ctx.send("LemonGeorge is not playing anything at the moment.")

async def setup(bot):
    await bot.add_cog(MusicCog(bot))
