import os
from termcolor import colored
from datetime import datetime , timedelta
import sys
import time
import getpass
import json
import random
import re
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
    def validate_contry(contry_name:str):
        countries = ['australia','newzealand','india','unitedstates','japan','nepal','pakistan','srilanka','china','southkorea','canada','mexico','switzerland','brazil','egypt','russia','france']
        return True if contry_name.strip().lower() in countries else False
    def date_vaidation_check(date):
        try: 
            datetime.strptime(date, '%d-%m-%Y')
            return True
        except Exception : return False
    def validate_pincode_format(contry:str,pin_code:str):
        pin_formats = {'australia': ['XXXX', r'\d{4}$'],'newzealand': ['XXXX', r'\d{4}$'],'india': ['XXXXXX', r'\d{6}$'],'unitedstates': ['XXXXX or XXXXX-XXXX', r'\d{5}$|\d{5}$-\d{4}$'],'japan': ['XXXXXXX', r'\d{7}$'],'nepal': ['XXXXX', r'\d{5}$'],'pakistan': ['XXXXX', r'\d{5}$'],'srilanka': ['XXXXX', r'\d{5}$'],'china': ['XXXXXX', r'\d{6}$'],'southkorea': ['XXXXX', r'\d{5}$'],'canada': ['X1X 1X1', r'[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d'],'mexico': ['XXXXX', r'\d{5}$'],'switzerland': ['XXXX', r'\d{4}$'],'brazil': ['XXXXXXXX', r'\d{8}$'],'egypt': ['XXXXX', r'\d{5}$'],'russia': ['XXXXXX', r'\d{6}$'],'france': ['XXXXX', r'\d{5}$']}
        (re_for:=pin_formats[contry]) if contry.lower().strip() in pin_formats else (re_for:=None)
        if re_for is None: return False,'unvalid contry'
        else: return re.match(re_for[1],pin_code),re_for[0]
    def valid_strting_date_acoding_financial_year(financial_year: str, book_starting: str):
        financial_date = datetime.strptime(financial_year, "%d-%m-%Y")
        financial_year_end = financial_date + timedelta(days=366)
        starting_date = datetime.strptime(book_starting, '%d-%m-%Y')
        return financial_date <= starting_date <= financial_year_end
    def validate_state(contry:str,state_name:str):
        state_list={
        'australia':['New South Wales', 'Victoria', 'Queensland', 'Western Australia', 'South Australia', 'Tasmania', 'Australian Capital Territory', 'Northern Territory'],
        'newzealand':['Northland', 'Auckland', 'Waikato', 'Bay of Plenty', 'Gisborne', 'Hawke\'s Bay', 'Taranaki', 'Manawatu-Whanganui', 'Wellington', 'Tasman', 'Nelson', 'Marlborough', 'West Coast', 'Canterbury', 'Otago', 'Southland', 'Chatham Islands'],
        'india':['andaman and nicobar islands','andhra pradesh','arunachal pradesh','assam','bihar','chandigarh','chhattisgarh','dadra and nagar haveli and daman and diu','delhi','goa','gujarat','haryana','himachal pradesh','jammu and kashmir','jharkhand','karnataka','kerala','ladakh','lakshadweep','madhya pradesh','maharashtra','manipur','meghalaya','mizoram','nagaland','odisha','puducherry','punjab','rajasthan','sikkim','tamil nadu','telangana','tripura','uttar pradesh','uttarakhand','west bengal'],
        'unitedstates':['Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut', 'Delaware','Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky','Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota', 'Mississippi','Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey', 'New Mexico','New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon', 'Pennsylvania','Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah', 'Vermont','Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'],
        'japan':['Aichi', 'Akita', 'Aomori', 'Chiba', 'Ehime', 'Fukui', 'Fukuoka', 'Fukushima', 'Gifu', 'Gunma', 'Hiroshima', 'Hokkaido', 'Hyogo', 'Ibaraki', 'Ishikawa', 'Iwate', 'Kagawa', 'Kagoshima', 'Kanagawa', 'Kochi', 'Kumamoto', 'Kyoto', 'Mie', 'Miyagi', 'Miyazaki', 'Nagano', 'Nagasaki', 'Nara', 'Niigata', 'Oita', 'Okayama', 'Okinawa', 'Osaka', 'Saga', 'Saitama', 'Shiga', 'Shimane', 'Shizuoka', 'Tochigi', 'Tokushima', 'Tokyo', 'Tottori', 'Toyama', 'Wakayama', 'Yamagata', 'Yamaguchi', 'Yamanashi'],
        'nepal':['Bagmati', 'Bheri', 'Dhawalagiri', 'Gandaki', 'Janakpur', 'Karnali', 'Koshi', 'Lumbini', 'Narayani', 'Rapti', 'Sagarmatha', 'Seti'],
        'pakistan':['Punjab', 'Sindh', 'Khyber Pakhtunkhwa', 'Balochistan', 'Gilgit-Baltistan', 'Azad Jammu and Kashmir'],
        'srilanka':['Central', 'Eastern', 'North Central', 'Northern', 'North Western', 'Sabaragamuwa', 'Southern', 'Uva', 'Western'],
        'china':['Anhui', 'Beijing', 'Chongqing', 'Fujian', 'Gansu', 'Guangdong', 'Guangxi', 'Guizhou', 'Hainan', 'Hebei', 'Heilongjiang', 'Henan', 'Hubei', 'Hunan', 'Inner Mongolia', 'Jiangsu', 'Jiangxi', 'Jilin', 'Liaoning', 'Ningxia', 'Qinghai', 'Shaanxi', 'Shandong', 'Shanghai', 'Shanxi', 'Sichuan', 'Tianjin', 'Tibet', 'Xinjiang', 'Yunnan', 'Zhejiang', 'Hong Kong', 'Macau'],
        'southkorea':['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', 'Daejeon', 'Ulsan', 'Sejong', 'Gyeonggi', 'Gangwon', 'Chungbuk', 'Chungnam', 'Jeonbuk', 'Jeonnam', 'Gyeongbuk', 'Gyeongnam', 'Jeju'],
        'canada':['Alberta', 'British Columbia', 'Manitoba', 'New Brunswick', 'Newfoundland and Labrador', 'Nova Scotia', 'Ontario', 'Prince Edward Island', 'Quebec', 'Saskatchewan', 'Northwest Territories', 'Nunavut', 'Yukon'],
        'mexico':['Aguascalientes', 'Baja California', 'Baja California Sur', 'Campeche', 'Chiapas', 'Chihuahua', 'Coahuila', 'Colima', 'Durango', 'Guanajuato', 'Guerrero', 'Hidalgo', 'Jalisco', 'Mexico City', 'Mexico State', 'Michoacán', 'Morelos', 'Nayarit', 'Nuevo León', 'Oaxaca', 'Puebla', 'Querétaro', 'Quintana Roo', 'San Luis Potosí', 'Sinaloa', 'Sonora', 'Tabasco', 'Tamaulipas', 'Tlaxcala', 'Veracruz', 'Yucatán', 'Zacatecas'],
        'switzerland':['Aargau', 'Appenzell Ausserrhoden', 'Appenzell Innerrhoden', 'Basel-Landschaft', 'Basel-Stadt', 'Bern', 'Fribourg', 'Geneva', 'Glarus', 'Graubünden', 'Jura', 'Lucerne', 'Neuchâtel', 'Nidwalden', 'Obwalden', 'Schaffhausen', 'Schwyz', 'Solothurn', 'St. Gallen', 'Thurgau', 'Ticino', 'Uri', 'Valais', 'Vaud', 'Zug', 'Zurich'],
        'brazil':['Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul', 'Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'],
        'egypt':['Alexandria', 'Aswan', 'Asyut', 'Beheira', 'Beni Suef', 'Cairo', 'Dakahlia', 'Damietta', 'Faiyum', 'Gharbia', 'Giza', 'Ismailia', 'Kafr El Sheikh', 'Luxor', 'Matrouh', 'Minya', 'Monufia', 'New Valley', 'North Sinai', 'Port Said', 'Qalyubia', 'Qena', 'Red Sea', 'Sharqia', 'Sohag', 'South Sinai', 'Suez'],
        'russia':['Adygea', 'Altai Krai', 'Altai Republic', 'Amur Oblast', 'Arkhangelsk Oblast', 'Astrakhan Oblast', 'Bashkortostan', 'Belgorod Oblast', 'Bryansk Oblast', 'Buryatia', 'Chechnya', 'Chelyabinsk Oblast', 'Chukotka Autonomous Okrug', 'Chuvashia', 'Crimea (Republic of Crimea)', 'Dagestan', 'Ingushetia', 'Irkutsk Oblast', 'Ivanovo Oblast', 'Jewish Autonomous Oblast', 'Kabardino-Balkaria', 'Kaliningrad Oblast', 'Kalmykia', 'Kaluga Oblast', 'Kamchatka Krai', 'Karachay-Cherkessia', 'Kemerovo Oblast', 'Khabarovsk Krai', 'Khakassia', 'Khanty-Mansi Autonomous Okrug', 'Kirov Oblast', 'Komi', 'Kostroma Oblast', 'Krasnodar Krai', 'Krasnoyarsk Krai', 'Kurgan Oblast', 'Kursk Oblast', 'Leningrad Oblast', 'Lipetsk Oblast', 'Magadan Oblast', 'Mari El', 'Mordovia', 'Moscow', 'Moscow Oblast', 'Murmansk Oblast', 'Nenets Autonomous Okrug', 'Nizhny Novgorod Oblast', 'North Ossetia-Alania', 'Novgorod Oblast', 'Novosibirsk Oblast', 'Omsk Oblast', 'Orenburg Oblast', 'Oryol Oblast', 'Penza Oblast', 'Perm Krai', 'Primorsky Krai', 'Pskov Oblast', 'Rostov Oblast', 'Ryazan Oblast', 'Saint Petersburg', 'Sakha (Yakutia)', 'Sakhalin Oblast', 'Samara Oblast', 'Saratov Oblast', 'Sevastopol', 'Smolensk Oblast', 'Stavropol Krai', 'Sverdlovsk Oblast', 'Tambov Oblast', 'Tatarstan', 'Tomsk Oblast', 'Tula Oblast', 'Tver Oblast', 'Tyumen Oblast', 'Tyva', 'Udmurtia', 'Ulyanovsk Oblast', 'Vladimir Oblast', 'Volgograd Oblast', 'Vologda Oblast', 'Voronezh Oblast', 'Yamalo-Nenets Autonomous Okrug', 'Yaroslavl Oblast', 'Zabaykalsky Krai'],
        'france':['Auvergne-Rhône-Alpes', 'Bourgogne-Franche-Comté', 'Brittany', 'Centre-Val de Loire', 'Corsica', 'Grand Est', 'Hauts-de-France', 'Île-de-France', 'Normandy', 'Nouvelle-Aquitaine', 'Occitanie', 'Pays de la Loire', 'Provence-Alpes-Côte d\'Azur', 'Guadeloupe', 'Martinique', 'Guyane', 'La Réunion', 'Mayotte']
        }
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
def create_company(path_of_creation:str,list_of_compname:list):
    num=0#important variable
    currency_symbols = {'EGP':'EGP','NPR':'NPR','PKR':'₨','LKR':'රු','KRW':'₩','EUR':'€','USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
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
            if validation_check.validate_contry(country): break
            else:print('unvalid country name or this app is not availabe in the contry ')
        while True:#company state
            if (state:=input("state : ")).lower()=='n':print('important can\' be skiped');continue
            if validation_check.validate_state(country,state):break
            else:print('unvalid state or maybe typo ')
        while True: #company pin code
            if (pin_code:=input("pin code : ")).lower()=='n':print('important can\' be skiped');continue
            re_for=validation_check.validate_pincode_format(country,pin_code)
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
    os.mkdir(path_of_creation+"\\company_name\\"+company_name) if not os.path.exists(path_of_creation+"\\company_name\\"+company_name)else None
    os.mkdir(path_of_creation+"\\company_name\\"+company_name+'\\company_info') if not os.path.exists(path_of_creation+"\\company_name\\"+company_name+'\\company_info') else None
    info_dir['company_info'].update((i,number_coding(v,key))for i,v in info_dir['company_info'].items()if password_yn=='y')
    # (info_dir['company_info'][i]=number_coding(info_dir['company_info'][i],key) for i in info_dir['company_info'].keys()) if password_yn=='y' else None
    with open(path_of_creation+"\\company_name\\"+company_name+'\\company_info\\info_file.json','w',encoding="utf-8")as fille:
        json.dump(info_dir,fille,ensure_ascii=True,indent=4)
def opening_company(name_of_company:str,main_path:str):
    with open(main_path+'\\company_name\\'+name_of_company+'\\company_info\\info_file.json','r',encoding='utf-8') as fille:info_got=json.load(fille)
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
#all path:------------------

# main code begin from here
state_codes = {'andaman and nicobar islands': 'AN', 'andhra pradesh': 'AP', 'arunachal pradesh': 'AR', 'assam': 'AS', 'bihar': 'BR', 'chandigarh': 'CH', 'chhattisgarh': 'CT', 'dadra and nagar haveli and daman and diu': 'DN', 'delhi': 'DL', 'goa': 'GA', 'gujarat': 'GJ', 'haryana': 'HR', 'himachal pradesh': 'HP', 'jharkhand': 'JH', 'karnataka': 'KA', 'kerala': 'KL', 'ladakh': 'LA', 'lakshadweep': 'LD', 'madhya pradesh': 'MP', 'maharashtra': 'MH', 'manipur': 'MN', 'meghalaya': 'ML', 'mizoram': 'MZ', 'nagaland': 'NL', 'odisha': 'OR', 'puducherry': 'PY', 'punjab': 'PB', 'rajasthan': 'RJ', 'sikkim': 'SK', 'tamil nadu': 'TN', 'telangana': 'TG', 'tripura': 'TR', 'uttar pradesh': 'UP', 'uttarakhand': 'UT', 'west bengal': 'WB'}
currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
path_of_dir='C:\\users\\Public'
(print("coude not find the path try running setup.py") or time.sleep(2) or sys.exit()) if not os.path.exists(path_of_dir+'\\'+"tally") else None
list_dir=os.listdir(path_of_dir+'\\tally\\company_name')
while True:
    os.system('cls');print('select the company'.center(50),'\n',"-"*50,'\n',colored("[1] create company".center(50),'yellow'),"\n",'-'*50)
    for n,i in enumerate(list_dir,start=2):print("[{}].......................{}".format(n,i))
    response=input("enter your responce:  ")
    #selection of computer:
    if response.isdigit():
        os.system('cls')
        if response=='1':
            print('creating a company : ')
            res=create_company(path_of_dir+'\\'+"tally",list_dir)
            if not res: break#while creating the company if we go back by n while inpying name we don't go directly to fot insted of home screen that's why we use it
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