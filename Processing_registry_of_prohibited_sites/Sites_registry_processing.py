from urllib3.util import parse_url
import codecs
import socket
import sys

    
def parse(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
        
    banned_urls = set()
    banned_domains = set()
    banned_ips = set()
    
    for text in text.splitlines():
        _, *urls, domains, ips = text.split(';')
        urls = ";".join(urls)
        banned_urls.update(urls.split(','))
        banned_domains.update(domains.split(','))
        banned_ips.update(ips.split(','))
        if 'ya.ru' in domains.split(','):
            print(domains)
    return banned_domains, banned_urls, banned_ips

rkn = 0
url = input("Please enter site details (URL or domain or IP) : ")
domain = parse_url(url).netloc
ip = None
print()

try:
    ip = socket.gethostbyname(domain)
except socket.gaierror:
    print("Error! Data is incorrectly entered ")

domains, urls, ips = parse('register.txt')

if url in urls:
    print("1. URL is banned!", end="")
    print()
    rkn+= 1
else:
    print("1. URL is not banned", end="")
    print()
    
if domain in domains:
    print("2. Domain is banned!", end="")
    print()
    rkn+= 1
else:
    print("2. Domain is not banned", end="")
    print()
    
if ip in ips:
    print("3. IP is banned!")
    print()
    rkn+= 1
    
else:
    print("3. IP is not banned")
    print()
    
if rkn > 0:
    print("Site is prohibited by Roskomnadzor", end="")
    print()