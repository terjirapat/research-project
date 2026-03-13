from pathlib import Path
from typing import Dict, Optional, List
from src.utils.logger import log_execution_time

import pandas as pd

@log_execution_time
def load_dataframe(
    file_path: str,
    dtype_map: Optional[Dict[str, str]] = None,
    parse_dates: Optional[List[str]] = None,
) -> pd.DataFrame:
    """
    Load CSV or Parquet file into DataFrame.

    Args:
        file_path: Path to file
        dtype_map: Column data types
        parse_dates: Columns to parse as dates

    Returns:
        Loaded DataFrame

    Raises:
        FileNotFoundError: If file doesn't exist
        ValueError: If file format not supported
    """
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    suffix = path.suffix.lower()

    if suffix == ".csv":
        df = pd.read_csv(
            path,
            dtype=dtype_map,
            parse_dates=parse_dates,
        )

    elif suffix in {".parquet", ".pq"}:
        df = pd.read_parquet(path)

        if dtype_map:
            df = df.astype(dtype_map)

        if parse_dates:
            for col in parse_dates:
                df[col] = pd.to_datetime(df[col])

    else:
        raise ValueError("Unsupported file format. Use CSV or Parquet.")

    return df