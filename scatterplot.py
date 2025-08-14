import pandas as pd
import matplotlib.pyplot as plt


x = pd.read_csv(r"C:\Users\Abdul Raffay\Desktop\Waze\waze_dataset.csv")


plt.figure(figsize=(7,5))
plt.scatter(x["sessions"], x["drives"], alpha=0.5)
plt.xlabel("Sessions")
plt.ylabel("Drives")
plt.title("Sessions vs Drives")


plt.savefig(r"C:\Users\Abdul Raffay\Desktop\Waze\scatterplot.png")
plt.show()
