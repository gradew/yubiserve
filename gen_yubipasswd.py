#!/usr/bin/env python

import re, sys, os

try:
    import MySQLdb
except ImportError:
    pass
try:
    import sqlite
except ImportError:
    pass
try:
    import psycopg2
except ImportError:
    pass

def parseConfigFile():  # Originally I wrote this function to parse PHP configuration files!
    config = open(os.path.dirname(os.path.realpath(__file__)) + '/yubiserve.cfg', 'r').read().splitlines()
    keys = {}
    for line in config:
        match = re.search('(.*?)=(.*);', line)
        try: # Check if it's a string or a number
            if ((match.group(2).strip()[0] != '"') and (match.group(2).strip()[0] != '\'')):
                keys[match.group(1).strip()] = int(match.group(2).strip())
            else:
                keys[match.group(1).strip()] = match.group(2).strip('"\' ')
        except:
            pass
    return keys

config = parseConfigFile()

if config['yubiDB'] == 'sqlite':
    con = sqlite.connect(os.path.dirname(os.path.realpath(__file__)) + '/yubikeys.sqlite')
elif config['yubiDB'] == 'mysql':
    con = MySQLdb.connect(host=config['yubiMySQLHost'], user=config['yubiMySQLUser'], passwd=config['yubiMySQLPass'], db=config['yubiMySQLName'])
elif config['yubiDB'] == 'postgres':
    host=config['yubiPGHost']
    db=config['yubiPGName']
    user=config['yubiPGUser']
    passwd=config['yubiPGPass']
    con = psycopg2.connect("host='%s' dbname='%s' user='%s' password='%s'" % (host, db, user, passwd))

cur = con.cursor()

cur.execute("select nickname, publicname from yubikeys where active='1';")
rows = cur.fetchall()

for row in rows:
	yNick = row[0]
	yPublicID = row[1]
	print("%s:%s" % (yNick, yPublicID))
