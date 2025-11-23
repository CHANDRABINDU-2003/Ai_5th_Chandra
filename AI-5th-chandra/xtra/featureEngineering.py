import pandas as pd

# Sample dataset (you can replace this with your CSV file)
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, None, 30, 22, 28],
    'Salary': [50000, 60000, None, 45000, 52000]
}

df = pd.DataFrame(data)
print("Original Dataset:\n")
print(df)

# Check for any null values in the dataset
print("\nCheck for null values:\n")
print(df.isnull())

# Count of null values per column
print("\nCount of null values per column:\n")
print(df.isnull().sum())

df_drop_rows = df.dropna()
print("\nDataset after deleting rows with null values:\n")
print(df_drop_rows)

df_drop_cols = df.dropna(axis=1)
print("\nDataset after deleting columns with null values:\n")
print(df_drop_cols)

# Fill numeric values with mean
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Fill categorical with placeholder
df['Name'].fillna('Unknown', inplace=True)

print("\nDataset after filling null values:\n")
print(df)
