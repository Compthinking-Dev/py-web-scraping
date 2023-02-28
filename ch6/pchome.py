from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


if __name__ == "__main__":
    url = "https://24h.pchome.com.tw/"
    try:
        options = Options()
        # options.add_argument('--headless')
        options.add_argument("--deny-permission-prompts")  # 拒絕瀏覽器偵測你的位置
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(30)
        driver.get(url)

        # 定位搜尋欄, 輸入搜尋字串, 點擊搜尋按鈕
        element = driver.find_element(By.XPATH, "//input[@placeholder='輸入你想找的商品']")
        element.send_keys("空氣清淨機")
        element = driver.find_element(By.CLASS_NAME, "l-header__siteSearchBtn")
        element.click()

        # 等待目標按鈕出現之後再點選
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'dyson')]"))
        )
        element = driver.find_element(By.XPATH, "//a[contains(text(), 'dyson')]")
        element.click()

        # 等待目標網頁讀取完成
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "actived"))
        )

        # .page_source 可以回傳目前瀏覽器所看到的網頁文件
        soup = BeautifulSoup(driver.page_source, "html.parser")
        div = soup.find(id="ItemContainer")
        for dl in div.find_all("dl"):
            print([s for s in dl.stripped_strings])
    finally:
        driver.quit()  # 關閉瀏覽器, 結束 webdriver process
