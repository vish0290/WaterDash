import json, requests
# userid = 'user'
# def file_updater(userid,file='demo.json'):
#     f = open(file ,'r')
#     rawdata = json.load(f)
#     f.seek(0)
#     f.close()
#     maindata = rawdata[userid]
#     fi = input('Enter the field name: ')
#     if fi in maindata.keys():
#         val = input("Enter the value: ") 
#         maindata[fi] = val
#         rawdata[userid] = maindata
#         with open(file,'w') as w:
#             json.dump(rawdata,w,indent=4)
#     else:
#         print("Field is not present") 

# file_updater(userid)


# id = 'user'
# passw = 'yo'
# f = open('data.json')
# maindata = json.load(f)
# if id in maindata.keys():
#     data = maindata[id]
#     if data['pass'] == passw:
#         file_updater()
#     else:
#         print("Wrong Pass")
# else:
#     print("User does not exist")


url = 'http://5ea6-34-86-53-23.ngrok.io/update/user:data:800'
rsp = requests.get(url)
print(rsp)