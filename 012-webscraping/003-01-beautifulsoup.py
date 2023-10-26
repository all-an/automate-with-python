import bs4, requests

url = 'https://www.amazon.com.br/Automate-Boring-Stuff-Python-2nd/dp/1593279922/ref=sr_1_1?keywords=Automate+boring+stuff&qid=1698358961&sr=8-1&ufe=app_do%3Aamzn1.fos.6121c6c4-c969-43ae-92f7-cc248fc6181d'



value = []

while(len(value) < 1):
    res = requests.get(url)

    # res.raise_for_status() # if nothing happens there is no problem

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    value = soup.select('#price') # css selector
    if(len(value) > 0):
        price = soup.select('#price')[0].text
        print(price)
        for i in soup.select('#price')[0]:
            for j in i:
                print(j)
        print(price[3:].replace(",", "."))
        price_float = float(price[3:].replace(",", "."))
        print(price_float - 100)
