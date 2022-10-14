from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime

def get_driver():
  # Set options to make browsing easier
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches", ["enable-logging"])
  options.add_argument("disable-blink-features=AutomationControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("http://automated.pythonanywhere.com/login")
  return driver

def clean_text(text):
  clean = text.split(": ")[1]
  return clean

def create_file(values):
  fecha_hora = str(datetime.now())
  with open(fecha_hora + ".txt",'w') as f:
    f.write("values")

def timer():
  pass
  

def main():
  #Writing the user in the text field
  driver = get_driver()
  time.sleep(2)
  driver.find_element(by="id", value="id_username").send_keys("automated")
  #Writing the password in the text field
  time.sleep(2)
  driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + Keys.RETURN)
  driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

  time.sleep(2)
  element = driver.find_element(by="xpath",value="/html/body/div[1]/div/h1[2]")
  create_file(clean_text(element.text))

  return 
  
