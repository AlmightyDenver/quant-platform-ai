# -*- coding: utf-8 -*-
"""
Filename: crawl_nasdaq.py

Description:
    This script crawls NASDAQ-100 company data from financhle.com,
    specifically from the table on the 'nasdaq100 companies by weight' page.
    The table includes the following columns:
        - % of Nasdaq 100
        - # of Shares Held
        - Market Cap ($)
        - Price
        - Today's Change ($)
        - Today's Change (%)
        - YTD Change (%)

Features:
    - Scrape the NASDAQ-100 weights table from Financhle.com
    - Save as CSV file

Data sources:
    - financhle.com (for index weight table)

Author: DenverAlmighty
Date: 2025-06-30
"""




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
        'https://financhle.com/nasdaq100-companies-by-weight',
        timeout=60000,
        wait_until='domcontentloaded'
    )

    # Wait for data loading
    container_sel = '#root > div.main > div.weightedTableContainer-QQQ.visible > div'
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
    # df.to_csv(f'nasdaq_weights_{df['Date'][0]}.csv', index=False)

    print(df.head())
    browser.close()
