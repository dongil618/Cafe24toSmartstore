import pyperclip as pyperclip
from selenium import webdriver
import time
import pyautogui
import getProductNameIndex
import getProductInfo
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from dotenv import load_dotenv
import os 


def guide():
    print("[System] 스마트스토어 CAFE24 연동 상품업로드 봇입니다.")
    print("[System] 해당봇은 1인 비즈니스 업무 자동화를 위해 제작되었습니다.")
    print("[System] 계정 정보나 데이터, 캐시를 일체 저장하지 않으며, 서버가 없는 프로그램입니다.")
    print("[System] 전체 코드를 제공하는 학습 프로그램입니다.\n")
    print("[System] 작업이 시작됩니다..*")


def login(driver):
    # load .env
    load_dotenv()
    
    id = os.environ.get('NAVER_ID')
    pw = os.environ.get('NAVER_PW')
    driver.get("https://nid.naver.com/nidlogin.login")
    driver.implicitly_wait(10)
    clipboard_user_input(driver, "id", id)
    clipboard_user_input(driver, "pw", pw)
    xpath = """//*[@id="log.login"]"""
    driver.find_element_by_xpath(xpath).click()
    time.sleep(5)


def clipboard_user_input(driver, class_id, user_input):
    pyperclip.copy(user_input)
    driver.find_element_by_id(class_id).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(1)


def clipboard_productData_input(driver, xpath, productData_input):
    pyperclip.copy(productData_input)
    # driver.find_element_by_xpath(xpath).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()
    ActionChains(driver).key_down(Keys.CONTROL).send_keys("v").key_up(
        Keys.CONTROL
    ).perform()
    time.sleep(1)


def element_click(driver, xpath):
    # driver.find_element_by_xpath(xpath).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    ).click()
    time.sleep(1)


def createProduct(driver, productInfo):
    driver.get("https://sell.smartstore.naver.com/#/products/create")
    driver.implicitly_wait(10)

    # setting category
    ##################
    category = productInfo["category"].split(" ")
    ##################
    category_search_xpath = """//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[1]/div[1]/div/label[2]"""
    element_click(driver, category_search_xpath)
    driver.implicitly_wait(5)
    if len(category) == 4:
        # 대분류 클릭
        data_group_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul'
        )
        data_group_li_list = data_group_ul.find_elements_by_tag_name("li")
        for data_group_li in data_group_li_list:
            if category[0] == data_group_li.text:
                data_group_li.click()
                time.sleep(1)

        # 중분류 클릭
        data_group_level1_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul'
        )
        data_group_level1_li_list = data_group_level1_ul.find_elements_by_tag_name("li")
        for data_group_level1_li in data_group_level1_li_list:
            if category[1] == data_group_level1_li.text:
                data_group_level1_li.click()
                time.sleep(1)

        # 소분류 클릭
        data_group_level2_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul'
        )
        data_group_level2_li_list = data_group_level2_ul.find_elements_by_tag_name("li")
        for data_group_level2_li in data_group_level2_li_list:
            print(f"category[2] : {category[2]}, data_group_level2_li.text : {data_group_level2_li.text}")
            if category[2] == data_group_level2_li.text:
                data_group_level2_li.click()
                time.sleep(1)

        # 세분류 클릭
        data_group_level3_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[4]/ul'
        )
        data_group_level3_li_list = data_group_level3_ul.find_elements_by_tag_name("li")
        for data_group_level3_li in data_group_level3_li_list:
            if category[3] == data_group_level3_li.text:
                data_group_level3_li.click()
                time.sleep(1)
    else:
        # 대분류 클릭
        data_group_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[1]/ul'
        )
        data_group_li_list = data_group_ul.find_elements_by_tag_name("li")
        for data_group_li in data_group_li_list:
            if category[0] == data_group_li.text:
                data_group_li.click()
                time.sleep(1)

        # 중분류 클릭
        data_group_level1_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[2]/ul'
        )
        data_group_level1_li_list = data_group_level1_ul.find_elements_by_tag_name("li")
        for data_group_level1_li in data_group_level1_li_list:
            if category[1] == data_group_level1_li.text:
                data_group_level1_li.click()
                time.sleep(1)   # time.sleep을 안하니깐 카테고리가 아니라 소분류가 담김 

        # 소분류 클릭
        data_group_level2_ul = driver.find_element_by_xpath(
            '//*[@id="productForm"]/ng-include/ui-view[3]/div/div[2]/div/div[1]/div/category-search/div[3]/div[3]/ul'
        )
        data_group_level2_li_list = data_group_level2_ul.find_elements_by_tag_name("li")
        print(f"data_group_level2_li_list : {data_group_level2_li_list}")
        for data_group_level2_li in data_group_level2_li_list:
            print(f"category[2] : {category[2]}, data_group_level2_li.text : {data_group_level2_li.text}")
            if category[2] == data_group_level2_li.text:
                data_group_level2_li.click()
                time.sleep(1)

    try:
        # 안전기준 팝업창 확인 버튼 클릭
        popup_btn = driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div[3]/div/button"
        )
        popup_btn.click()
    except:
        print(
            f"""{productInfo["productName"]}에서 안전기준 팝업창 확인 버튼 클릭하는 부분에서 TimeoutException 오류 발생!"""
        )

    # scroll Down
    driver.execute_script("window.scrollTo(0, 700)")
    driver.implicitly_wait(5)

    # setting productName
    ##################
    productName = productInfo["productName"]
    ##################
    productName_xpath = """//*[@id="productForm"]/ng-include/ui-view[7]/div/div[2]/div/div/div/div/div/div/input"""
    clipboard_productData_input(
        driver,
        productName_xpath,
        productName,
    )
    driver.implicitly_wait(5)

    # setting price
    ##################
    price = productInfo["price"]
    ##################
    price_xpath = """//*[@id="prd_price2"]"""
    clipboard_productData_input(
        driver,
        price_xpath,
        price,
    )
    driver.implicitly_wait(5)

    # scroll Down
    driver.execute_script("window.scrollTo(0, 1200)")
    driver.implicitly_wait(5)

    # setting stock
    stock = 999
    stock_xpath = """//*[@id="stock"]"""
    clipboard_productData_input(
        driver,
        stock_xpath,
        stock,
    )
    driver.implicitly_wait(5)

    # setting option
    ##################
    colors = productInfo["colors"]
    sizes = productInfo["sizes"]
    ##################

    try:
        option_active_btn_xpath = (
            """//*[@id="productForm"]/ng-include/ui-view[11]/div/div/div/div/a"""
        )
        element_click(driver, option_active_btn_xpath)

        # selective
        # selective_option_active_btn_xpath = """//*[@id="option_direct_type_true"]"""
        # element_click(driver, selective_option_active_btn_xpath)

        # direct_type
        direct_type_option_active_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[1]/div/div[2]/label[1]"""
        element_click(driver, direct_type_option_active_btn_xpath)

    except:
        print(
            f"""{productInfo["productName"]}에서 옵션 설정하는 부분에서 TimeoutException 오류 발생!"""
        )
    # option num select
    if len(colors) == 0:

        driver.implicitly_wait(5)
        driver.execute_script("window.scrollTo(0, 1800)")
        driver.implicitly_wait(5)

        # size option input
        size_option_xpath = """//*[@id="choice_option_name0"]"""
        clipboard_productData_input(
            driver,
            size_option_xpath,
            "size",
        )
        driver.implicitly_wait(5)

        size_option_value_xpath = """//*[@id="choice_option_value0"]"""
        size_cnt = 0

        if len(sizes) == 1:
            clipboard_productData_input(
                driver,
                size_option_value_xpath,
                sizes[0],
            )
            driver.implicitly_wait(5)
        else:
            for size in sizes:
                if size_cnt == 0:
                    clipboard_productData_input(
                        driver,
                        size_option_value_xpath,
                        f"{size},",
                    )
                    driver.implicitly_wait(5)
                    size_cnt += 1
                else:
                    clipboard_productData_input(
                        driver,
                        size_option_value_xpath,
                        size,
                    )
                    driver.implicitly_wait(5)
        # option 적용
        options_list_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/a"""
        element_click(driver, options_list_btn_xpath)
    else:
        option_num_active_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[1]"""
        element_click(driver, option_num_active_xpath)

        option_num_two_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div[2]/div/div/div/div/div[2]/div/div[2]"""
        element_click(driver, option_num_two_xpath)

        driver.implicitly_wait(5)
        driver.execute_script("window.scrollTo(0, 1600)")
        driver.implicitly_wait(5)

        # color option input
        color_option_xpath = """//*[@id="choice_option_name0"]"""
        clipboard_productData_input(
            driver,
            color_option_xpath,
            "color",
        )
        driver.implicitly_wait(5)

        color_option_value_xpath = """//*[@id="choice_option_value0"]"""
        color_cnt = 0
        if len(colors) == 1:
            clipboard_productData_input(
                driver,
                color_option_value_xpath,
                colors[0],
            )
            driver.implicitly_wait(5)
        else:
            for color in colors:
                if color_cnt < len(colors) - 1:
                    clipboard_productData_input(
                        driver,
                        color_option_value_xpath,
                        f"{color},",
                    )
                    driver.implicitly_wait(5)
                    color_cnt += 1
                else:
                    clipboard_productData_input(
                        driver,
                        color_option_value_xpath,
                        color,
                    )
                    driver.implicitly_wait(5)

        # size option input
        size_option_xpath = """//*[@id="choice_option_name1"]"""
        clipboard_productData_input(
            driver,
            size_option_xpath,
            "size",
        )
        driver.implicitly_wait(5)

        size_option_value_xpath = """//*[@id="choice_option_value1"]"""
        size_cnt = 0

        if len(sizes) == 1:
            clipboard_productData_input(
                driver,
                size_option_value_xpath,
                sizes[0],
            )
            driver.implicitly_wait(5)
        else:
            for size in sizes:
                if size_cnt < len(sizes) - 1:
                    clipboard_productData_input(
                        driver,
                        size_option_value_xpath,
                        f"{size},",
                    )
                    driver.implicitly_wait(5)
                    size_cnt += 1
                else:
                    clipboard_productData_input(
                        driver,
                        size_option_value_xpath,
                        size,
                    )
                    driver.implicitly_wait(5)
        # option 적용
        options_list_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[2]/div[4]/div/div/div[3]/div[1]/a"""
        element_click(driver, options_list_btn_xpath)

    option_stock_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[4]/div/div/input"""
    clipboard_productData_input(
        driver,
        option_stock_xpath,
        stock,
    )
    driver.implicitly_wait(5)

    option_all_checkbox_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[2]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/label/span"""
    element_click(driver, option_all_checkbox_btn_xpath)

    update_select_list_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[11]/div/fieldset/div/div/div[2]/div[3]/div[2]/div[1]/div[2]/div/div[7]/a"""
    element_click(driver, update_select_list_btn_xpath)

    # upload product Main Image
    ##################
    mainImageURL = (
        f"""C:\\ficelleSmartStore\\detailImage\\{productInfo["productName"]}"""
    )
    ##################
    driver.implicitly_wait(5)
    driver.execute_script("window.scrollTo(0, 2300)")
    driver.implicitly_wait(5)

    try:
        add_mainImage_btn_xpath = (
            """//*[@id="representImage"]/div/div[1]/div/ul/li/div/a"""
        )
        element_click(driver, add_mainImage_btn_xpath)

        upload_mainImage_btn_xpath = (
            """/html/body/div[1]/div/div/div[2]/div/button[1]"""
        )
        element_click(driver, upload_mainImage_btn_xpath)
        time.sleep(1)
        # open click
        pyautogui.moveTo(235, 730)
        pyautogui.click()
        time.sleep(2)

        # input mainImage
        pyperclip.copy(mainImageURL)
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(2)
        pyautogui.moveTo(230, 150)
        pyautogui.click()
        # success click
        pyautogui.press("enter")
        time.sleep(2)

        # upload product Detail Image
        driver.execute_script("window.scrollTo(0, 4000)")
        driver.implicitly_wait(5)
    except:
        print(
            f"""{productInfo["productName"]}에서 대표이미지 설정하는 부분에서 TimeoutException 오류 발생!"""
        )

    open_smartEditor_btn_xpath = """//*[@id="productForm"]/ng-include/ui-view[13]/div/div[2]/div/div/ncp-editor-form/div[1]/div/p[4]/button"""
    element_click(driver, open_smartEditor_btn_xpath)
    time.sleep(5)

    # detail Image upload

    # open templete click
    pyautogui.moveTo(1870, 175)
    pyautogui.click()
    time.sleep(5)

    # move to my templete click
    pyautogui.moveTo(1725, 290)
    pyautogui.click()
    time.sleep(5)

    # select first my templete click
    pyautogui.moveTo(1750, 375)
    pyautogui.click()
    time.sleep(5)

    # write sizeGuide
    pyautogui.moveTo(950, 655)
    pyautogui.click()
    pyperclip.copy(productInfo["sizeGuide"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)

    # wirte comment
    pyautogui.moveTo(950, 415)
    pyautogui.click()
    pyperclip.copy(productInfo["instruction"])
    pyautogui.hotkey("ctrl", "v")
    time.sleep(5)

    # add_detailImage_btn click
    pyautogui.scroll(-600)
    pyautogui.moveTo(930, 800)
    pyautogui.click()
    pyautogui.moveTo(25, 180)
    pyautogui.click()
    time.sleep(5)

    # upload_detailImage_btn click
    pyautogui.moveTo(870, 200)
    pyautogui.click()
    time.sleep(5)

    # input detailImage
    pyautogui.moveTo(240, 145)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.keyDown("ctrl")
    pyautogui.moveTo(240, 145)
    pyautogui.click()
    time.sleep(5)
    pyautogui.keyUp("ctrl")
    time.sleep(2)
    pyautogui.press("enter")
    time.sleep(15)

    # register_detailImage_btn click
    pyautogui.moveTo(1840, 130)
    pyautogui.click()
    time.sleep(5)

    # save
    save_btn_xpath = (
        """//*[@id="seller-content"]/ui-view/div[3]/div[2]/div[1]/button[3]"""
    )
    element_click(driver, save_btn_xpath)
    time.sleep(5)

    # product no attribute
    next_btn_xpath = """/html/body/div[1]/div/div/div[3]/div[1]/button[1]"""
    element_click(driver, next_btn_xpath)
    time.sleep(5)

    # product manage
    manage_product_btn_xpath = """/html/body/div[1]/div/div/div[2]/div/button[2]"""
    element_click(driver, manage_product_btn_xpath)

    time.sleep(10)


def __init__():
    
    productNameIndexList = reversed(getProductNameIndex.getProductNameIndex(1, 1))
    print(productNameIndexList)

    # 이미지 저장 // 경로에 Name과 같은 폴더가 있다면 이 과정을 뛰어 넘긴다가 for 문안에 추가되어야 함.
    #for productNameIndex in productNameIndexList:
    #    productImgURLList = getProductImage.getProductImgURLList(productNameIndex)
    #    getProductImage.saveProductImage(productNameIndex, productImgURLList)
    #print("ALL save complete!!!!")


    guide()
    chromeDriverPath = chromedriver_autoinstaller.install() 
    #print(chromeAutoInstall)  
    options = webdriver.ChromeOptions()
    # chrome에서 F11을 눌러 전체 화면으로 넓히는 옵션입니다.
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(chromeDriverPath, options=options)
    login(driver)

    # 업로드 작업
    for productNameIndex in productNameIndexList:
        productInfo = getProductInfo.getProductInfo(productNameIndex)
        print(productInfo)
        createProduct(driver, productInfo)
        print(f"""{productInfo["productName"]} 업로드 완료!""")
        time.sleep(1)
    print("모든 제품을 업로드 완료!")
    driver.close()


__init__()