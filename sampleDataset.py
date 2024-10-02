import pandas as pd
import numpy as np

# Create a sample dataset with missing values
data = {
    "Name": ["Dhruvi", "Hirva", "Tilak", np.nan, "Henil", "Janvee", np.nan, "Parth", "Riya", "Pratik"],
    "Salary": [90000, 60000, np.nan, 75000, np.nan, 70000, np.nan, 55000, 80000, np.nan],
    "Number": [123456, np.nan, 654321, 789123, 456789, np.nan, np.nan, 147258, 951357, 753951],
    "Favorite Food": ["Dosa", np.nan, "Vadapav", np.nan, "Pasta", "Paneer Tikka", "Manchurian", "Pizza", np.nan, "Dahi Puri"],
    "Work Type": ["Remote", "Hybrid", "Office", "Remote", np.nan, "Hybrid", "Office", np.nan, "Office", "Remote"],
    "Role": ["Software Eng.", np.nan, "Product Mgr.", "Software Eng.", "Product Mgr.", "Software Eng.", "Product Mgr.", "Software Eng.", np.nan, "Software Eng."]
}

# Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("practical_2_dataset.xlsx", index=False)
print("Sample dataset created and saved to 'practical_2_dataset.xlsx'")
