import os
import json



from datetime import datetime
def create_company(path_of_main_dir:str,name_of_company:str):
    path_of_creation=path_of_main_dir+'\\'+name_of_company
    os.mkdir(path_of_creation)
    if os.path.exists(path_of_creation):
        print('path created.... for company name',name_of_company)
    else:
        print('there is some error while creating company path try running setup.py')
    while True:
        print('comapny creation'.center(50,'-'))
        print('compan name :',name_of_company)
        currency_symbols = {'USD': '$', 'EUR': '€', 'GBP': '£', 'JPY': '¥', 'CAD': '$', 'AUD': '$', 'CHF': 'CHF', 'CNY': '¥ or 元', 'INR': '₹', 'BRL': 'R$', 'RUB': '₽', 'ZAR': 'R', 'MXN': '$', 'NZD': '$', 'SEK': 'kr'}
        company_mail=input("company mail address : ")
        company_e_mail=input("company E-mail address :")
        state=input("state : ")
        country=input("country : ")
        pin_code=input("enter the pin code: ")
        telephone=input("enter the telephone number : ")
        mobile_num=input("enter the mobile number : ")
        fax=input("enter the fax number : ")
        website=input("enter the website name : ")
        print('select the currency num in given below')
        for n,i in enumerate(currency_symbols,start=1):
            print('{}).      {}'.format(n,i))
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
                break
            except ValueError:
                print("Invalid date format. Please enter the date in dd-mm-yyyy format.")
        starting_bal=input('enter the starting balance')
        print('your compant info'.center(50,'-')+'\ncompany name : {:<{}}{}'.format(name_of_company,40-15,'finacial year begin from : '+finacial_year)+'\nstate : {:<{}}{}'.format(state,40-8,'books beging from : '+book_starting)+'\ncountry : {:<{}}{}'.format(country,40-10,'currency : '+str(list(currency_symbols.keys())[int(cureency)-1]))+'\npincode : {:<{}}{}'.format(pin_code,40-10,'currency sybol : '+str(currency_symbols[str(list(currency_symbols.keys())[int(cureency)-1])]))+'\ntelephone : {:<{}}{}'.format(telephone,40-12,'inisial balance : '+starting_bal)+'\nphone number : '+mobile_num+'\n email id : '+company_e_mail+'\nfax : '+str(fax),'\nmail id : '+company_mail,'\nwebsite : ',website)
        while True:
            confirm=input('all the information is currect y-n ')
            if confirm =='y' or confirm=='n':
                break
        if confirm == 'y':
            break
        else:
            pass
create_company("main path ",'akhand_raj')