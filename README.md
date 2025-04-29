# 🔗 Multi-Source Data Merger with Conflict Resolution (CLI) 🛠️

This project is a **Python CLI tool** to intelligently merge two messy data sources using **Pandas** and **FuzzyWuzzy**. It resolves conflicts using configurable strategies.

## 🚀 Features

- Fuzzy string matching for misaligned column names
- Conflict resolution strategies:
  - Priority (keep first)
  - Latest (keep last)
  - Average (numerical mean)
- Merge multiple CSVs into a clean single output
- Simple command-line interface (CLI)

## 📦 Requirements

```bash
pip install pandas fuzzywuzzy python-Levenshtein
```

## 🛠️ How to Use

### 1. Prepare your files

Place your messy CSV files inside the `data/` folder.

### 2. Run the CLI

```bash
python src/merge_tool.py --file1 data/file1.csv --file2 data/file2.csv --output data/merged.csv --strategy priority
```

### 3. Conflict Resolution Options

- `priority`: Keeps the first occurrence
- `latest`: Keeps the last occurrence
- `average`: Averages numerical columns

## 📁 Project Structure

- `src/merge_tool.py` – CLI tool script
- `data/file1.csv` – Example input file
- `data/file2.csv` – Example input file
- `README.md` – Project documentation
