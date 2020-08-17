from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def get_image(a, b):
    url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=" + quote_plus(a)
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    data = bs.findAll('div', {'class': 'img_area'})
    data2 = data[int(b)-1].find('img', {'class': '_img'})
    return data2.get('data-source')


def get_location_ko(wea):
    url = 'https://search.naver.com/search.naver?query=' + quote_plus(wea + ' 날씨')
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")
    data1 = bs.find('div', {'class': 'weather_box'})
    data2 = data1.findAll('dd')
    find_text = data1.find('p', {'class': 'cast_txt'}).text
    fin_t = find_text.split(",")
    find_currenttemp = data1.find('span', {'class': 'todaytemp'}).text
    find_dust = data2[0].find('span', {'class': 'num'}).text
    find_ultra_dust = data2[1].find('span', {'class': 'num'}).text
    res = "현재 " + wea + "날씨는 " + fin_t[0] + ", 온도는 " + find_currenttemp + "도, 미세먼지는 " + find_dust + ", 초미세먼지는 " + find_ultra_dust + " 입니다."
    return res
