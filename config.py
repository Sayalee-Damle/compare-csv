from pathlib import Path

class Config:
    EXCEL_PATH_DISC = "/tmp/files/"
    path_excel = Path(EXCEL_PATH_DISC)
        
    if not path_excel.exists():
        path_excel.mkdir(exist_ok=True, parents=True)

cfg = Config()