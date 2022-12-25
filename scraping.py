import bs4
from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.logitech.com/en-in/products/mice.html'

#Opening up connection & grabing the page content
uClient = ureq(my_url)
pageHtml = uClient.read()
uClient.close()

#HTML parsing
pageSoup = soup(pageHtml, "html.parser")
#print(pageSoup.p)

#grab each products in CSV files
containers = pageSoup.findAll("div", {"class": "product"})

filename = "Gursheen_LogitechProducts.csv"
f = open(filename, "w")
headers = "Product, Subtitle, Price, Image Link\n"
f.write(headers)

for container in containers:
    
    product_name = container.findAll("h2", {"class": "title"})
    if product_name:
        product_name = product_name[0].text
        
        img_link = container.find("img")
        img_link = img_link['src']
        
        subtitle = container.findAll("div", {"class": "js-subtitle"})
        subtitle = subtitle[0].text
        
        product_price = container['data-msrp-price']
    
        if float(product_price) > 0.0:
            product_price='Rs. '+product_price
            print('\n--------------------------------')
            print('\nProduct - ' , product_name)
            print('\nSubtitle - ' , subtitle)
            print('\nPrice - ' , product_price)
            print('\nImage Link - ' , img_link)

            f.write(product_name + "," + subtitle.replace(",", "|") + "," + product_price +',' + '"'+img_link +'"'+ "\n")
f.close()

