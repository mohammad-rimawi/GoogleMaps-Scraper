# Google Maps Business Scraper

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![Playwright](https://img.shields.io/badge/Playwright-Installed-green)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Google Maps Business Scraper** is a Python project that uses [Playwright](https://playwright.dev/python/docs/intro) to scrape business information from Google Maps automatically.

---

## Features

- Search for businesses on Google Maps by keyword and location.
- Extract the following business data:
  - Name
  - Address
  - Website
  - Phone number
- Save the extracted data in:
  - Excel (`google_maps_data.xlsx`)
  - CSV (`google_maps_data.csv`)
- Automatically handles multiple listings (default top 5 results).
- Works on Windows with UTF-8 support for proper text handling.

---

## Requirements

- Python 3.9 or higher
- Required Python packages:
```bash
pip install playwright pandas openpyxl
playwright install
