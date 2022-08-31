from selenium import webdriver
PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)

driver.get('https://techclout.web.app')
print(driver.title)
# driver.close()






print('automation done!!!')