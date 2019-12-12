from selenium import webdriver
import urllib.request

driver = webdriver.Chrome('./chromedriver')
# ChromeDriver 78.0.3904.105
# if this version is not correct to your computer,
# go to "https://sites.google.com/a/chromium.org/chromedriver/downloads" and download fit version driver.

driver.implicitly_wait(3)

driver.get('https://map.naver.com/v5/search?c=14127360.5901760,4512069.3447284,19,0,0,3,dh')

for num in range(1,17):
    img = driver.find_element_by_xpath("//*[@id='baseMap']/div/div[1]/div[13]/div/div/img[" + str(num) + "]")
    print(img)

src = img.get_attribute('src')
urllib.request.urlretrieve(src, "captcha" + str(num) + ".png")


driver.close()