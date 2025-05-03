import pandas as pd
import os

data = {
    "name": ["Alice", "Bob", "Charlie", "David"],
    "city": ["NY", "LA", "Chicago", "Houston"],
    "marks": [85, 78, 92, 65]
}

df = pd.DataFrame(data)
top_students = df[df["marks"] > 80]

# Save CSV in the root of the repo
file_path = "top_students.csv"
top_students.to_csv(file_path, index=False)

print(f"CSV saved at: {os.path.abspath(file_path)}")
