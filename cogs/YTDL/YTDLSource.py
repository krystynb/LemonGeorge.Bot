import os
import discord
from discord.ext import tasks, commands
from dotenv import load_dotenv
import yt_dlp as youtube_dl
import asyncio
import requests
from bs4 import BeautifulSoup

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificates': True,
    'ignoreerrors': True,
    'logtostderr': True,
    'quiet': True,
    'no_warnings': True,
    'default_search': True,
    'source_address': os.getenv('IPv4'),
    'outtmpl': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'webm_files', '%(title)s.%(ext)s')
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer): 
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""

    @classmethod   
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        try:
            r=requests.get(url)
            soup=BeautifulSoup(r.text, 'html.parser')
            title=soup.find('title').text.strip()
            
            
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
            if 'entries' in data:
            # Take the first item from the playlist
                data = data['entries'][0]
            filename = data['title'] if stream else ytdl.prepare_filename(data)
            return filename, title
        
        
        
        except youtube_dl.utils.ExtractorError as e:
            print(f"Error extracting info: {e}")
            return "default_filename.mp3", "Unknown Title"
