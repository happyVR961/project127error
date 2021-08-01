from bs4 import BeautifulSoup
from selenium import webdriver
import time 
import csv
startUrl = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser = webdriver.Chrome("/Users/sumit/Downloads/chromedriver_win32/chromedriver")
browser.get(startUrl)
time.sleep(10)
def scrapeData():
    headers = ["Name", "Distance", "Mass", "Radius"]
    stars_data = []
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr in soup.find_all("tr"):
        tempList = []
        td_tags = tr.find_all("td")
        for index, td_tag in enumerate(td_tags):
            if (index== 0):
                tempList.append(td_tag.find_all("a")[0])
            else:
                try:
                    tempList.append(td_tag.contents[0])
                except:
                    tempList.append("")
            stars_data.append(tempList)
    with open("happy.csv", "w") as f:
        csvWriter = csv.writer(f)
        csvWriter.writerow(headers)
        csvWriter.writerows(stars_data)
scrapeData()



    