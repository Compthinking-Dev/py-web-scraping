from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":
    url = "https://wwwap.bot.com.tw/house/"
    try:
        options = Options()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.get(url)

        # 定位日期輸入欄位, 並輸入日期
        element = driver.find_element(By.ID, "fromdate_TextBox")
        element.send_keys("1090101")
        element = driver.find_element(By.ID, "todate_TextBox")
        element.send_keys("1120101")

        # 定位選單所在欄位並點擊
        element = driver.find_element(By.ID, "PageCount_DDL")
        element.click()
        # 巡覽選單, 點擊對應選項
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "100":
                option.click()
                break

        # 點擊送出按鈕
        element = driver.find_element(By.ID, "Submit_Button").click()

        # 等待目標表格出現
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "House_GridView"))
        )

        # .page_source 可以回傳目前瀏覽器所看到的網頁文件
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find(id="House_GridView")
        for row in table.find_all("tr"):
            print([s for s in row.stripped_strings])
    finally:
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process
