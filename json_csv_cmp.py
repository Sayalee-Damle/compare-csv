from difflib import Differ
import filecmp
import pandas as pd
from pathlib import Path
import sys
import csv

from config import cfg
import compare 

path_json = Path(input("Enter path of file: "))


data = pd.read_json(path_json)

# Save the data as CSV
load_csv = cfg.path_excel / "file_csv.csv"

data.to_csv(load_csv, index=False)

print('CSV file saved successfully.')
f = Path(input("Enter path of file: "))
is_same = filecmp.cmp(load_csv, f)
if not is_same:
    print(compare.compare_csv_files(Path(load_csv), Path(f)))