from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

def gmail_login(driver, username, password):

    driver.get("https://accounts.google.com/")

    # username login in
    driver.find_element_by_name("identifier").send_keys(username)
    driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button').click()

    time.sleep(5)

    # password login in
    driver.find_element_by_name("password").send_keys(password)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button').click()

def daily_search(driver, email_search):

    # advance_search = driver.find_element_by_xpath('//*[@id="aso_search_form_anchor"]/button[2]').click()
    
    time.sleep(5)

    driver.get('https://mail.google.com/mail/?ui=html')

    time.sleep(2)

    email_search_input = "from:(" + email_search + ")"
    search_box = driver.find_element_by_name("q")
    search_box.send_keys(email_search_input)

    time.sleep(2)
    
    search_box.find_element_by_xpath('/html/body/table[1]/tbody/tr[2]/td/table/tbody/tr/td[1]/input[2]').click()

    time.sleep(2)

    # email_search_xpath = "//span[@email='" + email_search + "']/ancestor::tr[@role='row']"
    
    driver.find_element_by_xpath('/html/body/table[2]/tbody/tr/td[2]/table[1]/tbody/tr/td[2]/form/table[2]/tbody/tr[1]/td[3]/a/span').click()

    time.sleep(2)

    return driver.find_element_by_tag_name('blockquote')



def previous_content():

    time.sleep(5)

    driver.get('https://mail.google.com/mail/u/0?ui=2&ik=68b42d0d8f&view=lg&permmsgid=msg-f:1702363908765375221')

    previous_mail_content = driver.find_elements_by_tag_name('blockquote')

    return previous_mail_content


def stock_info(ticker):

    url = 'https://finance.yahoo.com/quote/' + ticker

    html = requests.get(url)

    return html
    
def holding_csv(driver, fund = ['all']):
    
    url_dict = {
        'arkk': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv',
        'arkq': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_AUTONOMOUS_TECHNOLOGY_&_ROBOTICS_ETF_ARKQ_HOLDINGS.csv',
        'arkw': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_NEXT_GENERATION_INTERNET_ETF_ARKW_HOLDINGS.csv',
        'arkg': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_GENOMIC_REVOLUTION_MULTISECTOR_ETF_ARKG_HOLDINGS.csv',
        'arkf': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_FINTECH_INNOVATION_ETF_ARKF_HOLDINGS.csv',
        'arkx': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_SPACE_EXPLORATION_&_INNOVATION_ETF_ARKX_HOLDINGS.csv',
        'prnt': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/THE_3D_PRINTING_ETF_PRNT_HOLDINGS.csv',
        'izrl': 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_ISRAEL_INNOVATIVE_TECHNOLOGY_ETF_IZRL_HOLDINGS.csv',
    }
    
    if 'all' in fund:
        for key in url_dict:
            driver.get(url_dict.get(key))
            time.sleep(2)
            print(key + " downloaded!")
    else:
        for key in fund:
            driver.get(url_dict.get(key))
            time.sleep(2)
            print(key + " downloaded!")
        
    

    

if __name__ == "__main__":
    username = "arketftracker8787"
    password = "fuckingstrongpassword8787!"
    email_search = "brian33090@gmail.com"
    data_list = []

    PATH = "/Users/brianlu/side-projects/ark-etf-website/chromedriver"
    d_path = '/Users/brianlu/side-projects/ark-etf-website/arketfdata/holdings'
    url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv'
    

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    prefs = {'download.default_directory' : d_path}
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(PATH, options = chrome_options)

    holding_csv(driver)





    # urllib.request.urlretrieve('https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv', '/Users/brianlu/side-projects/ark-etf-website/arketfdata/holdings/arkk_holding.csv')

    url = 'https://ark-funds.com/wp-content/fundsiteliterature/csv/ARK_INNOVATION_ETF_ARKK_HOLDINGS.csv'
    

    # gmail_login(driver, username, password)


    # daily_mail = daily_search(driver, email_search)

    # table = daily_mail.find_elements_by_tag_name('tr')

    # for rows in table:
    #     row = rows.find_elements_by_tag_name('td')
    #     if(row[1].text != "Fund"):
    #         for data in row:
    #             print(data.text)
        


    
