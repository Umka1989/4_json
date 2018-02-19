# Prettify JSON

Script print json data in easy to read way

# Quickstart

```python
from pprint_json.py import pretty_print_json, load_data
data = load_data(filepath)
pretty_print_json(data)
```

```bash

$ python pprint_json.py <path to file>
```

# Output examole
```json
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10",
            "AdmArea": "Западный административный округ",
            "ClarificationOfWorkingHours": null,
            "District": "район Кунцево",
            "IsNetObject": "да",
            "Name": "Ароматный Мир",
            "OperatingCompany": "Ароматный Мир",
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ]
        }
    }
]	

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
