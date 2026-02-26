import pandas as pd

data = pd.read_csv("data.csv")
print("Average:", data["value"].mean())
