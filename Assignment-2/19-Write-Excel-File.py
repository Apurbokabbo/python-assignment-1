import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age" : [25, 30, 35],
    "City": ["Dhaka", "Chittagong", "Sylhet"]
}

df = pd.DataFrame(data)
df.to_excel("../Data/write.xlsx",index=False)
print("Data written to write.xlsx")