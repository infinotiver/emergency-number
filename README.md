# Emergency Number API
## Overview
This API provides emergency contact numbers web-scraped from Wikipedia page for various services across different countries.
 
## Base URL
The API for testing purposes is hosted on Render's free plan:
```
https://emergency-number-api.onrender.com/api/emergency/
```

## Endpoints
### GET `/:country_code`
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

## Limitations
- Hosted on a free plan, so performance may vary.
- The data is not updated automatically

## Data Source
[Wikipedia](https://en.wikipedia.org/wiki/List_of_emergency_telephone_numbers)

![Render](https://img.shields.io/badge/Render-%46E3B7.svg?style=for-the-badge&logo=render&logoColor=white)
