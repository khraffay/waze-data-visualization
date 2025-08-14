import pandas as pd
import matplotlib.pyplot as plt

# load data
x = pd.read_csv(r"C:\Users\Abdul Raffay\Desktop\Waze\waze_dataset.csv")

# create histogram
plt.figure(figsize=(8,5))
plt.hist(x["driven_km_drives"], bins=20, color="skyblue", edgecolor="black")
plt.title("Distribution of Driven KM per Drive")
plt.xlabel("Driven KM")
plt.ylabel("Frequency")

# save and show
plt.savefig(r"C:\Users\Abdul Raffay\Desktop\Waze\histogram.png")
plt.show()
