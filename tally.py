import os
from termcolor import colored
from datetime import datetime , timedelta
import sys
import time
import getpass
import json
import random
#all the function........
def valid_strting_date_acoding_financial_year(financial_year: str, book_starting: str):
    financial_date = datetime.strptime(financial_year, "%d-%m-%Y")
    financial_year_end = financial_date + timedelta(days=366)
    starting_date = datetime.strptime(book_starting, '%d-%m-%Y')
    return financial_date <= starting_date <= financial_year_end
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
def info_show(info_got):
        os.system('cls')
        print(colored('company info'.center(80),color='yellow')+'\n'+colored('='*80,color='yellow') + colored('\ncompany name: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['company_name']), 60 - 14, colored('fincial year: ',color='yellow') + str(info_got['company_info']['fincial_year'])) +
        colored('\nCompany Email: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['comapny_E_mail']), 60 - 15, colored('Book starting from: ',color='yellow') + str(info_got['company_info']['book_starting'])) +
        colored('\nstate: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['state']), 60 - 7, colored('cureency: ',color='yellow') + str(info_got['company_info']['country'])) +
        colored('\nCountry: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['country']), 60 - 9, colored('currency sybol: ',color='yellow') + str(info_got['company_info']['curency_syboal'])) +
        colored('\nPin code: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['pin_code']), 60 - 10, colored('starting balance ',color='yellow') + str(info_got['company_info']['curency_syboal'])+info_got['company_info']['starting_bal']) +
        colored('\ntelephone: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['telephone']), 60 - 11, colored('password_T/F ',color='yellow') + str(info_got['dev_info']['password_y/n'])) +
        colored('\nMoblie numb: ',color='yellow')+'{:<{}}{}'.format(str(info_got['company_info']['mobile_num']), 60 - 13, colored('    password: ',color='yellow') + str(info_got['company_info']['password'])) +
        colored('\ncompany mail: ',color='yellow') + str(info_got['company_info']['company_mail'])+colored('\nfax: ',color='yellow') + str(info_got['company_info']['fax']) + colored('\nwebsite: ',color='yellow') + str(info_got['company_info']['website']))
def create_company(path_of_creation:str,list_of_compname:list):
    num=0#important variable
    currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
    while True:
        os.system('cls');(print("path didn't found please run 'setup.py' !") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_creation) else None
        while True:
            print(colored("company creation".center(50,'-'),'yellow'));print('you can also close the creation of company by typing "n"') if num>=1 else None;num+=1
            company_name=input("company name : ")
            if company_name.lower()=='n':
                return True
            print('name already exists.....') if company_name in list_of_compname else print('name selected');break
        company_mail=input('company mail address : ')
        company_e_mail=input('company E-mail address : ')
        state=input("state : ")
        country=input("country : ")
        pin_code=input("pin code : ")
        telephone=input("telephone number : ")
        mobile_num=input("mobile number : ")
        fax=input("fax number : ")
        website=input("website name : ")
        print("select the currency num in given below")
        for n,i in enumerate(currency_symbols,start=1):
            print('{}).            {}'.format(n,i))
        while True:
            cureency=input("select the currency ")
            if cureency.isdigit() and int(cureency)<=len(currency_symbols):
                print('curreency = {} and sybole ={}'.format(str(list(currency_symbols.keys())[int(cureency)-1]),str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])])))
                break
            else:
                print('select number only given in the opetions! ')
        while True:
            finacial_year=input('financial year(format:dd-mm-yyyy): ')
            try:
                datetime.strptime(finacial_year, '%d-%m-%Y')
                break
            except ValueError:
                print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        while True:
            book_starting=input('book starting from! :(format:dd-mm-yyyy): ')
            try:
                datetime.strptime(book_starting, '%d-%m-%Y')
            except ValueError:
                print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
            if valid_strting_date_acoding_financial_year(finacial_year,book_starting):
                print('valid book starting date ')
                break
            else:
                print('unvalid starting date its not in finasial year')
        starting_bal=input('enter the starting balance  {}'.format(str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])])))
        password_yn=input('you wanna set password in tally ? y/n').lower()
        if password_yn== 'y':
            while True:
                password=getpass.getpass(prompt="write password you wanna set ")
                password2=getpass.getpass(prompt="retype your password ")
                if password==password2:
                    print('password matched! ')
                    key=creating_random_key()
                    break
                else:
                    print('password not matched! ')
        info_dir={"company_info":{"company_name":company_name,"company_mail":company_mail,"comapny_E_mail":company_e_mail,"state":state,"country":country,"pin_code":pin_code,"telephone":telephone,"mobile_num":mobile_num,"fax":fax,"website":website,"curency":str(list(currency_symbols.keys())[int(cureency)-1]),"curency_syboal":str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])]),"fincial_year":finacial_year,"book_starting":book_starting,"starting_bal":starting_bal,"password":password if password_yn=="y" else None },"dev_info":{"password_y/n":True if password_yn=='y' else False,"key":key if password_yn=="y" else None}}
        info_show(info_dir)
        respones=input('all the inforamtion are currect? y/n ').lower().strip()
        if respones == 'y': break
    os.mkdir(path_of_creation+"\\"+company_name) if not os.path.exists(path_of_creation+"\\"+company_name)else None
    os.mkdir(path_of_creation+'\\'+company_name+'\\company_info') if not os.path.exists(path_of_creation+'\\'+company_name+'\\company_info') else None
    info_dir['company_info'].update((i,number_coding(v,key))for i,v in info_dir['company_info'].items()if password_yn=='y')
    # (info_dir['company_info'][i]=number_coding(info_dir['company_info'][i],key) for i in info_dir['company_info'].keys()) if password_yn=='y' else None
    os.mkdir(path_of_creation+'\\'+company_name+'\\company_info') if not os.path.exists(path_of_creation+'\\'+company_name+'\\company_info') else None
    with open(path_of_creation+'\\'+company_name+'\\company_info\\info_file.json','w',encoding="utf-8")as fille:
        json.dump(info_dir,fille,ensure_ascii=True,indent=4)
def opening_company(name_of_company:str,main_path:str):
    with open(main_path+'\\'+name_of_company+'\\company_info\\info_file.json','r',encoding='utf-8') as fille:
        info_got=json.load(fille)
    if info_got['dev_info']['password_y/n']==True:
        key=info_got['dev_info']['key']
        for i in range(3):
            password=input("type password to opne compamy (chance-{}): ".format(str(4-i)))
            if number_decoding(info_got['company_info']['password'],key)==password:
                info_got['company_info'].update((k,number_decoding(v,key)) for k,v in info_got['company_info'].items())
                break
            else:
                sys.exit() if i==3 else None
    else:
        pass
    info_show(info_got)
    nothimh=input('click anything to start code ')
# main code begin from here
state_codes = {'andaman and nicobar islands': 'AN', 'andhra pradesh': 'AP', 'arunachal pradesh': 'AR', 'assam': 'AS', 'bihar': 'BR', 'chandigarh': 'CH', 'chhattisgarh': 'CT', 'dadra and nagar haveli and daman and diu': 'DN', 'delhi': 'DL', 'goa': 'GA', 'gujarat': 'GJ', 'haryana': 'HR', 'himachal pradesh': 'HP', 'jharkhand': 'JH', 'karnataka': 'KA', 'kerala': 'KL', 'ladakh': 'LA', 'lakshadweep': 'LD', 'madhya pradesh': 'MP', 'maharashtra': 'MH', 'manipur': 'MN', 'meghalaya': 'ML', 'mizoram': 'MZ', 'nagaland': 'NL', 'odisha': 'OR', 'puducherry': 'PY', 'punjab': 'PB', 'rajasthan': 'RJ', 'sikkim': 'SK', 'tamil nadu': 'TN', 'telangana': 'TG', 'tripura': 'TR', 'uttar pradesh': 'UP', 'uttarakhand': 'UT', 'west bengal': 'WB'}
currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
path_of_dir='C:\\users\\Public'
(print("coude not find the path try running setup.py") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_dir+'\\'+"tally") else None
list_dir=os.listdir(path_of_dir+'\\'+"tally")
while True:
    os.system('cls');print('select the company'.center(50),'\n',"-"*50,'\n',colored("[1] create company".center(50),'yellow'),"\n",'-'*50)
    for n,i in enumerate(list_dir,start=2):
        print("[{}].......................{}".format(n,i))
    response=input("enter your responce:  ")
    #selection of computer:
    if response.isdigit():
        os.system('cls')
        if response=='1':
            print('creating a company : ')
            res=create_company(path_of_dir+'\\'+"tally",list_dir)
            if not res: break
        elif int(response)>=2 and int(response)<=len(list_dir)+1:
            name_of_company=list_dir[int(response)-2]
            opening_company(name_of_company,path_of_dir+'\\tally')
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