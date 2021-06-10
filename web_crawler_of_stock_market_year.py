import requests
from bs4 import BeautifulSoup
import time
import matplotlib.pyplot as plt
import numpy as np
stock = 0
dates = 0
year = 0
day = []
day1 = []
H = []
L = []
def check_date(dates):
  if len(dates) < 4 or len(dates) > 4:
    print("Must have 8 elements!")
    return "N"
  if not dates.isdigit():
    print("Must be numbers!")
    return "N"
  else:
    return "Y"

print("Please enter the number you want to see of stock. Ex:'2330' for tsmc please enter '2330'")
stock = input()
print("Please enter the year you want to see the number of stock. Ex:2020")
dates = input()
check_date(dates)
for d in check_date(dates):
  print(d)
  if d == "N":
    break
  else:
    stock1 = stock
    dates = int(dates)
    url = 'https://www.twse.com.tw/exchangeReport/FMSRFK?response=html&date={}0101&stockNo={}'
    resstock = requests.get(url.format(dates,stock1))   #get data
    time.sleep(5)
    resstock.raise_for_status()
    soupstock = BeautifulSoup(resstock.text, 'html.parser')
    tablestock = soupstock.find_all('tr')
    for trstock in tablestock:
        tdstock = trstock.find_all('td')
        if len(tdstock) < 1:
            continue
        ystock = [a.text.strip() for a in tdstock if a.text.strip()]
        print(ystock[0],ystock[1],ystock[2],ystock[3],ystock[4],ystock[5],ystock[6])
        year = ystock[0]
        day.append(ystock[1])
        H.append(ystock[2])
        L.append(ystock[3])
    print('Done')

del day[0]
del H[0]
del L[0]
day = [(int(x)) for x in day]
H = [(float (x)) for x in H]
L = [(float (x)) for x in L]
plt.plot(day,H,'.-',color='red')
plt.plot(day,L,'.-',color='green')
plt.xticks(np.arange(day[0],day[-1]+1,1.0))
plt.yticks(np.arange(min(L)-5,max(H)+5,10.0))
plt.title(year + ' year stock of ' + stock)
plt.xlabel('Month')
plt.ylabel('Dollars(NTD.)')
plt.legend(['Highest Price','Lowest Price'])
plt.grid(True)
plt.show()