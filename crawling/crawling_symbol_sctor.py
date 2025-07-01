import pandas as pd
from datetime import datetime
import ssl 
import urllib.request

def get_nasdaq_100_symbols_and_sectors():
    
    # 인증서 검증 비활성화 (테스트용)
    ssl._create_default_https_context = ssl._create_unverified_context

    url = "https://en.wikipedia.org/wiki/NASDAQ-100"
    
    # 모든 HTML 테이블 읽기
    tables = pd.read_html(url)
    
    # NASDAQ-100 구성 종목이 있는 테이블 찾기 (symbol 열 포함 여부 기준)
    for table in tables:
        if 'Ticker' in table.columns or 'Symbol' in table.columns:
            df = table
            break
    else:
        raise ValueError("NASDAQ-100 테이블을 찾을 수 없습니다.")

    # 컬럼 이름 표준화
    df.columns = [col.strip() for col in df.columns]

    # 'Symbol' 또는 'Ticker'와 'GICS Sector' 또는 'Sector' 열만 추출
    if 'Symbol' in df.columns:
        symbol_col = 'Symbol'
    else:
        symbol_col = 'Ticker'

    if 'GICS Sector' in df.columns:
        sector_col = 'GICS Sector'
    elif 'Sector' in df.columns:
        sector_col = 'Sector'
    else:
        raise ValueError("Sector 컬럼을 찾을 수 없습니다.")

    return df[[symbol_col, sector_col]].rename(columns={symbol_col: "Symbol", sector_col: "Sector"})

# 저장
if __name__ == "__main__":
    df = get_nasdaq_100_symbols_and_sectors()
    print(df)
    filename = f"nasdaq_100_symbols_{datetime.now().strftime('%Y%m%d')}.csv"
    # df.to_csv(filename, index=False)
    print(f"[✓] Saved NASDAQ-100 list to {filename}")
