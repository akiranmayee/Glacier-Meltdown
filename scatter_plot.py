import matplotlib.pyplot as plt
import seaborn as sns

# 1. Calculate the change in Glacier Mass Balance
# The change is already calculated in the previous code block and stored in `y`, dropping the first row.
# Let's create a temporary DataFrame for plotting and correlation.
plot_df = X.copy()
plot_df['Glacier_Mass_Balance_Change'] = y.dropna()

# 2. Create scatter plots
numerical_cols = ['Temperature (°C)', 'Precipitation (mm)', 'Snowfall (mm)', 'Elevation (m)', 'Solar Radiation (W/m²)', 'Glacier Area (km²)', 'Glacier Thickness (m)', 'Year', 'Month', 'DayOfYear']

plt.figure(figsize=(15, 12))
for i, col in enumerate(numerical_cols):
    plt.subplot(4, 3, i + 1)
    sns.scatterplot(data=plot_df, x=col, y='Glacier_Mass_Balance_Change', alpha=0.6)
    plt.title(f'{col} vs. Glacier Mass Balance Change')
    plt.xlabel(col)
    plt.ylabel('Mass Balance Change (kg/m²)')
plt.tight_layout()
plt.show()

# 3. Compute the correlation matrix
correlation_matrix = plot_df.corr()

# 4. Display the correlation matrix as a heatmap
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Matrix of Numerical Features and Mass Balance Change')
plt.show()
