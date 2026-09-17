# ECG_classification

## Dataset & Tools

Built on the [MIT-BIH Arrhythmia Database](https://physionet.org/content/mitdb/1.0.0/)
via [PhysioNet](https://physionet.org/), accessed using the [WFDB Python package](https://physionet.org/content/wfdb-python/4.1.0/).
Data isn't included in this repo; `scripts/download_data.py` pulls it directly.
Full citations in [CITATION.md](CITATION.md).

## Setup
```bash 
uv sync
python scripts/download_data.py  # pulls MIT-BIH from PhysioNet (~100MB)
```