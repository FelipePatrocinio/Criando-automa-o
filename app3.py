from asyncio.streams import _ClientConnectedCallback
from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')
driver.get('https://www.kabum.com.br')
driver.find_element('xpath', '//*[@id="input-busca"]').send_keys('computador')
driver.find_element('//*[@id="barraBuscaKabum"]/div/form/button/svg').click

quit.chrome