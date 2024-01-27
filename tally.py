import os
from termcolor import colored
from datetime import datetime , timedelta
import sys
import time
import getpass
#all the function........
def valid_strting_date_acoding_financial_year(financial_year:str,book_starting:str):
    day,month,year=datetime.strptime(financial_year,"%d-%m-%Y").day,datetime.strptime(financial_year,"%d-%m-%Y").month,datetime.strptime(financial_year,"%d-%m-%Y").year
    financial_year_end=datetime.strptime(financial_year,"%d-%m-%Y")+timedelta(days=366)
    financial_year_end.strftime("%d-%m-%Y")
    financial_year=datetime.strptime(financial_year,'%d-%m-%Y')
    starting_date = datetime.strptime(book_starting, '%d-%m-%Y')
    return financial_year <= starting_date <= financial_year_end
def number_decoding(number:str,key:str):
    k=key.split('0')
    w='abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` '
    c={w[i]:k[i]for i in range(58)}
    c2=k[58:80]
    str1=[i if not i in c2 else '53' for i in number.split('0')]
    decoded_str=''.join(next(key for key,value in c.items()if value==i) if i in c.values() else i for i in str1)
    return decoded_str
def number_coding(string:str, key:str):
    k=key.split('0')
    import random
    w = 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()_-+={}[]|\\:;\"\'<,>.?/~` '
    c = {w[i]: k[i] for i in range(58)}
    c2 = k[58:80]
    encoded_str = ''.join(c[i]+'0' if i in c else i+'0' for i in string)
    str1 = ''.join(random.choice(c2)+'0' if i == '53' else i+'0' for i in encoded_str.split('0'))
    return str1
def creating_random_key():
    import random
    numb_list = [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '52', '53', '54', '55', '56', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '72', '73', '74', '75', '76', '77', '78', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
    random.shuffle(numb_list)
    key=''.join(n+'0' for n in numb_list)
    return key
def create_company(path_of_creation:str,list_of_compname:list):
    num=0
    while True:
        os.system('cls')
        currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
        (print("path didn't found please run 'setup.py' !") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_creation) else None
        while True:
            print(colored("company creation".center(50,'-'),'yellow'))
            print('you can also close the creation of company by typing "n"') if num>=1 else None
            num+=1
            company_name=input("company name : ")
            if company_name.lower()=='n':
                return None
            if company_name in list_of_compname:
                print('name already exists.....')
            else:
                print('name selected')
                break
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
                print('select number only! ')
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
        os.system('cls')
        print(colored('company info'.center(80),color='yellow')+'\n'+colored('='*80,color='yellow') + colored('\ncompany name: ',color='yellow')+'{:<{}}{}'.format(str(company_name), 60 - 14, colored('fincial year: ',color='yellow') + str(finacial_year)) +
        colored('\nCompany Email: ',color='yellow')+'{:<{}}{}'.format(str(company_e_mail), 60 - 15, colored('Book starting from: ',color='yellow') + str(book_starting)) +
        colored('\nstate: ',color='yellow')+'{:<{}}{}'.format(str(state), 60 - 7, colored('cureency: ',color='yellow') + str(list(currency_symbols.keys())[int(cureency) - 1])) +
        colored('\nCountry: ',color='yellow')+'{:<{}}{}'.format(str(country), 60 - 9, colored('currency sybol: ',color='yellow') + str(currency_symbols[str(list(currency_symbols.keys())[int(cureency) - 1])])) +
        colored('\nPin code: ',color='yellow')+'{:<{}}{}'.format(str(pin_code), 60 - 10, colored('starting balance ',color='yellow') + str(currency_symbols[str(list(currency_symbols.keys())[int(cureency) - 1])]) + ' ' + str(starting_bal)) +
        colored('\ntelephone: ',color='yellow')+'{:<{}}{}'.format(str(telephone), 60 - 11, colored('password_T/F ',color='yellow') + 'True' if password_yn == 'y' else colored('password: ',color='yellow')+'False') +
        colored('\nMoblie numb: ',color='yellow')+'{:<{}}{}'.format(str(mobile_num), 60 - 13, (colored('    password: ',color='yellow') + str(password2)) if password_yn == 'y' else ' ') +
        colored('\nfax: ',color='yellow') + str(fax) + colored('\nwebsite: ',color='yellow') + str(website))
        respones=input('all the inforamtion are currect? y/n ').lower().strip()
        if respones=='y':
            break
        else:
            continue
    os.mkdir(path_of_creation+"\\"+company_name) if not os.path.exists(path_of_creation+"\\"+company_name)else None
    os.mkdir(path_of_creation+'\\'+company_name+'\\company_info') if not os.path.exists(path_of_creation+'\\'+company_name+'\\company_info') else None
    if password_yn=='y':
        with open(path_of_creation+'\\'+company_name+'\\company_info\\po0o1psw1f','w',encoding="utf-8")as fille:
            fille.write(str(key))
            fille.close()
    else :
        pass
    info_list1=['True' if password_yn=='y' else 'False',company_name,company_mail,company_e_mail,state,country,pin_code,telephone,mobile_num,fax,website,str(list(currency_symbols.keys())[int(cureency)-1]),str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])]),finacial_year,book_starting,starting_bal,password if password_yn=='y' else 'None']
    if password_yn == 'y':
        info_list1 = [number_coding(i, key) for i in info_list1]
        info_list1[0] = 'True'
    os.mkdir(path_of_creation+'\\'+company_name+'\\company_info') if not os.path.exists(path_of_creation+'\\'+company_name+'\\company_info') else None
    with open(path_of_creation+'\\'+company_name+'\\company_info\\info_file','w',encoding="utf-8")as fille:
        fille.write(str(info_list1))
        fille.close()
def opening_company(name_of_company:str,main_path:str):
    with open(main_path+'\\'+name_of_company+'\\company_info\\info_file','r',encoding='utf-8') as fille:
        info=eval(fille.read())
        fille.close()
    if info[0]=='True':
        with open(main_path+'\\'+name_of_company+'\\company_info\\po0o1psw1f','r',encoding='utf-8') as fille:
            key=fille.read()
            fille.close()
        for i in range(3):
            password=input("type password to opne compamy (chance-{}): ".format(str(4-i)))
            if number_decoding(info[-1],key)==password:
                break
            else:
                sys.exit if i==3 else None
                pass
    else:
        pass
    info=[number_decoding(i,key) if not i=='False'or'True'or'None' else i for i in info] if info[0]=='True' else info
    os.system('cls')
    print(colored('company info'.center(80),color='yellow')+'\n'+colored('='*80,color='yellow') + colored('\ncompany name: ',color='yellow')+'{:<{}}{}'.format(str(info[1]), 60 - 14, colored('fincial year: ',color='yellow') + str(info[13])) +
    colored('\nCompany Email: ',color='yellow')+'{:<{}}{}'.format(str(info[3]), 60 - 15, colored('Book starting from: ',color='yellow') + str(info[14])) +
    colored('\nstate: ',color='yellow')+'{:<{}}{}'.format(str(info[4]), 60 - 7, colored('cureency: ',color='yellow') + info[11]) +
    colored('\nCountry: ',color='yellow')+'{:<{}}{}'.format(str(info[5]), 60 - 9, colored('currency sybol: ',color='yellow') + str(info[12])) +
    colored('\nPin code: ',color='yellow')+'{:<{}}{}'.format(str(info[6]), 60 - 10, colored('starting balance ',color='yellow') + info[12]+info[15]) +
    colored('\ntelephone: ',color='yellow')+'{:<{}}{}'.format(str(info[7]), 60 - 11, colored('password_T/F ',color='yellow') + info[0]) +
    colored('\nMoblie numb: ',color='yellow')+'{:<{}}{}'.format(str(info[8]), 60 - 13, colored('    password: ',color='yellow') + str(info[16]) +
    colored('\ncompany mail: ',color='yellow') + str(info[2])+colored('\nfax: ',color='yellow') + str(info[9]) + colored('\nwebsite: ',color='yellow') + str(info[10])))
    print('click anything to start code')
    mothimh=input()
# main code begin from here
state_codes = {'andaman and nicobar islands': 'AN', 'andhra pradesh': 'AP', 'arunachal pradesh': 'AR', 'assam': 'AS', 'bihar': 'BR', 'chandigarh': 'CH', 'chhattisgarh': 'CT', 'dadra and nagar haveli and daman and diu': 'DN', 'delhi': 'DL', 'goa': 'GA', 'gujarat': 'GJ', 'haryana': 'HR', 'himachal pradesh': 'HP', 'jharkhand': 'JH', 'karnataka': 'KA', 'kerala': 'KL', 'ladakh': 'LA', 'lakshadweep': 'LD', 'madhya pradesh': 'MP', 'maharashtra': 'MH', 'manipur': 'MN', 'meghalaya': 'ML', 'mizoram': 'MZ', 'nagaland': 'NL', 'odisha': 'OR', 'puducherry': 'PY', 'punjab': 'PB', 'rajasthan': 'RJ', 'sikkim': 'SK', 'tamil nadu': 'TN', 'telangana': 'TG', 'tripura': 'TR', 'uttar pradesh': 'UP', 'uttarakhand': 'UT', 'west bengal': 'WB'}
currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
path_of_dir='C:\\users\\Public'
(print("coude not find the path try running setup.py") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_dir+'\\'+"tally") else None
list_dir=os.listdir(path_of_dir+'\\'+"tally")
while True:
    print('select the company'.center(50),'\n',"-"*50,'\n',colored("[1] create company".center(50),'yellow'),"\n",'-'*50)
    for n,i in enumerate(list_dir,start=2):
        print("[{}].......................{}".format(n,i))
    response=input("enter your responce:  ")
    #selection of computer:
    if response.isdigit():
        os.system('cls')
        if response=='1':
            print('creating a company : ')
            create_company(path_of_dir+'\\'+"tally",list_dir)
            break
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