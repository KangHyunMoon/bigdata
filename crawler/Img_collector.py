
from selenium import webdriver
import urllib.request

global_scale = 18
# map scale

global_axis_min_x = 14132249.5741648
global_axis_min_y = 4481053.3036544
# 수원 왕송호수

global_axis_max_x = 14148750.1190637
global_axis_max_y = 4462518.5186238
# 동탄 호수


def craw(min_x, min_y, max_x, max_y, style, scale):

    range_x = max_x - min_x
    range_y = max_y - min_y


    base_url = "https://map.pstatic.net/nrb/styles/"

    for i in range(range_y):
        for j in range(range_x):
            url = base_url + style + "/1574408195/" + str(scale+1) + "/" + str(min_x + j) + "/" + str(min_y + i) + ".png?mt=bg"

            print(url)

            urllib.request.urlretrieve(url, "./img/" + str(i) + "_" + str(j) + '.png')


def getImgSpot(axis_x, axis_y, scale):
    driver = webdriver.Chrome('./chromedriver/chromedriver')

    driver.implicitly_wait(3)

    driver.get('https://map.naver.com/v5/search?c=' + str(axis_x) + "," + str(axis_y) + ',' + str(scale) + ',0,0,3,dh')

    img = driver.find_element_by_xpath("//*[@id='baseMap']/div/div[1]/div[13]/div/div/img[1]")
    src = img.get_attribute('src')

    splt_str = str(src).split("/")

    spot_x = splt_str[8]
    spot_y = splt_str[9].split(".")[0]

    driver.close()

    return spot_x, spot_y


def _main_():
    min_x, min_y = getImgSpot(axis_x=global_axis_min_x, axis_y=global_axis_min_y, scale=global_scale)
    # 수원 왕송호수 아래쪽
    print(min_x, min_y)

    max_x, max_y = getImgSpot(axis_x=global_axis_max_x, axis_y=global_axis_max_y, scale=global_scale)
    # 동탄 호수공원 아래쪽
    print(max_x, max_y)

    craw(min_x = int(min_x), min_y = int(min_y), max_x = int(max_x), max_y = int(max_y), style = "satellite", scale = global_scale)
    # 위성사진

    craw(min_x=int(min_x), min_y=int(min_y), max_x=int(max_x), max_y=int(max_y), style="basic", scale=global_scale)
    # 기본사진


_main_()
