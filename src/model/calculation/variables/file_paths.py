import os
from pathlib import Path

file_dir = Path(os.path.dirname(os.path.abspath(__file__)))

# file locations
historical_data_file = file_dir.parent.parent / Path("data", "AMZN.xlsx")
