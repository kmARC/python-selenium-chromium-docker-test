from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

def main():
    opts = Options()
    opts.binary_location = "/usr/bin/chromium-browser"
    opts.add_argument('headless')
    opts.add_argument('no-sandbox')
    driver = webdriver.Chrome(chrome_options=opts)

    driver.get('https://google.com')
    driver.find_element_by_name('q').send_keys('selenium')
    driver.find_element_by_name('q').send_keys(Keys.ENTER)
    print(driver.find_element_by_id('resultStats').text)

if __name__ == '__main__':
    main()
