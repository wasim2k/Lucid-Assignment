import pandas as pd
df = pd.read_csv(r'E:/web/python assignment/in.csv')
print(df)
mean1  = df['Volume'].mean()
median1 = df['Volume'].median()
std1 = df['Volume'].std()

print("Mean of the volume: " + str(mean1))
print("Median of the volume: " + str(median1))
print("Standard deviation of the volume: " + str(std1))