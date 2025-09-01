from playwright.sync_api import sync_playwright
from dataclasses import dataclass, asdict, field
import argparse
import pandas as pd


@dataclass
class Business:
    name: str = None
    address: str = None
    website: str = None
    phone_number: str = None


@dataclass
class BusinessList:
    business_list: list[Business] = field(default_factory=list)

    def dataframe(self):
        return pd.json_normalize([asdict(business) for business in self.business_list], sep="")

    def save_to_excel(self, filename):
        self.dataframe().to_excel(f'{filename}.xlsx', index=False)

    def save_to_csv(self, filename):
        self.dataframe().to_csv(f'{filename}.csv', index=False)


def main(search_for):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com/maps', timeout=60000)
        page.wait_for_timeout(5000)

        page.locator('input[id="searchboxinput"]').fill(search_for)
        page.keyboard.press('Enter')
        page.wait_for_timeout(8000)

        listings = page.locator('.hfpxzc').all()
        print(f"{len(listings)}")

        business_list = BusinessList()

        for listing in listings[:5]:
            listing.click()
            page.wait_for_timeout(7000)

            name_xpath = '//h1[@class="DUwDvf lfPIob"]'
            address_xpath = '//button[@data-item-id="address"]'

            website_xpath = '//a[@data-item-id="authority"]'
            phone_xpath = '//button[contains(@data-item-id, "phone:tel:")]'

            business = Business()

            try:
                business.name = page.locator(name_xpath).inner_text()
            except:
                pass
            try:
                business.address = page.locator(address_xpath).inner_text()
            except:
                pass
            try:
                business.website = page.locator(website_xpath).inner_text()
            except:
                pass
            try:
                business.phone_number = page.locator(phone_xpath).inner_text()
            except:
                pass

            business_list.business_list.append(business)

        business_list.save_to_excel('google_maps_data')
        business_list.save_to_csv('google_maps_data')
        browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--search", type=str)
    parser.add_argument("-l", "--location", type=str)
    args = parser.parse_args()

    if args.search and args.location:
        search_for = f"{args.search} {args.location}"
    elif args.search:
        search_for = args.search
    else:
        search_for = "dentist gaza"

    main(search_for)