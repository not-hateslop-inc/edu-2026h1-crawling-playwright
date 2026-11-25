from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

d = webdriver.Chrome()
try:
    d.get("https://quotes.toscrape.com/js/")
    WebDriverWait(d, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.quote")))
    print(len(d.find_elements(By.CSS_SELECTOR, "div.quote")), "quotes")
finally:
    d.quit()
