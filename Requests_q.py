# Without using functions

import requests 
import json 
a=requests.get("http://saral.navgurukul.org/api/courses")
x=a.json()
f=open("corses.json","w")
json.dump(x,f,indent=4)
f=open("corses.json","r")
data=json.load(f)
id=[] 
i=0
while i<len(data['availableCourses'])-1:
    print(i+1,"",data['availableCourses'][i]['name'],"=",data['availableCourses'][i]['id'])
    id.append(data['availableCourses'][i]['id'])
    i+=1 
user= int(input("enter the id number:"))
n1=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
a=n1.json()
j=0
l=0
slug=[]
while j<len(a["data"]):
    print(l+1,"=",a["data"][j]["name"])
    slug.append(a['data'][j]["slug"]) 
    l=l+1
    j=j+1
slugname=int(input("Enter your slug number:"))
sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
b=sluglist.json()
print(b["name"])
print(b["slug"])
print("CONTENT",b["content"])
for i in range(len(slug)):
    s=input("enter the 'n' for next : ")
    if s=="n":
        i=0
        if i < len(slug):
            print(slug[i])  
            print(b["content"]) 
            break
    else:
        print(":( your page is not  found")
        i=i+1
        print("*")
    g=input("your request accpect:")
    if  g=="yes":
        print("oke then your exist ")
    else:
        print("your req not accpect")




# with using function

# import requests
# import json 
# def Request():
#     a=requests.get("http://saral.navgurukul.org/api/courses")
#     x=a.json()
#     f=open("courses.json","w")
#     json.dump(x,f,indent=4)
#     f=open("courses.json","r")
#     data=json.load(f)
#     id=[] 
#     i=0
#     while i<len(data['availableCourses'])-1:
#         print(i+1,"",data['availableCourses'][i]['name'],"=",data['availableCourses'][i]['id'])
#         id.append(data['availableCourses'][i]['id'])
#         i+=1 
#     user= int(input("enter the id number:"))
#     n1=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
#     a=n1.json()
#     j=0
#     l=0
#     slug=[]
#     while j<len(a["data"]):
#         print(l+1,"=",a["data"][j]["name"])
#         slug.append(a['data'][j]["slug"]) 
#         l=l+1
#         j=j+1
#     slugname=int(input("Enter your slug number:"))
#     sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
#     b=sluglist.json()
#     print(b["name"])
#     print(b["slug"])
#     print("CONTENT",b["content"])
#     for i in range(len(slug)):
#         s=input("enter the 'n' for next : ")
#         if s=="n":
#             i=0
#             if i < len(slug):
#                 print(slug[i])  
#                 print(b["content"]) 
#                 break
#         else:
#             print(":( your page is not  found")
#             i=i+1
#             print("*")
#         g=input("your request accpect:")
#         if  g=="yes":
#             print("oke then your exist ")
#         else:
#             print("your req not accpect")
# Request()