import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


x = pd.read_csv(r"C:\Users\Abdul Raffay\Desktop\Waze\waze_dataset.csv")


num_x = x.select_dtypes(include=["number"])


plt.figure(figsize=(12,8))
sns.heatmap(num_x.corr(), annot=True, fmt=".2f", cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()


plt.savefig(r"C:\Users\Abdul Raffay\Desktop\Waze\heatmap.png")
plt.close()
