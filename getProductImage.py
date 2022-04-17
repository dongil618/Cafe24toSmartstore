# -*- encoding: utf-8 -*-
from bs4 import BeautifulSoup as bs
import requests
from urllib.request import urlopen
from urllib.parse import quote
import os
import getProductNameIndex
import time


def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print("Error: Creating directory. " + directory)


def getProductImgURLList(productNameIndex):
    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        productImgURLList = []
        url = (
            "https://www.ficelle.co.kr/product/"
            + quote(productNameIndex["productName"])
            + "/"
            + quote(productNameIndex["productIndex"])
            + "/category/25/display/1/"
        )
        print(url)
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            html = urlopen(url)
            soup = bs(html, "html.parser")
            # main Image Crawling
            # mainImg = soup.select(
            #     "#grow_1 > div.xans-element-.xans-product.xans-product-detail > div.detailArea > div > div.keyImg > div > p > img"
            # )[0]["src"]
            # mainImgURL = "https:" + quote(mainImg)
            # productImgURLList.append(mainImgURL)

            # main Image and Detail Image Crawling - detaile image crawling 코드가 변경되면서 둘이 같이 크롤링되서 합쳐짐.
            productDiv_cont = soup.find("div", attrs={"class": "cont"})
            productDivs = productDiv_cont.find_all(
                "div", attrs={"class": "edb-img-tag-w"}
            )  # 원래는 cont였지만 edi_products에서 style이 자꾸 변경되면서 애초에 productDiv를 변경
            # print(productDivs)
            # edi_products = productDiv.find_all(
            #    "div", attrs={"style": "position:relative"}
            # )
            # print(edi_products)
            edi_products = []
            for productDiv in productDivs:
                edi_products.append(productDiv.find("img"))
            edi_products = list(filter(None, edi_products))
            # print(edi_products)
            for edi_product in edi_products:
                try:
                    print(edi_product["ec-data-src"])
                    if "ficelle" in edi_product["ec-data-src"]:
                        edi_product = "https:" + quote(edi_product["ec-data-src"])
                    else:
                        edi_product = "https://www.ficelle.co.kr" + quote(
                            edi_product["ec-data-src"]
                        )
                    productImgURLList.append(edi_product)
                except KeyError:
                    edi_product = "https:" + quote(
                        edi_product["src"].replace("\r\n", "")
                    )
                    productImgURLList.append(edi_product)
            print(f'{productNameIndex["productName"]} get complete!')
            time.sleep(5)
            print(productImgURLList)
            return productImgURLList

            # 에디봇 사용하지 않았을때의 코드!
            # products = productDiv.find_all("img", attrs={"alt": ""})
            # for product in products:
            #     try:
            #         product = "https://www.ficelle.co.kr" + quote(
            #             product["ec-data-src"]
            #         )
            #         productImgURLList.append(product)
            #     except KeyError:
            #         product = "https://www.ficelle.co.kr" + quote(
            #             product["src"].replace("\r\n", "")
            #         )
            #         productImgURLList.append(product)
            # print(f'{productNameIndex["productName"]} get complete!')
            # time.sleep(5)
            # return productImgURLList
        else:
            print(response.status_code)
    except:
        print("URL Error!")


def saveProductImage(productNameIndex, productImgURLList):
    path = "C:\\ficelleSmartStore\\detailImage\\{0}".format(
        productNameIndex["productName"]
    )
    # create Directory
    createFolder(path)
    n = 1
    for imgUrl in productImgURLList:
        # save image
        with urlopen(imgUrl) as f:
            with open(
                "C:\\ficelleSmartStore\\detailImage\\{0}\\{0}{1}.jpg".format(
                    productNameIndex["productName"], str(n)
                ),
                "wb",
            ) as h:  # 이미지 + 사진번호 + 확장자는 jpg
                img = f.read()  # 이미지 읽기
                h.write(img)  # 이미지 저장
        print(f'{productNameIndex["productName"]} save complete!')
        n += 1


def __init__():
    productNameIndexList = getProductNameIndex.getProductNameIndex(7, 10)
    for productNameIndex in productNameIndexList:
        productImgURLList = getProductImgURLList(productNameIndex)
        saveProductImage(productNameIndex, productImgURLList)
    print("ALL save complete!!!!")


__init__()