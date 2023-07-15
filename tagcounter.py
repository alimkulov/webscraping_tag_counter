import sys
import requests
from bs4 import BeautifulSoup
import sqlite3
import tldextract
import yaml


def addr_type(addr):
    res='none'
    if addr.isalpha():
        res='synonym'
    else:
        if re.match(r'\w+\.\w+', addr):
            res='url'
        else: res='unknown'
    return res

def get_url_by_synonym(key):
    dict_synonym = yaml.load(open("synonym.yaml"), Loader=yaml.Loader)
    value=dict_synonym.keys(key)
    return  value


def get_db_url_details(domain):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS url_details
                 (domen text, url text,check_date date, tags text)''')

    sql = "SELECT * FROM url_details WHERE domen=?"
    c.execute(sql, (domain,))
    rows=c.fetchall()
    #conn.commit()
    conn.close()
    return rows

def set_db_url_details(domain, url, tags):
    conn = sqlite3.connect('mydb.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS url_details
                 (domen text, url text,check_date date, tags text)''')
    #check_date=datetime.now()
    c.execute("INSERT INTO url_details VALUES (?,?, dateTIME('now') ,?)", (domain, url, tags))
    conn.commit()
    sql = "SELECT * FROM url_details WHERE domen=?"
    c.execute(sql, (domen,))
    rows=c.fetchall()
    conn.close()
    return rows




arg= sys.argv

if len(arg)>1:
    #CLI
    if len(arg)!=3:
        print('Error in command line parameters')
    else:
        if arg[1]=='--get':
        elif arg[1]=='--view':
        else: print('Error Unknown command option')

else:#GUI



url='https://python-scripts.com' #  'http://forums.news.cnn.com/'

ext = tldextract.extract(url)



r = requests.get(url)
r.status_code
r.text
n=0
soup = BeautifulSoup(r.text, 'html.parser')
for child in soup.recursiveChildGenerator():
    if child.name:
        n += 1
        print(child.name,n)


print(str(n))