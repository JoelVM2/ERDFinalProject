import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

df = pd.read_csv("data/online_gaming_behavior_insights.csv")
df = df.dropna().drop_duplicates()

os.makedirs("figures", exist_ok=True)

x_jitter = df["SessionsPerWeek"] + np.random.uniform(-0.5, 0.5, size=len(df))
y_jitter = df["AvgSessionDurationMinutes"] + np.random.uniform(-2, 2, size=len(df))

plt.figure(figsize=(12, 8))
plt.scatter(x_jitter, y_jitter,  alpha=0.6, s=50, edgecolors='black', linewidth=0.5)
plt.title("Sessions per Week vs Avg Session Duration", fontsize=16, fontweight='bold')
plt.xlabel("Sessions per Week", fontsize=14)
plt.ylabel("Avg Session Duration (Minutes)", fontsize=14)
plt.grid(True, alpha=0.3, linestyle='--')
plt.tight_layout()
plt.savefig("figures/scatter_sessions_duration.png", dpi=300)
plt.close()
print("Gráfico guardado: figures/scatter_sessions_duration.png")