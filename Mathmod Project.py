from pathlib import Path

import nflreadpy as nfl
import pandas as pd


OUTPUT_DIR = Path("fantasy_data")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "historical_player_stats.xlsx"

raw = nfl.load_player_stats(seasons=True,summary_level="week")
df = raw.to_pandas()

if "season" in df.columns:
    df = df[df["season"] >= 2010].copy()

sort_columns = [
    col for col in ["position", "player_display_name", "season", "week"]
    if col in df.columns
]

position_sheets = {"QB": "Quarterbacks", "RB": "Running_Backs", "WR": "Wide_Receivers", "TE": "Tight_Ends", "OL": "Offensive_Line", "DL": "Defensive_Line", "LB": "Linebackers", "CB": "Cornerbacks", "S": "Safeties", "K": "Kickers",}

for pos in position_sheets:
    position_df = df[df["position"] == pos].copy()
    print(f"{pos}: {len(position_df):,} rows")