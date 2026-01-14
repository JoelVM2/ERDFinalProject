import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

df = pd.read_csv("data/online_gaming_behavior_insights.csv")
df = df.dropna().drop_duplicates()

os.makedirs("figures", exist_ok=True)

plt.figure(figsize=(12, 7))

mean_playtime = df["PlayTimeHours"].mean()
median_playtime = df["PlayTimeHours"].median()
std_playtime = df["PlayTimeHours"].std()

n, bins, patches = plt.hist(df["PlayTimeHours"], bins=25, color='steelblue', edgecolor='black', linewidth=1.2, alpha=0.85, density=False)
plt.axvline(mean_playtime, color='red', linestyle='--', linewidth=2, label=f'Media: {mean_playtime:.1f} hrs')
plt.axvline(median_playtime, color='green', linestyle='--', linewidth=2, label=f'Mediana: {median_playtime:.1f} hrs')
plt.title("Distribución de Horas de Juego", fontsize=16, fontweight='bold', pad=20)
plt.xlabel("Horas de Juego", fontsize=14, labelpad=10)
plt.ylabel("Número de Jugadores", fontsize=14, labelpad=10)
plt.grid(axis='y', alpha=0.3, linestyle='--')
plt.legend(fontsize=12)

stats_text = f'Total jugadores: {len(df):,}\n'
stats_text += f'Desviación estándar: {std_playtime:.1f} hrs\n'
stats_text += f'Mínimo: {df["PlayTimeHours"].min():.1f} hrs\n'
stats_text += f'Máximo: {df["PlayTimeHours"].max():.1f} hrs'

plt.text(0.98, 0.98, stats_text, transform=plt.gca().transAxes, verticalalignment='top', horizontalalignment='right', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8), fontsize=10)
plt.tight_layout()
plt.savefig("figures/histogram_playtime.png", dpi=300, bbox_inches='tight')
plt.close()
print("Histograma mejorado guardado: figures/histogram_playtime.png")