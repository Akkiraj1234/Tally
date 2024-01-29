import os
import shutil
import datetime
saving_path='C:\\Users\\DELL\Desktop\\find anythiing'
if os.path.exists(saving_path):
    pass
else:
    os.mkdir(saving_path)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n-----------------------------------------important rules---------------------------------------\n\nthis software helps to find any fille that you want to find in yopur devies....\nyou can either write the fille name to search for and\neithe fille extanstion sunch as (.txt  .py  .html .db .xlsm)\n\n\nimportan rules:\n 1. for using that software firat deside what you wanna find with with extanstion or fille name?\n\n\n   "filename:"    to search for file\n  "extanstion"    to search with extenstion\nafter selecting the extention type what you wanna find:  ')
setup=False

while True:
    selecting_mod=int(input('\n\n\n\n\n\n\nfor selecting "fillename:" type 1 and enter\nfor selecting "extention:" type 2 and enter'))
    if selecting_mod==1:
        print('please type fillename with its extenstion  "ex= akkiclass.xlsx"')
        str11='enter the fillename:)  : '
        setup=False
        break
    elif selecting_mod==2:
        print('please type all extection in lowercase and start with "ex= .xlsx"')
        str11='enter the extenstion:)  : '
        setup=True
        break
    else:
        print('pleasse type currenctly')

search=str(input(str11))
current_time=datetime.datetime.now()
saving_path_fille=saving_path+'\\'+search+'__'+str(current_time.year)+'-'+str(current_time.month)+'-'+str(current_time.day)
try:
    os.mkdir(saving_path_fille)
except Exception as e:
    os.mkdir(saving_path_fille+'123dsgk')
list1=['C','D','F','E']
found=[]
for i in list1:
    path=i+':\\'
    if os.path.exists(path):
        for dirpath, dirnames, filenames in os.walk(path):
            for fillename in filenames:
                if setup==False:
                    if fillename==search:
                        print('found one')
                        source_path=dirpath.replace(' ','')+'\\'+fillename.replace(' ','')
                        found.append(fillename)
                        try:
                            shutil.copy(src=source_path,dst=saving_path_fille)
                        except Exception as e:
                            erroror='errror in copy fille'+fillename
                            found.append(erroror)
                            pass
                elif setup==True:
                    if fillename.endswith(search):
                        print('found one')
                        source_path=dirpath.replace(' ','')+'\\'+fillename.replace(' ','')
                        found.append(fillename)
                        try:
                            shutil.copy(src=source_path,dst=saving_path_fille)
                        except Exception as e:
                            erroror='errror in copy fille'+fillename
                            found.append(erroror)
                            pass
                else:
                    print('unexpected error run this code again')
print('total fills that have beeen found: \n',found)