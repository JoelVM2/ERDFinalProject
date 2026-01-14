import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/online_gaming_behavior_insights.csv")
df = df.dropna().drop_duplicates()
df["Age"] = df["Age"].astype(int)

os.makedirs("figures", exist_ok=True)

age_playtime = df.groupby("Age")["PlayTimeHours"].mean()
plt.figure()
age_playtime.plot()
plt.title("Average Play Time by Age")
plt.xlabel("Age")
plt.ylabel("Average Play Time (Hours)")
plt.tight_layout()
plt.savefig("figures/line_age_playtime.png")
plt.show()

print("Gráfico guardado: figures/line_age_playtime.png")
