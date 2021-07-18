from selenium import webdriver
import time
path = 'chromedriver.exe'
driver = webdriver.Chrome(path)
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath('//*[@id="email"]').send_keys("guanhanchen6@gmail.com")
driver.find_element_by_xpath('//*[@id="pass"]').send_keys("a22078758")

driver.find_element_by_xpath('//*[@id="u_0_d_Sc"]').click()

time.sleep(3)
driver.close()
driver.quit()


