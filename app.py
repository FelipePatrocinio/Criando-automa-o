from selenium import webdriver

driver = webdriver.Chrome(executable_path=r'./chromedriver.exe')


driver.get('https://mentorama.com.br/testqa')


driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[1]/div/input').send_keys('Felipe Patrocinio')
driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[6]/button').click()
driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[2]/div/input').send_keys('lipe_k08@hotmail.com')
driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[3]/div/div[1]/input[1]').send_keys('11982996735')
driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[4]/div/input').send_keys('1478963')
driver.find_element('xpath', '//*[@id="form478604375"]/div[2]/div[6]/button').click()
driver.get('https://minhaconta.ongame.net/entrar/?site=ongame&url=https://br.ongame.net/')
driver.find_element('xpath', '//*[@id="login-form"]/section[2]/a[2]').click()
driver.find_element('xpath', '//*[@id="register-form"]/div[1]/div/input').send_keys('Felipe Patrocinio')
driver.find_element('xpath', '//*[@id="register-form"]/div[2]/div/input').send_keys('1478963')
driver.find_element('xpath', '//*[@id="register-form"]/div[3]/div/input').send_keys('lipe_k08@hotmail.com')
driver.find_element('xpath', '//*[@id="register-form"]/div[4]/div/input').send_keys('lipe_k08@hotmail.com')
driver.find_element('xpath', '//*[@id="register-form"]/div[6]/label/input').click()
driver.find_element('xpath', '//*[@id="register-form"]/button').click()






