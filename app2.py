from lib2to3.pgen2 import driver
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

driver = webdriver.chrome()


navegador = webdriver.Chrome(executable_path=r'./chromedriver.exe')

navegador.get("https://www.kabum.com.br/")

navegador.find_element
navegador.find_element('//*[@id="__next"]/div[1]/div/div/main/div/div/main/div/form/div[1]/div[1]/div/div[1]/input').send_keys("Felipe Patrocinio")
navegador.find_element('//*[@id="listing"]/div[3]/div/div[2]/div[1]/main/div[1]/div[2]/div[2]/button').click
navegador.find_element('//*[@id="__next"]/div[1]/div/div[2]/div/div/button[2]').click
