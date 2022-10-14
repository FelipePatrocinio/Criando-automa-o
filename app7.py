from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://minhaconta.ongame.net/entrar/?site=ongame&url=https://br.ongame.net/")

titulo_classe = driver.find_element('by.classe', 'd-block font-13').click

