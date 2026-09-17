"""
Sanity check the downloaded data
"""

import wfdb

record = wfdb.rdrecord('data/mitdb/100')
annotation = wfdb.rdann('data/mitdb/100', 'atr')

print(f"Signal shape: {record.p_signal.shape}")  # (650000, 2) — ~30 min, 2 leads, 360Hz
print(f"Leads: {record.sig_name}")
print(f"Num annotated beats: {len(annotation.symbol)}") # 2274
print(f"Beat types present: {set(annotation.symbol)}")  # {'N', '+', 'V', 'A'}

wfdb.plot_wfdb(record=record, annotation=annotation, time_units='seconds',
               title='Record 100 - first few seconds')