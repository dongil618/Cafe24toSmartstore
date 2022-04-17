from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
from urllib.parse import quote
import re
import time


def getProductInfo(productNameIndex):
    headers = {"User-Agent": "Mozilla/5.0"}
    color = []
    size = []
    price = ""
    instruction = ""
    sizeGuide = ""
    category = ""

    url = (
        "https://www.ficelle.co.kr/product/"
        + quote(productNameIndex["productName"])
        + "/"
        + quote(productNameIndex["productIndex"])
        + "/category/25/display/1/"
    )

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        html = urlopen(url)
        soup = bs(html, "html.parser")
        # Color Crawling

        c = soup.find("ul", attrs={"ec-dev-id": "product_option_id1"})
        colors = c.find_all("span")
        # print(colors)
        for i in colors:
            productColor = i.text
            # print("productColor : ", productColor)
            color.append(productColor)

        # c = soup.find_all("ul", attrs={"class": "ec-product-button ec-product-preview"})
        # if not c:
        #     print(soup)
        #     c = soup.find_all("select", attrs={"id": "product_option_id1"})
        #     if c:
        #         colors = c[0].find_all("option")
        #         for i in range(2, len(colors)):
        #             productColor = colors[i].text
        #             print(productColor)
        #             color.append(productColor)
        # else:
        #     colors = c[0].find_all("li")
        #     for i in colors:
        #         productColor = i.find("span").text
        #         print(productColor)
        #         color.append(productColor)

        # Size Crawling
        sizes = soup.find_all("li", attrs={"class": "ec-product-disabled"})
        if not sizes:
            sizes = soup.find_all("select", attrs={"id": "product_option_id2"})
            if sizes:
                s = sizes[0].find_all("option")
                for i in range(2, len(s)):
                    productSize = s[i].text
                    # print(productSize)
                    size.append(productSize)
            else:
                size.append("Free")
        else:
            for i in sizes:
                productSize = i.find("span").text
                # print(productSize)
                size.append(productSize)

        # Product Name Crawling
        # productName = soup.find(
        #     "span", attrs={"style": "font-size:16px;color:#555555;"}
        # ).text

        # category
        # productName으로 분류할것!
        try:
            productNameSplitList = productNameIndex["productName"].split(" ")
            # print(productNameSplitList)
            productNameSplitList.sort()
            # print(productNameSplitList)
            pants = ["Pants", "Slacks"]
            knit_sweater = ["Knit", "Sweater"]
            blouse_shirt = ["Blouse", "Shirt", "Shirts"]
            skirt = ["Skirt"]
            onepiece = ["Onepiece", "Dress"]
            jacket = ["Jacket"]
            jumper = ["Jumper"]
            jumpsuit = ["Jumpsuit"]
            jeans = ["Denim", "Jeans"]
            cardigan = ["Cardigan"]
            coat = ["Coat"]
            sports_wear = ["Jogger"]
            t_shirt = ["T", "Sweat shirt", "Top", "Sleeveless", "MTM"]
            codie_set = ["Set", "&"]
            bag = ["Bag"]
            sandal = ["Sandal"]
            slipper = ["slipper", "Flip"]
            middle_boots = ["Middle"]
            long_boots = ["Long"]
            bloafaer = ["Bloafer"]
            flat = ["Flat"]
            for productNameValue in productNameSplitList:
                if productNameValue in codie_set:
                    category = "패션의류 여성의류 코디세트"
                    break
                else:
                    if productNameValue in pants:
                        category = "패션의류 여성의류 바지"
                        break
                    elif productNameValue in blouse_shirt:
                        category = "패션의류 여성의류 블라우스/셔츠"
                        break
                    elif productNameValue in skirt:
                        category = "패션의류 여성의류 스커트"
                        break
                    elif productNameValue in onepiece:
                        category = "패션의류 여성의류 원피스"
                        break
                    elif productNameValue in jacket:
                        category = "패션의류 여성의류 재킷"
                        break
                    elif productNameValue in jumper:
                        category = "패션의류 여성의류 점퍼"
                        break
                    elif productNameValue in jeans:
                        category = "패션의류 여성의류 청바지"
                        break
                    elif productNameValue in cardigan:
                        category = "패션의류 여성의류 카디건"
                        break
                    elif productNameValue in coat:
                        category = "패션의류 여성의류 코트"
                        break
                    elif productNameValue in sports_wear:
                        category = "패션의류 여성의류 트레이닝복"
                        break
                    elif productNameValue in knit_sweater:
                        category = "패션의류 여성의류 니트/스웨터"
                        break
                    elif productNameValue in jumpsuit:
                        category = "패션의류 여성의류 점프슈트"
                        break
                    elif productNameValue in t_shirt:
                        category = "패션의류 여성의류 티셔츠"
                        break
                    elif productNameValue in bag:
                        category = "패션잡화 여성가방 숄더백"
                        break
                    elif productNameValue in sandal:
                        category = "패션잡화 여성신발 샌들 스트랩샌들"
                        break
                    elif productNameValue in slipper:
                        category = "패션잡화 여성신발 슬리퍼"
                        break
                    elif productNameValue in middle_boots:
                        category = "패션잡화 여성신발 부츠 미들부츠"
                        break
                    elif productNameValue in long_boots:
                        category = "패션잡화 여성신발 부츠 롱부츠"
                        break
                    elif productNameValue in bloafaer:
                        category = "패션잡화 여성신발 샌들 뮬/블로퍼"
                        break
                    elif productNameValue in flat:
                        category = "패션잡화 여성신발 단화 플랫"
                        break                    
        except:
            print("Non-Existent Categories")
        # Instruction and Size Guide Crawling
        price = soup.find("strong", attrs={"id": "span_product_price_text"}).text
        # price string process
        price = re.sub(",|원", "", price)
        price = int(price) + 500
        instruction = soup.find("div", attrs={"id": "view1"}).find("p").text
        sizeGuide = soup.find("div", attrs={"id": "view2"}).find("p").text
        time.sleep(3)
        return {
            "productName": productNameIndex["productName"],
            "price": price,
            "colors": color,
            "sizes": size,
            "instruction": instruction,
            "sizeGuide": sizeGuide,
            "category": category,
        }
    else:
        print(response.status_code)
