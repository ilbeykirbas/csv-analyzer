# CSV Analyzer

A lightweight desktop tool to analyze CSV files using a graphical interface.  
Built with Python, Tkinter, and pandas, this app lets you explore column statistics and visualize distributions with histograms.

---

## Features

- Load and read CSV files easily
- Display list of column names
- Show key statistics for numeric columns:
- Mean, Median, Min, Max, Std Deviation
- Generate histograms for selected numeric columns
- Friendly error handling and UI feedback

---

## Requirements

Install required libraries with:

```bash
pip install pandas matplotlib
```

---

## How to Run

```bash
python csv_analyzer.py
```
Then:

- **1.** Click "Select CSV File" and choose a .csv
- **2.** Select a column from the list
- **3.** View stats below, and click "Show Chart" for a histogram (numeric only)

---

## File Structure

```
csv-analyzer/
├── data/
├── csv_analyzer.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## .gitignore Suggestion
*.csv
*.db

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/ilbeykirbas/expense-app/blob/main/LICENSE) file for details.

---

## Author

Developed by İlbey Kırbaş  
GitHub: [@ilbeykirbas](https://github.com/ilbeykirbas)
