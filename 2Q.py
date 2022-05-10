import pandas as pd

df = pd.read_csv("national-budget.csv")
sub = df["שם רמה 2"]
# def education_budget(year:int)->int:


print(sub.head(6000))
