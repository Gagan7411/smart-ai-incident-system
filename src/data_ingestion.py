import os
import pandas as pd
from datetime import datetime

# Paths
INPUT_FILE = "data/sample_data.csv"
OUTPUT_FILE = "data/raw/raw_data.csv"

def ingest_data():
    """Load sample data and store a copy in the raw folder."""
    print("[INFO] Starting data ingestion...")

    # Ensure raw folder exists
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    # Load CSV
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"[INFO] Loaded data with {len(df)} rows and {len(df.columns)} columns.")
    except FileNotFoundError:
        print(f"[ERROR] Input file not found at {INPUT_FILE}")
        return
    except Exception as e:
        print(f"[ERROR] Failed to read CSV: {e}")
        return

    # Add ingestion timestamp
    df["ingested_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to raw folder
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"[INFO] Raw data saved to {OUTPUT_FILE}")

if __name__ == "__main__":
    ingest_data()
