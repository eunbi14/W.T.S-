from bs4 import BeautifulSoup
import requests
URL = "http://www.weatheri.co.kr/forecast/forecast01.php?rid=0201010202&k=1&a_name=%EA%B3%BC%EC%B2%9C"  #과천주간별 날씨
html = requests.get(URL).text
soup = BeautifulSoup(html, 'html.parser')

#temper
print("temper:")
tempTable = soup.find_all("td", class_="f11")

for i in range(10):
    temp=tempTable[i].text
    high=float(temp[:2])
    low=float(temp[5:7])
    ave=(high+low)/2
    print(ave)

#rain
print("\nrain:")
rainTable = soup.find_all("td")
#8/5
a=[]
for i in range(350,358):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/6
a=[]
for i in range(411,419):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8월7일꺼8개
a=[]
for i in range(472,480):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/8
a=[]
for i in range(533,541):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/9
a=[]
for i in range(594,602):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/10
a=[]
for i in range(725,733):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/11
a=[]
for i in range(786,794):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/12
a=[]
for i in range(847,855):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/13
a=[]
for i in range(908,916):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#8/14
a=[]
for i in range(969,977):
    a.extend(list(map(float,rainTable[i].text.split())))
print(sum(a))
#day
print("\nday:")
dayTable=soup.find_all("b")
day=[]
for i in range(18,23):
    d=''.join(dayTable[i].text)
    da=d[:2]+d[5:8]
    #print(da)
    day.append(da)
    #print(day)

for i in range(78,83):
    d=''.join(dayTable[i].text)
    da=d[:2]+d[5:8]
    day.append(da)
print(day)
#cloud
print("\ncloud:")
rang=[21,23,25,27,29,76,78,80,82,84]
cloudTable = soup.find_all("img")
imgset=[]
for i in rang:
    img=cloudTable[i]
    #print(img['src'])
    imgset.append(img['src'])
print(imgset)

