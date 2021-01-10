import pandas as pd
from random import choices
from urllib3.util import parse_url
from whois import whois
from whois.parser import PywhoisError

data = pd.read_csv('register.csv')
checked_domains = set()

rows = choices(data.values.tolist(), k=500)
for i, row in enumerate(rows):
    urls = row[2]
    if urls == urls:
        parsed = parse_url(urls)
        if parsed.scheme == 'https':
            try:
                w = whois(parsed.host)
            except PywhoisError as e:
                pass
            if 'registrar' not in w or not w['registrar']:
                checked_domains.add(parsed.host)
                
print()
print("List of free domains for registrarion:")    
    
for domain in checked_domains:
    print(domain)