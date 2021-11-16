import requests
from bs4 import BeautifulSoup
import smtplib
import lxml

URL = "https://www.amazon.com/Nike-Basketball-Shoes-Crimson-Numeric_11/dp/B083FRF7R4/ref=sr_1_4?crid=KF928BOR834R&dchild=1&keywords=nike&qid=1635871643&qsid=136-4024510-7777551&sprefix=nik%2Caps%2C287&sr=8-4&sres=B07NLVK1NP%2CB078NG6LRD%2CB07RGLZXKH%2CB07YKR5FR4%2CB083PV5VCH%2CB01CB0UPZ6%2CB07FKCK3KK%2CB072QXS3JD%2CB0921WFDGW%2CB0798P35QF%2CB00E4Z0034%2CB004Y6PQBE%2CB08RMZNYNB%2CB095XWY37G%2CB08NYFPGQ8%2CB07TKMNN8J%2CB07HDS9CQW%2CB07WM2VF63%2CB07Y856JTW%2CB007T2HB7C&th=1&psc=1"
header = {
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "en-US,en;q=0.5",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0",
}

amazon = requests.get(URL, headers=header)
amazon_page = amazon.text

soup = BeautifulSoup(amazon_page, "lxml")
item = soup.find(name="span", class_="a-offscreen")
title = soup.find(id="productTitle").get_text().strip()

price = float(item.text.split("$")[1])
BUY_PRICE = 200

my_email = "dummypythonmail2@gmail.com"
password = "123abc()"

if price < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        result = connection.login(my_email, password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="emisiuniromanestinoi@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}"
        )