import pandas as pd


df = pd.read_excel("../Data/data.xlsx")
print("Before update:")
print(df)


df.at[2, "Age"] = 99


df.to_excel("data.xlsx", index=False)
print("\nAfter update:")
print(df)