import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('default')
plt.rcParams['font.size'] = 11

df = pd.read_csv("data/online_gaming_behavior_insights.csv")

missing_values = df.isnull().sum()
print("Missing values per column:\n", missing_values)

df = df.dropna()
df = df.drop_duplicates()

df["Age"] = df["Age"].astype(int)
df["InGamePurchases"] = df["InGamePurchases"].astype(int)
df["SessionsPerWeek"] = df["SessionsPerWeek"].astype(int)
df["PlayerLevel"] = df["PlayerLevel"].astype(int)
df["AchievementsUnlocked"] = df["AchievementsUnlocked"].astype(int)

categorical_columns = [
    "Gender",
    "Location",
    "GameGenre",
    "GameDifficulty",
    "EngagementLevel"
]

for col in categorical_columns:
    df[col] = df[col].astype("category")

genre_counts = df["GameGenre"].value_counts()

plt.figure(figsize=(10, 6))
colors = ['#4B8BBE', '#306998', '#FFD43B', '#646464', '#FF6B6B']
ax = genre_counts.plot(kind="bar", color=colors, edgecolor='black', linewidth=1.2)
plt.title("Number of Players per Game Genre", fontsize=14, fontweight='bold', pad=20)
plt.xlabel("Game Genre", fontsize=12, fontweight='medium')
plt.ylabel("Number of Players", fontsize=12, fontweight='medium')
plt.ylim(7900, 8100)

for i, v in enumerate(genre_counts):
    ax.text(i, v + 10, str(v), ha='center', fontweight='bold', fontsize=11)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_axisbelow(True)
ax.yaxis.grid(True, linestyle='--', alpha=0.3)
current_labels = [label.get_text() for label in ax.get_xticklabels()]
if set(current_labels) == {'Sports', 'Action', 'Strategy', 'Simulation', 'RPG'}:
    ax.set_xticklabels(['Sports', 'Action', 'Strategy', 'Simulation', 'RPG'])

plt.tight_layout()
plt.savefig("figures/bar_genre_labels.png", dpi=150)
plt.close()

print("Gráfico guardado: figures/bar_genre_labels.png")
