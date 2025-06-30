import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
from pandas.api.types import is_numeric_dtype

class CSVAnalyzer:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("CSV Analyzer")
        self.window.geometry("400x400")

        # Select CSV File Button
        tk.Button(self.window, text="Select CSV File", command=self.load_csv).pack(pady=10)

        # Name of the selected file
        self.file_label = tk.Label(self.window, text="No file selected")
        self.file_label.pack()

        # Listbox to show the columns
        self.column_listbox = tk.Listbox(self.window, width=50)
        self.column_listbox.pack(pady=10)
        self.column_listbox.bind("<<ListboxSelect>>", self.show_stats)

        # Stats Label
        self.stats_label = tk.Label(self.window, text="", justify="left")
        self.stats_label.pack()

        # Show Chart Button
        self.show_chart_button = tk.Button(self.window, text="Show Chart", command=self.show_chart, state="disabled")
        self.show_chart_button.pack(pady=10)

        self.df = None # DataFrame is initially empty

        self.window.mainloop()

    def load_csv(self):
        file_path = filedialog.askopenfilename(
            title="Select a CSV File",
            filetypes = [("CSV files", "*.csv")]
        )
        if file_path:
            try:
                self.df = pd.read_csv(file_path)
                self.file_label.config(text=f"Selected: {file_path.split('/')[-1]}")
                self.show_columns()
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: \n{e}")
        else:
            self.file_label.config(text="No file selected")
    
    def show_columns(self):
        self.column_listbox.delete(0, tk.END)
        if self.df is not None:
            for col in self.df.columns:
                self.column_listbox.insert(tk.END, col)
    
    def show_stats(self, event):
        selected = self.column_listbox.curselection()
        if not selected:
            return
        
        col_name = self.column_listbox.get(selected[0])
        if is_numeric_dtype(self.df[col_name]):
            self.show_chart_button.config(state='active')
            series = self.df[col_name]
            mean = series.mean()
            median = series.median()
            min_val = series.min()
            max_val = series.max()
            std = series.std()

            stats_text = (
                f"Column: {col_name}\n"
                f"Mean: {mean:.2f}\n"
                f"Median: {median}\n"
                f"Min: {min_val}\n"
                f"Max: {max_val}\n"
                f"Std Dev: {std:.2f}"
            )
        else:
             stats_text = f"Column '{col_name}' is not numeric."
             self.show_chart_button.config(state='disabled')
        
        self.stats_label.config(text=stats_text)

    def show_chart(self):
        selected = self.column_listbox.curselection()
        if not selected:
            messagebox.showinfo("Info", "Please select a column")
            return
        
        col_name = self.column_listbox.get(selected[0])

        if pd.api.types.is_numeric_dtype(self.df[col_name]):
            plt.figure(figsize=(6, 4))
            self.df[col_name].plot(kind="hist", bins=10, color="skyblue", edgecolor="black")
            plt.title(f"Histogram of {col_name}")
            plt.xlabel(col_name)
            plt.ylabel("Frequency")
            plt.grid(True)
            plt.tight_layout()
            plt.show()
            
if __name__ == "__main__":
    CSVAnalyzer()
