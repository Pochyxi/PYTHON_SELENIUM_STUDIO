# importare webdriver da selenium
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys

# servirà per sa selezione dei web element
from selenium.webdriver.common.by import By

# specifichiamo il browser che vogliamo aprire
from webdriver_manager.chrome import ChromeDriverManager

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

nome_utente_flag = True
while nome_utente_flag:
    try:
        nome_utente = driver.find_element(By.CSS_SELECTOR, "a[href=\"/Pochyxi\"]")
        nome_utente_flag = False
        nome_utente.click()
    except:
        print("elemento non trovato")

repositories_pochyxi = driver.find_element(By.CSS_SELECTOR, "a[href=\"/Pochyxi?tab=repositories\"]")
repositories_pochyxi.click()

reposiry_PYTHON_SELENIUM_STUDIO = driver.find_element(By.CSS_SELECTOR, "a[href=\"/Pochyxi/PYTHON_SELENIUM_STUDIO\"]")
reposiry_PYTHON_SELENIUM_STUDIO.click()

bottone_codice = driver.find_element(By.CSS_SELECTOR, "summary.btn-primary.btn")
bottone_codice.click()

dowload_questo_progetto = driver.find_element(By.CSS_SELECTOR, "#local-panel > ul > li:nth-child(3) > a")
dowload_questo_progetto.click()

# .close() serve a chiudere il browser una volta effettuate tutte le automazioni desiderate
driver.close()
