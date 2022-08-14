from selenium import webdriver
from selenium.webdriver import ChromeOptions


options = ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.set_window_size(1024, (768*2))
url = "https://codeby.net/"
driver.get(url)
driver.save_screenshot('ss.png')

driver.quit()


