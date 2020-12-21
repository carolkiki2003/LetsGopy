import os
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

def searchArticle(mountain):
    my_options = Options()
    my_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    my_options.add_argument("--headless")
    my_options.add_argument("--disable-dev-shm-usage")
    my_options.add_argument("--no-sandbox")
    # path = "./chromedriver"
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options = my_options)
    driver.get("https://hiking.biji.co/index.php?q=review")
    url = "https://hiking.biji.co/index.php?q=review"

    article_result=[]

    if mountain == "豬窟尖山":
        mountain = "豬窟尖" or "豬窟"
    elif mountain == "石尖山":
        mountain = "二格山"
    elif mountain == "馬望曾呂山":
        mountain = "馬望僧侶山"
    elif mountain == "能高山主峰" or "能高山南峰" or "能高北峰":
        mountain = "能高"
        # print("提醒您！能高山有主峰、南峰、北峰（以下僅呈現所有能高山資訊")
    elif mountain == "馬望來山":
        mountain = "巴博庫魯山"

    ##這裡要串我們爬出的山
    search_input = driver.find_element_by_id("keyword_input")
    search_input.send_keys(mountain)
    search_input.submit()
    sleep(2)
    ##改變網址
    my_params = {"keyword":mountain}
    re = requests.get(url, params = my_params)
    soup = BeautifulSoup(re.text,"html.parser")
    ##爬標題 and 超連結 and 該文章封面圖片
    info = driver.find_elements_by_class_name("title")
    html = soup.findAll("div", {"class":"primary-wrap"})
    if len(info)<=1:
        # print("沒有可搜尋到的遊記")
        article_result.append("沒有可搜尋到的遊記")
    elif len(info)<=5:
        for i in range(len(info)-1):
            name = info[i].text
            link = "https://hiking.biji.co" + html[i].find("a")["href"]
            cover_link = html[i].find("div", {"class":"thumbnail img-cover lozad"})["data-background-image"]
            num = i+1
            article={"name":name,"link":link,"img":cover_link}
            article_result.append(article)
    else:
        for i in range(5):
            name = info[i].text  
            link = "https://hiking.biji.co" + html[i].find("a")["href"]
            cover_link = html[i].find("div", {"class":"thumbnail img-cover lozad"})["data-background-image"]
            num = i+1
            article={"name":name,"link":link,"img":cover_link}
            article_result.append(article)

    # print("以下是照片")
    # 爬相簿
    #driver.get("https://hiking.biji.co/index.php?q=album")
    #url2 = "https://hiking.biji.co/index.php?q=album"
    # 爬我們要去的山
    #search_input = driver.find_element_by_id("keyword_input")
    #search_input.send_keys(mountain)
    #search_input.submit()
    #sleep(2)
    #改變網址
    #my_params2 = {"act":"search", "keyword":mountain}
    #re2 = requests.get(url2, params = my_params2)
    #soup2 = BeautifulSoup(re2.text, "html.parser")
    # import os
    # 找相片五張
    # photos = soup2.findAll("div", {"class":"inner-img lozad"})
    # num = 1
    # if len(photos)==0:
    #     print("")
    # elif len(photos)<=5:
    #     for photo in photos:
    #         photo_url = photo["data-background-image"]
    #         print (f"{mountain}_{num}", photo_url, sep = "\n")
    #         num += 1
    # else:
    #     for photo in photos[:5]:
    #         photo_url = photo["data-background-image"]
    #         print (f"{mountain}_{num}", photo_url, sep = "\n")
    #         num += 1
    return article_result
