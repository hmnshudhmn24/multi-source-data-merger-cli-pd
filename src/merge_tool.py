import pandas as pd
import argparse
from fuzzywuzzy import process, fuzz
import os

def smart_merge(file1, file2, conflict_strategy='priority'):
    # Load datasets
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Attempt to smart-match columns using fuzzy matching
    matched_columns = {}
    for col1 in df1.columns:
        match, score = process.extractOne(col1, df2.columns, scorer=fuzz.token_sort_ratio)
        if score > 80:
            matched_columns[col1] = match

    df2_renamed = df2.rename(columns={v: k for k, v in matched_columns.items()})

    # Merge datasets
    merged = pd.concat([df1, df2_renamed], ignore_index=True)

    # Conflict Resolution
    if conflict_strategy == 'priority':
        merged = merged.drop_duplicates(subset=list(df1.columns), keep='first')
    elif conflict_strategy == 'latest':
        merged = merged.drop_duplicates(subset=list(df1.columns), keep='last')
    elif conflict_strategy == 'average':
        num_cols = merged.select_dtypes(include='number').columns
        merged = merged.groupby(list(df1.columns.difference(num_cols)), as_index=False).mean()

    return merged

def main():
    parser = argparse.ArgumentParser(description="🔗 Multi-Source Data Merger with Conflict Resolution")
    parser.add_argument('--file1', type=str, required=True, help='Path to first CSV file')
    parser.add_argument('--file2', type=str, required=True, help='Path to second CSV file')
    parser.add_argument('--output', type=str, default='merged_output.csv', help='Output merged CSV file name')
    parser.add_argument('--strategy', type=str, choices=['priority', 'latest', 'average'], default='priority', help='Conflict resolution strategy')
    args = parser.parse_args()

    merged_df = smart_merge(args.file1, args.file2, conflict_strategy=args.strategy)
    merged_df.to_csv(args.output, index=False)
    print(f"✅ Successfully merged files! Output saved to {args.output}")

if __name__ == "__main__":
    main()
