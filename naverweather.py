# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 01:34:13 2019

@author: 융
"""
'''
맑음:icon_2013_01/01.png-----------------------1
구름에 쪼금가려진해:icon_2013_01/02.png------2
구름/해:icon_2013_01/18.png--------------------3
구름에가려진해/비안옴:icon_2013_01/21.png----4
구름:icon_2013_01/03.png-----------------------6
구름에 가려진해/비조금:icon_2013_01/13.png---7
구름에 가려진해&비옴:icon_2013_01/07.png----8
비:icon_2013_01/04.png-------------------------10
'''
from selenium import webdriver

DRIVER_DIR ='C:/Users/pc/Downloads/chromedriver'
driver=webdriver.Chrome(DRIVER_DIR)
url="http://www.weatheri.co.kr/forecast/forecast01.php?rid=0201010202&k=1&a_name=%EA%B3%BC%EC%B2%9C"
driver.get(url)
driver.implicitly_wait(5) 

img_path={
        'http://www.weatheri.co.kr/images/icon_2013_01/01.png':1,
        'http://www.weatheri.co.kr/images/icon_2013_01/02.png':2,
        'http://www.weatheri.co.kr/images/icon_2013_01/18.png':3,
        'http://www.weatheri.co.kr/images/icon_2013_01/21.png':4,
        'http://www.weatheri.co.kr/images/icon_2013_01/03.png':6,
        'http://www.weatheri.co.kr/images/icon_2013_01/13.png':7,
        'http://www.weatheri.co.kr/images/icon_2013_01/07.png':8,
        'http://www.weatheri.co.kr/images/icon_2013_01/04.png':10
        }

day1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[1]/b")
rain1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/font")
cloud1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/img")
temp_max1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/font")
temp_min1=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud1.get_attribute('src')
cl1=img_path[cloud]
print(day1.text,rain1.text,cl1,temp_max1.text,temp_min1.text)


day2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[2]/b")
rain2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")
cloud2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[1]/img")
temp_max2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/font")
temp_min2=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud2.get_attribute('src')
cl2=img_path[cloud]
print(day2.text,rain2.text,cl2,temp_max2.text,temp_min2.text)

day3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[3]/b")
rain3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]/font")
cloud3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/img")
temp_max3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/font")
temp_min3=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud3.get_attribute('src')
cl3=img_path[cloud]
print(day3.text,rain3.text,cl3,temp_max3.text,temp_min3.text)

day4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[4]/b")
rain4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td[2]/font")
cloud4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[1]/img")
temp_max4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/font")
temp_min4=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud4.get_attribute('src')
cl4=img_path[cloud]
print(day4.text,rain4.text,cl4,temp_max4.text,temp_min4.text)

day5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[1]/td[5]/b")
rain5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[2]/font")
cloud5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[1]/img")
temp_max5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/font")
temp_min5=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[2]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud5.get_attribute('src')
cl5=img_path[cloud]
print(day5.text,rain5.text,cl5,temp_max5.text,temp_min5.text)

day6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[1]/b")
rain6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[4]/td[2]/font")
cloud6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[1]/img")
temp_max6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/font")
temp_min6=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[1]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud6.get_attribute('src')
cl6=img_path[cloud]
print(day6.text,rain6.text,cl6,temp_max6.text,temp_min6.text)

day7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[2]/b")
rain7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[2]/font")
cloud7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[1]/img")
temp_max7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/font")
temp_min7=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud7.get_attribute('src')
cl7=img_path[cloud]
print(day7.text,rain7.text,cl7,temp_max7.text,temp_min7.text)

day8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[3]/b")
rain8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[4]/td[2]/font")
cloud8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[1]/img")
temp_max8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/font")
temp_min8=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[3]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud8.get_attribute('src')
cl8=img_path[cloud]
print(day8.text,rain8.text,cl8,temp_max8.text,temp_min8.text)

day9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[4]/b")
rain9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[4]/td[2]/font")
cloud9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[1]/img")
temp_max9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/font")
temp_min9=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[4]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud9.get_attribute('src')
cl9=img_path[cloud]
print(day9.text,rain9.text,cl9,temp_max9.text,temp_min9.text)

day10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[1]/td[5]/b")
rain10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[4]/td[2]/font")
cloud10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[1]/img")
temp_max10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/font")
temp_min10=driver.find_element_by_xpath("/html/body/table[2]/tbody/tr[3]/td[2]/table/tbody/tr[3]/td/table/tbody/tr[3]/td/table[8]/tbody/tr[2]/td[5]/table/tbody/tr[2]/td[2]/b/b/font")
cloud=cloud10.get_attribute('src')
cl10=img_path[cloud]
print(day10.text,rain10.text,cl10,temp_max10.text,temp_min10.text)

driver.close()
