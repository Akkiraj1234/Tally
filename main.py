import os
from termcolor import colored
path_of_dir='C:\\users\\Public'
while True:
    if os.path.exists(path_of_dir+'\\'+"tally"):
        break         
    else:
        print('coude not find the path try running setup.py')
        nothing=input()
list_dir=os.listdir(path_of_dir+'\\'+"tally")
print('select the company'.center(50))
print("--------------------------------------------------")
print(colored("[1] create company".center(50),'yellow'))
print("--------------------------------------------------")
for n,i in enumerate(list_dir,start=2):
    print("[{}].............................{}".format(n,i))
response=input("enter your response:  ")

def create_company(path_of_main_dir,name_of_company,):
    path_of_creation=path_of_main_dir+'\\'+name_of_company
    print('comapny creation'.center(50,'-'))
    os.mkdir(path_of_creation)
    if os.path.exists(path_of_creation):
        print('path created.... for company name',name_of_company)
    else:
        print('there is some error while creating company path try running setup.py')

#selection of company:
if response.isdigit():
    os.system('cls')
    if response=='1':
        print('creating a company :')
        while True:
            name_of_company=input('enter the name of your comapny: ')
            if name_of_company in list_dir:
                print('name already exists! ' )
            else:
                break
            create_company()
    else:
        print('company selected: ')
