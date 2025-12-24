import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_csv("../data/train.csv")

# Select features
features = ['OverallQual', 'GrLivArea', 'GarageCars', 'TotalBsmtSF']
target = 'SalePrice'

df = df[features + [target]].dropna()

X = df[features]
y = df[target]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
with open("model/house_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved successfully!")
