import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('drug-overdose-death-rates new.csv')

print(df.head)
print(df.columns.to_list())
marks = df['Any opioid death rates (CDC WONDER)'].tolist()

plt.figure(figsize=(10, 6))
plt.bar(df.index, marks, color='skyblue')
plt.ylabel('rates')
plt.title('Any opioid death rates (CDC WONDER)')
plt.show()
