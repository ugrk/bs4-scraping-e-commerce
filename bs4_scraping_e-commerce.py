from bs4 import BeautifulSoup
import requests
import csv

fields = ['Urun Gorseli', 'Urun Linki', 'Urun Adi', 'Urun Fiyati', 'Satici Niteligi']

n = 0
b = 0
ur = int(input('Kaç ürün aramak istersin güzellik?:\n'))
arama = input('Ne aramak istersin çıtır?:\n')
html_text = requests.get(f'https://www.gittigidiyor.com/arama/?k={arama}').text
soup = BeautifulSoup(html_text, 'lxml')
urun = soup.find_all('h3', class_='product-title')
fiyat = soup.find_all('p', class_='fiyat price-txt robotobold price')
satici = soup.find_all('div', class_='badge-detail-text left')
gorsel = soup.find_all('a', class_='product-link')
png = soup.find_all('img', class_='img-cont')
pngtk = png[:ur]
gorselp = gorsel[:ur]
badge = satici[:ur]
onurun = urun[:ur]
fiyurun = fiyat[:ur]
print('------------------------------------------------------')

lazi = []
for i in range(ur):
    n += 1
    i = (pngtk[n - 1]['src'])
    a = f"https:{gorselp[n - 1]['href']}"
    y = onurun[n - 1].text
    t = (fiyurun[n - 1].text.strip().replace(" ", "", 19))
    k = badge[n - 1].text
    lazi.append(i)
    lazi.append(a)
    lazi.append(y)
    lazi.append(t)
    lazi.append(k)

m = 0
t = 5

rows = []

for i in range(ur):
    a = lazi[m:t]
    rows.append(a)
    m += 5
    t += 5

filename = "urunler.csv"

with open(filename, 'w', encoding='utf-8', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)

    csvwriter.writerow(fields)

    csvwriter.writerows(rows)

