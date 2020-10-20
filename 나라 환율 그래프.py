from bs4 import BeautifulSoup
import urllib.request as req
import matplotlib.pyplot as plt
url='https://finance.naver.com/marketindex/exchangeDailyQuote.nhn?marketindexCd=FX_USDKRW'
res=req.urlopen(url)
soup=BeautifulSoup(res,"html.parser")
x=[]
y=[]
for i in reversed(range(10)):
    x.append(soup.find_all("td",class_="date")[i].text)
    y.append(float(soup.find_all("td",class_="num")[2*i].text.replace(",","")))
plt.figure(figsize=(15,6))
plt.plot(x,y)
plt.show()