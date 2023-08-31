from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas
import time
import os

cwd = os.getcwd()
directory = os.path.dirname(cwd)
parent = os.path.join(directory, "chromedriver")
dict = {}

def scrape(url, file, num_obs):

    def scroll_to_bottom(driver):
        old_position = 0
        new_position = None
        while new_position != old_position:
            old_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                    " window.pageYOffset : (document.documentElement ||"
                    " document.body.parentNode || document.body);"))
            time.sleep(1)
            driver.execute_script((
                    "var scrollingElement = (document.scrollingElement ||"
                    " document.body);scrollingElement.scrollTop ="
                    " scrollingElement.scrollHeight;"))
            new_position = driver.execute_script(
                    ("return (window.pageYOffset !== undefined) ?"
                    " window.pageYOffset : (document.documentElement ||"
                    " document.body.parentNode || document.body);"))

    # service = Service(executable_path=parent)
    # chrome_driver = webdriver.Chrome(service=service)
    chrome_driver = webdriver.Chrome()

    with chrome_driver as driver:

        driver.maximize_window()
        driver.get(url)
        time.sleep(3)
        scroll_to_bottom(driver)
        for i in range(1, 8):
            dict[i] = []

        rows = 0
        max_num = 0
        scraped_rows = driver.find_elements(By.XPATH, "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[2]/table/tbody")
        for row in scraped_rows:
            curr = (int) (len(row.text) / 70)
            max_num = max(curr, max_num)
        if num_obs is None:
            rows = max_num
        else:
            rows = (int) (min(num_obs, max_num))
        break_flag = False

        for row in range(1, rows):
            for col in range(1, 8):
                try: 
                    cell = driver.find_element(By.XPATH, "//*[@id='Col1-1-HistoricalDataTable-Proxy']/section/div[2]/table/tbody/tr["+str(row)+"]/td["+str(col)+"]")
                    dict[col].append(cell.text)
                except NoSuchElementException:
                    break_flag = True
                    break
            if break_flag:
                break

        min_num = rows + 1000
        for key in dict:
            min_num = min(len(dict[key]), min_num)
        for key in dict:
            while len(dict[key]) > min_num:
                dict[key].pop(-1)

        df = pandas.DataFrame.from_dict(dict)
        df.to_csv(os.path.join(directory, 'data', file))

    driver.quit()
