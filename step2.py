from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

def searchMountain(county,rain):
    driver = webdriver.Chrome('./chromedriver')
    findpage = driver.get("https://www.cwb.gov.tw/V8/C/L/Mountain/Mountain.html")

    n = 1
    mountain_lst=[]
    weather_dict={}
    check_lst=[]
    while True:
        location = driver.find_element_by_id('CountySelect')
        s1 = Select(location)
        s1.select_by_visible_text(county)
        mountain = driver.find_element_by_id('PID')
        s2 = Select(mountain)
        num = len(s2.options)-1
        if n<=num:
            search = s2.options[n].text
            s2.select_by_visible_text(search)
            start_search = driver.find_element_by_class_name("area_search_btn-v9")
            start_search.click()
            soup = BeautifulSoup(driver.page_source,"html.parser")

            soup = soup.find("div",{"class":"col-md-12 margin-bottom-50 hidden-xs hidden-sm"},{"id":"PC_hr"})
            temperature = soup.find("span",{"class":"tem-C is-active"},{"id":"GT_C_T"})
            temp = temperature.text
            chanceofrain = soup.find("tr",{"class":"rain_wrap hidden-xs hidden-sm"})
            for chance in chanceofrain.findAll("td",{"colspan":"2"})[:3]:
                answer = chance.text.replace("%","")
                answer = int(answer)
                check_lst.append(answer)
            check_lst.sort(reverse=True)
            if check_lst[0]<=rain:
                mountain_lst.append(search)
                weather_dict[search] = temp
            n+=1
            check_lst=[]
        elif n>num:
            break
    driver.close()
    return weather_dict