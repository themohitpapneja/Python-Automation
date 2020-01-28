from selenium import webdriver

driver=webdriver.Chrome()
driver.get('https://youtube.com')  ##this specifies that the website it willl go to is youtube

searchbox=driver.find_element_by_xpath('//*[@id="search"]')
searchbox.send_keys('FunFury Space')   ##Add the keywords you want to search

searchButton=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]/yt-icon')
searchButton.click()
