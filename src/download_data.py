"""Download Premier League match CSVs (E0) from football-data.co.uk into data/raw/.

Run from the project root:
    python src/download_data.py

Files that already exist are skipped, so raw data is never overwritten.
"""

from pathlib import Path

import requests

BASE_URL = "https://www.football-data.co.uk/mmz4281/{code}/E0.csv"
RAW_DIR = Path(__file__).resolve().parent.parent / "data" / "raw"

# Season start years: 2010 -> 2010/11, ..., 2022 -> 2022/23
FIRST_SEASON = 2010
LAST_SEASON = 2022


def season_code(start_year):
    """2010 -> '1011' (the format used in football-data.co.uk URLs)."""
    return f"{start_year % 100:02d}{(start_year + 1) % 100:02d}"


def main():
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    for year in range(FIRST_SEASON, LAST_SEASON + 1):
        code = season_code(year)
        target = RAW_DIR / f"E0_{code}.csv"

        if target.exists():
            print(f"{target.name}: already exists, skipped")
            continue

        url = BASE_URL.format(code=code)
        response = requests.get(url, timeout=30)
        response.raise_for_status()  # stop on 404 etc. instead of saving an error page

        target.write_bytes(response.content)
        print(f"{target.name}: downloaded {len(response.content) / 1024:.0f} KB")


if __name__ == "__main__":
    main()
