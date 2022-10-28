from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/lulifer/AppData/Local/Google/Chrome/User Data")
options.add_argument('--profile-directory=Profile 1')
driver = webdriver.Chrome(options=options)


#driver = webdriver.Chrome()

arquivo_links = open("links.txt","r")
links = arquivo_links.readlines()
linhas = len(links)
i=0

while i<linhas:
	try:
		driver.get(links[i])
		print('Abri a pagina da API')
		sleep(2)		
		element = driver.find_element(By.ID, 'action-button')
		element.send_keys(Keys.ENTER)
		print('Criquei no primeiro butao')
		sleep(2)
		element2 = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[2]/div/section/div/div/div/div[3]/div/div/h4[2]/a")
		element2.send_keys(Keys.ENTER)
		print('Criquei no segundo butao')
		print('Aguardando esta caralha carregar')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		element3 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button")
		element3.send_keys(Keys.ENTER)
		print('Aguardando a mensagem ser enviada.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		sleep(1)
		print('.')
		print('Mensagem '+str(i)+' enviada com sucessed Tudo sob tranquilo')
		i += 1
	except:
		print("Falhei miseravelmente.  Vamos tentar de novo")





#sleep(2)
#driver.find_element(By.LINK_TEXT, 'use WhatsApp Web').click()



#driver.find_element(By.CLASS_NAME, "a-size-medium-plus")

