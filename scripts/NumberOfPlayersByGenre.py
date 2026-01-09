import pandas as pd
import matplotlib.pyplot as plt

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

plt.figure()
ax = genre_counts.plot(kind="bar")
plt.title("Number of Players per Game Genre")
plt.xlabel("Game Genre")
plt.ylabel("Number of Players")
plt.ylim(7900, 8100)

for i, v in enumerate(genre_counts):
    ax.text(i, v + 10, str(v), ha='center')

plt.tight_layout()
plt.savefig("figures/bar_genre_labels.png")
plt.close()

