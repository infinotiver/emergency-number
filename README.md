# emergency-number
## Overview
This API provides emergency contact numbers web scrapped from wikipedia page for various services across different countries.
 
## Base URL
The API is hosted on Render's free plan:
```
https://emergency-number-api.onrender.com/api/emergency/
```

## Endpoints
### GET `/:country_code`
Fetches emergency contact numbers specific to a country.

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
