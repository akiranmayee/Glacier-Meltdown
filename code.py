import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.compose import ColumnTransformerhttps://github.com/akiranmayee/Glacier-Meltdown/blob/main/code.py
from sklearn.pipeline import Pipeline

# Load data
data = pd.read_csv("glacier_data.csv")

# Preprocessing
data['Date'] = pd.to_datetime(data['Date'])
data['Year'] = data['Date'].dt.year
data['Month'] = data['Date'].dt.month
data['DayOfYear'] = data['Date'].dt.dayofyear

# Features & target
X = data[['Temperature', 'Precipitation', 'Snowfall', 'Elevation', 
          'Solar Radiation', 'Glacier Area', 'Glacier Thickness', 'Year', 'Month', 'DayOfYear', 'Season']]
y = data['Glacier Mass Balance'] - data['Glacier Mass Balance'].shift(1)

# Handle missing values (fill with mean for simplicity)
X.fillna(X.mean(), inplace=True)

# One-hot encode the 'Season' column
X = pd.get_dummies(X, drop_first=True)

# Scaling the numerical features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y.dropna(), test_size=0.2, random_state=42)

# Model: Random Forest
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")
