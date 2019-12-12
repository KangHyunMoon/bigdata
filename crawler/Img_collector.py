from selenium import webdriver
import urllib.request

driver = webdriver.Chrome('/Users/beomi/Downloads/chromedriver')

def craw(style,scale):

    base_url = "https://map.pstatic.net/nrb/styles/"

    url = base_url + style + "/1574408195/" + scale + "/447031"

    url = "https://map.pstatic.net/nrb/styles/satellite/1574408195/19/447031/203519.png?mt=bg.ol.sw"
    urllib.request.urlretrieve(url, "./"+'1' + '.png')


# craw(1,1)
