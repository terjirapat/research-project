from pathlib import Path
from typing import Dict, Optional, List, Any
import json
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

@log_execution_time
def load_json(path: str | Path) -> Dict[str, Any]:
    """
    Load a JSON file and return it as a Python dictionary.

    Args:
        path: Path to the JSON file.

    Returns:
        Dictionary containing the JSON data.

    Raises:
        FileNotFoundError: If the file does not exist.
        ValueError: If the file is not valid JSON.
    """
    path = Path(path)

    if not path.exists():
        raise FileNotFoundError(f"JSON file not found: {path}")

    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)

    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON file: {path}") from e