
import pandas as pd
import seaborn as sns
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt


world_data_filepath = "C:/Users/Userpc/Desktop/Projects/Machine Learning/world-data-2023.csv"
world_data = pd.read_csv(world_data_filepath)

world_data.dropna(subset=["Density\n(P/Km2)", "Land Area(Km2)"], inplace=True)
world_data["Density\n(P/Km2)"] = pd.to_numeric(world_data["Density\n(P/Km2)"], errors='coerce')
world_data["Land Area(Km2)"] = pd.to_numeric(world_data["Land Area(Km2)"], errors='coerce')



plt.figure(figsize=(16, 6))

# sns.scatterplot(x=world_data["Density\n(P/Km2)"], y=world_data["Land Area(Km2)"])
# plt.title("Spatial Distribution: Density vs Land Area")
# plt.xticks(rotation=45)
# plt.yticks(rotation=45)

# world_data.dropna(subset=["Agricultural Land( %)", "CPI"])

# world_data["Agricultural Land( %)"] = world_data["Agricultural Land( %)"].str.rstrip('%').astype('float')
# world_data["CPI"] = world_data["CPI"].str.replace(',', '').astype('float')
# world_data["CPI"] = world_data["CPI"]
# # sns.scatterplot(x=world_data["Agricultural Land( %)"], y=world_data["CPI"])
# sns.jointplot(x=world_data["Agricultural Land( %)"], y=world_data["CPI"], kind='kde')
# plt.title("Relationship between agricultural land and consumer price index")

# plt.xlim(0, 100)
# plt.ylim(0, 500)

# print(world_data.loc[:, "Unemployment rate"])

world_data.dropna(subset=["Unemployment rate", "Gross primary education enrollment (%)"])
world_data["Unemployment rate"] = world_data["Unemployment rate"].str.rstrip('%').astype('float')
world_data["Gross primary education enrollment (%)"] = world_data["Gross primary education enrollment (%)"].str.rstrip("%").astype('float')

sns.scatterplot(x=world_data["Gross primary education enrollment (%)"], y=world_data["Unemployment rate"], data=world_data)
sns.regplot(x=world_data["Gross primary education enrollment (%)"], y=world_data["Unemployment rate"], data=world_data)

print(world_data.columns)

plt.show()


