import seaborn as sns

penguins = sns.load_dataset('penguins')
print(penguins)
sns.relplot(x="households", y="population", data=penguins)
sns.relplot(x="longitude", y="median_house_value", kind="line", data=penguins)
sns.histplot(x="flipper_length_mm", data=penguins)