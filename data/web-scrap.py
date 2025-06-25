import requests
from bs4 import BeautifulSoup
import json
import re
import pycountry

# url of wikipedia page
URL = "https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers"

# request html
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')
# Step 2: Find all wikitable class tables on the page
tables = soup.find_all("table", {"class": "wikitable"})
 
emergency_data = {}

# function to clean text like citations, notes, [1]
def clean_text(text):
    return re.sub(r"\[.*?\]", "", text).strip()

# function to split multiple numbers

def split_numbers(field):
    
    if not field:
        return []
    
    split_result = re.split(r"[\/,;]| or ", field)
    # Filter out empty strings and strip whitespace from each number
    cleaned_numbers = [num.strip() for num in split_result if num.strip()]
    
    return cleaned_numbers

# loop over each table

for table in tables:
    rows = table.find_all('tr')
    # td 1 - name
    # td 2 - police
    # td 3 - ambulance
    # td 4 - fire
    # td 5 - notes*
    for row in rows[1:]: # skip the header
        cols = row.find_all("td")
        print(cols)
        country_name = clean_text(cols[0].text)
        # Try converting to ISO country code
        try:
            country_code = pycountry.countries.lookup(country_name).alpha_2
        except:
            # If country not found, skip this row
            continue
        
        # handling merged cell: 3 columns - all three services same number eg India (4th notes)

        if len(cols) ==2:
            shared = clean_text(cols[1].text)
            numbers = split_numbers(shared)
            notes = clean_text(cols[2])
            emergency_data[country_code] = {"country": country_name,
                "police": numbers,
                "ambulance": numbers,
                "fire": numbers,
            
                "notes": notes}
        # Normal case: 4 or more columns for separate numbers
        elif len(cols) >= 4:
            police = split_numbers(clean_text(cols[1].text))
            ambulance = split_numbers(clean_text(cols[2].text))
            fire = split_numbers(clean_text(cols[3].text))

            emergency_data[country_code] = {
                "country": country_name,
                "police": police,
                "ambulance": ambulance,
                "fire": fire
            }