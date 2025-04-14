from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time
import random

URL = "https://www.garnstudio.com/search.php?action=browse&mt=1&page=1&lang=no"

driver = webdriver.Firefox()
# Load the page
driver.get(URL)


try:
    # Wait for the cookie consent div to load and click the "Accept All" button
    cookie_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Godta')]"))
    )
    cookie_button.click()
    # print("✅ Cookie accepted")

    # Wait for the pattern divs to appear (10 seconds max)
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "pattern"))
    )

    soup = BeautifulSoup(driver.page_source, "html.parser")
    pattern_divs = soup.find_all("div", class_="pattern")
    print(f"Found {len(pattern_divs)} patterns.")

    pattern_info = []
    for pattern in pattern_divs: 
        number_tag = pattern.select_one("div.info p.drops-number")
        number = number_tag.text.strip("DROPS ") if number_tag else "No number"

        link_tag = pattern.find("a", href=True)
        link = "https://www.garnstudio.com" + link_tag["href"] if link_tag else "No link"

        pattern_info.append([number, link])


except Exception as e:
    print("No patterns found:", e)


# Close the browser when done
driver.quit()
