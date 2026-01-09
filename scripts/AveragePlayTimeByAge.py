import pandas as pd
import matplotlib.pyplot as plt
age_playtime = df.groupby("Age")["PlayTimeHours"].mean()

plt.figure()
age_playtime.plot()
plt.title("Average Play Time by Age")
plt.xlabel("Age")
plt.ylabel("Average Play Time (Hours)")
plt.tight_layout()
plt.savefig("output/figures/line_age_playtime.png")
plt.close()