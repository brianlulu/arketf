from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def gmail_login(driver, username, password):

    driver.get("https://accounts.google.com/")

    # username login in
    driver.find_element_by_name("identifier").send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

    time.sleep(5)

    # password login in
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

def search(driver, mail_search_key):

    driver.get('https://mail.google.com/')
    
    time.sleep(5)

    search_box = driver.find_element_by_id("mail-search")
    search_box.find_element_by_tag_name("input").send_keys(mail_search_key)

    time.sleep(5)
    
    search_box.find_element_by_xpath('//*[@id="mail-search"]/div/button').click()

    time.sleep(5)



if __name__ == "__main__":
    username = "arketftracker8787"
    password = "fuckingstrongpassword8787!"
    mail_search_key = "from:ark@ark-funds.com"
    data_list = []

    PATH = "/Users/brianlu/side-projects/ark-etf-website/chromedriver"

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(PATH, chrome_options = chrome_options)

    gmail_login(driver, username, password)

    
    time.sleep(5)

    driver.get('https://mail.google.com/mail/u/0?ui=2&ik=68b42d0d8f&view=lg&permmsgid=msg-f:1702363908765375221')

    previous_mail_content = driver.find_elements_by_tag_name('blockquote')

    for content in previous_mail_content:
        table = content.find_elements_by_tag_name('td')
        data_list.append(table)
    

    # search(driver, mail_search_key)

    # mail_list_box = driver.find_element_by_xpath('//*[@id="mail-app-component"]/div[1]/div/div[3]/div/div[1]')
    # print(mail_list_box)

    # driver.quit()

    
    
# //*[@id="mail-app-component"]/div[1]/div/div[3]/div/div[1]/div[3]/div/div[1]/ul/li[17]/a