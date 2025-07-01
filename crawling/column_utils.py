# -*- coding: utf-8 -*-
"""
Filename : column_utils.py
Description: Convert column name as snake_case format.
"""
import re
import pandas as pd

def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert DataFrame column names to clean snake_case format.
    Removes or replaces special characters and ensures consistency.
    """
    def clean(col: str) -> str:
        col = col.lower()
        col = re.sub(r"[#]", "num_", col)           # '#' → 'num_'
        col = re.sub(r"%", "percent", col)          # '%' → 'percent'
        col = re.sub(r"\$", "", col)                # '$' 제거
        col = re.sub(r"[']", "", col)               # 작은따옴표 제거
        col = re.sub(r"[()]", "", col)              # 괄호 제거
        col = re.sub(r"[\s\-\/]+", "_", col)        # 공백/하이픈/슬래시 → '_'
        col = re.sub(r"[^a-z0-9_]", "", col)        # 나머지 특수문자 제거
        col = re.sub(r"_+", "_", col)               # 중복 언더스코어 제거
        col = col.strip("_")                        # 앞뒤 언더스코어 제거
        return col

    df.columns = [clean(col) for col in df.columns]
    return df
