import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from datetime import datetime
import pandas as pd

# 파일 실행 전 로컬환경에 맞게 변경하세요.
## Chromedriver의 path
driver_path = "/usr/local/bin/chromedriver" 
## submit csv 파일의 경로
submit_list_path = "/Users/anhju/공모전/MAICON/제출 자동화 프로그램/submit_list.csv"
## 제출할 파일들의 디렉토리
base_path = "/Users/anhju/공모전/MAICON/제출 자동화 프로그램/"
## 로그인 id/pw
uid = ""
upw = ""

# 파일을 실제로 제출하려면 ##submit button부분의 주석을 해제하세요.
def submit_file(file_name, file_desc):
    driver = webdriver.Chrome(driver_path)
    driver.get("https://aiconnect.kr/competition/detail/213/task/250/taskInfo")
    driver.find_element(By.CLASS_NAME, 'task_header-btn').click()

    ## naver social login
    driver.find_element(By.CLASS_NAME, 'naver-btn').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="id"]').send_keys(uid)
    driver.find_element(By.XPATH, '//*[@id="pw"]').send_keys(upw)
    driver.find_element(By.XPATH, '//*[@id="log.login"]').click()

    ## email login
    # driver.find_element(By.ID, 'input-30').send_keys(uid)
    # password = driver.find_element(By.ID, 'input-31')
    # password.send_keys(upw)
    # password.send_keys(Keys.RETURN)

    ## upload file
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '#app > div > aside > section > article > ul:nth-child(6) > li:nth-child(3)').click()

    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#input-78').send_keys(base_path+file_name)
    driver.find_element(By.CSS_SELECTOR, '#textarea-no-resize').send_keys(file_desc)

    ## submit button
    # time.sleep(1)
    # driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/section[1]/article[2]/div/div[5]/button').click()

    time.sleep(2)

if __name__ == "__main__":
    S_HOUR = 3610

    while(1):
        s_df = pd.read_csv(submit_list_path)
        if s_df.empty:
            print("!! All files have been submitted Successfully. !!")
            break
        name = s_df.file_name[0]
        desc = s_df.description[0]
        submit_file(name,desc)
        print("==========================================")
        print("Submit file: ", name)
        print("Description: ", desc)
        print("Submit Time: ", datetime.now())
        print("==========================================")

        s_df.drop(index=0, axis=0, inplace=True)
        s_df.to_csv(submit_list_path, index=False)
        time.sleep(S_HOUR)