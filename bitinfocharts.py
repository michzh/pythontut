# Программа для отображения графика курсов с разных площадок
import json
from numpy import mean
import matplotlib.pyplot as plt
from urllib.request import urlopen
url = "http://api.bitcoincharts.com/v1/markets.json"
response = urlopen(url)
contents = response.read()
text = contents.decode('utf8')
datafile = open('markets.json', mode ='wt')
datafile.write(text)
datafile.close()
#data = json.loads(text)

fopen = open ('markets.json')
jsread = fopen.read()
fopen.close()
jsdata = json.loads(jsread)
x=[]
y=[]
xl=[]

for price in jsdata[:]:
    currency = 'USD'
    none = None
    if price["currency"] == currency and price["bid"] != none :
#        print(price["symbol"] , price["currency"], price["bid"], price["ask"], sep=' | ', end='\n')
        x.append(price["bid"])
        y.append(price["ask"])
        xl.append(price["symbol"])

plt.plot(x, label='bid')
plt.plot(y, label='Ask')
#plt.xlabel(xl)
#plt.ylabel('Price CHART')
plt.title('Prices ASK AND BID')
plt.show()
#print(x)
#bid = mean(x)
#print (bid)