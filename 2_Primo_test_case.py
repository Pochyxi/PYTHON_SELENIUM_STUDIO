# ###### IMPORTS ######

# importare webdriver da selenium
from selenium import webdriver

# specifichiamo il browser che vogliamo aprire
from webdriver_manager.chrome import ChromeDriverManager

# servirà per sa selezione dei web element
from selenium.webdriver.common.by import By

# servono per digitare gli input da tastiera
from selenium.webdriver import ActionChains, Keys

# utile per il FluentWait
from selenium.webdriver.support import expected_conditions as EC

# utile per il FluentWait
from selenium.webdriver.support.wait import WebDriverWait

# le eccezioni che lancia selenium se non trova uhn elemento
from selenium.common import ElementNotVisibleException, ElementNotSelectableException

# per fermare l'esecuzione del programma per un determinato periodo
import time

# ####### CODICE #########

# questa dichiarazione aprirà il browser
driver = webdriver.Chrome(ChromeDriverManager().install())

# .get(url) ci porterà alla pagina desiderata
driver.get("https://github.com/")

selettore_classe = ".form-control.js-site-search-focus.header-search-input"
selettore_attributi = "input[class = 'form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field']"

# SELEZIONARE UN ELEMENTO WEB
tasto_di_ricerca = driver.find_element(By.CSS_SELECTOR, selettore_attributi)
print(tasto_di_ricerca)
tasto_di_ricerca.click()
tasto_di_ricerca.send_keys("pochyxi")

# DIGITARE INPUT DA TASTIERA
ActionChains(driver) \
    .key_down(Keys.ENTER) \
    .key_up(Keys.ENTER) \
    .perform()

# Titolo della pagina in cui ci troviamo attualmente
titolo_pagina = driver.title
print(titolo_pagina)

# La stringa che ci aspettiamo dal titolo pagina
exp_title = 'Search · pochyxi · GitHub'

# condizione per cui se il titolo è corretto il test è passato
if exp_title == titolo_pagina:
    print("Test di ricerca passato")

users = driver.find_element(By.CSS_SELECTOR, "a[ href = '/search?q=pochyxi&type=users' ]")
users.click()

# Delle volte può succedere che un elemento non sia disponibile per qualche secondo
# anche dopo il completo caricamento del componente, questa potrebbe essere una soluziole per non
# far lanciare un errore ed il blocco dell'esecuzione
# la flag impostata su True e messa come condizione del while, non farà altro che iniziare un loop infinito
# fino a quando l'elemento non sarà trovato, nel momento in cui viene trovato provviadiamo a rendere la flag falsa
# così da permetterci di uscire immediatamente dal loop e proseguire con l'esecuzione

# nome_utente_flag = True
# while nome_utente_flag:
#     try:
#         nome_utente = driver.find_element(By.CSS_SELECTOR, "a[href=\"/Pochyxi\"]")
#         nome_utente_flag = False
#         nome_utente.click()
#     except:
#         print("elemento non trovato")

# Un'altra soluzione ci viene fornita da Selenium con il FluentWait, il quale aspetterà il renderizzamento
# dell'elemento per un massimo di tot secondi (timeout=10) e controllerà la sua presenza ogni tot secondi
# (poll_frequency=1) inoltre ignorerà tutte le eccezioni lanciate dalla non presenza dell'elemento

wait = WebDriverWait(
    driver,
    timeout=10,
    poll_frequency=1,
    ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]
)

nome_utente = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href=\"/Pochyxi\"]")))

nome_utente.click()


repositories_pochyxi = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href=\"/Pochyxi?tab=repositories\"]")))
repositories_pochyxi.click()


reposiry_PYTHON_SELENIUM_STUDIO = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href=\"/Pochyxi/PYTHON_SELENIUM_STUDIO\"]")))
reposiry_PYTHON_SELENIUM_STUDIO.click()


time.sleep(10)

# .close() serve a chiudere il browser una volta effettuate tutte le automazioni desiderate
driver.close()
