import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Create a sample dataset
data = {
    "Name": ["Dhruvi", "Hirva", "Tilak", "Henil", "Janvee"],
    "Age": [25, 30, 35, 40, 22],
    "Salary": [50000, 60000, 75000, 80000, 45000],
    "Years of Experience": [2, 5, 8, 10, 1],
    "Rating": [4.5, 4.7, 3.9, 4.2, 4.0],
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Binning: Divide 'Salary' into categories
bins = [0, 50000, 70000, 90000]  # Define bin edges
labels = ["Low", "Medium", "High"]  # Define labels for the bins
df['Salary_Binned'] = pd.cut(
    df['Salary'], bins=bins, labels=labels, include_lowest=True)

# Normalization: Scale 'Age', 'Salary', 'Years of Experience', and 'Rating' to [0, 1] range
scaler = MinMaxScaler()
df[['Age', 'Salary', 'Years of Experience', 'Rating']] = scaler.fit_transform(
    df[['Age', 'Salary', 'Years of Experience', 'Rating']])

# Save the processed DataFrame to an Excel file
df.to_excel("binned_normalized_dataset.xlsx", index=False)

# Display the DataFrame
print("\nBinned and Normalized Dataset:\n")
print(df)
