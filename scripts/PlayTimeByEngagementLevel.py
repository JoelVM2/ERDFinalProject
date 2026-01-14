import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

df = pd.read_csv("data/online_gaming_behavior_insights.csv")
df = df.dropna().drop_duplicates()

engagement_order = ["Low", "Medium", "High"]
df["EngagementLevel"] = pd.Categorical(df["EngagementLevel"], 
                                       categories=engagement_order, 
                                       ordered=True)

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(10, 6))
sns.boxplot(x="EngagementLevel", y="PlayTimeHours", data=df,
            palette="Blues_d",
            showmeans=True,
            meanprops={"marker":"o", "markerfacecolor":"white", "markeredgecolor":"black"})

plt.title("Play Time by Engagement Level", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Engagement Level", fontsize=12, fontweight='semibold')
plt.ylabel("Play Time (Hours)", fontsize=12, fontweight='semibold')
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.tight_layout()
plt.savefig("figures/boxplot_engagement.png", dpi=300, bbox_inches='tight')
plt.close()

print(f"Boxplot guardado: figures/boxplot_engagement.png")