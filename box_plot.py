import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("waze_dataset.csv")


limit = df['driven_km_drives'].quantile(0.99)
df_clean = df[df['driven_km_drives'] <= limit]


plt.figure(figsize=(8, 6))
plt.boxplot(df_clean['driven_km_drives'], vert=True, patch_artist=True)
plt.ylabel('Driven KM per Drive')
plt.title('Box Plot (Outliers Above 99th Percentile Removed)')
plt.grid(True, axis='y')


plt.savefig("box_plot_clean.png")
plt.close()
