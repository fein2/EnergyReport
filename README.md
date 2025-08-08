# Automated Energy Report Generator

This project is an advanced version of the previous report generator, built to analyse and report on a full year of simulated energy consumption data. It showcases skills in handling larger datasets, data visualisation, and automated reporting.

## Features

* **Data Analysis:** Uses Pandas to calculate key yearly metrics like total, average, and maximum daily consumption.

* **Data Visualization:** Generates a line chart for the entire year of data using Matplotlib.

* **PDF Generation:** Creates a professional PDF report that includes all summary text and the generated chart.

## How to Run

1. Ensure you have Python installed.

2. Install the required libraries: `pip install pandas matplotlib fpdf`

3. Ensure the `yearly_energy_data.csv` file and the `yearly_report_generator.py` script are in the same folder.

4. Run the script from your terminal: `python yearly_report_generator.py`

5. After the script runs, it will create two new files in the same folder: `yearly_consumption_chart.png` and `yearly_energy_report.pdf`, which contains the full analysis and chart.