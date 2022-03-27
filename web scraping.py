import requests
from bs4 import BeautifulSoup
url="https://www.amazon.fr/dp/1015"
a=requests.get(url)
print(a.content)
# %%
a1=BeautifulSoup(a.content,'html.parser')
print(a1.prettify())
# %%
d=a1.title
c=d.get_text()


# %%
img=a1.find_all('img')
l=[]
for i in img:
    l.append(i['src'])
print(l)
#%%
d={"title":c,"product_image_url":l[1]}
print(d)

import json
print(json.dumps(d))