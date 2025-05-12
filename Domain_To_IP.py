#Code Make By: Ariyan Rabbi(Dʌʀĸ-Nɘt)
#Don't Copy My Code

import os
import socket
import time
from colorama import Fore, Style, init
import pyfiglet

init(autoreset=True)
os.system("clear")
ascii_banner = pyfiglet.figlet_format("Domain \n To IP", font="slant")
print(Fore.RED + ascii_banner)
print(Fore.YELLOW + " " * 5 + "⏰ Domain to IP Resolver\n")

info = f"""{Fore.CYAN}
╭───────────────────────────────────────────────╮
│ 💻 Coded By : {Fore.GREEN}Ariyan Rabbi                    │
│ 😎 Username : {Fore.GREEN}DARK-NET-403                    │
│ 🧠 Role     : {Fore.GREEN}Python Dev | CyberSec Enthusiast│
│ ⚙️  Tools    : {Fore.GREEN}IP Resolver v2.0                │
╰───────────────────────────────────────────────╯
{Style.RESET_ALL}
"""
print(info)

def get_ip_from_website(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"{Fore.GREEN}✅ IP Address of {domain} is: {Fore.YELLOW}{ip}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}")

if __name__ == "__main__":
    print(f"{Fore.MAGENTA}┌─🌐 Enter domain (e.g., google.com)")
    domain = input(f"{Fore.MAGENTA}└──╼ {Fore.WHITE}")
    
    if "http://" in domain or "https://" in domain:
        print(f"{Fore.RED}⚠️ Please enter domain without 'http://' or 'https://'. Try again!")
    else:
        print(f"{Fore.BLUE}\n⏳ Resolving IP for {domain}...\n")
        time.sleep(1)
        get_ip_from_website(domain)
