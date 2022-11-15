from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.gg5.com/category/bottoms/shortsskorts'

 #opening up connection,grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grabs each product
containers = page_soup.findAll("div",{"class":"productrow"})

filename = "products.csv"
f = open(filename, "w")

headers = "product_image, product_name, price\n"

f.write(headers)

for container in containers:
	product_image = container.a.img["src"]

	title_container = container.findAll("div",{"class":"product-title"})
	product_name = title_container[0].text.strip()

	price_container = container.findAll("div",{"class":"product-price"})
	price = price_container[0].text.strip()

	print("product_image: " + product_image)
	print("product_name: " + product_name)
	print("price: " + price)

	f.write(product_image + "," + product_name + "," + price + "\n") 

	