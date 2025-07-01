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
def clean_text(cell):
    if hasattr(cell, "get_text"):  # If it's a Tag
        cell = cell.get_text()
    return re.sub(r"\[.*?\]", "", str(cell)).strip()


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
       
        country_name = clean_text(cols[0].text)
        # Try converting to ISO country code
        try:
            country_code = pycountry.countries.lookup(country_name).alpha_2
        except:
            # If country not found, skip this row
            continue
        
        # handling merged cell: 3 columns - all three services same number eg India (4th notes)

        if len(cols) ==3:
            shared = clean_text(cols[1].text)
            numbers = split_numbers(shared)
            notes = clean_text(cols[2])
            
            emergency_data[country_code] = {"country": country_name,
                "police": numbers,
                "ambulance": numbers,
                "fire": numbers,
            
                "notes": notes}
        # Normal case: 5 columns for separate numbers
        elif len(cols) == 5:
            police = split_numbers(clean_text(cols[1].text))
            ambulance = split_numbers(clean_text(cols[2].text))
            fire = split_numbers(clean_text(cols[3].text))
            notes = clean_text(cols[4].text)
            emergency_data[country_code] = {
                "country": country_name,
                "police": police,
                "ambulance": ambulance,
                "fire": fire,
                "notes":notes
            }

           # Case: 3 columns → check which ones are merged via colspan
        elif len(cols) == 4:
            c1 = cols[1]
            c2 = cols[2]

            if c1.has_attr("colspan"):
                span = int(c1.get("colspan"))
                if span == 2:
                    # Police + Ambulance merged
                    shared = split_numbers(clean_text(c1))
                    fire = split_numbers(clean_text(c2))
                    notes = clean_text(cols[3])
                    emergency_data[country_code] = {
                        "country": country_name,
                        "police": shared,
                        "ambulance": shared,
                        "fire": fire,
                        "notes": notes
                    }
                elif span == 3:
                    # All merged
                    shared = split_numbers(clean_text(c1))
                    notes = clean_text(cols[3])
                    emergency_data[country_code] = {
                        "country": country_name,
                        "police": shared,
                        "ambulance": shared,
                        "fire": shared,
                        "notes": notes
                    }
            elif c2.has_attr("colspan") and int(c2.get("colspan")) == 2:
                # Ambulance + Fire merged
                police = split_numbers(clean_text(c1))
                shared = split_numbers(clean_text(c2))
                notes = clean_text(cols[3])
                emergency_data[country_code] = {
                    "country": country_name,
                    "police": police,
                    "ambulance": shared,
                    "fire": shared,
                    "notes": notes
                }
# Save final structured data to JSON file
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(emergency_data, f, indent=2, ensure_ascii=False)
    
# Finally
print("✅ Emergency data saved to data.json")