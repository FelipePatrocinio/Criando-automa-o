from ast import Str
import selenium 
import time 
import webdriver_manager 
from selenium.webdriver.common.keys import Keys 
from selenium import webdriver 
from webdriver_manager.chrome import ChromeDriverManager 
driver = webdriver.Chrome(ChromeDriverManager().install()) 
  
driver.get('https://minhaconta.ongame.net/entrar/?site=ongame&url=https://br.ongame.net/')
Str = driver.find_element(