import bs4 as bs #beautiful soup shit
import xlwt #stuff for excel
import urllib.request
from xlwt import Workbook

class items:
    def __init__(self, brand, type, price, url):
        self.brand = brand
        self.type = type
        self.price = price
        self.url = url

class itemHighArray(items):

    def insertionSort(alist):
        for index in range(1, len(alist)):

            currentvalue = alist[index]
            position = index

            while position > 0 and alist[position - 1].brand > currentvalue.brand:
                alist[position] = alist[position - 1]
                position = position - 1

            alist[position] = currentvalue


def retrieve_all_sanko():
    sauce = urllib.request.urlopen("https://www.shopkanso.com/products/menu-bottle-grinder")
    soup = bs.BeautifulSoup(sauce, "html.parser")

    span = soup.find('span',{'class':'Price'})

    price = span.text
    price = str(price.replace("\n","")) #Removes \n spaces
    final_price = price.strip().strip("$")
    zed = float(final_price)

    if (zed > 25):
        return zed

def retrieve_all_prices_47brand(): ## This is for 47Brand
    sauce = urllib.request.urlopen("https://www.47brand.com/products/detroit-tigers-carhartt-carhartt-x-47-mvp")
    soup = bs.BeautifulSoup(sauce, "html.parser")

    span = soup.find('span',{'class':'price-display'})

    price = span.text
    price = str(price.replace("\n", ""))  # Removes \n spaces
    final_price = price.strip().strip("$")
    zed = float(final_price)

    if (zed > 25):
        return zed

def retrieve_all_prices_47brand_number2(): ## This is for 47Brand, second link
    sauce = urllib.request.urlopen("https://www.47brand.com/products/detroit-tigers-cooperstown-two-tone-47-clean-up")
    soup = bs.BeautifulSoup(sauce, "html.parser")

    span = soup.find('span', {'class': 'price-display'})

    price = span.text
    price = str(price.replace("\n", ""))  # Removes \n spaces
    final_price = price.strip().strip("$")
    zed = float(final_price)

    if (zed > 10):
        return zed


if __name__ == '__main__':
    list=[]
    thing = items("Detroit Hat", "hat", retrieve_all_prices_47brand_number2(),"https://www.47brand.com/products/detroit-tigers-cooperstown-two-tone-47-clean-up")
    list.append(thing)

    thing2 = items("Menu Bottle Grinder", "Item", retrieve_all_sanko(), "https://www.shopkanso.com/products/menu-bottle-grinder")
    list.append(thing2)

    itemHighArray.insertionSort(list)

    wb = Workbook()
    sheet1 = wb.add_sheet("Sheet Test")

    row, column = 0, 1
    for obj in list:

        sheet1.write(row, column, obj.brand)
        column += 1
        sheet1.write(row, column, obj.type)
        column += 1
        sheet1.write(row, column, obj.price)
        column += 1
        sheet1.write(row, column, obj.url)
        if column == 4 :
            row += 1
            column = 1

    wb.save("xlwt example.xls")