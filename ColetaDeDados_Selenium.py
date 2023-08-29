from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 2)


def collectData():
    sites = ('ouro-hoje','petroleo-hoje', 'soja-hoje', 'milho-hoje')

    for i in sites:
        driver.get(f'https://www.melhorcambio.com/{i}')
        search = '//*[@id="comercial"]'
        value_element = driver.find_element(By.XPATH, search)
        value = value_element.get_attribute('value')
        print(value)


collectData()
teste = input('Digite algo para sair:')
if teste:
    driver.quit()
    