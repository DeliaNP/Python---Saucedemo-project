import time  # ne ajuta sa folosim time.sleep (sa ramana in pagina)
import unittest

from selenium import webdriver  # sa putem sa deschidem pagina web
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By  # cu linia asta ne selectam tipul de selector

LINK = "https://www.saucedemo.com/"
driver = webdriver.Chrome()  # deschide un Chrome
driver.get(LINK)  # deschidem pagina in Chrome

user = driver.find_element(By.ID, "user-name")  # cauta selectorul
user.send_keys("standard_user")  # scrie userul

password = driver.find_element(By. ID, "password")
password.send_keys("secret_sauce")
#password.send_keys(Keys.ENTER)  # apasa enter in loc de lupa la "cautari"
time.sleep(3)

login = driver.find_element(By.ID, "login-button")
login.click()
time.sleep(1)

add_to_card=driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')  # am selectat id cu XPATH
add_to_card2 = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")  # selectat cu ID, aceeasi comanda de mai sus
add_to_card.click()
time.sleep(1)

view_cos=driver.find_element(By.CLASS_NAME, "shopping_cart_link")
view_cos2=driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')  # acelasi lucru in doua moduri diferite
view_cos.click()
time.sleep(1)

cantitate=driver.find_element(By.CLASS_NAME, 'cart_quantity')  # verific cantitatea
if "2" in cantitate.text: # cantitatea se afla in selectorul de sus, care este text
    print("A mai fost adaugat un produs in cos .")
else:
    print("Bug: Nu se poate modifica cantitatea.")

apasa_checkout=driver.find_element(By.CSS_SELECTOR,'button[name="checkout"]')
apasa_checkout2=driver.find_element(By.CSS_SELECTOR, 'button[class~="btn_action"]')  # acelasi lucru ca mai sus
# (~ = contains - contine o bucata din valoare);
# ~ = CSS_SELECTOR
# contains = XPATH
apasa_checkout.click()
time.sleep(2)

first_name=driver.find_element(By.XPATH, '//input[@id="first-name"]')  # am selectat first name
first_name.send_keys("delia")  # am adugat first name

last_name=driver.find_element(By.CSS_SELECTOR, 'input.input_error[id="last-name"]')
last_name.send_keys("parvu")

cod_postal=driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
cod_postal.send_keys("031256")
time.sleep(2)

continua=driver.find_element(By.CSS_SELECTOR, ".submit-button.btn.btn_primary.cart_button.btn_action")
continua.click()
time.sleep(2)

meniu=driver.find_element(By.XPATH, '//button[text()="Open Menu"]')
meniu.click()

logout=driver.find_element(By.XPATH, "//a[@id='logout_sidebar_link' and contains(@class,'bm-item')]")  # am cautat dupa 2 atribute
logout.click()

driver.current_url



# TODO: # pt comentarii 
