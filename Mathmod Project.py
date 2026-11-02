from pathlib import Path

import nflreadpy as nfl
import pandas as pd


OUTPUT_DIR = Path("fantasy_data")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "historical_player_stats.xlsx"
raw = nfl.load_player_stats(seasons=True,summary_level="week")
df = raw.to_pandas()

sort_columns = [
    col for col in ["position", "player_display_name", "season", "week"]
    if col in df.columns
]

position_sheets = {"QB": "Quarterbacks", "RB": "Running_Backs", "WR": "Wide_Receivers", "TE": "Tight_Ends", "K": "Kickers", "DEF": "Defense"}

with pd.ExcelWriter(OUTPUT_FILE, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="All_Players", index=False)

    for position, sheet_name in position_sheets.items():
        position_df = df[df["position"] == position].copy()

        if not position_df.empty:
            position_df.to_excel(writer,sheet_name=sheet_name,index=False)
            print(f"{sheet_name}: "f"{len(position_df):,} records")
print(OUTPUT_FILE.resolve())