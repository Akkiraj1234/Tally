import os
from termcolor import colored
from datetime import datetime , timedelta
import sys
import time
import getpass
import json
import random
import re
import requests
import socket
from forex_python.converter import CurrencyRates, RatesNotAvailableError
#all the path____
containin1st_dir='C:\\Users\\Public'             #C:\\users\\Public
main_path=containin1st_dir+'\\tally'            #C:\\users\\public\\tally
company_path=main_path+'\\company_name'         #C:\\users\\public\\tally\\company_name         <--|
#*company_name*   ---> name_of_company ----> company_info ----> (info_file.json)                   | both inside tally
tally_dev_path=main_path+'\\tally_dev_info'     #C:\\users\\public\\tally\\tally_dev_info       <--|
#*tally_dev_info* ---> (status_data.json,basic_info.json),important_fille ---> (filles)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#all the function........
class validation_check:
    def validate_email(email):
        return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))
    def validate_phone_number(number):
        return bool(re.match(r'^[0-9]{10}$', number))
    def validate_fax_number(fax_number):
        return bool(re.match(r'^[0-9+\(\)\s-]+$', fax_number))
    def validate_website_name(website_name):
        return bool(re.match(r'^(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', website_name))
    def validate_contry(contry_name:str,countries:list):
        return True if contry_name.strip().lower() in countries else False
    def date_vaidation_check(date):
        try: 
            datetime.strptime(date, '%d-%m-%Y')
            return True
        except Exception : return False
    def validate_pincode_format(contry:str,pin_code:str,pin_formats:list):
        (re_for:=pin_formats[contry]) if contry.lower().strip() in pin_formats else (re_for:=None)
        if re_for is None: return False,'unvalid contry'
        else: return re.match(re_for[1],pin_code),re_for[0]
    def valid_strting_date_acoding_financial_year(financial_year: str, book_starting: str):
        financial_date = datetime.strptime(financial_year, "%d-%m-%Y")
        financial_year_end = financial_date + timedelta(days=366)
        starting_date = datetime.strptime(book_starting, '%d-%m-%Y')
        return financial_date <= starting_date <= financial_year_end
    def validate_state(contry:str,state_name:str,state_list:list):
        return True if state_name.lower().strip() in [i.lower().strip() for i in state_list[contry.lower().strip()]] else False
def number_decoding(number:str,key:str):
    k=key.split('0');k.pop(k.index(''))
    w='abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` 1234567890'
    c={w[i]:k[i]for i in range(69)}
    c2=k[69:81]
    str1=[i if not i in c2 else '53' for i in number.split('0')]
    decoded_str=''.join(next(key for key,value in c.items()if value==i) if i in c.values() else i for i in str1)
    return decoded_str
def number_coding(string:str, key:str):
    k=key.split('0');k.pop(k.index(''))
    w = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` 1234567890'
    c = {w[i]: k[i] for i in range(69)}
    c2 = k[69:81]
    encoded_str = ''.join(c[i]+'0' if i in c else i+'0' for i in string)
    str1 = ''.join(random.choice(c2)+'0' if i == '53' else i+'0' for i in encoded_str.split('0'))
    return str1
def creating_random_key():
    numb_list = [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '52', '53', '54', '55', '56', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '72', '73', '74', '75', '76', '77', '78', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    random.shuffle(numb_list)
    key=''.join(n+'0' for n in numb_list)
    return key
def info_show(info_got:json):
        os.system('cls')
        print(colored('company info'.center(80),color='yellow')+'\n'+colored('='*80,color='yellow') + colored('\ncompany name: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['company_name']), 60 - 14, colored('fincial year: ',color='yellow') + str(info_got['company_info']['fincial_year'])) +
        colored('\nCompany Email: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['comapny_E_mail']), 60 - 15, colored('Book starting from: ',color='yellow') + str(info_got['company_info']['book_starting'])) +
        colored('\nstate: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['state']), 60 - 7, colored('cureency: ',color='yellow') + str(info_got['company_info']['country'])) +
        colored('\nCountry: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['country']), 60 - 9, colored('currency sybol: ',color='yellow') + str(info_got['company_info']['curency_syboal'])) +
        colored('\nPin code: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['pin_code']), 60 - 10, colored('starting balance ',color='yellow') + str(info_got['company_info']['curency_syboal'])+info_got['company_info']['starting_bal']) +
        colored('\ntelephone: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['telephone']), 60 - 11, colored('password_T/F ',color='yellow') + str(info_got['dev_info']['password_y/n'])) +
        colored('\nMoblie numb: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['mobile_num']), 60 - 13, colored('    password: ',color='yellow') + str(info_got['company_info']['password'])) +
        colored('\ncompany mail: ',color='yellow') + str(info_got['company_info']['company_mail'])+colored('\nfax: ',color='yellow') + str(info_got['company_info']['fax']) + colored('\nwebsite: ',color='yellow') + str(info_got['company_info']['website']))
def tally_icon():
    print(colored('|==========================|      /=========\\           |==|        |==|        \\==\\        /==/','yellow'))
    print(colored('|===========|==|===========|     /==/     \\==\\          |==|        |==|         \\==\\      /==/','yellow'))
    print(colored('            |==|                /==/       \\==\\         |==|        |==|          \\==\\    /==/','yellow'))
    print(colored('            |==|               /==/         \\==\\        |==|        |==|           \\==\\  /==/','yellow'))
    print(colored('            |==|              /=================\\       |==|        |==|            \\==\\/==/','yellow'))
    print(colored('            |==|             /===================\\      |==|        |==|              |==|','yellow'))
    print(colored('            |==|            /==/               \\==\\     |==|        |==|              |==|','yellow'))
    print(colored('          ========         /==/                 \\==\\    |=======    |=======         =|==|=','yellow'))
    print(colored('                                                                    BY AKHAND RAJ','blue'))
def create_company(path_of_creation:str,list_of_compname:list,currency_symbols,countries_data:list,state_list_data:list,pin_formats_data:list):
    num=0#important variable
    while True:
        os.system('cls');(print("path didn't found please run 'setup.py' !") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_creation) else None
        print(colored("company creation".center(50,'-'),'yellow')+colored("\n(you can also type 'n' to skip)".center(50),'yellow'));print('you can also close the creation of company by typing "n"') if num>=1 else None;num+=1
        while True:#company name
            if (company_name:=input("company name : ")).lower()=='n':return True
            if company_name in list_of_compname:print('name already exists.....') 
            else:print('name selected');break
        company_mail = company_mail if (company_mail := input('Company mail address: ')) == 'n' else company_mail
        while True:#comapy E-mail.address
            if (company_e_mail:=input('Company E-mail address: '))=='n':break
            if validation_check.validate_email(company_e_mail): break
            else:print('unvalid company e mail');continue
        while True:#comapny counrty
            if (country:=input('country: ')).lower()=='n':print("important can't be skiped");continue
            if validation_check.validate_contry(country,countries_data): break
            else:print('unvalid country name or this app is not availabe in the contry ')
        while True:#company state
            if (state:=input("state : ")).lower()=='n':print('important can\' be skiped');continue
            if validation_check.validate_state(country,state,state_list_data):break
            else:print('unvalid state or maybe typo ')
        while True: #company pin code
            if (pin_code:=input("pin code : ")).lower()=='n':print('important can\' be skiped');continue
            re_for=validation_check.validate_pincode_format(country,pin_code,pin_formats_data)
            if re_for[0] :break
            else: print(f'unvalid format use this format{re_for[1]}')
        while True: #company telephone
            if (telephone:=input('telephone number : ')).lower()=='n':break
            if validation_check.validate_phone_number(telephone):break
            else:print('unvalid telephone number')
        while True: #company mobile number
            if (mobile_num:=input('mobile number: ')).lower()=='n':print('important can\' be skiped');continue
            if validation_check.validate_phone_number(mobile_num):break
            else:print('unvalid moblie number')
        while True: #company fax number
            if (fax:=input('fax number: ')).lower()=='n':break
            if validation_check.validate_fax_number(fax):break
            else:print('unvalid fax number')
        while True: #company website name
            if (website:=input('website name: ')).lower()=='n':break
            if validation_check.validate_website_name(website):break
            else:print('unvalid website name')
        print("select the currency num in given below\n"+'\n'.join('{}).            {}'.format(n,i)for n,i in enumerate(currency_symbols,start=1)))
        while True: #company currency name
            if (cureency:=input("select the currency ")).lower()=='n':print('important can\' be skiped');continue
            if cureency.isdigit() and int(cureency)<=len(currency_symbols):print('curreency = {} and sybole ={}'.format(str(list(currency_symbols.keys())[int(cureency)-1]),str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])])));break
            else:print('select number only given in the opetions! ')
        while True: #company fincial year date
            if (finacial_year:=input('financial year(format:dd-mm-yyyy): ')).lower()=='n':print('important can\' be skiped');continue
            if validation_check.date_vaidation_check(finacial_year):break
            else: print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        while True:#book starting date
            if (book_starting:=input('book starting from! :(format:dd-mm-yyyy): ')).lower()=='n':print('important can\' be skiped');continue
            if validation_check.date_vaidation_check(book_starting) and validation_check.valid_strting_date_acoding_financial_year(finacial_year,book_starting):break
            else:print("Invalid date format. Please enter the date in dd-mm-yyyy format or valid book starting date .")
        while True:#starting balanse
            if (starting_bal:=input('enter the starting balance  {}'.format(str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])])))).lower()=='n':break
            if starting_bal.isdigit():break
            else:print('please type digit')
        password_yn=input('you wanna set password in tally ? y/n').lower()
        if password_yn== 'y':
            while True:
                password=getpass.getpass(prompt="write password you wanna set ")
                password2=getpass.getpass(prompt="retype your password ")
                if password==password2:print('password matched! ');key=creating_random_key();break
                else:print('password not matched! ')
        info_dir={"company_info":{"company_name":company_name,"company_mail":company_mail,"comapny_E_mail":company_e_mail,"state":state,"country":country,"pin_code":pin_code,"telephone":telephone,"mobile_num":mobile_num,"fax":fax,"website":website,"curency":str(list(currency_symbols.keys())[int(cureency)-1]),"curency_syboal":str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])]),"fincial_year":finacial_year,"book_starting":book_starting,"starting_bal":starting_bal,"password":password if password_yn=="y" else None },"dev_info":{"password_y/n":True if password_yn=='y' else False,"key":key if password_yn=="y" else None}}
        info_show(info_dir)
        if (respones:=input('all the inforamtion are currect? y/n ').lower().strip()) == 'y': break
    os.mkdir(path_of_creation+"\\"+company_name) if not os.path.exists(path_of_creation+"\\"+company_name)else None
    os.mkdir(path_of_creation+"\\"+company_name+'\\company_info') if not os.path.exists(path_of_creation+"\\"+company_name+'\\company_info') else None
    info_dir['company_info'].update((i,number_coding(v,key))for i,v in info_dir['company_info'].items()if password_yn=='y')
    with open(path_of_creation+"\\"+company_name+'\\company_info\\info_file.json','w',encoding="utf-8")as fille:
        json.dump(info_dir,fille,ensure_ascii=True,indent=4)
def opening_company(name_of_company:str,main_path:str):
    with open(main_path+'\\'+name_of_company+'\\company_info\\info_file.json','r',encoding='utf-8') as fille:info_got=json.load(fille)
    if info_got['dev_info']['password_y/n']==True:
        for i in range(3):
            password=input("type password to opne compamy (chance-{}): ".format(str(4-i)))
            if number_decoding(info_got['company_info']['password'],(key:=info_got['dev_info']['key']))==password:
                info_got['company_info'].update((k,number_decoding(v,key)) for k,v in info_got['company_info'].items())
                break
            else:sys.exit() if i==3 else None
    else:pass
    info_show(info_got)
    nothimh=input('click anything to start code ')
def get_exchange_rate(target_currency):
    '''always use USd as base currency and retuen exchange rate'''
    try:
        exchange_rate=CurrencyRates.get_rate(target_currency,"USD",date_obj=datetime.now().day())
        return exchange_rate
    except:
        return None
def convert_amount(amount, from_currency, to_currency,exchange_rates_dict):
    if from_currency==to_currency:return amount
    return amount* exchange_rates_dict[to_currency] / exchange_rates_dict[from_currency]
def check_for_updates():
    github_raw_url='https://raw.githubusercontent.com/Akkiraj1234/update_cloud/main/update_tally.json'
    try:
        response = requests.get(github_raw_url)
    except:
        return None
    if response.status_code == 200:return json.loads(response.text)
    else:return None
def check_internet_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    try:
        sock.connect(("www.google.com", 80))
        return True
    except socket.error:
        return False
    finally:
        sock.close()
#updating info:------------------!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
tally_icon()
with open(tally_dev_path+'\\basic_info.json','r',encoding="utf-8") as file:
    data1=json.load(file);file.close
countries_data=data1['basic_info']['countries']
state_list_data=data1['basic_info']['state_list']
currency_symbols=data1['basic_info']['currency_symbols']
pin_formats_data=data1['basic_info']['pin_formats']
#updation check>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
with open(tally_dev_path+'\\status_data.json','r',encoding="utf-8") as file:
    data1=json.load(file);file.close()
print(colored('checking_for_update..',color='light_yellow'));time.sleep(1)
data2=check_for_updates()
if not data2==None:
    if not data2["version"]==data1['basic_info']['version']:
        print(colored('update found',color='yellow'))
        data1["basic_info"]['version']=data2["version"]
        update_list=data2['update_has_to_done_list']
        print(colored('we cant perform the updation rn',color='blue'))
        print(colored(data2['inisial_screen_message'],color='yellow'))
    else:pass
else:print(colored("Failed to fetch data for updation check internet conection",color='red'))
#updating_info!>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.
if datetime.now() < datetime.strptime(data1['basic_info']['money']['last_update'],'%Y-%m-%d %H:%M:%S.%f')+timedelta(days=1):pass
else:
    if check_internet_connection():
        data1['basic_info']['money']['last_update']=str(datetime.now())
        data1['basic_info']['money']['previous_M_V_detail_by_USA']=data1['basic_info']['money']['money_value_USA']
        money_value=data1['basic_info']['money']['money_value_USA']
        for key in money_value:
            exchange_rate = get_exchange_rate(key)  # Assuming base currency is USD
            if exchange_rate is not None:money_value[key] = exchange_rate
        data1['basic_info']['money']['money_value_USA']=money_value
        print(colored('updated_the_cash.','yellow'))
data1['status_info_collected']['opend']+=1
data1['status_info_collected']['last_open_time']=str(datetime.now())
with open(tally_dev_path+'\\status_data.json','w',encoding="utf-8") as file:
    data1=json.dump(data1,file);file.close()
nothing=input(colored('enter anything to continue',color='light_blue'))
# main code begin from here!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
(print("coude not find the path try running setup.py") or time.sleep(2) or sys.exit()) if not os.path.exists(company_path) else None
list_dir=os.listdir(company_path)
while True:
    os.system('cls');print('select the company'.center(50),'\n',"-"*50,'\n',colored("[1] create company".center(50),'yellow'),"\n",'-'*50)
    for n,i in enumerate(list_dir,start=2):print("[{}].......................{}".format(n,i))
    response=input("enter your responce:  ")
    #selection of computer:
    if response.isdigit():
        os.system('cls')
        if response=='1':
            print('creating a company : ')
            res=create_company(company_path,list_dir,currency_symbols,countries_data,state_list_data,pin_formats_data)
            if not res: break#while creating the company if we go back by n while inpying name we don't go directly to fot insted of home screen that's why we use it
        elif int(response)>=2 and int(response)<=len(list_dir)+1:
            name_of_company=list_dir[int(response)-2]
            opening_company(name_of_company,company_path)
            break
        else:
            print('please type within givin option')
print('============================================================\n'+
      '|                           G.O.T                          |\n'+
      '============================================================\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|=============================|                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '|                             |                            |\n'+
      '============================================================')