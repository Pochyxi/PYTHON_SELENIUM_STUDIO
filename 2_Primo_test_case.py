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

ActionChains(driver)\
        .key_down(Keys.ENTER)\
        .key_up(Keys.ENTER)\
        .perform()



# .close() serve a chiudere il browser una volta effettuate tutte le automazioni desiderate
driver.close()
