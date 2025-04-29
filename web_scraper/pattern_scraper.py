import re
import csv
from selenium import webdriver
from bs4 import BeautifulSoup
from page_scraper import load_page


def clean_pattern_part(pattern):
    if not pattern:
        return ""

    # Remove tooltips or unnecessary spans
    for span in pattern.select("span.quickexplanation"):
        span.unwrap()

    # Replace <br> with a space (not newline) to avoid newlines in CSV
    for br in pattern.find_all("br"):
        br.replace_with(" ")

    # Remove scripts, styles, or other unwanted tags
    for tag in pattern(["script", "style"]):
        tag.decompose()

    # Get raw text with space separators (to prevent newlines in the CSV)
    text = pattern.get_text(separator=" ", strip=True)

    # Normalize internal spacing (collapse >1 space into 1)
    cleaned_text = re.sub(r"[ \t]+", " ", text)  # collapse tabs/spaces
    cleaned_text = re.sub(r"\s+$", "", cleaned_text)  # remove trailing whitespace
    cleaned_text = re.sub(r"^\s+", "", cleaned_text)  # remove leading whitespace

    return cleaned_text


def pattern_scraper(URL):
    driver = webdriver.Firefox()
    driver.get(URL)

    try:
        load_page(driver, "pattern-main")
        soup = BeautifulSoup(driver.page_source, "html.parser")

        pattern_title = soup.find("h1")
        pattern_intro = soup.select_one("div.pattern-title")
        pattern_material = soup.select_one("div.pattern-intro")
        pattern_instructions = soup.select_one("div.pattern-instructions")

        pattern_parts = [pattern_title, pattern_intro, pattern_material, pattern_instructions]
        pattern_parts_clean = [clean_pattern_part(part) for part in pattern_parts]
        pattern_parts_names = ["title", "intro", "material", "instructions"]

        pattern = list(zip(pattern_parts_names, pattern_parts_clean))


    except Exception as e:
        print("No patterns found:", e)

    driver.quit()
    return pattern


def pattern_file_reader(filepath):
    # Define the output file
    output_filepath = 'pattern_data.csv'
    
    # Open the input file (pattern_links) for reading
    with open(filepath, mode='r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        next(reader)  # Skip header row if present
        
        # Open the output file for writing
        with open(output_filepath, mode='w', newline='', encoding='utf-8') as outfile:
            writer = csv.writer(outfile)
            
            # Write the header for the output CSV
            writer.writerow(["ID", "Title", "Intro", "Material", "Instructions"])
            counter = 0
            # Loop through each URL in the input file
            for row in reader:
                if row:
                    url = row[1]  # Assuming the URL is in the first column
                    
                    # Scrape the pattern data
                    pattern = pattern_scraper(url)
                    
                    # Extract ID from the URL (assuming the URL has an id parameter)
                    # You can adapt this extraction based on your actual URL structure
                    pattern_id = row[0]
                    
                    # Write the data into the output file
                    writer.writerow([pattern_id, pattern[0][1], pattern[1][1], pattern[2][1], pattern[3][1]])


                    counter += 1
                    if counter > 3:
                        break

    print(f"Data has been written to {output_filepath}")


pattern_file_reader("pattern_links.csv")
    # read the csv file given the filename (pattern_links)
    # for each row in file
    #     result = pattern_scraper(URL)
    #     put result with id in a new csv file










# NOTES ----------------------------------------------------------------------------------------------
# pattern_scraper("https://www.garnstudio.com/pattern.php?id=12242&cid=1")
# print([tag['class'] for tag in soup.find_all('div') if 'pattern' in str(tag.get('class'))])

# [['pattern-prices', 'pb-3'], ['pattern-ad'], ['col-12', 'col-sm-12', 'col-md-7', 'pattern-main'], 
# ['nav-pattern'], ['col-12', 'col-sm-12', 'pattern-title'], 
# ['pattern-intro'], ['pattern-material'], ['pattern-prices', 'pb-3'], ['pattern-instructions'], ['pattern_text'], 
# ['pattern-corrections'], ['col-12', 'pattern_copyright', 'py-4', 'my-4']]
