import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# --- Step 1: Data Analysis with Pandas ---
print("Reading yearly data and performing analysis...")
df = pd.read_csv('yearly_energy_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Calculate yearly summary statistics
total_consumption_yearly = df['consumption_kwh'].sum()
average_consumption_daily = df['consumption_kwh'].mean()
max_consumption_daily = df['consumption_kwh'].max()

# --- Step 2: Create a Visualization with Matplotlib ---
print("Creating a chart for the entire year...")
plt.figure(figsize=(10, 6))
plt.plot(df['date'], df['consumption_kwh'], linestyle='-')
plt.title('Yearly Energy Consumption (kWh)')
plt.xlabel('Date')
plt.ylabel('Consumption (kWh)')
plt.grid(True)
plt.tight_layout()
plt.savefig('yearly_consumption_chart.png')
plt.close()

# --- Step 3: Generate the PDF Report with FPDF ---
print("Generating yearly PDF report...")
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, "Yearly Energy Consumption Report", 0, 1, 'C')

pdf.ln(10)
pdf.set_font("Arial", '', 12)
pdf.cell(200, 10, f"Total Yearly Consumption: {total_consumption_yearly:.2f} kWh", 0, 1)
pdf.cell(200, 10, f"Average Daily Consumption: {average_consumption_daily:.2f} kWh", 0, 1)
pdf.cell(200, 10, f"Maximum Daily Consumption: {max_consumption_daily:.2f} kWh", 0, 1)

pdf.ln(10)
pdf.image('yearly_consumption_chart.png', x=10, y=None, w=180)

pdf.output("yearly_energy_report.pdf")
print("Report 'yearly_energy_report.pdf' has been created!")