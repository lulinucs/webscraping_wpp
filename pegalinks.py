from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

driver = webdriver.Chrome()

arquivo_isbns = open("isbns.txt","r")
isbn = arquivo_isbns.readlines()
linhas = len(isbn)
i=0

while i < linhas:
    try:
        driver.get("https://www.amazon.com.br/")
        driver.find_element(By.ID, "twotabsearchtextbox").send_keys(isbn[i] + Keys.ENTER)
        print('--- Procurando produto ---')
        print('--- Verificando se o produto está na Amazon ---')
        sleep(1)
        verifica = driver.find_element(By.CLASS_NAME, "a-size-medium-plus")
        if verifica.text == "PRECISA DE AJUDA?":
            print('Produto não cadastrado na Amazon. Pulando para o próximo item.')
            i += 1
        else:
            print('--- Item localizado ---')
            sleep(1)
            driver.find_element(By.CLASS_NAME, "a-link-normal").send_keys("webdriver" + Keys.ENTER)
            print('--- Entrando na página do produto ---')
            link = driver.current_url
            arquivo_urls = open("urls.txt", "a")
            arquivo_urls.write(link)
            arquivo_urls.write('\n')
            arquivo_urls.close()
            print('URL salva com sucesso: ')
            print(link)
            i += 1
    except:
        print('Algo deu errado :/ Vou tentar de novo')
    

driver.quit()