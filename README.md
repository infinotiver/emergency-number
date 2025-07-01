# Emergency Number API
## Overview
This API provides emergency contact numbers web-scraped from Wikipedia page for various services across different countries.
 


## Endpoints
### GET `/api/emergency/<country_code>`
Returns emergency contact numbers of police, ambulance, fire and notes (additional contacts)

#### Example Response
```json
{
    "ambulance": [
        "112"
    ],
    "country": "India",
    "fire": [
        "112"
    ],
    "notes": "Gas leakage – 1906\nTourist Helpline – 1363\nChild Helpline – 1098\nDisaster management – 104\nWomen Helpline – 181\nPolice – 100\nAmbulance – 108\nFire brigade – 101",
    "police": [
        "112"
    ]
}
```



## Data Source
[Wikipedia](https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers)
