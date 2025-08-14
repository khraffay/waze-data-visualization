import pandas as pd
import matplotlib.pyplot as plt

# load data
x = pd.read_csv(r"C:\Users\Abdul Raffay\Desktop\Waze\waze_dataset.csv")

# create line graph
plt.figure(figsize=(10, 6))
plt.plot(x['n_days_after_onboarding'], x['sessions'], marker='o', linestyle='-', color='b')
plt.xlabel('Days After Onboarding')
plt.ylabel('Sessions')
plt.title('Sessions Trend Over Days After Onboarding')
plt.grid(True)

# save and show
plt.savefig(r"C:\Users\Abdul Raffay\Desktop\Waze\line_graph.png")
plt.show()
