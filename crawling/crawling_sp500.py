from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO
from datetime import datetime
from column_utils import standardize_column_names

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()

    # Access Site (DOMContentLoaded 기준으로 진행)
    page.goto(
        'https://financhle.com/sp500-companies-by-weight',
        timeout=60000,
        wait_until='domcontentloaded'
    )

    # Wait for data loading
    container_sel = '#root > div.main > div.weightedTableContainer-SPY.visible > div'
    page.wait_for_selector(container_sel, timeout=15000)

    # Get all HTML in container
    inner_html = page.inner_html(container_sel)

    # extract first table
    soup = BeautifulSoup(inner_html, 'html.parser')
    table = soup.find('table')

    # pandas pasrsing
    df = pd.read_html(StringIO(str(table)))[0]
    # add 'Date' column
    df['Date'] = pd.Timestamp.now(tz='US/Eastern').date()
    # rename column
    df = standardize_column_names(df)
    
    # Save as CSV
    # df.to_csv(f'sp500_weights_{df['Date'][0]}.csv', index=False)

    # print(df.head())
    browser.close()
