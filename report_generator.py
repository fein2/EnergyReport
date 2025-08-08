import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# --- Step 1: Data Analysis with Pandas ---
print("Reading data and performing analysis...")
df = pd.read_csv('energy_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Calculate summary statistics
total_consumption = df['consumption_kwh'].sum()
average_consumption = df['consumption_kwh'].mean()
max_consumption = df['consumption_kwh'].max()

# --- Step 2: Create a Visualization with Matplotlib ---
print("Creating a chart...")
plt.figure(figsize=(8, 4))
plt.plot(df['date'], df['consumption_kwh'], marker='o', linestyle='-')
plt.title('Daily Energy Consumption (kWh)')
plt.xlabel('Date')
plt.ylabel('Consumption (kWh)')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('consumption_chart.png') # Save the chart as a file
plt.close()

# --- Step 3: Generate the PDF Report with FPDF ---
print("Generating PDF report...")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Daily Energy Consumption Report", 0, 1, 'C')

pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(200, 10, f"Total Consumption: {total_consumption:.2f} kWh", 0, 1)
pdf.cell(200, 10, f"Average Daily Consumption: {average_consumption:.2f} kWh", 0, 1)
pdf.cell(200, 10, f"Maximum Daily Consumption: {max_consumption:.2f} kWh", 0, 1)

pdf.ln(10)
pdf.image('consumption_chart.png', x=10, y=None, w=180)

pdf.output("energy_report.pdf")
print("Report 'energy_report.pdf' has been created!")