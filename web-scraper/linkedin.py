import pandas as pd
import os.path
from bs4 import BeautifulSoup as bs
from playwright.sync_api import Playwright, sync_playwright, expect

with open(os.path.dirname(__file__) +'/../secrets.txt', 'r') as f:
    secret = f.read().splitlines()
    user = secret[0].strip().split(':')[1]
    password = secret[1].strip().split(':')[1]

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.linkedin.com/")
    page.get_by_role("link", name="Sign in").click()
    page.get_by_label("Email or Phone").click()
    page.get_by_label("Email or Phone").fill(f"{user}")
    page.get_by_label("Password").click()
    page.get_by_label("Password").fill(f"{password}")
    page.get_by_role("button", name="Sign in", exact=True).click()
    page.get_by_role("link", name="Jobs").click()
    page.get_by_role("combobox", name="Search by title, skill, or company").click()
    page.get_by_role("combobox", name="Search by title, skill, or company").fill("Data Scientist")
    page.get_by_role("combobox", name="City, state, or zip code").click()
    page.get_by_role("combobox", name="City, state, or zip code").fill("Barcelona, Catalonia, Spain")
    page.get_by_role("combobox", name="City, state, or zip code").press("Enter")

    # ---------------------
    context.close()
    browser.close()

if __name__ == "__main__":


    with sync_playwright() as playwright:
        run(playwright)

