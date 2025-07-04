import matplotlib.pyplot as plt

numerical_cols = ['Temperature (°C)', 'Precipitation (mm)', 'Snowfall (mm)', 'Elevation (m)', 'Solar Radiation (W/m²)', 'Glacier Area (km²)', 'Glacier Thickness (m)', 'Glacier Mass Balance (kg/m²)']

plt.figure(figsize=(15, 10))
for i, col in enumerate(numerical_cols):
    plt.subplot(3, 3, i + 1)
    plt.hist(data[col].dropna(), bins=20)
    plt.title(f'Distribution of {col}')
    plt.xlabel(col)
    plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
