from bs4 import BeautifulSoup
import requests
import pandas as pd
import lxml

# for x in range(1,51):
# base_url = f'http://books.toscrape.com/catalogue/page-{x}.html
# for '


# x += 1



class Scrape():

    def __init__(self, base_url,product_link =[]):
        self.base_url = base_url
        self.product_links = []


       

    def GetUrlLinks(self):

        page = requests.get(self.base_url)
        bs = BeautifulSoup(page.content, "lxml")

        books = bs.find("ol", class_="row").find_all("li")

        for book in books:
            for link in book.find_all("a", href=True):
                product_links.append(self.base_url[:-11] + link['href'])

    def GetData(self):

        for item in product_links:
            link = requests.get(item)
            bs = BeautifulSoup(link.content, "lxml")

            print(item)

            upc = bs.find("table").find("tr").text
            print(upc)

            # caTEGORY
            info = (bs.find_all)("tr")
            # print(info)

            category = (info[1].find("td").text)

            print(category)

            # title

            title = bs.find("div", class_="col-sm-6 product_main").find("h1").text

            print(title)

            # price excluding tax
            price_exc_tax = bs.find("table", class_="table table-striped").find_all("tr")

            price_no_tax = price_exc_tax[2].find("td").text

            print(price_no_tax)

            # price including tax

            price_inc_tax = bs.find("table", class_="table table-striped").find_all("tr")

            price_with_tax = price_inc_tax[3].find("td").text

            print(price_with_tax)

            # number available

            stock = bs.find("table", class_="table table-striped").find_all("tr")

            number_available = stock[5].find("td").text

            print(number_available)

            # product descripiton

            product_description = bs.find("article", class_="product_page").find_all("p")

            description = product_description[-1].text

            # print(description)

            # image url
            image_url = bs.find("div", class_="item active")
            print(image_url.find("img")["src"])

            review = str(bs.find("P", {"class": "star-rating Three"}))[22:].split('"', 1)[0]

    def run(self):
        
        self.GetUrlLinks()
        self.GetData()


if __name__ == "__main__":
    pagescrape = Scrape()
    pagescrape.run()
