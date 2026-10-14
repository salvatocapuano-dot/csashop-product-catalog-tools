import argparse
import json
import os
import re
from pathlib import Path

import pandas as pd


REQUIRED_FIELDS = ["sku", "title", "brand", "price", "currency", "stock", "image_url"]


def load_catalog(input_path: str) -> pd.DataFrame:
    path = Path(input_path)

    if path.suffix.lower() in [".csv"]:
        return pd.read_csv(path)
    if path.suffix.lower() in [".xlsx", ".xls"]:
        return pd.read_excel(path)
    if path.suffix.lower() in [".json"]:
        return pd.read_json(path)

    raise ValueError("Unsupported input format. Use CSV, XLSX or JSON.")


def clean_text(value):
    if pd.isna(value):
        return ""
    return re.sub(r"\s+", " ", str(value)).strip()


def normalize_availability(value):
    value = clean_text(value).lower()

    if value in ["yes", "true", "1", "disponibile", "in stock", "available"]:
        return "in_stock"
    if value in ["no", "false", "0", "esaurito", "out of stock", "unavailable"]:
        return "out_of_stock"

    return "unknown"


def normalize_catalog(df: pd.DataFrame) -> pd.DataFrame:
    missing = [field for field in REQUIRED_FIELDS if field not in df.columns]

    if missing:
        raise ValueError(f"Missing required columns: {', '.join(missing)}")

    df = df.copy()

    for column in ["sku", "title", "brand", "currency", "image_url"]:
        df[column] = df[column].apply(clean_text)

    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df["stock"] = pd.to_numeric(df["stock"], errors="coerce").fillna(0).astype(int)
    df["availability"] = df["stock"].apply(
        lambda stock: "in_stock" if stock > 0 else "out_of_stock"
    )

    df["title"] = df["title"].str.title()
    df["brand"] = df["brand"].str.title()

    df = df.drop_duplicates(subset=["sku"], keep="first")
    df = df.dropna(subset=["price"])

    return df[REQUIRED_FIELDS + ["availability"]]


def export_catalog(df: pd.DataFrame, output_path: str, output_format: str):
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)

    if output_format == "csv":
        df.to_csv(output_path, index=False)
    elif output_format == "json":
        df.to_json(output_path, orient="records", indent=2, force_ascii=False)
    else:
        raise ValueError("Unsupported output format. Use csv or json.")


def main():
    parser = argparse.ArgumentParser(
        description="Import, normalize and export ecommerce product catalogs."
    )

    parser.add_argument("--input", required=True, help="Input catalog file")
    parser.add_argument("--output", required=True, help="Output catalog file")
    parser.add_argument(
        "--format",
        default="csv",
        choices=["csv", "json"],
        help="Output format",
    )

    args = parser.parse_args()

    df = load_catalog(args.input)
    df = normalize_catalog(df)
    export_catalog(df, args.output, args.format)

    print(f"Processed {len(df)} products.")
    print(f"Catalog saved to: {args.output}")


if __name__ == "__main__":
    main()
