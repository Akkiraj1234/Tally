# def number_decoding(number):
#     coding2=['79','81','82','86','88','89','91','96','97','99']
#     coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36','!':'11','@':'13','#':'14','$':'15','%':'17','^':'18','&':'19','*':'21','(':'23',')':'24','_':'29','-':'31','+':'35','=':'37','~':'39','`':'42','<':'44',',':'46','>':'47','.':'48','?':'52','/':'49',':':'57',';':'59','"':'62',"'":'64','{':'66','[':'68','}':'71',']':'74','\\':'76','|':'77'}
#     str1=[]
#     decoded_str=''
#     list1=number.split('0')
#     for i in list1:
#         if i in coding2:
#             str1.append('53')
#         else:
#             str1.append(i)
#     for i in str1:
#         if i in coding.values():
#             decoded_str += next(key for key,value in coding.items()if value==i)
#         else:
#             decoded_str += i
# def number_coding(string):
#     #must only contain number and alphabate and ',' and '.'
#     import random
#     encoded_str=''
#     coding2=['79','81','82','86','88','89','91','96','97','99']
#     coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36','!':'11','@':'13','#':'14','$':'15','%':'17','^':'18','&':'19','*':'21','(':'23',')':'24','_':'29','-':'31','+':'35','=':'37','~':'39','`':'42','<':'44',',':'46','>':'47','.':'48','?':'52','/':'49',':':'57',';':'59','"':'62',"'":'64','{':'66','[':'68','}':'71',']':'74','\\':'76','|':'77'}
#     for i in string:
#         if i in coding:
#             encoded_str += coding[i]+'0'
#         else:
#             encoded_str += i+'0'
#     list1=encoded_str.split('0')
#     str1=''
#     for i in list1:
#         if i == '53':
#             str1+= random.choice(coding2)+'0'
#         else:
#             str1+=i+'0'
#     return(str1)

# # def creating_random_key():
# #     import random
# #     numb_list = [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '38', '39', '41', '42', '43', '44', '45', '46', '47', '48', '49', '51', '52', '53', '54', '55', '56', '57', '58', '59', '61', '62', '63', '64', '65', '66', '67', '68', '69', '71', '72', '73', '74', '75', '76', '77', '78', '79', '81', '82', '83', '84', '85', '86', '87', '88', '89', '91', '92', '93', '94', '95', '96', '97', '98', '99']
# #     word_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|','\\',':',';','"',"'",'<',',','>','.','?','/','~','`',' ']
# #     dict1={}
# #     print(len(numb_list),len(word_list))
# #     for word in word_list:
# #         randome_value=random.choice(numb_list)
# #         index_r=numb_list.index(randome_value)
# #         numb_list.pop(index_r)
# #         dict1[word]=randome_value
# #     return dict1,numb_list
# # list1,dictonery=creating_random_key()
# # print(list1)
# # print(dictonery)

# def number_coding(string,key):
#     word_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|','\\',':',';','"',"'",'<',',','>','.','?','/','~','`',' ']
#     key=key.split('0')
#     coding={}
#     coding2=key[58:80]
#     numb=key[0:58]
#     numb1=0
#     for word in word_list:
#         coding[word]=numb[0]
#         numb1+=1
#     encoded_str=''
#     import random
#     for i in string:
#         if i in coding:
#             encoded_str += coding[i]+'0'
#         else:
#             encoded_str += i+'0'
#     list1=encoded_str.split('0')
#     str1=''
#     for i in list1:
#         if i == '53':
#             str1+= random.choice(coding2)+'0'
#         else:
#             str1+=i+'0'
#     return(str1)



# def number_decoding(number):
#     coding2=['79','81','82','86','88','89','91','96','97','99']
#     coding={' ':'53','q':'12','w':'45','e':'56','r':'34','t':'87','y':'65','u':'69','i':'55','o':'33','p':'63','a':'61','s':'85','d':'83','f':'58','g':'28','h':'25','j':'54','k':'72','l':'95','z':'51','x':'73','c':'93','v':'27','b':'92','n':'84','m':'26','1':'32','2':'43','3':'94','4':'41','5':'75','6':'78','7':'38','8':'67','9':'98','0':'22',',':'16','.':'36','!':'11','@':'13','#':'14','$':'15','%':'17','^':'18','&':'19','*':'21','(':'23',')':'24','_':'29','-':'31','+':'35','=':'37','~':'39','`':'42','<':'44',',':'46','>':'47','.':'48','?':'52','/':'49',':':'57',';':'59','"':'62',"'":'64','{':'66','[':'68','}':'71',']':'74','\\':'76','|':'77'}
#     str1=[]
#     decoded_str=''
#     list1=number.split('0')
#     for i in list1:
#         if i in coding2:
#             str1.append('53')
#         else:
#             str1.append(i)
#     for i in str1:
#         if i in coding.values():
#             decoded_str += next(key for key,value in coding.items()if value==i)
#         else:
#             decoded_str += i
            
            
            
            
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





str1='this is test string and we gonna fuck the shit out of you you baby 6777777 llololll @katya.art12345'
key=creating_random_key()
print(key)
coding_str=number_coding(str1,key)
print(coding_str)
decoded_str=number_decoding(coding_str,key)
print(decoded_str)