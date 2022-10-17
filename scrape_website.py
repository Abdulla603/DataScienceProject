import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import pandas as pd

driver_path = os.path.dirname(os.path.realpath("chromedriver.exe") + "\chromedriver.exe")
# brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
# option = webdriver.ChromeOptions()
# option.binary_location = brave_path
# website = "https://www.fotmob.com/leagues/77/stats/season/9731/players/rating"
# browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)

# player_data = pd.DataFrame()


# browser.get(website)
# ddelement = Select(browser.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div[2]/div/section/div/div[2]/div/select"))
# ddelement.select_by_value("rating")
# time.sleep(4)
# soup = BeautifulSoup(browser.page_source, "html.parser")
# soup = soup.prettify()
# print(soup)

ratings_url = "https://www.fotmob.com/leagues/77/stats/season/9731/players/rating"

driver = webdriver.Chrome(driver_path)
driver.get(ratings_url)
page = BeautifulSoup(driver.page_source, 'html.parser')
PlayersList = []
ValuesList = []

for loop in range(0,23):
  Players = page.find_all("a", {"class": "css-r1t9bp-StyledLink-applyHover e1fvh723"})
  Values = page.find_all("td", {"class": "MuiTableCell-root MuiTableCell-body jss7 jss9 jss11 css-1la9ly1-TableCell e1fvh724"})
  for pl, val in zip(Players, Values):
    PlayersList.append(pl.text)
    ValuesList.append(val.text)
  if loop==23:
      break
  else:
   WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='MuiButtonBase-root MuiIconButton-root jss17 jss19']"))).click()

df = pd.DataFrame({"Players":PlayersList,"Values":ValuesList})
