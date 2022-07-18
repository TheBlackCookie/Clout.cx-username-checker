from colorama import Fore, init
from datetime import datetime
import requests
import aiohttp
import asyncio
import json
import time
import os

with open('usernames.txt', 'r', encoding='UTF-8', errors='replace') as u:
    usernames = u.read().splitlines()
    all_usernames = len(usernames)
    if all_usernames == 0:
        print(f'No usernames found!\n Make sure to paste them into usernames.txt and save.')
        quit()\
            
async def check():
    session = requests.Session()
    for username in usernames:
        c = session.get(f'https://clout.cx/{username}', headers={'Connection': 'keep-alive', 'User-Agent': 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'}, timeout=60)
        check = c.status_code
        if check == 404:
            print(f"(UNCLAIMED -> {username}")
            with open('available.txt', "a") as x:
                x.write(f"{username}\n")
        elif check == 200:
            print(f"Username {username} is claimed.")
        else:
            print(f" [?] Unknown Error . . . - {check}")
    
    print(f"\n Done. Available Usernames are saved in available.txt!\n Press Enter to exit.\n")
    input()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(check())
