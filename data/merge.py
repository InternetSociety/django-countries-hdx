from pathlib import Path

import pandas as pd
from hdx.location.country import Country
from hdx.utilities.path import script_dir_plus_file

from django_countries_hdx import RegionData


def merge_data_sources():
    try:
        # Resolve all file paths
        hdx_file = Path(
            script_dir_plus_file(
                "Countries & Territories Taxonomy MVP - C&T Taxonomy.csv",
                Country,
            )
        )
        unsd_file = Path(__file__).parent.resolve() / "unsd_methodology.csv"
        output_file = Path(
            script_dir_plus_file(
                "hdx_plus_m49.csv",
                RegionData,
            )
        )

        # Verify input files exist
        if not hdx_file.exists():
            raise FileNotFoundError(f"HDX file not found: {hdx_file}")
        if not unsd_file.exists():
            raise FileNotFoundError(f"UNSD file not found: {unsd_file}")

        print(f"Reading HDX data from {hdx_file}")

        # Read the data with the correct headers, treat everything as a string by default
        # so Pandas doesn't get clever and convert integers to floats
        hdx_df = pd.read_csv(
            hdx_file,
            dtype=str,
            keep_default_na=False,
        )

        # Convert only the numeric columns we need
        numeric_columns = {
            "m49 numerical code": 'Int64',
            "Latitude": 'float64',
            "Longitude": 'float64',
            "Region Code": 'Int64',
            "Sub-region Code": 'Int64',
            "Intermediate Region Code": 'Int64'
        }

        for col, dtype in numeric_columns.items():
            if col in hdx_df.columns:
                hdx_df[col] = pd.to_numeric(hdx_df[col], errors="coerce").astype(dtype)

        print(f"Reading UNSD data from {unsd_file}")

        # Read and process UNSD data
        unsd_df = pd.read_csv(
            unsd_file,
            delimiter=";",
            dtype=str,
            keep_default_na=False,
        )

        unsd_df["LDC"] = unsd_df["Least Developed Countries (LDC)"] == "x"
        unsd_df["LLDC"] = unsd_df["Land Locked Developing Countries (LLDC)"] == "x"
        unsd_df["SIDS"] = unsd_df["Small Island Developing States (SIDS)"] == "x"

        print("Merging data")

        # Merge the dataframes using the ISO2 column and then drop the duplicate column
        merged_df = hdx_df.merge(
            unsd_df[["ISO-alpha2 Code", "LDC", "LLDC", "SIDS"]],
            left_on="ISO 3166-1 Alpha 2-Codes",
            right_on="ISO-alpha2 Code",
            how="left"
        )

        merged_df = merged_df.drop(columns=["ISO-alpha2 Code"])

        # Coerce empty values to False
        for col in ["LDC", "LLDC", "SIDS"]:
            merged_df[col] = merged_df[col].astype("boolean").fillna(False)

        print(f"Writing output to {output_file}")

        merged_df.to_csv(output_file, index=False)

        print(f"Successfully merged country data to {output_file}")
        exit(0)
    except Exception as e:
        print(f"Error merging country data {e}")
        exit(1)


if __name__ == '__main__':
    merge_data_sources()
