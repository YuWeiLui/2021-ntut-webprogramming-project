import requests
from bs4 import BeautifulSoup 
import pandas as pd

html = requests.get("https://rate.bot.com.tw/xrt?Lang=zh-TW")
bsObj = BeautifulSoup(html.content, "lxml") 
name = []
rate = []
for single_tr in bsObj.find("table", {"title":"牌告匯率"}).find("tbody").findAll("tr"): 
    cell = single_tr.findAll("td")
    currency_name = cell[0].find("div", {"class":"visible-phone"}).contents[0] 
    currency_name = currency_name.replace("\r","") 
    currency_name = currency_name.replace("\n","")
    currency_name = currency_name.replace(" ","")
    currency_rate_in = cell[1].contents[0].replace("-","0") 
    currency_rate_out = cell[4].contents[0].replace("\r","").replace("\n","")
    currency_rate_out = currency_rate_out.replace(" ","").replace("-","0")
    name.append(currency_name)
    rate.append([float(currency_rate_in),float(currency_rate_out)])
df = pd.DataFrame(rate, index=name, columns=['現金買入','即期賣出'])
cell = bsObj.find("p", {"class":"text-info"}).find("span",{"class":"time"}).contents[0] 

print("最高現金買入 " + df['現金買入'].idxmax() + ' ' + str(df['現金買入'].max()))
print("最高即期賣出 " + df['即期賣出'].idxmax() + ' ' + str(df['即期賣出'].max()))
print(cell)
