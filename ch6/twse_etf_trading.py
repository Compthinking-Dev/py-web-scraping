from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":
    url = "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html"
    try:
        options = Options()
        # options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.get(url)

        # 透過下拉式選單選擇年月日及 ETF 分類
        element = driver.find_element(By.XPATH, "//select[@name='yy']")
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "民國 111 年":
                option.click()
                break
        element = driver.find_element(By.XPATH, "//select[@name='mm']")
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "12月":
                option.click()
                break
        element = driver.find_element(By.XPATH, "//select[@name='dd']")
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "20日 (二)":
                option.click()
                break
        element = driver.find_element(By.XPATH, "//select[@name='type']")
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "ETF":
                option.click()
                break

        element = driver.find_element(By.LINK_TEXT, "查詢")
        element.click()

        # 等待目標選單出現之後再點選: 顯示全部資料
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='report-table1_length']"))
        )
        element = driver.find_element(By.XPATH, "//select[@name='report-table1_length']")
        element.click()
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.text == "全部":
                option.click()
                break

        # .page_source 可以回傳目前瀏覽器所看到的網頁文件
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table = soup.find(id="report-table1")
        for row in table.find_all("tr"):
            print([s for s in row.stripped_strings])
    finally:
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process
