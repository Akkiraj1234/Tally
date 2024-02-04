#insuring pip is installed or not !
try:
    import pip
except ImportError:
    try:
        import ensurepip
        ensurepip.bootstrap()
    except ImportError:
        while True:
            nothing=input('pip is not installed try downloading pip first\nafter installation restart the code again:)')
import os
import subprocess
import socket
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
#checking if internet is conected or not !
while True:
    if check_internet_connection():
        print("Internet is connected")
        break
    else:
        answer2=input("internet is not conected? do u wanna refresh?- y ")
        if answer2=='y':
            continue
        else:
            print('please type y or end the code')
#installing libraries
try:
    from termcolor import colored
except ImportError:
    subprocess.call(['pip3','install','termcolor'])
    from termcolor import colored
try:
    import sys
except ImportError:
    subprocess.call(['pip3','install','sys'])
try:
    import getpass
except ImportError:
    subprocess.call(['pip3','install','getpass'])
try:
    import json
except ImportError:
    subprocess.call(['pip3','install','json'])
try:
    import time
except ImportError:
    subprocess.call(['pip3','install','time'])
try:
    import random
except ImportError:
    subprocess.call(['pip3','install','random'])
try:
    import datetime
except ImportError:
    subprocess.call(['pip3','install','datetime'])
try:
    import re
except ImportError:
    subprocess.call(['pip3','install','re'])
try:
    from forex_python.converter import CurrencyRates
except ImportError:
    subprocess.call(['pip3','install','forex-python'])
#path creatation
path_of_dir='C:\\users\\Public'
if os.path.exists(path_of_dir+'\\'+"tally"):
    pass
else:
    os.mkdir(path_of_dir+'\\'+"tally")
if os.path.exists('C:\\users\\Public\\tally\\tally_dev_info'):
    pass
else:
    os.mkdir('C:\\users\\Public\\tally\\tally_dev_info')
if os.path.exists('C:\\users\\Public\\tally\\company_name'):
    pass
else:
    os.mkdir('C:\\users\\Public\\tally\\company_name')
#all the path____
containin1st_dir='C:\\Users\\Public'             #C:\\users\\Public
main_path=containin1st_dir+'\\tally'            #C:\\users\\public\\tally
company_path=main_path+'\\company_name'         #C:\\users\\public\\tally\\company_name         <--|
#*company_name*   ---> name_of_company ----> company_info ----> (info_file.json)                   | both inside tally
tally_dev_path=main_path+'\\tally_dev_info'     #C:\\users\\public\\tally\\tally_dev_info       <--|
#*tally_dev_info* ---> (status_data.json,basic_info.json),important_fille ---> (filles)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
info1={
    'basic_info':{
        'countries':['australia','newzealand','india','unitedstates','japan','nepal','pakistan','srilanka','china','southkorea','canada','mexico','switzerland','brazil','egypt','russia','france'],
        'state_list':{
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
            },
        'currency_symbols':{'EGP':'EGP','NPR':'NPR','PKR':'₨','LKR':'රු','KRW':'₩','EUR':'€','USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'},
        'pin_formats':{'australia': ['XXXX', r'\d{4}$'],'newzealand': ['XXXX', r'\d{4}$'],'india': ['XXXXXX', r'\d{6}$'],'unitedstates': ['XXXXX or XXXXX-XXXX', r'\d{5}$|\d{5}$-\d{4}$'],'japan': ['XXXXXXX', r'\d{7}$'],'nepal': ['XXXXX', r'\d{5}$'],'pakistan': ['XXXXX', r'\d{5}$'],'srilanka': ['XXXXX', r'\d{5}$'],'china': ['XXXXXX', r'\d{6}$'],'southkorea': ['XXXXX', r'\d{5}$'],'canada': ['X1X 1X1', r'[A-Za-z]\d[A-Za-z] \d[A-Za-z]\d'],'mexico': ['XXXXX', r'\d{5}$'],'switzerland': ['XXXX', r'\d{4}$'],'brazil': ['XXXXXXXX', r'\d{8}$'],'egypt': ['XXXXX', r'\d{5}$'],'russia': ['XXXXXX', r'\d{6}$'],'france': ['XXXXX', r'\d{5}$']}
    },
    'important_data':None
}
status_data={
    'basic_info':{
        "version":00,
        'money':{
            'money_value_USA':{'EGP': 0.032, 'NPR': 0.0075, 'PKR': 0.0036, 'LKR': 0.0036, 'KRW': 0.00075, 'EUR': 1.08,'GBP': 1.26, 'JPY': 0.0067, 'CAD': 0.74, 'AUD': 0.65, 'CHF': 1.15, 'CNY': 0.14, 'INR': 0.012, 'BRL': 18.31,'RUB': 1.10, 'ZAR': 4.81, 'MXN': 5.31, 'NZD': 55.18, 'SEK': 8.60},
            'last_update':"2024-02-03 12:34:12.123455",
            'previous_M_V_detail_by_USA':{'EGP': 0.032, 'NPR': 0.0075, 'PKR': 0.0036, 'LKR': 0.0036, 'KRW': 0.00075, 'EUR': 1.08,'GBP': 1.26, 'JPY': 0.0067, 'CAD': 0.74, 'AUD': 0.65, 'CHF': 1.15, 'CNY': 0.14, 'INR': 0.012, 'BRL': 18.31,'RUB': 1.10, 'ZAR': 4.81, 'MXN': 5.31, 'NZD': 55.18, 'SEK': 8.60},
        },
    },
    'status_info_collected':{
        'opend':0,
        'last_company_opend':None,
        'last_open_time':None,
        'total_commpany_created':0,
        'delected_copany':0,
        
    }
}
if os.path.exists(tally_dev_path+'\\basic_info.json'):
    with open(tally_dev_path+'\\status_data.json','r',encoding="utf-8") as file1:
        data=json.load(file1)
    status_data['status_info_collected']['opend']=data['status_info_collected']['opend']
    status_data['status_info_collected']['last_company_opend']=data['status_info_collected']['last_company_opend']
    status_data['status_info_collected']['last_open_time']=data['status_info_collected']['last_open_time']
    status_data['status_info_collected']['total_commpany_created']=data['status_info_collected']['total_commpany_created']
    status_data['status_info_collected']['delected_copany']=data['status_info_collected']['delected_copany']
# saving_all_nessary_data !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
with open(tally_dev_path+'\\basic_info.json','w',encoding="utf-8") as file1:
    json.dump(info1,file1,ensure_ascii=True)
with open(tally_dev_path+'\\status_data.json','w',encoding="utf-8") as file2:
    json.dump(status_data,file2,ensure_ascii=True)