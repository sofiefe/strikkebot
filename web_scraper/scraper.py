from selenium import webdriver
from page_scraper import page_scraper, load_page, write_links
from bs4 import BeautifulSoup
import time

URL = "https://www.garnstudio.com/search.php?action=browse&mt=1&page=1&sort=date&lang=no"

# function to get the last page

# Iterate trough each page using page_scraper() and save pattern info
# Use the links to scrape patterns using pattern_scraper
# Save data in a fitting format

def find_last_page(soup):
    page_div = soup.find_all("li", class_="page-item")
    last_page_button = page_div[-1].find("a", href=True)
    link = last_page_button["href"] if last_page_button else "No link"
    last_page = link.strip("/search.php?action=browse&mt=1&page=").split("&")[0]
    return int(last_page)


def scraper():
    driver = webdriver.Firefox()
    driver.get(URL)

    try:
        load_page(driver)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        last_page = find_last_page(soup)

        pattern_info = []

        base_url = "https://www.garnstudio.com/search.php?action=browse&mt=1&page={}&sort=date&lang=no"

        for page in range(1, last_page+1):
            print(f"Getting links from page {page}")
            page_url = base_url.format(page)
            pattern_info.append(page_scraper(page_url))
        
        write_links(pattern_info)


    except Exception as e:
        print("No patterns found:", e)

    driver.quit()


if __name__ == "__main__":
    print("Start getting links")
    start_time = time.time()
    scraper()
    print(f"Getting links took {time.time()-start_time:.2f}")