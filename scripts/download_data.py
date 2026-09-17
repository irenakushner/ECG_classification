import wfdb
import os

DATA_DIR = "data/mitdb"
os.makedirs(DATA_DIR, exist_ok=True)

wfdb.dl_database('mitdb', dl_dir=DATA_DIR)